from models import QuanLyFileJSON, Validator
from datetime import datetime

class BaiDoXeManager:
    """Lớp quản lý các nghiệp vụ chính của bãi đỗ xe."""
    def __init__(self, file_path="data_parking.json"):
        self.file_path = file_path
        self.ds_xe = QuanLyFileJSON.doc_file(self.file_path)

    def them_xe_vao_bai(self, ma_xe, bien_so, loai_xe, vi_tri):
        if not Validator.kiem_tra_bien_so(bien_so):
            return False, "Biển số xe không đúng định dạng!"
        
        # Kiểm tra trùng mã
        for xe in self.ds_xe:
            if xe["ma_xe"] == ma_xe:
                return False, "Mã vé/xe đã tồn tại trên hệ thống!"

        thoi_gian_nhap = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = {
            "ma_xe": ma_xe,
            "bien_so": bien_so,
            "loai_xe": loai_xe,
            "vi_tri": vi_tri,
            "thoi_gian_vao": thoi_gian_nhap,
            "trang_thai": "Đang đỗ"
        }
        self.ds_xe.append(record)
        QuanLyFileJSON.ghi_file(self.file_path, self.ds_xe)
        return True, "Thêm xe vào bãi thành công!"

    def cho_xe_ra_bai(self, ma_xe):
        for xe in self.ds_xe:
            if xe["ma_xe"] == ma_xe and xe["trang_thai"] == "Đang đỗ":
                xe["trang_thai"] = "Đã ra"
                xe["thoi_gian_ra"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                QuanLyFileJSON.ghi_file(self.file_path, self.ds_xe)
                return True, "Xe đã rời bãi!"
        return False, "Không tìm thấy xe đang đỗ với mã này!"

    def tim_kiem(self, tu_khoa, loai_tim_kiem="bien_so"):
        ket_qua = []
        for xe in self.ds_xe:
            val = xe.get(loai_tim_kiem, "")
            if tu_khoa.lower() in str(val).lower():
                ket_qua.append(xe)
        return ket_qua
