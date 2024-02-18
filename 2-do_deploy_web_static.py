#!/usr/bin/python3
"""
Distributes an archive to web servers
"""

from fabric.api import run, put, env
from os.path import isfile


env.hosts = ['35.231.225.57', '104.196.171.213']


def do_deploy(archive_path):
    """ Distributes an archive to web servers """
    if not isfile(archive_path):
        return False
    try:
        localpath = archive_path.split('/')[1]
        newpath = localpath.split('.')[0]
        rempath = "/data/web_static/releases/"

        put(archive_path, "/tmp/".format(localpath))
        run("mkdir -p {}{}".format(rempath, newpath))
        run("tar -xzf /tmp/{} -C {}{}".format(localpath, rempath, newpath))
        run("rm /tmp/{}".format(localpath))
        run("mv {0}{1}/web_static/* {0}{1}/".format(rempath, newpath))
        run("rm -rf {}{}/web_static".format(rempath, newpath))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(rempath, newpath))
        return True
    except:
        return False
