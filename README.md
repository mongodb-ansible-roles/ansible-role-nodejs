Ansible role for nodejs
==================================

Installs multiple versionf of NodeJS into a toolchain

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-nodejs/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-nodejs/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-nodejs/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-nodejs/actions?query=workflow%3A%22Release%22)

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `nodejs_versions` | List of versions of NodeJS to install. A list of versions can be found here: https://nodejs.org/dist/ | list | - v12.16.0<br>- v8.11.3 | no |

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-nodejs
      vars:
        nodejs_versions:
          - v12.16.0
          - v8.11.3
```

License
-------

[Apache License](LICENSE)
