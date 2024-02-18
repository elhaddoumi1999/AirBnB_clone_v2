#!/usr/bin/python3
<<<<<<< HEAD
"""
Generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Function that makes a packs """
    try:
        now = datetime.now()
        date_create = now.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        do_tgz = "web_static_{}.tgz".format(date_create)
        local("tar -cvzf versions/{} web_static".format(do_tgz))
        return do_tgz
    except:
        return None
=======
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


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
>>>>>>> a1a68afd0dca7866b0e2a5e292f4e0a52be6468c
