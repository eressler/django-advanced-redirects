import os
from distutils.core import setup
from setuptools import find_packages
VERSION = __import__("seo_redirects").__version__
CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU GPL V2 License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
]
install_requires = [
    'django>=1.7',
]
# taken from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)
for dirpath, dirnames, filenames in os.walk('seo_redirects'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[12:] # Strip "admin_tools/" or "admin_tools\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))
setup(
    name="django-seo-redirects",
    description="Django application to provide more robust redirect options with 404 page monitoring",
    version=VERSION,
    author="Eric Ressler",
    author_email="ericr@smashingideas.com",
    url="https://github.com/eressler/django-seo-redirects",
    download_url="https://bitbucket.org/guillaumepiot/cotidia-admin-tools/downloads/cotidia-admin-tools-0.4.1.tar.gz",
    package_dir={'seo_redirects': 'seo_redirects'},
    packages=packages,
    package_data={'seo_redirects': data_files},
    include_package_data=True,
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
)