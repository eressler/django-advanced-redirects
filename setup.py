from distutils.core import setup

VERSION = __import__("advanced_redirects").__version__

setup(
    name='django-advanced-redirects',
    packages=['django-advanced-redirects'],  # this must be the same as the name above
    version=VERSION,
    description='Advanced redirect management for Django applications.',
    author='Eric Ressler',
    author_email='eric@ericressler.com',
    url='http://eressler.github.io/django-advanced-redirects/',  # use the URL to the github repo
    download_url="https://github.com/eressler/django-advanced-redirects/tarball/{0}".format(VERSION),  # I'll explain this in a second
    keywords=['django', 'redirects', 'seo'], # arbitrary keywords
    classifiers=[],
)
