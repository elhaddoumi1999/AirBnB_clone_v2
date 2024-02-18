#!/usr/bin/python3
"""
Generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo
"""
import os.path
from fabric.api import *
from datetime import datetime

env.hosts = ['104.196.171.213', '35.231.225.57']


def deploy():
    """ creates and distributes an archive to the web servers """
    full_deploy = do_pack()
    if os.path.exists(full_deploy) is False:
        return False
    return do_deploy(full_deploy)


def do_pack():
    """ Function that makes packages"""
    try:
        now = datetime.now()
        date_create = now.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        do_tgz = "versions/web_static_{}.tgz".format(date_create)
        local("tar -cvzf {} web_static".format(do_tgz))
        return do_tgz
    except:
        return None


def do_deploy(archive_path):
    """ distributes an archive to a web server """
    if os.path.exists(archive_path) is False:
        return False
    try:
        path_id = archive_path.split('/')
        a = path_id[1].split('.')
        put(archive_path, "/tmp")
        run("mkdir -p /data/web_static/releases/{}".format(a[0]))
        run("tar -xzf /tmp/{} -C\
        /data/web_static/releases/{}".format(path_id[1], a[0]))
        run("rm /tmp/{}".format(path_id[1]))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(a[0], a[0]))
        run("rm -rf /data/web_static/releases/{}/web_static".format(a[0]))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/\
        /data/web_static/current".format(a[0]))
        print("New version deployed!")
        return True
    except:
        return False
