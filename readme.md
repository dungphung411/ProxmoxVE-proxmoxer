# A. Giới thiệu về Proxmoxer và Quản lý Proxmox với Proxmoxer

## Proxmoxer là gì?

Proxmoxer là một thư viện Python được thiết kế để tương tác với API REST của Proxmox VE (Virtual Environment). Nó giúp đơn giản hóa việc quản lý và tự động hóa các tác vụ trên môi trường Proxmox thông qua các lệnh Python, thay vì thao tác trực tiếp qua giao diện web hoặc API thủ công.

Thư viện này hỗ trợ các thao tác cơ bản như lấy thông tin về node, quản lý máy ảo (VM), container (LXC), lưu trữ, mạng và các chức năng của cụm Proxmox.

## Tính năng chính của Proxmoxer

- Tương tác đầy đủ với API Proxmox REST API v2.
- Hỗ trợ các phương thức HTTP: GET, POST, PUT, DELETE qua các hàm tương ứng `get()`, `create()`, `set()`, `delete()`.
- Hỗ trợ kết nối qua HTTPS, SSH và các backend khác.
- Dễ dàng viết các script Python để tự động hóa quản lý Proxmox.
- Hỗ trợ lấy và cấu hình chi tiết các tài nguyên Proxmox như node, VM, storage, network.

## Cách cài đặt
Cài thư viện cần thiết
```bash
pip install proxmoxer 
pip install requests  
pip install paramiko
```
Để dùng .env tăng bảo mật
```bash
pip install dotenv
```
Rồi tạo file env và trỏ vào nó trong code
## Tài liệu tham khảo 
- [Proxmoxer Documentation](https://proxmoxer.github.io/docs/)
- [Proxmox VE API](https://pve.proxmox.com/pve-docs/api-viewer/index.html)

# B. Kế hoạch triển khai 
 ** NOTED ** THIS CODE IS NOT IAC
 
### Hoàn thành 
- Proxmoxnetwork
- Cluster Status
- Proxmox get logs
- Pool create and assign
- SDN basic with Simple Zone and VLAN Zone 

### Tiếp tục triển khai
- QEMU và template 
- Storage 
- User and Permission
- Firewall

### Nâng cao
- Đặt biến chung
- Vấn đề HA, live migrate

