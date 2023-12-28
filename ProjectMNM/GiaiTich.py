# calculus_module.py
import tkinter as tk
from tkinter import ttk, filedialog
import sympy as sym
import csv


def show_calculus_window(show_main_function):
    file_path = None
    def xoa_du_lieu():
        for entry in input_entries:
            entry.delete(0, 'end')
        result_label.config(text="")
        result_label_dao_ham.config(text="")
        result_label_khai_trien.config(text="")
        result_label_rut_gon.config(text="")

    def hien_thi_chuc_nang(chuc_nang):
        for frame in input_frames.values():
            frame.grid_remove()

        input_frames[chuc_nang].grid()

    def thuc_hien_tinh_toan(chuc_nang, *args, **kwargs):
        try:
            for arg in args:
                if not arg:
                    raise ValueError("Bạn chưa nhập đủ thông tin.")

            return True, ""
        except ValueError as e:
            return False, f"Lỗi: {str(e)}"

    def tinh_tich_phan():
        bieu_thuc, bien, gioi_han_start, gioi_han_end = (
            bieu_thuc_tich_phan_entry.get(),
            bien_tich_phan_entry.get(),
            gioi_han_start_entry.get(),
            gioi_han_end_entry.get()
        )

        valid, error_message = thuc_hien_tinh_toan("Tích phân", bieu_thuc, bien, gioi_han_start, gioi_han_end)
        if not valid:
            result_label_tich_phan.config(text=error_message)
            return

        x = sym.symbols(bien)
        try:
            ket_qua_tich_phan = sym.integrate(bieu_thuc, (x, float(gioi_han_start), float(gioi_han_end)))
            result_label_tich_phan.config(text=f"Kết quả tích phân: {ket_qua_tich_phan}")
            create_luu_button(frame_tich_phan, "Tich phan", ket_qua_tich_phan)
        except Exception as e:
            result_label_tich_phan.config(text=f"Lỗi: {str(e)}")

    def tinh_gioi_han():
        bieu_thuc, bien, diem_gioi_han = (
            bieu_thuc_gioi_han_entry.get(),
            bien_gioi_han_entry.get(),
            diem_gioi_han_entry.get()
        )

        valid, error_message = thuc_hien_tinh_toan("Giới hạn", bieu_thuc, bien, diem_gioi_han)
        if not valid:
            result_label.config(text=error_message)
            return

        x = sym.symbols(bien)
        try:
            gioi_han = sym.limit(bieu_thuc, x, float(diem_gioi_han))
            result_label.config(text=f"Giới hạn tại điểm {diem_gioi_han}: {gioi_han}")
            create_luu_button(frame_gioi_han, "Gioi han", gioi_han)
        except Exception as e:
            result_label.config(text=f"Lỗi: {str(e)}")

    def tinh_dao_ham():
        bieu_thuc, bien = bieu_thuc_dao_ham_entry.get(), bien_dao_ham_entry.get()
        valid, error_message = thuc_hien_tinh_toan("Đạo hàm", bieu_thuc, bien)
        if not valid:
            result_label_dao_ham.config(text=error_message)
            return

        x = sym.symbols(bien)
        try:
            dao_ham = sym.diff(bieu_thuc, x)
            result_label_dao_ham.config(text=f"Đạo hàm: {dao_ham}")
            create_luu_button(frame_dao_ham, "Dao ham", dao_ham)
        except Exception as e:
            result_label_dao_ham.config(text=f"Lỗi: {str(e)}")

    def khai_trienn():
        bieu_thuc = bieu_thuc_khai_trien_entry.get()
        try:
            bieu_thuc_khai_trien = sym.expand(bieu_thuc)
            result_label_khai_trien.config(text=f"Biểu thức khai triển: {bieu_thuc_khai_trien}")
            create_luu_button(frame_khai_trien, "Khai trien", bieu_thuc_khai_trien)
        except Exception as e:
            result_label_khai_trien.config(text=f"Lỗi: {str(e)}")

    def rut_gon_bieu_thuc():
        bieu_thuc = bieu_thuc_rut_gon_entry.get()
        try:
            bieu_thuc_rut_gon = sym.simplify(bieu_thuc)
            result_label_rut_gon.config(text=f"Biểu thức rút gọn: {bieu_thuc_rut_gon}")
            create_luu_button(frame_rut_gon, "Rut gon", bieu_thuc_rut_gon)
        except Exception as e:
            result_label_rut_gon.config(text=f"Lỗi: {str(e)}")
    def luu_ket_qua_csv(chuc_nang, ket_qua):
        nonlocal file_path
        if file_path is None:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if not file_path:
                return  # Người dùng đã hủy lựa chọn file
        with open(file_path, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([chuc_nang, str(ket_qua)])

    def create_luu_button(frame, chuc_nang, ket_qua):
        def save_and_choose_file():
            nonlocal file_path
            if file_path is None:
                file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
                if not file_path:
                    return
            luu_ket_qua_csv(chuc_nang, ket_qua)

        luu_button = ttk.Button(frame, text="Lưu", command=save_and_choose_file)
        luu_button.grid(row=6, columnspan=2)

    calculus_window = tk.Toplevel()
    calculus_window.title("Màn hình Giải tích")
    calculus_window.geometry("400x300")

    # Thêm nút "Back" để quay lại màn hình chính
    back_button = tk.Button(calculus_window, text="Back",command=lambda: show_main_function(calculus_window))
    back_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

    tich_phan_button = ttk.Button(calculus_window, text="Tích phân", command=lambda: hien_thi_chuc_nang("Tích phân"))
    tich_phan_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    gioi_han_button = ttk.Button(calculus_window, text="Giới hạn", command=lambda: hien_thi_chuc_nang("Giới hạn"))
    gioi_han_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

    dao_ham_button = ttk.Button(calculus_window, text="Đạo hàm", command=lambda: hien_thi_chuc_nang("Đạo hàm"))
    dao_ham_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

    khai_trien_button = ttk.Button(calculus_window, text="Khai triển", command=lambda: hien_thi_chuc_nang("Khai triển"))
    khai_trien_button.grid(row=0, column=3, padx=10, pady=10, sticky="e")

    rut_gon_button = ttk.Button(calculus_window, text="Rút gọn", command=lambda: hien_thi_chuc_nang("Rút gọn"))
    rut_gon_button.grid(row=0, column=4, padx=10, pady=10, sticky="e")

    frame_tich_phan = ttk.Frame(calculus_window)
    frame_tich_phan.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    bieu_thuc_tich_phan_label = ttk.Label(frame_tich_phan, text="Biểu thức:")
    bieu_thuc_tich_phan_label.grid(row=0, column=0)
    bieu_thuc_tich_phan_entry = ttk.Entry(frame_tich_phan)
    bieu_thuc_tich_phan_entry.grid(row=0, column=1)

    bien_tich_phan_label = ttk.Label(frame_tich_phan, text="Biến:")
    bien_tich_phan_label.grid(row=1, column=0)
    bien_tich_phan_entry = ttk.Entry(frame_tich_phan)
    bien_tich_phan_entry.grid(row=1, column=1)



    gioi_han_start_label = ttk.Label(frame_tich_phan, text="Giới hạn bắt đầu:")
    gioi_han_start_label.grid(row=2, column=0)
    gioi_han_start_entry = ttk.Entry(frame_tich_phan)
    gioi_han_start_entry.grid(row=2, column=1)

    gioi_han_end_label = ttk.Label(frame_tich_phan, text="Giới hạn kết thúc:")
    gioi_han_end_label.grid(row=3, column=0)
    gioi_han_end_entry = ttk.Entry(frame_tich_phan)
    gioi_han_end_entry.grid(row=3, column=1)

    tinh_tich_phan_button = ttk.Button(frame_tich_phan, text="Tính Tích Phân", command=tinh_tich_phan)
    tinh_tich_phan_button.grid(row=4, columnspan=2)

    result_label_tich_phan = ttk.Label(frame_tich_phan, text="")
    result_label_tich_phan.grid(row=5, columnspan=2)

    frame_dao_ham = ttk.Frame(calculus_window)
    frame_dao_ham.grid(row=1, column=2, padx=10, pady=10, sticky="w")

    bieu_thuc_dao_ham_label = ttk.Label(frame_dao_ham, text="Biểu thức:")
    bieu_thuc_dao_ham_label.grid(row=0, column=0)
    bieu_thuc_dao_ham_entry = ttk.Entry(frame_dao_ham)
    bieu_thuc_dao_ham_entry.grid(row=0, column=1)

    bien_dao_ham_label = ttk.Label(frame_dao_ham, text="Biến:")
    bien_dao_ham_label.grid(row=1, column=0)
    bien_dao_ham_entry = ttk.Entry(frame_dao_ham)
    bien_dao_ham_entry.grid(row=1, column=1)

    tinh_dao_ham_button = ttk.Button(frame_dao_ham, text="Tính Đạo Hàm", command=tinh_dao_ham)
    tinh_dao_ham_button.grid(row=2, columnspan=2)

    result_label_dao_ham = ttk.Label(frame_dao_ham, text="")
    result_label_dao_ham.grid(row=3, columnspan=2)

    frame_khai_trien = ttk.Frame(calculus_window)
    frame_khai_trien.grid(row=1, column=3, padx=10, pady=10, sticky="e")

    bieu_thuc_khai_trien_label = ttk.Label(frame_khai_trien, text="Biểu thức:")
    bieu_thuc_khai_trien_label.grid(row=0, column=0)
    bieu_thuc_khai_trien_entry = ttk.Entry(frame_khai_trien)
    bieu_thuc_khai_trien_entry.grid(row=0, column=1)

    tinh_khai_trien_button = ttk.Button(frame_khai_trien, text="Khai Triển", command=khai_trienn)
    tinh_khai_trien_button.grid(row=1, columnspan=2)

    result_label_khai_trien = ttk.Label(frame_khai_trien, text="")
    result_label_khai_trien.grid(row=2, columnspan=2)

    frame_rut_gon = ttk.Frame(calculus_window)
    frame_rut_gon.grid(row=1, column=4, padx=10, pady=10, sticky="e")

    bieu_thuc_rut_gon_label = ttk.Label(frame_rut_gon, text="Biểu thức:")
    bieu_thuc_rut_gon_label.grid(row=0, column=0)
    bieu_thuc_rut_gon_entry = ttk.Entry(frame_rut_gon)
    bieu_thuc_rut_gon_entry.grid(row=0, column=1)

    tinh_rut_gon_button = ttk.Button(frame_rut_gon, text="Rút Gọn", command=rut_gon_bieu_thuc)
    tinh_rut_gon_button.grid(row=1, columnspan=2)

    result_label_rut_gon = ttk.Label(frame_rut_gon, text="")
    result_label_rut_gon.grid(row=2, columnspan=2)

    result_label = ttk.Label(frame_tich_phan, text="")
    result_label.grid(row=5, columnspan=2)

    frame_gioi_han = ttk.Frame(calculus_window)
    frame_gioi_han.grid(row=1, column=1, padx=10, pady=10, sticky="e")

    bieu_thuc_gioi_han_label = ttk.Label(frame_gioi_han, text="Biểu thức:")
    bieu_thuc_gioi_han_label.grid(row=0, column=0)
    bieu_thuc_gioi_han_entry = ttk.Entry(frame_gioi_han)
    bieu_thuc_gioi_han_entry.grid(row=0, column=1)

    bien_gioi_han_label = ttk.Label(frame_gioi_han, text="Biến:")
    bien_gioi_han_label.grid(row=1, column=0)
    bien_gioi_han_entry = ttk.Entry(frame_gioi_han)
    bien_gioi_han_entry.grid(row=1, column=1)

    diem_gioi_han_label = ttk.Label(frame_gioi_han, text="Điểm giới hạn:")
    diem_gioi_han_label.grid(row=2, column=0)
    diem_gioi_han_entry = ttk.Entry(frame_gioi_han)
    diem_gioi_han_entry.grid(row=2, column=1)

    tinh_gioi_han_button = ttk.Button(frame_gioi_han, text="Tính Giới Hạn", command=tinh_gioi_han)
    tinh_gioi_han_button.grid(row=3, columnspan=2)

    result_label = ttk.Label(frame_gioi_han, text="")
    result_label.grid(row=4, columnspan=2)

    #xoa du lieu
    xoa_du_lieu_button = ttk.Button(calculus_window, text="Xóa dữ liệu", command=xoa_du_lieu)
    xoa_du_lieu_button.grid(row=0, column=5, padx=10, pady=10, sticky="e")

    for frame in [frame_tich_phan, frame_gioi_han, frame_dao_ham, frame_khai_trien, frame_rut_gon]:
        frame.grid_remove()
    # Lưu trữ các entry để dễ quản lý
    input_entries = [
        bieu_thuc_tich_phan_entry, bien_tich_phan_entry, gioi_han_start_entry, gioi_han_end_entry,
        bieu_thuc_dao_ham_entry, bien_dao_ham_entry,
        bieu_thuc_khai_trien_entry, bieu_thuc_rut_gon_entry
    ]

    # Lưu trữ các frame để dễ quản lý
    input_frames = {
        "Tích phân": frame_tich_phan,
        "Giới hạn": frame_gioi_han,
        "Đạo hàm": frame_dao_ham,
        "Khai triển": frame_khai_trien,
        "Rút gọn": frame_rut_gon
    }

# Nếu bạn muốn kiểm tra module riêng lẻ, thì thêm đoạn mã sau
if __name__ == "__main__":
    show_calculus_window(None)
