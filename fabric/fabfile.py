from __future__ import with_statement
from fabric.api import sudo, env, run, put
import logging
logging.getLogger('paramiko.transport').addHandler(logging.NullHandler())
from paramiko import RSAKey
from fabric.colors import green as _green, yellow as _yellow
from fabric.context_managers import cd


# env.hosts = ['115.146.92.147']
# env.user = "ubuntu"
env.key_filename = "/Users/elikary/Downloads/eli.pem"


def sed_couch():
   	sudo('sed -i "s/bind_address = 127.0.0.1/bind_address = 0.0.0.0/" /etc/couchdb/default.ini')
   	sudo('service couchdb restart')


def git_clone():
    sudo('mkdir /mnt/data')
    print (_yellow("Cloning Twitter project"))
    directory = '/mnt/data'
    with cd(directory):
        sudo('git clone https://github.com/perseus086/Twitter-CCC')


def copy_keys():
    print(_yellow("Copying public key to the server"))
    dir = '/mnt/data/Twitter-CCC/public_keys'
    with cd(dir):
        sudo('cat jz.pub >> ~/.ssh/authorized_keys')
        sudo('cat id_rsa.pub >> ~/.ssh/authorized_keys')


def set_web():
    """Install a LAMP stack on the server."""
    # Install the packages
    print(_yellow("Installing Apache"))
    sudo("apt-get -q update")
    packages = "apache2 libapache2-mod-php5"
    sudo("apt-get install -q -y %s" % packages)

    with cd('/mnt/data/Twitter-CCC'):
        sudo('cp index.php /var/www/index.php')


def app_server():
    git_clone()
    copy_keys()
    set_web()
    print(_green("Application Server Done!"))


def couch_server():
    sed_couch()
    git_clone()
    copy_keys()
    print(_green("DataBase server Done!"))
