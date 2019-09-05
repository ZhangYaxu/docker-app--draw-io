import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_that_required_files_are_existing(host):
    test_dir = '../../../../tests/test--docker-compose--compose--create'
    for name in (
        test_dir + '/bash-commands/docker-compose--compose--create.sh',
        test_dir + '/bash-util/elevate.sh',
        test_dir + '/bash-util/functions.sh',
        test_dir + '/docker/server--draw-io/default.docker',
        test_dir + '/docker-compose/server--draw-io/default.docker-compose',
        test_dir + '/host.env',
    ):
        f = host.file(name)

        assert f.exists


def test_that_required_docker_container_is_existing(host):
    c = host.docker.get_containers(name='server--draw-io', status='created')

    assert len(c) == 1
