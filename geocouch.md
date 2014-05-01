Geocouch Installation
===========

1. Install couchdb dependencies:
    
	sudo apt-get install build-essential  
    	sudo apt-get install erlang-base-hipe  
    	sudo apt-get install erlang-dev  
    	sudo apt-get install erlang-manpages  
    	sudo apt-get install erlang-eunit  
    	sudo apt-get install erlang-nox  
    	sudo apt-get install libicu-dev  
    	sudo apt-get install libmozjs-dev  
    	sudo apt-get install libcurl4-openssl-dev  
    	sudo apt-get install pkg-config  

2. Download and extract http://mirror.sdunix.com/apache/couchdb/source/1.5.0/apache-couchdb-1.5.0.tar.gz
3. cd apache-couchdb-1.5.0/
4. execute:
	./configure && make
	### install
	sudo make install

	### remove leftovers from ubuntu packages
	sudo rm /etc/logrotate.d/couchdb /etc/init.d/couchdb

	### install logrotate and initd scripts
	sudo ln -s /usr/local/etc/logrotate.d/couchdb /etc/logrotate.d/couchdb  
	sudo ln -s /usr/local/etc/init.d/couchdb  /etc/init.d  
	sudo update-rc.d couchdb defaults  
5. Create missing folders:
	mkdir tmp/log  
	mkdir tmp/run  
	mkdir etc/couchdb/default.d/  
6. git clone https://github.com/couchbase/geocouch.git
7. cd geocouch
7. git chekout couchdb1.3.x
8. export COUCH_SRC=<couch-source-path>/src/couchdb
9. make
10. cp <geocouch-path>/etc/couchdb/default.d/geocouch.ini <couchdb-source-path>/etc/couchdb/default.d/
11. Futon tests:
	cp <geocouch>/share/www/script/test/* <vanilla-couch>/share/www/script/test/
	Add the test to <vanilla-couch>/share/www/script/couch_tests.js

	loadTest("spatial.js");  
	loadTest("list_spatial.js");  
	loadTest("etags_spatial.js");  
	loadTest("multiple_spatial_rows.js");  
	loadTest("spatial_compaction.js");  
	loadTest("spatial_design_docs.js");  
	loadTest("spatial_bugfixes.js");  
	loadTest("spatial_merging.js");  
	loadTest("spatial_offsets.js");  
12. Run couchdb with geocouch
	export ERL_FLAGS="-pa <geocouch-path>/ebin"
	ERL_FLAGS="-pa <geocouch-path>/ebin" <couchdb-source-path>/utils/run
