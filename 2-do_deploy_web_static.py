#!/usr/bin/python3
<<<<<<< HEAD
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
=======
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
>>>>>>> a1a68afd0dca7866b0e2a5e292f4e0a52be6468c
