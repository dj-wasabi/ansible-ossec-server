# Changelog

## [Unreleased](https://github.com/dj-wasabi/ansible-ossec-server/tree/HEAD)

[Full Changelog](https://github.com/dj-wasabi/ansible-ossec-server/compare/0.6.2...HEAD)

**Merged pull requests:**

- Change SSL key size to 3072 bits [\#38](https://github.com/dj-wasabi/ansible-ossec-server/pull/38) ([jchen1](https://github.com/jchen1))

## [0.6.2](https://github.com/dj-wasabi/ansible-ossec-server/tree/0.6.2) (2021-01-31)

[Full Changelog](https://github.com/dj-wasabi/ansible-ossec-server/compare/0.6.1...0.6.2)

**Implemented enhancements:**

- Added GH Action to automatically update CHANGELOG.md [\#37](https://github.com/dj-wasabi/ansible-ossec-server/pull/37) ([dj-wasabi](https://github.com/dj-wasabi))

**Merged pull requests:**

- Changing requirements file;Adding pre-commit-hooks and fixes [\#36](https://github.com/dj-wasabi/ansible-ossec-server/pull/36) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.6.1](https://github.com/dj-wasabi/ansible-ossec-server/tree/0.6.1) (2020-09-01)

[Full Changelog](https://github.com/dj-wasabi/ansible-ossec-server/compare/0.6.0...0.6.1)

## [0.6.0](https://github.com/dj-wasabi/ansible-ossec-server/tree/0.6.0) (2020-08-31)

[Full Changelog](https://github.com/dj-wasabi/ansible-ossec-server/compare/0.5.0...0.6.0)

## [0.5.0](https://github.com/dj-wasabi/ansible-ossec-server/tree/0.5.0) (2018-09-11)

[Full Changelog](https://github.com/dj-wasabi/ansible-ossec-server/compare/0.4.0...0.5.0)

**Closed issues:**

- The `restart ossec-server` handler fails when using the `rules` tag [\#28](https://github.com/dj-wasabi/ansible-ossec-server/issues/28)
- Issue with syslog\_outputs [\#9](https://github.com/dj-wasabi/ansible-ossec-server/issues/9)

## [0.4.0](https://github.com/dj-wasabi/ansible-ossec-server/tree/0.4.0) (2017-12-27)

[Full Changelog](https://github.com/dj-wasabi/ansible-ossec-server/compare/0.3.0...0.4.0)

**Implemented enhancements:**

- Define a variable for atomicorp repo version [\#20](https://github.com/dj-wasabi/ansible-ossec-server/issues/20)

## [0.3.0](https://github.com/dj-wasabi/ansible-ossec-server/tree/0.3.0) (2017-05-13)

[Full Changelog](https://github.com/dj-wasabi/ansible-ossec-server/compare/0.2.0...0.3.0)

**Merged pull requests:**

- refactor cis\_distribution\_filename usage to be more dry [\#16](https://github.com/dj-wasabi/ansible-ossec-server/pull/16) ([s01ipsist](https://github.com/s01ipsist))
- Fixing molecule [\#15](https://github.com/dj-wasabi/ansible-ossec-server/pull/15) ([dj-wasabi](https://github.com/dj-wasabi))
- Fix debian repository + systemd daemon reload [\#13](https://github.com/dj-wasabi/ansible-ossec-server/pull/13) ([aarnaud](https://github.com/aarnaud))

## [0.2.0](https://github.com/dj-wasabi/ansible-ossec-server/tree/0.2.0) (2017-02-14)

[Full Changelog](https://github.com/dj-wasabi/ansible-ossec-server/compare/0.1.0...0.2.0)

**Implemented enhancements:**

- Enable testing with Molecule [\#11](https://github.com/dj-wasabi/ansible-ossec-server/issues/11)

**Merged pull requests:**

- Added molecule to test role [\#12](https://github.com/dj-wasabi/ansible-ossec-server/pull/12) ([dj-wasabi](https://github.com/dj-wasabi))
- Remove ssl files and add task to generate them + Fix script init task [\#10](https://github.com/dj-wasabi/ansible-ossec-server/pull/10) ([aarnaud](https://github.com/aarnaud))
- Fix the permissions in the wazuh-authd in upstart system. [\#8](https://github.com/dj-wasabi/ansible-ossec-server/pull/8) ([jlruizmlg](https://github.com/jlruizmlg))
- add ossec authd as service [\#7](https://github.com/dj-wasabi/ansible-ossec-server/pull/7) ([jlruizmlg](https://github.com/jlruizmlg))
- Update CIS filename to CentOS & Redhat 7 [\#6](https://github.com/dj-wasabi/ansible-ossec-server/pull/6) ([jlruizmlg](https://github.com/jlruizmlg))
- - allow providing own local\_rules.xml template with var ossec\_server\_… [\#5](https://github.com/dj-wasabi/ansible-ossec-server/pull/5) ([recunius](https://github.com/recunius))
- Updates [\#4](https://github.com/dj-wasabi/ansible-ossec-server/pull/4) ([recunius](https://github.com/recunius))
- do not look for specific key ID. It appears that OSSEC released a new… [\#3](https://github.com/dj-wasabi/ansible-ossec-server/pull/3) ([recunius](https://github.com/recunius))

## [0.1.0](https://github.com/dj-wasabi/ansible-ossec-server/tree/0.1.0) (2015-11-16)

[Full Changelog](https://github.com/dj-wasabi/ansible-ossec-server/compare/0.0.2...0.1.0)

**Merged pull requests:**

- Updates to support Ubuntu and also adds more configuration options [\#2](https://github.com/dj-wasabi/ansible-ossec-server/pull/2) ([recunius](https://github.com/recunius))
- Fixes for CentOS/EL7 [\#1](https://github.com/dj-wasabi/ansible-ossec-server/pull/1) ([andskli](https://github.com/andskli))

## [0.0.2](https://github.com/dj-wasabi/ansible-ossec-server/tree/0.0.2) (2014-12-11)

[Full Changelog](https://github.com/dj-wasabi/ansible-ossec-server/compare/0.0.1...0.0.2)

## [0.0.1](https://github.com/dj-wasabi/ansible-ossec-server/tree/0.0.1) (2014-12-07)

[Full Changelog](https://github.com/dj-wasabi/ansible-ossec-server/compare/055ca4cfce21919e56a4135912d50efb83227dd5...0.0.1)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
