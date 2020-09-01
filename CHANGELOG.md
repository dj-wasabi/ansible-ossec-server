# ansible-ossec-server Release

Below an overview of all changes in the releases.

Version (Release date)

0.6.1   (2020-09-01)

  * Allow to override GPG checking while installing release.rpm file.

0.6.0   (2020-08-31)

  * Update to current ansible/molecule/testinfra and fix CentOS7 init. #31 (By pull request: skyscooby (Thanks!))
  * Amazon Linux & Local Postfix Relay #33 (By pull request: sblack4 (Thanks!))
  * Moved from travis to Github Actions.

0.5.0   (2018-09-11)

  * Added tests;Removing pyc file #21
  * Fixes #22 (By pull request: elrondvega (Thanks!))
  * Use specific version of libraries #24
  * Bunch of files #25
  * Moved some client-syslog after the installation of the configuration … #26
  * Added Ubuntu #27
  * Fixes issue #28 (By pull request: dale-c-anderson (Thanks!))
  * Fix check-mode with syslog-output configured #30 (By pull request: sigio (Thanks!))

0.4.0   (2017-12-27)

  * Fix some formatting issues with the example config in the readme file #19 (By pull request: dale-c-anderson (Thanks!))
  * Using Molecule V2 #18
  * Update atomic-release #17 (By pull request: aarnaud (Thanks!))

0.3.0   (2017-05-14)

  * refactor cis_distribution_filename usage to be more dry #16 (By pull request: s01ipsist (Thanks!))
  * Fixing molecule #15
  * Fix ossec upstream repository #14 (By pull request: s01ipsist (Thanks!))
  * Fix debian repository + systemd daemon reload #13  (By pull request: s01ipsist (Thanks!))

0.2.0   (2017-02-14)

  * Added molecule testing
  * do not look for specific key ID. It appears that OSSEC released a new… #3 (By pull request: recunius (Thanks!))
  * Updates #4 (By pull request: recunius (Thanks!))
  * allow providing own local_rules.xml template with var ossec_server_… #5  (By pull request: recunius (Thanks!))
  * Update CIS filename to CentOS & Redhat 7 #6 (By pull request: jlruizmlg (Thanks!))
  * add ossec authd as service #7 (By pull request: jlruizmlg (Thanks!))
  * Fix the permissions in the wazuh-authd in upstart system. #8  (By pull request: jlruizmlg (Thanks!))
  * Remove ssl files and add task to generate them + Fix script init task #10 (By pull request: aarnaud (Thanks!))

0.1.0   (2015-11-16)

  * Fixes for CentOS/EL7 #1 (By pull request: andskli (Thanks!))
  * Updates to support Ubuntu and also adds more configuration options #2 (By pull request: recunius (Thanks!))
  * Added kitchen test and serverspec tests

0.0.2   (2014-12-11)

  * Added possibilty to use other mail settings
  * Reworked module for better setup. Updated readme

0.0.1   (2014-12-04)

  * Initial creation
