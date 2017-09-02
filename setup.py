import os

from setuptools import find_packages, setup

VERSION = __import__("advanced_redirects").__version__

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ws-advanced-redirects',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    description='Advanced redirect management for wheel-size site.',
    long_description=README,
    url='https://github.com/sorlandet/django-advanced-redirects/',
    author='Evgeniy Medvedev',
    author_email='yevgeniy.medvedev@gmail.com',
    classifiers=[
        'Framework :: Django :: 1.8',  # replace "X.Y" as appropriate
        'Intended Audience :: Wheel-Size Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
)
