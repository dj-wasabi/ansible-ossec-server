Role Name
=========

This role will install the ossec server on a host.

Requirements
------------

This role will work on:
 * Red Hat
 * Debian

So, you'll need one of those operating systems.. :-)

Role Variables
--------------

This role has some variables which you can or need to override.
```
ossec_server_config: []
ossec_agent_configs: []
```

###Example setup

Edit the vars file for the host which runs the ossec-server: 
### host_vars/ossec-server
	ossec_server_config:
	  mail_to:
	    - me@example.com
	  mail_smtp_server: mail.example.com
	  mail_from: ossec@example.com
	  frequency_check: 72000
	  ignore_files:
	    - /etc/mtab
	    - /etc/mnttab
	    - /etc/hosts.deny
	  directories:
	    - check_all: 'yes'
	      dirs: /etc,/usr/bin,/usr/sbin
	    - check_all: 'yes'
	      dirs: /bin,/sbin
	  localfiles:
	    - format: 'syslog'
	      location: '/var/log/messages'
	    - format: 'syslog'
	      location: '/var/log/secure'
	  globals:
	    - '127.0.0.1'
	    - '192.168.2.1'
	  connection: 'secure'
	  log_level: 1
	  email_level: 7
	  commands:
	    - name: 'host-deny'
	      executable: 'host-deny.sh'
	      expect: 'srcip'
	      timeout_allowed: 'yes'
	  active_responses:
	    - command: 'host-deny'
	      location: 'local'
	      level: 6
	      timeout: 600
	  localfiles:
	    - format: 'syslog'
	      location: '/var/log/messages'
	    - format: 'syslog'
	      location: '/var/log/secure'

	ossec_agent_configs:
 	  - type: os
    	type_value: linux
    	frequency_check: 79200
		ignore_files:
		  - /etc/mtab
		  - /etc/mnttab
		  - /etc/hosts.deny
		  - /etc/mail/statistics
		  - /etc/svc/volatile
		directories:
		  - check_all: yes
			dirs: /etc,/usr/bin,/usr/sbin
		  - check_all: yes
			dirs: /bin,/sbin
		localfiles:
		  - format: 'syslog'
			location: '/var/log/messages'
		  - format: 'syslog'
			location: '/var/log/secure'
		  - format: 'syslog'
			location: '/var/log/maillog'
		  - format: 'apache'
			location: '/var/log/httpd/error_log'
		  - format: 'apache'
			location: '/var/log/httpd/access_log'
		  - format: 'apache'
			location: '/var/ossec/logs/active-responses.log'

####ossec_server_config:
At first, there is the server configuration. Change it for your needs, as this default setup won't do any good for you. (You don't have access to use the mail.example.com mailhost. :-))


####ossec_agent_configs:
http://ossec-docs.readthedocs.org/en/latest/manual/agent/agent-configuration.html

There are 3 "types":
  * os
  * name
  * profile

In the above setup, the type is os. And this configuration is for the "linux" os. You can have several types configured in the host_vars file, so you can create all kind of different configs.

You can find here some more information about the ossec shared agent configuration: http://ossec-docs.readthedocs.org/en/latest/manual/syscheck/

#### <_role_>/vars/main.yml
nil

Dependencies
------------

No dependencies.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: ossec-server.example.com
      roles:
         - { role: dj-wasabi.ossec-server }

##Molecule

This roles is configured to be tested with Molecule. You can find on this page some more information regarding Molecule: https://werner-dijkerman.nl/2016/07/10/testing-ansible-roles-with-molecule-testinfra-and-docker/
Molecule will boot 2 docker containers, containing the following OS:

* Debian 8
* CentOS 7


License
-------

GPLv3

Author Information
------------------

Please send suggestion or pull requests to make this role better. 

Github: https://github.com/dj-wasabi/ansible-ossec-server

mail: ikben [ at ] werner-dijkerman . nl
