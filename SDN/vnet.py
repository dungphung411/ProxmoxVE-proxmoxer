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

# Create a new VNETS
# var_vnet = {
#     "vnet": "mdpvnet",
#     "zone": "mdpsimp",
#     "vlanaware": "0",
#     "isolate-ports": "0",
#     "alias": "deptrai",
# }
# create_vnet = proxmox.cluster.sdn.vnets.post(**var_vnet)
# print("POST response:", create_vnet)

# Get vnet information
get_vnet = proxmox.cluster.sdn.vnets.get(pending="1", running="1")
print("GET vnet response:", json.dumps(get_vnet, indent=4))
with open('allvnet.json', 'w', encoding='utf-8') as f:
    json.dump(get_vnet, f, indent=2, ensure_ascii=False)
# Configure existing vnet
vnet_name = get_vnet[0]['vnet']      # ở đây lấy vnet mình muốn từ kết quả get_vnet (ví dụ 0 là vnet đầu tiên)
change_vnet = proxmox.cluster.sdn.vnets(vnet_name).put(alias="depgai",vlanaware="0")
# Delete existing vnet
# del_vnet = proxmox.cluster.sdn.vnets(vnet_name).delete()