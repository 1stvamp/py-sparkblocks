"""Installer for py-sparkblocks
"""

__version__ = '1.0.0'

try:
        from setuptools import setup, find_packages
except ImportError:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages
setup(
    name='py-sparkblocks',
    description='Util for generating unicode text based sparkline bargraphs'
                ' from lists of numbers',
    long_description=open('README.rst').read(),
    version=__version__,
    author='Wes Mason',
    author_email='wes@1stvamp.org',
    url='https://github.com/1stvamp/py-sparkblocks',
    packages=['sparkblocks'],
    license='BSD'
)
