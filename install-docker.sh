
#!/bin/bash

# Script để cài đặt Docker và Docker Compose trong WSL (Ubuntu)

# Kiểm tra quyền root
if [ "$EUID" -ne 0 ]; then
  echo "Vui lòng chạy script này với quyền sudo."
  exit 1
fi

# Cập nhật hệ thống
echo "Đang cập nhật hệ thống..."
apt update && apt upgrade -y

# Cài đặt các gói cần thiết
echo "Cài đặt các gói hỗ trợ..."
apt install -y apt-transport-https ca-certificates curl software-properties-common

# Thêm GPG key của Docker
echo "Thêm GPG key của Docker..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Thêm kho lưu trữ Docker
echo "Thêm kho lưu trữ Docker..."
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Cập nhật và cài đặt Docker
echo "Cài đặt Docker..."
apt update
apt install -y docker-ce docker-ce-cli containerd.io

# Khởi động và kích hoạt Docker
echo "Khởi động Docker..."
service docker start
systemctl enable docker

# Thêm người dùng hiện tại vào nhóm docker
echo "Cấu hình Docker chạy không cần sudo..."
usermod -aG docker $SUDO_USER

# Cài đặt Docker Compose
echo "Cài đặt Docker Compose..."
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Kiểm tra cài đặt
echo "Kiểm tra cài đặt Docker..."
docker --version
docker-compose --version

echo "Cài đặt hoàn tất! Hãy đăng xuất và đăng nhập lại để sử dụng Docker mà không cần sudo."

echo "Chạy 'docker run hello-world' để kiểm tra."