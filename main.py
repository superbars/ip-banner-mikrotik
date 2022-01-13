import netmiko
from netmiko import ConnectHandler

def connect_to_mikrotik(list):
    print("[!]Check your device type. Be sure this is the mikrotik and it has a mikrotik-routerOS[!]")
    ip_of_device = input('[*]Please, input ip of your router[*]\n')
    username = input('[*]Please, put down username[*]\n')
    password = input('[*]Please, put down password[*]\n')
    print("[!]Please wait...[!]")

    mikrotik_main_router = {
        'device_type':'mikrotik_routeros',
        'host':ip_of_device,
        'port':'22',
        'username':username,
        'password':password,
        'global_cmd_verify': False

    }
    sshCli = ConnectHandler(**mikrotik_main_router)
    print("Beginning ban of ip list")
    for ip in list:
        command = "/ip firewall filter add chain=forward src-address=" + ip + " action=drop comment=BlockedByScript"
        sshCli.send_command(command)
        print("IP: " + ip + " was banned")

    sshCli.disconnect()

ip_addresses = []
def read_ip():
    global ip_addresses
    filename = input("[!]Please specify your ip list[!]\n")
    with open(filename,'r') as f:
        ip_addresses = f.read().split()

read_ip()
connect_to_mikrotik(ip_addresses)