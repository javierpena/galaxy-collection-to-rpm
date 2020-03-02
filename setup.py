from setuptools import setup

import os
import sys

classifiers = [
    'Intended Audience :: Information Technology',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
]

with open("README.rst", "r") as fp:
    long_description = fp.read()

setup(name="galaxycollection_to_rpm",
      version='0.0.1',
      author="Javier Peña",
      author_email="jpena@redhat.com",
      url="https://github.com/javierpena/galaxy-collection-to-rpm",
      description="Create RPM spec for an Ansible Galaxy collection",
      long_description=long_description,
      license="Apache 2.0",
      classifiers=classifiers,
      packages=['galaxycollection_to_rpm'],
      package_data={
          "": ["data/*.j2"],
      },
      entry_points={
          "console_scripts": [
              "galaxy-collection-to-rpm = galaxycollection_to_rpm.galaxycollection_to_rpm:main",
          ]
        }
      )
