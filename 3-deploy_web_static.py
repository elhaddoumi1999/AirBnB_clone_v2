#!/usr/bin/python3
# fabfile that creates an archive and distributes it to a webserver
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["35.243.225.166", "35.231.8.188"]


def do_pack():
    """
    creates a .tgz archive of web_static contents
    """
    dt = datetime.utcnow()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                              dt.month,
                                                              dt.day,
                                                              dt.hour,
                                                              dt.minute,
                                                              dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    return file_name


def do_deploy(archive_path):
    """distributes an archive to our web_servers"""
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


def deploy():
    """create and distribute archive to web server"""
    file = do_pack()
    if file is None:
        return False

    return do_deploy(file)
