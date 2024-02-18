#!/usr/bin/python3
<<<<<<< HEAD
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
=======
# Fabfile to create and distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


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


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
>>>>>>> a1a68afd0dca7866b0e2a5e292f4e0a52be6468c
