#!/usr/bin/python3
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

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [sudo("rm -rf ./{}".format(a)) for a in archives]
