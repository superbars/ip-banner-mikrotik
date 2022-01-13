#!/usr/bin/python3
from netmiko import ConnectHandler

def connect_to_mikrotik(list):
    print("[!]Check your device type. Be sure this is the mikrotik and it has a mikrotik-routerOS[!]")
    print("[!]Check configuration in mikrotik_main-router[!]")
    print("[!]Establishing connection...[!]")

    mikrotik_main_router = {
        'device_type':'mikrotik_routeros',
        'host':'192.168.88.1',
        'port':'22',
        'username':'admin',
        'password':'',
        'global_cmd_verify': False

    }
    sshCli = ConnectHandler(**mikrotik_main_router)
    for ip in list:
        command = "/ip firewall filter add chain=forward src-address=" + ip + " action=drop comment=BlockedByScript"
        sshCli.send_command(command)
        print("IP: " + ip + " was banned")

    sshCli.disconnect()

ip_addresses = []
def read_ip():
    global ip_addresses
    filename = "ip_lists.txt"
    with open(filename,'r') as f:
        ip_addresses = f.read().split()

read_ip()
connect_to_mikrotik(ip_addresses)
