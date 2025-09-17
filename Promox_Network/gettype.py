# Initial
from proxmoxer import ProxmoxAPI
import json
import paramiko
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path="D:\\PROJECT\\script\\Python_Proxmox\\.env")
host = os.getenv("PROXMOX_HOST")
user = os.getenv("PROXMOX_USER")
password = os.getenv("PROXMOX_PASSWORD")
proxmox = ProxmoxAPI(host, user=user, password=password, verify_ssl=False)

# var
node1 = 'pve01'
# Get network type
nic = proxmox.nodes(node1).network.get(type='eth')
bridge = proxmox.nodes(node1).network.get(type='bridge')
print(json.dumps(nic, indent=2))
print(json.dumps(bridge, indent=2))

#  create bond 
# proxmox_bond = proxmox.nodes(node1).network.post(iface='bond0', type='bond', slaves='ens224, ens256', bond_mode='balance-rr', autostart='1', comments='Bond 2 NICs')