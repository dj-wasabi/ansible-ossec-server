import testinfra.utils.ansible_runner
# import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


# @pytest.mark.parametrize("ossec_service", [
#     ("ossec-hids"),
#     ("ossec-authd"),
# ])
# def test_ossec_running_and_enabled(Service, ossec_service):
#     ossec = Service(ossec_service)
#     assert ossec.is_enabled
#     assert ossec.is_running

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
