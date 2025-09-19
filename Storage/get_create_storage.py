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

# Create new storage
var_nfs = {
    "storage": "nfs_proxmoxer",
    "type": "nfs",
    "server": "10.200.10.222",
    "shared": "1",
    "content": "iso,backup,images",
    "path": "/mnt/pve/nfs-proxmoxer",
}

var_pbs = {
    "storage": "pbs_proxmoxer",
    "type": "pbs",
    "server": "",
    "username": "root@pam",
    "password": "your_password",
    "datastore": "your_datastore",
    "content": "backup",
    "fingerprint": "your_fingerprint",
}

var_lvm = {
    "storage": "lvm_proxmoxer",
    "type": "lvm",
    "vgname": "your_vgname",
    "content": "images,rootdir",
    "nodes": "proxmox_node_name",
    "snapshot-as-volume-chain": "0",
    "shared": "0",
}
create_storage = proxmox.storage.post(**var_nfs)

                                