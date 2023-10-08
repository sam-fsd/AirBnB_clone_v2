#!/usr/bin/python3
"""Defines a function for a fabfile"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """Creates a .tgz archive from
       contents of web_static"""
    local('mkdir -p versions')
    curr_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f'web_static_{curr_datetime}'
    result = local(
        f'tar -cvzf versions/{archive_name}.tgz web_static'
    )

    if result.succeeded:
        return f'versions/{archive_name}'
    else:
        return None
