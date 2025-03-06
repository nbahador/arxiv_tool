from setuptools import setup, find_packages

setup(
    name='arxiv_tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'arxiv',
        'pandas',
        'openpyxl',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool to search and analyze arXiv papers',
    url='https://github.com/yourusername/arxiv_tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)