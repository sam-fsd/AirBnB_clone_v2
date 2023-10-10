#!/usr/bin/python3
"""Defines a function"""

from fabric.api import *


do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.user = 'ubuntu'
env.hosts = ['34.203.75.238', '100.26.226.192']


def deploy():
    """Creates and distributes an archive to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    result = do_deploy(archive_path)

    return result
