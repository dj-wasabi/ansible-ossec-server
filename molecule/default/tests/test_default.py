import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ossec_packages(Package):
    ossec = Package('ossec-hids')
    assert ossec.is_installed


def test_ossec_configuration(File):
    ossec = File("/var/ossec/etc/ossec.conf")
    assert ossec.user == "root"
    assert ossec.group == "root"

    assert ossec.contains("<email_to>me@example.com</email_to>")
    assert ossec.contains("<ignore>/etc/hosts.deny</ignore>")
    assert ossec.contains("<white_list>127.0.0.1</white_list>")
