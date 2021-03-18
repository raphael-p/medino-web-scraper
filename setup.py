from setuptools import setup, find_packages
from io import open
from os import path

import pathlib
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# automatically captured required modules for install_requires in requirements.txt
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]

setup(
    name='MedProducts',
    description='A command line app and package for getting product information from the medino website',
    version='1.0',
    packages = find_packages(),
    install_requires = install_requires,
    entry_points='''
        [console_scripts]
        medproducts=medproducts.__main__:main
    ''',
    author='Raphael Piccolin',
    keyword='medino, web scrape'
)
