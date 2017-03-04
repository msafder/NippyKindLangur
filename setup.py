"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='dockcli',
    version='0.14.0',
    description='Flask in Docker that has one endpoint and a CLI for running it',
    url='https://github.com/sudomilk/NippyKindLangur',
    author='sudomilk',
    author_email='mailertaylor@gmail.com',
    keywords='docker python flask click',
    py_modules=["dockcli"],
    install_requires=['docker', 'Flask', 'click'],
    entry_points={'console_scripts': ['dockcli=dockcli:main']}
)
