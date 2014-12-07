Role Name
=========

This role will install the ossec server on a host.

Requirements
------------

This role will work on:
 * Red Hat
 * Debian
 * Ubuntu

So, you'll need one of those operating systems.. :-)

Role Variables
--------------

The roles has some arrays you can override:
`linux_frequency_check`: The amount of seconds it will do an frequency check. (Default 22 hours)
`windows_frequency_check`: The amount of seconds it will do an frequency check. (Default 22 hours)


`linux_ignore_files`: List of all files that can be ignored on a linux host.
```yaml
linux_ignore_files:
  - /etc/mtab
  - /etc/mnttab
  - /etc/hosts.deny
```

`ignore_windows_files`: List of all files that can be ignored on a Windows host.
```yaml
windows_ignore_files:
  - C:\WINDOWS/System32/LogFiles
  - C:\WINDOWS/Debug
  - C:\WINDOWS/WindowsUpdate.log
```

`monitor_files`: This has a mulitple key value pair for monitoring the logfiles. "format" will describe what kind of file it is, "location" is the path to the file.
```yaml
monitor_files:
  - { format: 'syslog', location: '/var/log/messages' }
  - { format: 'syslog', location: '/var/log/secure' }
  - { format: 'syslog', location: '/var/log/maillog' }
```

In the vars file, there is the following parameter:
`ossec_release_rpm`: This is the name of the ossec-release rpm file (Default: ossec-release-1.0-2.el6.art.noarch.rpm)

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: ossec-server.example.com
      roles:
         - { role: dj-wasabi.ossec-server }

License
-------

GPLv3

Author Information
------------------

Please send suggestion or pull requests to make this role better. 

Github: https://github.com/dj-wasabi/ansible-ossec-server

mail: ikben [ at ] werner-dijkerman . nl