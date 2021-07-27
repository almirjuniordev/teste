## setup.py

import io
import os

from setuptools import setup, find_packages

dir = os.path.dirname(__file__)

with io.open(os.path.join(dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aj-math',
    version='1.0',
    description='Lib que faz calculos matematicos',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/private_directory',
    author='Me',
    author_email='almir.junior@nova-8.com',
    license='GNU',
    python_requires='>=3',
    packages=find_packages()
)