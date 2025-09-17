import proxmoxer
from proxmoxer import ProxmoxAPI
import json
import paramiko

proxmox = ProxmoxAPI('10.200.5.201', user='root@pam', password='Nutanix/4u', verify_ssl=False)

# Var
node1 = 'pve01'
node2 = 'pve02'
node3 = 'pve03'
ifacenao   = 'vmbr1'
nodenao = node2
typenao = 'vlan'
vlan_id = '206'
bridge = 'vmbr1'

# Get network on node

import json

nodes = ['pve01', 'pve02', 'pve03']
all_networks = {}

for node in nodes:
    net = proxmox.nodes(node).network.get()
    all_networks[node] = net

with open('network.json', 'w', encoding='utf-8') as f:
    json.dump(all_networks, f, indent=2, ensure_ascii=False)

print("Network info for all nodes saved to network.json")

# Create Linux Bond

# Create Linux Bridge 
varvmbr ={
    "iface": "vmbr2",
    "bridge_ports": "ens256",
    "comments": "Python Proxmoxer create Bridge vmbr2",
    "type": "bridge",
    "bridge_vlan_aware": "1",
    "autostart": "1",
    "bridge_vids": "2-4094"
} 

create_bridge = proxmox.nodes(node1).network.post(**varvmbr)
print("POST response:", create_bridge)

# Create Linux VLAN 
varvlan = {
    "vlan-id": "121",
    "iface": "vmbr1.121",
    "vlan-raw-device": "vmbr1",
    "comments": "Python Proxmoxer create VLAN 121",
    "type": "vlan",
    "autostart": "1",
}
create_vlan = proxmox.nodes(node1).network.post(**varvlan)
print("POST response:", create_vlan)

# Change config of a bridge,bond,vlan 
# put_data = {
#     "comments": "Update IP VMBr1",
#     "type": "bridge",
#     "cidr": "10.200.6.206/24",
# }
# response_put = proxmox.nodes(node1).network("vmbr1").put(**put_data)
# print("PUT response:", response_put)


#  restart networking service on node -- tạm thời chạy xong vẫn chưa apply được, cần apply tay
username='root'
password='Nutanix/4u'
hostname='10.200.5.201' 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

stdin, stdout, stderr = ssh.exec_command('ifreload -a && systemctl restart networking')
exit_status = stdout.channel.recv_exit_status()
ssh.close()
# # DELETE ví dụ: xóa network device (ví dụ xóa vlan vmbr1.300 vừa tạo)
# response_delete = proxmox.nodes(node1).network("vmbr1.300").delete()
# print("DELETE response:", response_delete)
