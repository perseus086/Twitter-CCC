#Orchestration

Cloud orchestration involves the creation, management and manipulation of cloud resources, i.e., compute, storage and network, in order to realize user requests in a cloud environment (Liu, Loo, & Mao, 2011)
Since cloud was meant to provision resources on demand, these resources should be deployed very fast to the end user.  Orchestration allows deploying these resources automatically.  Without this, it would be difficult to have a system working immediately.


Fabric is a Python (2.5 or higher) library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. http://docs.fabfile.org/en/1.4.3/index.html

Boto is a Python package that provides interfaces to Amazon Web Services. https://github.com/boto/boto

For running the code it is necessary to install the following packages:

sudo pip python
sudo pip paramiko
sudo pip fabric
sudo pip boto

It is important to install fabric before boto because otherwise it will raise an error.

1.- create a boto config file in the home directory of your account: ~/.boto
    it should contain the credentials for connecting to the cloud
    <code>[Credentials] <br>
aws_access_key_id = <<your_id>> <br>
aws_secret_access_key = <<your_access_key>></code>

2.- Then run the following commands
	

<code>	fab create_couch setcouchc couch_server  </code>	
<code>	fab create_appserver sethosta app_server  </code>


