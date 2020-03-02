====================================
Ansible collections to RPM converter
====================================

This script will contact the Ansible Galaxy API to fetch information about an
Ansible Collection, and use that to build an RPM spec file.

Requirements
------------

- Jinja2
- pbr
- requests

Installation
------------

The script is provided as a Python package. You can install it on a local
virtual environment, or as an RPM package once it is prepared. You can also
run directly ``python galaxycollection_to_rpm/galaxycollection_to_rpm.py``
if needed, from the git checkout.

Usage
-----

.. code-block:: shell-session

  $ galaxy-collection-to-rpm --collection <collection-name>

This command-line will send the resulting spec file to standard output. You can
also specify the target file using:

.. code-block:: shell-session

  $ galaxy-collection-to-rpm --collection <collection-name> --output-file file.spec

Make sure you check the generated spec file, since some fields may require
adjustments. One example is the license, which may not be using the names
required by the packaging guidelines.

License
-------

Apache 2.0

Author
------

Javier Peña (`@fj_pena <https://github.com/javierpena>`_)
