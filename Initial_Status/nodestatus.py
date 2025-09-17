from proxmoxer import ProxmoxAPI
import json

proxmox = ProxmoxAPI('10.200.5.201', user='root@pam', password='Nutanix/4u', verify_ssl=False)

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