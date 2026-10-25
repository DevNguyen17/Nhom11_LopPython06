import tkinter as tk
from tkinter import ttk, messagebox
import requests

class ParkingGUI:
    """Lớp dựng giao diện đồ họa Tkinter."""
    def __init__(self, root, manager_obj):
        self.root = root
        self.root.title("Ứng dụng Quản lý Bãi đỗ xe - Đồ án Python")
        self.root.geometry("950x650")
        self.manager = manager_obj

        # Menu & Layout
        self.tao_widgets()

    def tao_widgets(self):
        # Tiêu đề
        lbl_title = tk.Label(self.root, text="QUẢN LÝ BÃI ĐỖ XE TỰ ĐỘNG", font=("Arial", 16, "bold"), fg="darkblue")
        lbl_title.pack(pady=10)

        # Bảng hiển thị Treeview
        frame_tree = tk.Frame(self.root)
        frame_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        cols = ("ma_xe", "bien_so", "loai_xe", "vi_tri", "thoi_gian_vao", "trang_thai")
        self.tree = ttk.Treeview(frame_tree, columns=cols, show="headings")
        for col in cols:
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, anchor=tk.CENTER, width=130)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Sơ đồ Canvas trực quan
        frame_canvas = tk.LabelFrame(self.root, text="Sơ đồ công suất ô đỗ (Canvas Widget)")
        frame_canvas.pack(fill=tk.X, padx=10, pady=10)
        
        self.canvas = tk.Canvas(frame_canvas, height=80, bg="white")
        self.canvas.pack(fill=tk.X, padx=5, pady=5)
        self.ve_so_do_o_do()

    def ve_so_do_o_do(self):
        # Vẽ các ô bãi đỗ tượng trưng trên Canvas
        for i in range(6):
            x1 = 15 + i * 150
            x2 = x1 + 130
            self.canvas.create_rectangle(x1, 15, x2, 65, fill="lightgreen", outline="black")
            self.canvas.create_text(x1 + 65, 40, text=f"Vị trí A-0{i+1}", font=("Arial", 9, "bold"))

    @staticmethod
    def crawl_du_lieu_thoi_tiet():
        """Hàm tích hợp API lấy dữ liệu bên ngoài theo yêu cầu đồ án."""
        try:
            response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=10.8231&longitude=106.6297&current_weather=true", timeout=5)
            if response.status_code == 200:
                return response.json().get("current_weather", {})
        except Exception:
            return None
