"""
Sanic
"""
import codecs
import os
import re
from setuptools import setup, find_packages


with codecs.open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'sanic_oauth', '__init__.py'), 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

install_requires = [
    'httptools>=0.0.9',
    'ujson>=1.35',
    'aiofiles>=0.3.0',
]

if os.name != 'nt':
    install_requires.append('uvloop>=0.5.3')

setup(
    name='Sanic-OAuth',
    version=version,
    url='https://github.com/Sniedes722/Sanic-OAuth',
    license='MIT',
    author='Shawn Niederriter',
    author_email='shawnhitsback@gmail.com',
    description=(
        'An OAuth extension for use with Sanic middleware.'),
    packages=find_packages('.'),
    platforms='any',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)