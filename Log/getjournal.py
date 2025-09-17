from proxmoxer import ProxmoxAPI
import json
import paramiko

proxmox = ProxmoxAPI('10.200.5.201', user='root@pam', password='Nutanix/4u', verify_ssl=False)

journal1 = proxmox.nodes('pve01').journal.get()
with open('journal1.json', 'w', encoding='utf-8') as f:
     json.dump(journal1, f, indent=2, ensure_ascii=False)

journal2 = proxmox.nodes('pve02').journal.get()
with open('journal2.json', 'w', encoding='utf-8') as f:
     json.dump(journal2, f, indent=2, ensure_ascii=False)

journal3 = proxmox.nodes('pve03').journal.get()
with open('journal3.json', 'w', encoding='utf-8') as f:
     json.dump(journal3, f, indent=2, ensure_ascii=False)                  