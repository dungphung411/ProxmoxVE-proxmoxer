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

journal1 = proxmox.nodes('pve01').journal.get()
with open('journal1.json', 'w', encoding='utf-8') as f:
     json.dump(journal1, f, indent=2, ensure_ascii=False)

journal2 = proxmox.nodes('pve02').journal.get()
with open('journal2.json', 'w', encoding='utf-8') as f:
     json.dump(journal2, f, indent=2, ensure_ascii=False)

journal3 = proxmox.nodes('pve03').journal.get()
with open('journal3.json', 'w', encoding='utf-8') as f:
     json.dump(journal3, f, indent=2, ensure_ascii=False)                  