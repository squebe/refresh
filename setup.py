# -*- coding: utf-8 -*-
import sys
from setuptools import find_packages, setup


# keep this package private
if set(sys.argv).intersection(['upload', 'register']):
	print('This setup is private and should not be uploaded or registered.')
	sys.exit(-1)


# package settings
setup(
	# info
	name='refresh',
	version='0.0.2',
	author=u'Stephen Quebe',
	author_email='squebe@gmail.com',
	url='https://github.com/squebe/refresh',
	description='Refresh will run a command and reload it when any files matching the specified pattern in the specified directory are changed.',
	long_description=open('README.md').read(),
	license='MIT',

	# include
	packages=find_packages(),
	include_package_data=True,
	install_requires=['watchdog >=0.8.3'],

	# keep this package private
	classifiers=['Private :: Do Not Upload'],

	# install as an executable script
	entry_points={'console_scripts': ['refresh = refresh:main']}
)