import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_nodejs(host):
    assert host.file("/opt/nodejs/node-v12.16.0-linux-x64").exists
    assert host.file("/opt/nodejs/node-v8.11.3-linux-x64").exists

    cmd = host.run("PATH=PATH:/opt/nodejs/node-v12.16.0-linux-x64/bin node --version")
    assert cmd.stdout == """v12.16.0
"""

    cmd = host.run("PATH=PATH:/opt/nodejs/node-v8.11.3-linux-x64/bin node --version")
    assert cmd.stdout == """v8.11.3
"""

    cmd = host.run("PATH=PATH:/opt/nodejs/node-v12.16.0-linux-x64/bin npm --version")
    assert cmd.stdout == """6.13.4
"""

    cmd = host.run("PATH=PATH:/opt/nodejs/node-v8.11.3-linux-x64/bin npm --version")
    assert cmd.stdout == """5.6.0
"""

    cmd = host.run("PATH=PATH:/opt/nodejs/node-v12.16.0-linux-x64/bin npx --version")
    assert cmd.stdout == """6.13.4
"""

    cmd = host.run("PATH=PATH:/opt/nodejs/node-v8.11.3-linux-x64/bin npx --version")
    assert cmd.stdout == """9.7.1
"""
