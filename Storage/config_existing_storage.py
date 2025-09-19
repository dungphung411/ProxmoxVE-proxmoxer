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

#  Var
#  Get storage information
types = ["btrfs", "cephfs", "cifs", "dir", "esxi", "iscsi", "iscsidirect", "lvm", "lvmthin", "nfs", "pbs", "rbd", "zfs", "zfspool"]     
all_storages = []

for storage_type in types:
    get_storage = proxmox.storage.get()
    all_storages.extend(get_storage)

with open('get_storage.json', 'w', encoding='utf-8') as f:
    json.dump(all_storages, f, indent=2, ensure_ascii=False)

# types = ["btrfs", "cephfs", "cifs", "dir", "esxi", "iscsi", "iscsidirect", "lvm", "lvmthin", "nfs", "pbs", "rbd", "zfs", "zfspool"]     
# all_storage_names = []

# for storage_type in types:
#     get_storage = proxmox.storage.get()
#     names = [s["storage"] for s in get_storage]
#     all_storage_names.extend(names)

# with open('storage_names.json', 'w', encoding='utf-8') as f:
#     json.dump(all_storage_names, f, indent=2, ensure_ascii=False)
