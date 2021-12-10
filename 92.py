trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]
trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}
def generate_access_config(intf_vlan_mapping,access_template):
    for i in intf_vlan_mapping.keys():
        restr = access_template[2]
        access_template[2] += ' ' + str(intf_vlan_mapping[i]).strip('[]')
        print(i, end='\n')
        print(*access_template, sep='\n')
        access_template[2]=restr
generate_access_config(trunk_config, trunk_mode_template)
