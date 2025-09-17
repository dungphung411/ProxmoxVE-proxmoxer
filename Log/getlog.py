from proxmoxer import ProxmoxAPI
import json
import paramiko

proxmox = ProxmoxAPI('10.200.5.201', user='root@pam', password='Nutanix/4u', verify_ssl=False)

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