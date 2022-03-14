from unicodedata import name
from setuptools import setup, find_packages

setup(
name="Malawi Ingetrated Sensor Suite Study", version='0.0.1',
description='Software package that uses different sensors to determine different stove metrics'
long_description=open('README.MD'.READ(),
author="Grant Ross",
author_email='rossgra@oregonstate.edu',
license="MIT",
packages=find_packages())
)