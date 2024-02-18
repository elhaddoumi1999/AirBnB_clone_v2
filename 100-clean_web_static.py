#!/usr/bin/python3
<<<<<<< HEAD
""" Deletes out-of-date archives """
from os import listdir
from fabric.api import sudo, local, cd, lcd, env, run

env.hosts = ['104.196.171.213', '35.231.225.57']

def do_clean(number=0):
    """ Deletes out-of-date archives locally and on my remote hosts """

    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    old_new = sorted(listdir("versions"))
    [old_new.pop() for i in range(number)]
    with lcd("versions"):
            [local("rm ./{}".format(arch)) for arch in old_new]
=======
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]
>>>>>>> a1a68afd0dca7866b0e2a5e292f4e0a52be6468c

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
<<<<<<< HEAD
        [sudo("rm -rf ./{}".format(a)) for a in archives]
=======
        [run("rm -rf ./{}".format(a)) for a in archives]
>>>>>>> a1a68afd0dca7866b0e2a5e292f4e0a52be6468c
