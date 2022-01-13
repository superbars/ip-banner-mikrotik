import netmiko
from netmiko import ConnectHandler

print("[!]Hello, first of all check your device type. Be sure this is the mikrotik and it has a mikrotik-routerOS[!]")
ip_of_device = input('[*]Please, input ip of your router[*]\n')
username = input('[*]Please, put down username[*]\n')
password = input('[*]Please, put down password[*]\n')


def connect_to_mikrotik(ip_address, username, password):
    print("[!]Please wait...[!]")
    mikrotik_main_router = {
        'device_type':'mikrotik_routeros',
        'host':ip_address,
        'port':'22',
        'username':username,
        'password':password
    }
    sshCli = ConnectHandler(**mikrotik_main_router)
    print(sshCli.find_prompt())
    sshCli.disconnect()

ip_addresses = []
def read_ip(filename):
    global ip_addresses
    with open(filename,'r') as f:
        ip_addresses = f.read().split()

connect_to_mikrotik(ip_of_device, username, password)