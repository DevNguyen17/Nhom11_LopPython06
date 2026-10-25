import json
import re
import os

class PhuongTien:
    """Lớp cha (Superclass) biểu diễn thông tin chung của phương tiện."""
    def __init__(self, ma_xe, bien_so, loai_xe):
        self.ma_xe = ma_xe
        self.bien_so = bien_so
        self.loai_xe = loai_xe

    def hien_thong_tin(self):
        return f"Mã: {self.ma_xe} | Biển số: {self.bien_so} | Loại: {self.loai_xe}"

class XeOTo(PhuongTien):
    """Lớp con kế thừa từ PhuongTien (Áp dụng kế thừa & ghi đè phương thức)."""
    def __init__(self, ma_xe, bien_so, so_cho_ngoi):
        super().__init__(ma_xe, bien_so, "Ô tô")
        self.so_cho_ngoi = so_cho_ngoi

    def hien_thong_tin(self):
        base_info = super().hien_thong_tin()
        return f"{base_info} | Số chỗ: {self.so_cho_ngoi}"

class XeMay(PhuongTien):
    """Lớp con kế thừa từ PhuongTien."""
    def __init__(self, ma_xe, bien_so, dung_tich):
        super().__init__(ma_xe, bien_so, "Xe máy")
        self.dung_tich = dung_tich

    def hien_thong_tin(self):
        base_info = super().hien_thong_tin()
        return f"{base_info} | Dung tích: {self.dung_tich}cc"

class QuanLyFileJSON:
    """Lớp chuyên trách xử lý đọc và ghi file JSON an toàn."""
    @staticmethod
    def doc_file(ten_file):
        if not os.path.exists(ten_file):
            return []
        try:
            with open(ten_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, Exception):
            return []

    @staticmethod
    def ghi_file(ten_file, data):
        try:
            with open(ten_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Lỗi khi ghi file: {e}")

class Validator:
    """Lớp kiểm tra dữ liệu bằng Regular Expression (Regex)."""
    @staticmethod
    def kiem_tra_bien_so(bien_so):
        # Ví dụ định dạng biển số xe Việt Nam cơ bản: 29A-123.45 hoặc 51F1-12345
        pattern = r'^\d{2}[A-Z][A-Z0-9]?-\d{3}\.\d{2}$|^\d{2}[A-Z][A-Z0-9]?-\d{4,5}$'
        return bool(re.match(pattern, bien_so))
