import os
 
import testinfra.utils.ansible_runner
 
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
 
 
# def test_is_docker_installed(host):
#     package_docker = host.package('docker-ce')
 
#     assert package_docker.is_installed
 
 
def test_run_hello_world_container_successfully(host):
    # hello_world_ran = host.run("docker run hello-world")
 
    haproxy_package  = host.package("haproxy")
    haproxy_service  = host.service("haproxy")

    assert haproxy_package.is_installed
    assert haproxy_service.is_enabled