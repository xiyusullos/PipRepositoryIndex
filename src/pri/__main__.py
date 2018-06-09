#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author    : xiyusullos <i@xy-jit.cc>
# @time      : 2018-06-09 14:46
# @copyright : Copyright (C) 2018 xiyusullos.
# @file      : prm.py
'''prm
Usage:
  prm ls
  prm use <repository_name>
  prm current
  prm (-v | --version)
  prm (-h | --help)
Options:
  -h, --help                   output usage information
  -v, --version                output the version number
'''
import configparser
import json
import os
import platform
import re

from docopt import docopt

from prm.version import __version__


def is_windows():
    return 'Windows' == platform.system()


PIPCONF_NAME = os.sep.join(['~', 'pip', 'pip.ini'] if is_windows() else ['~', '.pip', 'pip.conf'])
PIPCONF_PATH = os.path.expanduser(PIPCONF_NAME)
PIP_PATH = os.path.dirname(PIPCONF_PATH)


def init():
    if not os.path.exists(PIP_PATH):
        os.mkdir(PIP_PATH)


def _all_repositories():
    repositories_name = 'repositories.json'
    repositories_path = os.sep.join([os.path.dirname(__file__), repositories_name])
    with open(repositories_path, encoding='utf-8') as f:
        return json.load(f)


def _get_repository(name):
    repo = [x for x in _all_repositories() if x['name'] == name]
    return None if len(repo) < 1 else repo[0]


def _pip_conf_str(url, host=None):
    if host is None:
        return '''
[global]
index-url = {}
'''.format(url)
    else:
        return '''
[global]
index-url = {}
[install]
trusted-host = {}
'''.format(url, host)


def _is_valid_url(url):
    p = re.compile('^https?://.+?/simple/?$')
    return not p.match(url) == None


def list_repositories():
    print('%-20s' % 'repository name', 'repository url')
    print('-' * 79)
    for x in _all_repositories():
        print('%-20s' % x['name'], x['url'])


def current_repository():
    repository_name = 'pypi'
    if os.path.exists(PIPCONF_PATH):
        config = configparser.ConfigParser()
        config.read(PIPCONF_PATH)
        url = config.get('global', 'index-url')
        for x in _all_repositories():
            if url == x['url']:
                repository_name = x['name']
                break
    repo = _get_repository(repository_name)
    print('{}({})'.format(repo['name'], repo['url']))


def use_repository(repository_name):
    repo = _get_repository(repository_name)
    url = repo['url']
    with open(PIPCONF_PATH, 'w') as f:
        s = _pip_conf_str(url, url.split('/')[2])
        f.write(s)
    current_repository()


def show_version(option, opt, value, parser):
    print(__version__)


def main():
    init()
    args = docopt(__doc__, version=__version__)
    if args['ls']:
        list_repositories()
    elif args['current']:
        current_repository()
    elif args['use']:
        use_repository(args['<repository_name>'])
    else:
        print('something is error')


if __name__ == '__main__':
    main()
