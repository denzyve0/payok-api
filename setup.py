import sys
from warnings import warn

from setuptools import setup, find_packages
from payokapi import Stage, VERSION

try:
    from pip.req import parse_requirements
except ImportError:  # pip >= 10.0.0
    from pip._internal.req import parse_requirements

MINIMAL_PY_VERSION = (3, 6)

if sys.version_info < MINIMAL_PY_VERSION:
    warn('payokapi works only with Python {}+'.format('.'.join(map(str, MINIMAL_PY_VERSION))), RuntimeWarning)

def get_readme():
	with open("README.md", "r", encoding="utf-8") as f:
		return f.read()
		
def get_requirements():
    filename = 'requirements.txt'
    if VERSION.stage == Stage.DEV:
        filename = 'dev_' + filename

    install_reqs = parse_requirements(filename, session='hack')
    
    return [str(ir.requirement) for ir in install_reqs]

setup(
    name='payokapi',
    version=VERSION.version,
    description='Asynchronous library for work with PayOk.io API',
    long_description=get_readme(),
    author='Denzyve',
    author_email='solda740@gmail.com',
    url='https://github.com/denzyve0/payok-api',
    license='GPLv3',
    packages=find_packages(
    	where="payok-api",
    	exclude=["tests", "examples"]),
    install_requires=get_requirements(),
    classifiers=[
        VERSION.pypi_development_status,
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
