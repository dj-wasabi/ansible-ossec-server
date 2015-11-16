require 'serverspec'
require 'spec_helper'

describe 'Ossec Server Packages' do
    describe package('ossec-hids') do
        it { should be_installed }
    end
    describe package('ossec-hids-server') do
        it { should be_installed }
    end
end

describe 'Ossec Server Services' do
    describe service('ossec-hids') do
        it { should be_enabled }
    end
    describe service('ossec-maild') do
        it { should be_running }
    end
    describe service('ossec-execd') do
        it { should be_running }
    end
    describe service('ossec-analysisd') do
        it { should be_running }
    end
    describe service('ossec-logcollector') do
        it { should be_running }
    end
    describe service('ossec-syscheckd') do
        it { should be_running }
    end
    describe service('ossec-monitord') do
        it { should be_running }
    end
end

describe 'Ossec Server Configuration' do
    describe file('/var/ossec/etc/ossec-server.conf') do
        it { should be_file}
        it { should be_owned_by 'root'}
        it { should be_grouped_into 'root'}

        it { should contain "<ossec_config>" }
        it { should contain "<smtp_server>mail.example.com</smtp_server>" }
        it { should contain "<email_to>me@example.com</email_to>" }
        it { should contain "<email_from>ossec@example.com</email_from>" }
        it { should contain "<system_audit>/var/ossec/etc/shared/cis_rhel6_linux_rcl.txt</system_audit>" }
        it { should contain "<log_alert_level>1</log_alert_level>" }
        it { should contain "<email_alert_level>7</email_alert_level>" }
        it { should contain "</ossec_config>" }
    end
end
