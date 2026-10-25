import tkinter as tk
from tkinter import messagebox
from models import QuanLyFileJSON
from manager import BaiDoXeManager
from gui import ParkingGUI

class AuthManager:
    """Lớp quản lý tài khoản và phân quyền người dùng."""
    def __init__(self, user_file="users.json"):
        self.user_file = user_file
        self.users = QuanLyFileJSON.doc_file(self.user_file)
        if not self.users:
            # Tạo sẵn tài khoản mặc định nếu file rỗng
            self.users = [
                {"username": "admin", "password": "123", "role": "Admin"},
                {"username": "nv1", "password": "123", "role": "User"}
            ]
            QuanLyFileJSON.ghi_file(self.user_file, self.users)

    def dang_nhap(self, username, password):
        for u in self.users:
            if u["username"] == username and u["password"] == password:
                return True, u["role"]
        return False, None

# MAIN - KHỞI CHẠY ỨNG DỤNG
if __name__ == "__main__":
    root = tk.Tk()
    
    # Khởi tạo các manager
    auth = AuthManager()
    parking_mgr = BaiDoXeManager()

    # Mở giao diện chính (Hoặc Cửa sổ Đăng nhập)
    app = ParkingGUI(root, parking_mgr)
    
    root.mainloop()