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
# Get 
vm = proxmox.nodes(node1).qemu.get(full=1)
print(json.dumps(vm, indent=2))
with open('vm.txt', 'w', encoding='utf-8') as f:
     json.dump(vm, f, indent=2, ensure_ascii=False)