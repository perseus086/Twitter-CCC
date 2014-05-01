Installing CouchDB and configuring to save the DB in a mounted disk

# all of the following commands should be performed creating a python file with fabric libraries to do #it automatically
# after the creation of the instance and the volume. We need to attach the volume to its instance.
# to see if the disk is attached
sudo fdisk -l 
# format disk
sudo mkfs.ext4 /dev/vdc

#create a folder to manually mount the disk
sudo mkdir /mnt/data

#mount the disc
sudo mount /dev/vdc /mnt/data

#give permission to ubutntu user to save in the disk
sudo chown -R ubuntu /mnt/data

#modify /etc/fstab in order to mount the disk automaticlly when it reboots
sudo vi /etc/fstab

#add this line at the end of the file
/dev/vdc        /mnt/data       auto    defaults        0       1


#create a folder to install CouchDB database
sudo mkdir /mnt/data/couchdb

#reboot the instance
sudo reboot

#update apt
sudo apt-get update

#finally installing couchdb
sudo apt-get install couchdb -y

#install curl:
sudo apt-get install curl

#test couchdb
curl localhost:5984

#give CouchDB permissions to read and write in the folder that is located in the volume
sudo chown -R couchdb:couchdb /mnt/data/couchdb/

#backup default.ini (just in case that we need, it is not necesary)

cd /etc/couchdb
sudo cp default.ini default.ini.back

#open the port to acces FUTON in default.ini
#it seems like this:
#	[couchdb]
#	;database_dir = /var/lib/couchdb
#	;view_index_dir = /var/lib/couchdb
#	database_dir = /mnt/data/couchdb
#	view_index_dir = /mnt/data/couchdb
# [httpd]
# port = 5984
# bind_address = 0.0.0.0

#reboot ubuntu
sudo reboot

#test <ip_of_instance:5984>
