	Creating and using keypairs
	http://sshkeychain.sourceforge.net/mirrors/SSH-with-Keys-HOWTO/SSH-with-Keys-HOWTO-4.html#ss4.1
	
<code>	ssh-keygen -t dsa  </code>
	Passphrase: a1b2c3d4e5
	Saved in ~/.ssh
	
	Now we have to files the key and key.pub
	The key.pub should be in the server
	Cat key.pub >> authorized_keys  in the server
	
	The first time for login should require the passphrase
	
	We were using ssh protocl version2 

