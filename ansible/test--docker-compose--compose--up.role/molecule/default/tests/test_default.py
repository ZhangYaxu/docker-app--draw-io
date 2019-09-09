import pytest
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    '/bash-commands/docker-compose--compose--up.sh',
    '/bash-util/elevate.sh',
    '/bash-util/functions.sh',
    '/docker/server--draw-io/default.docker',
    '/docker-compose/server--draw-io/default.docker-compose',
    '/host.env',
])
def test_that_required_files_are_existing(host, name):
    test_dir = '../../../../tests/test--docker-compose--compose--up'

    f = host.file(test_dir + name)

    assert f.exists


def test_that_required_docker_container_is_existing(host):
    c = host.docker.get_containers(name='server--draw-io', status='running')

    assert len(c) == 1
