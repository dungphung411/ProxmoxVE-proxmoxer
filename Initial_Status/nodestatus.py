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

#  Get nodes status
status = proxmox.nodes.get()
print(json.dumps(status, indent=2))

status_node1 = proxmox.nodes('pve01').status.get()
print(json.dumps(status_node1, indent=2))
with open('node1log.txt', 'w', encoding='utf-8') as f:
     json.dump(status_node1, f, indent=2, ensure_ascii=False)
status_node2 = proxmox.nodes('pve02').status.get()
print(json.dumps(status_node2, indent=2))
with open('node2log.txt', 'w', encoding='utf-8') as f:
     json.dump(status_node2, f, indent=2, ensure_ascii=False)

status_node3 = proxmox.nodes('pve03').status.get()
print(json.dumps(status_node3, indent=2))
with open('node3log.txt', 'w', encoding='utf-8') as f:
     json.dump(status_node3, f, indent=2, ensure_ascii=False)