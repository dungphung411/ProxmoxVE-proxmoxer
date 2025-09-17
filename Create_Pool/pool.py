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
pool_id = 'pool01'


# get pool
getpool = proxmox.pools.get()
print(json.dumps(getpool, indent=2))
# # create new pool 
# createpool = proxmox.pools.post(poolid= pool_id , comment='Chuan chi pool 2')
# print("Create Pool:", createpool)
# # change pool member 
# addmem = proxmox.pools(pool_id).put(vms='140,141,142')
# print("Add member:", addmem)
#  delete pool
# delpool = proxmox.pools(pool_id).delete()
# print("Delete Pool:", delpool)