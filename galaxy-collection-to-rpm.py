#!/usr/bin/python3
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#

import argparse
import jinja2
import requests
import sys


def create_spec(collection, output_file):
    r = requests.get('https://galaxy.ansible.com/api/v2/collections/%s/' %
                     collection.replace('-', '/').replace('.', '/'))
    if r.status_code != 200:
        print('Error %s accessing %s' % (r.status_code, r.url))
        sys.exit(1)

    latest_version = r.json()['latest_version']['version']
    latest_v_url = r.json()['latest_version']['href']
    r = requests.get(latest_v_url)
    if r.status_code != 200:
        print('Error %s accessing %s' % (r.status_code, r.url))
        sys.exit(1)

    collection_info = r.json()
    if 'download_url' in collection_info and 'version' in collection_info:
        collection_info['download_url'] = collection_info['download_url'].replace(
            collection_info['version'], '%{version}')

    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(['.']))
    jinja_template = jinja_env.get_template('template.j2')
    content = jinja_template.render(info=collection_info)

    if output_file:
        with open(output_file, 'w') as fp:
            fp.write(content)
    else:
        print("%s" % content)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--collection',
                        help='Name of the collection. You can use a '
                             'namespace-name of namespace.name format.',
                             required=True)
    parser.add_argument('--output-file',
                        help='Name of the output file. If not specified,'
                             ' send to standard output.')

    options = parser.parse_args(sys.argv[1:])

    create_spec(options.collection, options.output_file)

if __name__ == '__main__':
    main()
