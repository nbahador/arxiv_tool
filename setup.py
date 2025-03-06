from setuptools import setup, find_packages

setup(
    name='arxiv_tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'arxiv',       # For interacting with the arXiv API
        'pandas',      # For data manipulation
        'openpyxl',    # For Excel file handling
    ],
    author='Nooshin Bahador',
    author_email='nooshin.bah@gmail.com',
    description='A tool to search and analyze arXiv papers',
    url='https://github.com/nbahador/arxiv_tool',
)