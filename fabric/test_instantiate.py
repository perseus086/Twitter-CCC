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

ip = []


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
    print(_yellow("...Creating CouchDB instance..."))
    
    images = conn.get_all_images()
    try:
        reservation = images[215].run(1, 1, key_name='eli', security_groups=['default','CouchDb'], instance_type='m1.small',
                                      user_data=open("user_data_1.sh").read(),
                                      placement="melbourne-np")
        print(_green("CouchDB instance created.  Reservation id: " + reservation.id))
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
    print _green("CouchDB IP: ")
    print _green(ip[items])
    return ip[items]


def create_serverapp(conn):
    """
    Creates Applications Server Instance
    """
    print(_yellow("...Creating Applications Server ..."))

    images = conn.get_all_images()
    try:
        reservation = images[215].run(1, 1, key_name='eli', security_groups=['default'], instance_type='m1.small',
                                      user_data=open("/Users/elikary/SkyDrive/Documentos/Melbourne/University/2nd/cloudcomputing/proj2/scripts/fabric/user_data_2.sh").read(),
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


def create_couch():
    c = connect()
    result = create_servercouch(c)
    return result


def create_appserver():
    d = connect()
    result2 = create_serverapp(d)
    return result2





