#!/usr/bin/env python

from distutils.core import setup

setup(name='dataeng',
      version='1.0',
      description='Python code for the Data Engineering Course Example',
      author='Me',
      author_email='test@email',
      url='TBC',
      packages=['test_module'],
    #   install_requires=['bs4','ansible-core','botocore','boto3', 'mr4mp', 'lxml'],
      entry_points={'console_scripts': ['test = test_module.hello_world:hello_world_function']}
     )