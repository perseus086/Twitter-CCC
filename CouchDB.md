<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title></title>
</head>
<body>
Installing CouchDB and configuring to save the DB in a mounted disk<br>
<br>
# all of the following commands should be performed creating a python
file with fabric libraries to do #it automatically<br>
# after the creation of the instance and the volume. We need to attach
the volume to its instance.<br>
# to see if the disk is attached<br>
sudo fdisk -l <br>
# format disk<br>
sudo mkfs.ext4 /dev/vdc<br>
<br>
#create a folder to manually mount the disk<br>
sudo mkdir /mnt/data<br>
<br>
#mount the disc<br>
sudo mount /dev/vdc /mnt/data<br>
<br>
#give permission to ubutntu user to save in the disk<br>
sudo chown -R ubuntu /mnt/data<br>
<br>
#modify /etc/fstab in order to mount the disk automaticlly when it
reboots<br>
sudo vi /etc/fstab<br>
<br>
#add this line at the end of the file<br>
/dev/vdc&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
/mnt/data&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; auto&nbsp;&nbsp;&nbsp;
defaults&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1<br>
<br>
<br>
#create a folder to install CouchDB database<br>
sudo mkdir /mnt/data/couchdb<br>
<br>
#reboot the instance<br>
sudo reboot<br>
<br>
#update apt<br>
sudo apt-get update<br>
<br>
#finally installing couchdb<br>
sudo apt-get install couchdb -y<br>
<br>
#install curl:<br>
sudo apt-get install curl<br>
<br>
#test couchdb<br>
curl localhost:5984<br>
<br>
#give CouchDB permissions to read and write in the folder that is
located in the volume<br>
sudo chown -R couchdb:couchdb /mnt/data/couchdb/<br>
<br>
#backup default.ini (just in case that we need, it is not necesary)<br>
<br>
cd /etc/couchdb<br>
sudo cp default.ini default.ini.back<br>
<br>
#open the port to acces FUTON in default.ini<br>
#it seems like this:<br>
#&nbsp;&nbsp;&nbsp; [couchdb]<br>
#&nbsp;&nbsp;&nbsp; ;database_dir = /var/lib/couchdb<br>
#&nbsp;&nbsp;&nbsp; ;view_index_dir = /var/lib/couchdb<br>
#&nbsp;&nbsp;&nbsp; database_dir = /mnt/data/couchdb<br>
#&nbsp;&nbsp;&nbsp; view_index_dir = /mnt/data/couchdb<br>
# [httpd]<br>
# port = 5984<br>
# bind_address = 0.0.0.0<br>
<br>
#reboot ubuntu<br>
sudo reboot<br>
<br>
#test &lt;ip_of_instance:5984&gt;<br>
<br>
</body>
</html>
