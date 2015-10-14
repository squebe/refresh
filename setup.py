# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
	# info
	name='refresh',
	version='0.0.1',
	author=u'Stephen Quebe',
	author_email='squebe@gmail.com',
	url='https://github.com/squebe/refresh',
	description='Refresh will run a command and reload it when any files matching the specified pattern in the specified directory are changed.',
	long_description=open('README.md').read(),

	# include
	packages=find_packages(),
	include_package_data=True,
	install_requires=[],

	# keep this package private
	classifier=['Private :: Do Not Upload'],
)