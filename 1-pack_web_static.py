#!/usr/bin/python3
# fabfile that generates a .tgz archive of web_static content
import os.path
from fabric.api import local
from datetime import datetime


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
    # create vetsions folder if it doesnt exist
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    return file_name
