import pytest


def test_ossec_package_installed(host):
    ossec = host.package('ossec-hids-server')
    assert ossec.is_installed


@pytest.mark.parametrize("ossec_service", (
        ("ossec-monitord"),
        ("ossec-syscheckd"),
        ("ossec-maild"),
        ("ossec-execd"),
        ("ossec-analysisd"),
        ("ossec-logcollector"),
        ("ossec-syscheckd"),
))
def test_ossec_service_running(host, ossec_service):
    cmd = host.run("ps -ef")
    assert ossec_service in cmd.stdout


def test_ossec_rootcheck_control(host):
    cmd = host.run("/var/ossec/bin/rootcheck_control -u all")
    assert 'Policy and auditing database updated.' in cmd.stdout
    assert cmd.rc == 0


def test_ossec_verify_agent_conf(host):
    cmd = host.run("/var/ossec/bin/verify-agent-conf")
    assert 'verify-agent-conf: Verifying [/var/ossec/etc/shared/agent.conf].' in cmd.stdout
    assert cmd.rc == 0


def test_sockets_open(host):
    if host.system_info.distribution == 'centos':
        assert host.socket("tcp://:::1515").is_listening


def test_ossec_configuration(host):
    ossec = host.file("/var/ossec/etc/ossec.conf")
    assert ossec.user == "root"
    assert ossec.group == "root"
    assert ossec.contains("<email_to>me@example.com</email_to>")
    assert ossec.contains("<ignore>/etc/hosts.deny</ignore>")
    assert ossec.contains("<white_list>127.0.0.1</white_list>")
