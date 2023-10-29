#!/usr/bin/env python

from distutils.core import setup

setup(name='pip-test',
      version='1.0',
      description='Python code for the Data Engineering Course Example',
      author='Me',
      author_email='test@email',
      url='TBC',
      packages=['test_module','data_process'],
      install_requires=['pandas','numpy'],
      entry_points={'console_scripts': ['pip-test-print = test_module.hello_world:hello_world_function',
                                        'pip-test-split = data_process.split:split_Data']}
     )