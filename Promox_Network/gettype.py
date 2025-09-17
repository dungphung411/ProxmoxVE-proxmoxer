from proxmoxer import ProxmoxAPI
import json
import paramiko

proxmox = ProxmoxAPI('10.200.5.201', user='root@pam', password='Nutanix/4u', verify_ssl=False)

# var
node1 = 'pve01'
# Get network type
nic = proxmox.nodes(node1).network.get(type='eth')
bridge = proxmox.nodes(node1).network.get(type='bridge')
print(json.dumps(nic, indent=2))
print(json.dumps(bridge, indent=2))

#  create bond 
# proxmox_bond = proxmox.nodes(node1).network.post(iface='bond0', type='bond', slaves='ens224, ens256', bond_mode='balance-rr', autostart='1', comments='Bond 2 NICs')