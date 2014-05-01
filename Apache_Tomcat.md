<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title></title>
</head>
<body>
Installing Java and Apache TomCat<br>
<br>
<br>
sudo apt-get update<br>
<br>
sudo apt-get install default-jre<br>
<br>
sudo apt-get install default-jdk<br>
<br>
<br>
-- openjdk<br>
sudo apt-get install openjdk-7-jre <br>
sudo apt-get install openjdk-7-jdk<br>
<br>
-- oraclejdk<br>
sudo apt-get install python-software-properties<br>
sudo add-apt-repository ppa:webupd8team/java<br>
sudo apt-get update<br>
<br>
sudo apt-get install oracle-java7-installer<br>
<br>
-- choosing default jdk<br>
sudo update-alternatives --config java<br>
<br>
<br>
--
http://install-things.com/2013/05/07/how-to-install-apache-tomcat-7-0-35-on-ubuntu-13-04-linux/<br>
<br>
-- but in step 4<br>
<br>
-- edit this line and uncomment: JAVA_HOME=/usr/lib/jvm/java-7-oracle<br>
<br>
<br>
-- then stop tomcat and modify:<br>
cd /var/lib/tomcat7/conf<br>
sudo vi server.xml<br>
-- edit the following lines:<br>
--&nbsp; &nbsp;&nbsp; &lt;Connector port="8080" protocol="HTTP/1.1"<br>
-- &nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
address="0.0.0.0"<br>
-- &nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
connectionTimeout="20000"<br>
-- &nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
URIEncoding="UTF-8"<br>
-- &nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
redirectPort="8443" /&gt;<br>
<br>
sudo service tomcat7 start<br>
<br>
-- test in a browser<br>
—————<br>
-- also we can install:<br>
apt-get install tomcat7-admin<br>
apt-get install tomcat7-docs<br>
apt-get install tomcat7-examples<br>
<br>
-- then restart the services:<br>
sudo service tomcat7 stop<br>
-- edit the file:<br>
cd /var/lib/tomcat7/conf<br>
sudo vi&nbsp; tomcat-users.xml<br>
-- and add the line: <br>
-- &lt;user username="admin" password="amdin"
roles="admin-gui,standard,manager-gui"/&gt;<br>
<br>
<br>
sudo service tomcat7 start<br>
<br>
# test: http://115.146.95.26:8080/<br>
#the links for the admin interfaces are: tomcat7-admin: This package
installs…<br>
#login:admin&nbsp;&nbsp; &nbsp;password:admin<br>
#
</body>
</html>

