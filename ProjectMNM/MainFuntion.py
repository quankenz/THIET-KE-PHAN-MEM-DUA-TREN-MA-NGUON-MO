# main.py
import tkinter as tk
from tkinter import ttk
from GiaiTich import show_calculus_window
from DaiSoTT import show_linear_algebra_window

def on_button_click(option):
    selected_option_label.config(text=f"Bạn đã chọn {option}")
    window.iconify()  # Ẩn cửa sổ chính khi mở màn hình con
    if option == "Giải tích":
        show_calculus_window(show_main_window)
    elif option == "Đại số tuyến tính":
        show_linear_algebra_window(show_main_window)

def on_exit_button_click():
    window.destroy()

def show_main_window(child_window):
    child_window.destroy()  # Đóng cửa sổ con
    window.deiconify()  # Hiển thị lại cửa sổ chính
    selected_option_label.config(text="")  # Xóa lựa chọn trước đó

def flash_title_color(color_index=0):
    current_color = title_label.cget("fg")
    next_color_index = (color_index + 1) % len(color_palette)
    next_color = color_palette[next_color_index]
    title_label.config(fg=next_color)
    window.after(500, flash_title_color, next_color_index)

# Tạo cửa sổ
window = tk.Tk()
window.title("Thinkter")
window.geometry("400x350")  # Đặt kích thước cửa sổ ban đầu

# Tạo style cho nút
style = ttk.Style()
style.configure("Calculus.TButton",
                font=("Arial", 14),
                padding=10,
                background="#3498db",  # Màu xanh dương
                foreground="blue",
                )


style.configure("LinearAlgebra.TButton",
                font=("Arial", 14),
                padding=10,
                background="#2ecc71",  # Màu xanh lá cây
                foreground="green",
                )

# Tạo danh sách màu sắc cho nhấp nháy
color_palette = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Tạo label tiêu đề
title_label = tk.Label(window, text="Toán Học", font=("Arial", 18), fg="black")
title_label.pack(pady=10)

# Bắt đầu hiệu ứng nhấp nháy màu cho chữ "Toán Học"
flash_title_color()

# Tạo nút cho Giải tích
calculus_button = ttk.Button(window, text="Giải tích", style="Calculus.TButton", command=lambda: on_button_click("Giải tích"))
calculus_button.pack(pady=5)


# Tạo nút cho Đại số tuyến tính
linear_algebra_button = ttk.Button(window, text="Đại số tuyến tính", style="LinearAlgebra.TButton", command=lambda: on_button_click("Đại số tuyến tính"))
linear_algebra_button.pack(pady=5)

# Label hiển thị lựa chọn
selected_option_label = tk.Label(window, text="")
selected_option_label.pack(pady=10)

# Tạo nút thoát
exit_button = ttk.Button(window, text="Thoát", command=on_exit_button_click)
exit_button.pack(pady=10)

# Khởi chạy vòng lặp sự kiện
window.mainloop()