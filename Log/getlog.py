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

log = proxmox.cluster.log.get()
with open('log.json', 'w', encoding='utf-8') as f:
     json.dump(log, f, indent=2, ensure_ascii=False)

syslog1 = proxmox.nodes('pve01').syslog.get()
with open('syslog1.json', 'w', encoding='utf-8') as f:
     json.dump(log, f, indent=2, ensure_ascii=False)

syslog2 = proxmox.nodes('pve02').syslog.get()
with open('syslog2.json', 'w', encoding='utf-8') as f:
     json.dump(log, f, indent=2, ensure_ascii=False)

syslog3 = proxmox.nodes('pve03').syslog.get()
with open('syslog3.json', 'w', encoding='utf-8') as f:
     json.dump(log, f, indent=2, ensure_ascii=False)