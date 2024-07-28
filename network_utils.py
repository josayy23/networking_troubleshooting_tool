import socket
import subprocess
import platform

def ping_host(host):
    """
    Ping a host to check connectivity
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', host]
    return subprocess.run(command, stdout=subprocess.PIPE).stdout.decode()

def traceroute(host):
    """
        Perform a traceroute to a host.
        """
    command = ['tracecert', host] if platform.system().lower() == 'windows' else ['traceroute', host]
    return subprocess.run(command, stdout=subprocess.PIPE).stdout.decode()

def get_network_config():
    """
        Display the current network configuration.
        """
    command = ['ipconfig'] if platform.system().lower() == 'windows' else ['ipconfig']
    return subprocess.run(command, stdout=subprocess.PIPE).stdout.decode()

