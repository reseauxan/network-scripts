from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.203",
    "username": "reseauxan",
    "password": "reseauxan",
    "port": 22,
    "secret": "cisco",
}
ssh_connect = ConnectHandler(**device)
ssh_connect.enable()
print("BEFORE")
result = ssh_connect.send_command("show ip int brief")
print(result)
configcmds = ["interface vlan 10", "ip add 10.10.10.1 255.255.255.0"]
ssh_connect.send_config_set(configcmds)
print("AFTER")
result = ssh_connect.send_command("show ip int brief")
ssh_connect.disconnect()
print("")
print(result)
