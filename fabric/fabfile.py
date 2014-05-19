from fabric.api import *
from fabric.api import sudo, env
import logging

logging.getLogger('paramiko.transport').addHandler(logging.NullHandler())
from paramiko import RSAKey
from fabric.colors import green as _green, yellow as _yellow
import boto
import boto.ec2
from boto.ec2.regioninfo import RegionInfo
from config import *
import time
import paramiko
import sys


def connect():
    print(_yellow("Connecting to the cloud"))
    region = RegionInfo(name='melbourne-np', endpoint='nova.rc.nectar.org.au')
    print region
    conn = boto.connect_ec2(is_secure=True, port=8773, path='/services/Cloud', region=region, validate_certs=False)
    return conn


def create_servercouch(conn):
    """
    Creates CouchDB Instance
    """
    ip = []
    print(_yellow("...Creating CouchDB instance..."))
    script1 = """#!/bin/bash
        #
        sudo apt-get update
        sudo apt-get install couchdb -y
        sudo apt-get install curl
        sudo apt-get install git -y
        """

    try:

        reservation = conn.run_instances('ami-00001e9d',
                                         key_name='eli',
                                         instance_type='m1.small',
                                         security_groups=['default', 'CouchDb'],
                                         user_data=script1,
                                         placement="melbourne-np")

        print(_green("CouchDB instance started.  Reservation id: " + reservation.id))
    except:
        print "Error:", sys.exc_info()[1]
        sys.exit(1)
    reservations = conn.get_all_reservations()
    for res in reservations:
        instances = res.instances
        for ins in instances:
            status = ins.update()
            print(_yellow(status))
            while status == 'pending':
                time.sleep(10)
                status = ins.update()
            if status == 'running':
                ip.append(ins.ip_address)
                print _green('running')
    items = len(ip) - 1
    print _green("AppServer IP: ")
    print _green(ip[items])
    return ip[items]


def create_serverapp(conn):
    """
    Creates Applications Server Instance
    """
    ip = []
    print(_yellow("...Creating Applications Server ..."))
    script2 = """#!/bin/bash
        #
        sudo apt-get update
        sudo apt-get install git -y
        """
    try:
        reservation = conn.run_instances('ami-00001e9d',
                                         key_name='eli',
                                         instance_type='m1.small',
                                         security_groups=['default'],
                                         user_data=script2,
                                         placement="melbourne-np")
        print(_green("Applications Server  created.  Reservation id: " + reservation.id))
    except:
        print "Error:", sys.exc_info()[1]
        sys.exit(1)
    reservations = conn.get_all_reservations()
    for res in reservations:
        instances = res.instances
        for ins in instances:
            status = ins.update()
            print(_yellow(status))
            while status == 'pending':
                time.sleep(10)
                status = ins.update()
            if status == 'running':
                ip.append(ins.ip_address)
                print _green('running')
                # print(_green(ins.id + " " + ins.ip_address))
    print "IPs in the reservation: ", ip
    items = len(ip) - 1
    print _green("AppServer IP: ")
    print _green(ip[items])
    return ip[items]


def sethost():
    time.sleep(40)
    listh = hosts()
    env.host_string = str(listh[0])
    print env.hosts
    env.user = "ubuntu"
    env.key_filename = "/Users/elikary/Downloads/eli.pem"


def hosts():
    ip = []
    cnx = connect()
    reservations = cnx.get_all_reservations()
    for res in reservations:
        instances = res.instances
        for ins in instances:
            status = ins.update()
            while status == 'pending':
                time.sleep(10)
                status = ins.update()
            if status == 'running':
                ip.append(ins.ip_address)
    print "IPs in the reservation: ", ip
    return ip


# executing everything

def create_couch():
    c = connect()
    result = create_servercouch(c)
    return result


def create_appserver():
    d = connect()
    result2 = create_serverapp(d)
    return result2


# setting up configuration on servers

def sed_couch():
    time.sleep(5)
    sudo('sed -i "s/bind_address = 127.0.0.1/bind_address = 0.0.0.0/" /etc/couchdb/default.ini')
    sudo('service couchdb restart')


def git_clone():
    sudo('mkdir /mnt/data')
    print (_yellow("Cloning Twitter project"))
    directory = '/mnt/data'
    with cd(directory):
        sudo('git clone https://github.com/perseus086/Twitter-CCC')


def git_web():
    with cd('/var'):
        sudo('rm -rf www')
        sudo('git clone https://github.com/josebui/Twitter-CCC-webapp www')
        sudo('service apache2 restart')


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
    packages = "php5 apache2 libapache2-mod-php5 php5-json"
    sudo("apt-get install -q -y %s" % packages)
    git_web()


def install_harvester():
    with cd('/home/ubuntu/'):
        run('wget https://pypi.python.org/packages/source/C/CouchDB/CouchDB-0.9.tar.gz')
        sudo('tar -zxvf CouchDB-0.9.tar.gz')
        with cd('CouchDB-0.9'):
            sudo('python setup.py install')
    start_harvester()


def start_harvester():
    sudo('apt-get install python-tweepy')
    with cd('/mnt/data/Twitter-CCC/TweetStreamPython/newharverter'):
        sudo('curl -X PUT http://127.0.0.1:5984/melbourne')
        sudo('python melbne.py localhost  melbourne')


def app_server():
    git_clone()
    copy_keys()
    set_web()
    print(_green("Application Server Done!"))


def couch_server():
    sed_couch()
    git_clone()
    copy_keys()
    install_harvester()
    print(_green("DataBase server Done!"))







