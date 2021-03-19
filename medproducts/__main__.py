import click
from medproducts.urlBuilder import Browse, Search, FilterBy, SortBy


class Config(object):

    def __init__(self):
        self.max_results = None
        self.sort_by = None
        self.filter_by = None
        self.file = None
        self.pretty = None


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('-n', default=10, show_default=True, type=int,
              help='The maximum number of results to display')
@click.option('-s', '--sort', default=None, type=click.Choice([s.name.lower() for s in SortBy]))
@click.option('-t', '--tag', default=None, type=click.Choice([f.name.lower() for f in FilterBy]))
@click.option('-f', '--file', default='-', type=click.File('w'),
              help='File in which to store the results as comma separated values')
@click.option('-p', '--pretty', is_flag=True, default=False, show_default=True,
              help='An option to display the results in a table rather than as a csv')
@pass_config
def main(config, n, sort, tag, file, pretty):
    config.max_results = n
    if sort:
        config.sort_by = SortBy[sort.upper()]
    if tag:
        config.filter_by = FilterBy[tag.upper()]
    config.file = file
    config.pretty = pretty


@main.command()
@click.argument('page', type=click.Choice([b.name for b in Browse]))
@pass_config
def browse(config, page):
    """[popular|accessories|aches_and_pains|allergy_and_hayfever]"""
    results = Browse[page.upper()].sort_by(config.sort_by).filter_by(config.filter_by).fetch()
    output(config, results)


@main.command()
@click.argument('keyword', type=str)
@pass_config
def search(config, keyword):
    """search_term"""
    results = Search.query(keyword).sort_by(config.sort_by).filter_by(config.filter_by).fetch()
    output(config, results)


def output(config, results):
    if config.file:
        config.file.write(results.display_as_csv(0, start_row=0))
    if config.pretty:
        click.echo(results.display_as_table(config.max_results))
    else:
        click.echo(results.display_as_csv(config.max_results))
