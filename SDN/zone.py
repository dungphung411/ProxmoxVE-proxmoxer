

from proxmoxer import ProxmoxAPI

import json

proxmox = ProxmoxAPI('10.200.5.201', user='root@pam', password='Nutanix/4u', verify_ssl=False)

# Create new simple zone
# var_zone ={
#     "type": "simple",      
#     "zone": "mdpsimp",
#     "nodes": "pve01",
#     "ipam": "pve",
# } 

# create_zone = proxmox.cluster.sdn.zones.post(**var_zone)
# print("POST response:", create_zone)

# Create new VLAN zone 
# var_zone_vlan ={
#     "type": "vlan",      
#     "zone": "mdpvlan",
#     "bridge": "vmbr1",
#     "ipam": "pve",
#     "mtu": "1500",
# }
# create_zone_vlan = proxmox.cluster.sdn.zones.post(**var_zone_vlan)
# print("POST response:", create_zone_vlan)

# Get zone information
types = ["evpn", "faucet", "qinq", "simple", "vlan", "vxlan"]
all_zones = []

for zone_type in types:
    get_zone = proxmox.cluster.sdn.zones.get(pending="1", running="1", type=zone_type)
    all_zones.extend(get_zone)

with open('allsdn.json', 'w', encoding='utf-8') as f:
    json.dump(all_zones, f, indent=2, ensure_ascii=False)




zone_name = all_zones[0]['zone']      # ở đây lấy zone mình muốn từ kết quả get_zone (ví dụ 0 là zone đầu tiên)
                        
# Configure existing zone
change_zone = proxmox.cluster.sdn.zones(zone_name).put(mtu="1300", nodes="pve02",dhcp = "dnsmasq")

# Delete existing zone
# del_zone = proxmox.cluster.sdn.zones(zone_name).delete()
