import imp
import os
from setuptools import (setup, find_packages)

PACKAGE_NAME = 'pri'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst'), encoding='utf-8').read()
except:
    README = ''
VERSION = imp.load_source('version', os.path.join(here, 'src/%s/version.py' % PACKAGE_NAME)).__version__

setup(
    name='pri',
    version=VERSION,
    keywords='python, PyPi mirror, pip repository manager',
    description="Pip Repository Manager. Switch PyPi mirror.",
    long_description=README,

    author='xiyusullos',
    author_email='i@xy-jit.cc',
    url='https://github.com/xiyusullos/PipRepositoryIndex',
    license='MIT',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    platforms='any',
    zip_safe=True,
    include_package_data=True,

    install_requires=[
        'docopt==0.6.2',
    ],

    classifiers=[],

    entry_points={
        'console_scripts': [
            'pri = pri.__main__:main'
        ]
    },
)
