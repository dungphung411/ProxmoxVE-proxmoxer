from proxmoxer import ProxmoxAPI
import json
import paramiko

proxmox = ProxmoxAPI('10.200.5.201', user='root@pam', password='Nutanix/4u', verify_ssl=False)

# var
node1 = 'pve01'
# Get 
vm = proxmox.nodes(node1).qemu.get(full=1)
print(json.dumps(vm, indent=2))
with open('vm.txt', 'w', encoding='utf-8') as f:
     json.dump(vm, f, indent=2, ensure_ascii=False)