====================================
Ansible collections to RPM converter
====================================

This script will contact the Ansible Galaxy API to fetch information about an
Ansible Collection, and use that to build an RPM spec file.

Requirements
------------

- Jinja2
- requests

Usage
-----

.. code-block:: shell-session

  $ ./galaxy-collection-to-rpm.py --collection <collection-name>

This command-line will send the resulting spec file to standard output. You can
also specify the target file using:

.. code-block:: shell-session

  $ ./galaxy-collection-to-rpm.py --collection <collection-name> --output-file file.spec

Make sure you check the generated spec file, since some fields may require
adjustments. One example is the license, which may not be using the names
required by the packaging guidelines.

License
-------

Apache 2.0

Author
------

Javier Peña (`@fj_pena <https://github.com/javierpena>`_)
