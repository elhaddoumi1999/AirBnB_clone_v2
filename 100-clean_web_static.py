#!/usr/bin/python3
"""
keep it clean module
"""
import os
from fabric.api import *

env.hosts = ["100.25.179.61", "18.207.140.4"]


def do_clean(number=0):
    """
    Deletes out of date archives
    """
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
