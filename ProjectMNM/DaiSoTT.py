# DaiSoTT.py
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import csv
import pandas as pd
import io

# Biến equation_entries_list là biến toàn cục
equation_entries_list = []

# Hàm tạo cửa sổ giải hệ phương trình tuyến tính
def show_linear_algebra_window(show_main_function):
    global equation_entries_list  # Khai báo equation_entries_list là biến toàn cục
    history = []

    def add_to_history(coefficients, results, solution):
        history.append({'coefficients': coefficients, 'results': results, 'solution': solution})

    def create(entry):

        num_equations = int(entry.get())
        for i in range(num_equations):
            frame = tk.Frame(window)
            frame.pack(side=tk.TOP, padx=10, pady=5)
            equation_frames.append(frame)

            equation_entries = []
            label = tk.Label(frame, text=f"Phương trình {i + 1}:")
            label.pack(side=tk.LEFT)

            for j in range(num_equations + 1):
                entry = tk.Entry(frame)
                entry.pack(side=tk.LEFT)
                equation_entries.append(entry)

            equation_entries_list.append(equation_entries)

    def delete_fields():
        result.delete(1.0, tk.END)
        equation_entries_list.clear()
        for frame in equation_frames:
            frame.destroy()

        n_entry.delete(0, tk.END)

    def validate_input(entry):
        try:
            num_equations = entry.get()
            if not num_equations.isdigit():
                raise ValueError("Nhập số nguyên hợp lý.")

            num_equations = int(num_equations)

            if num_equations <= 0 or num_equations > 10:
                raise ValueError("Nhập lại số phương trình hợp lệ.")

            return True
        except ValueError:
            messagebox.showerror("Error", "Nhập đúng dữ liệu (số nguyên từ 1 đến 10).")
            return False

    def solve():
        try:
            num_equations_str = n_entry.get()

            # Kiểm tra xem chuỗi nhập vào có rỗng hay không
            if not num_equations_str:
                raise ValueError("Nhập số phương trình.")

            num_equations = int(num_equations_str)
            coefficients = []
            results = []

            for entry_list in equation_entries_list:
                equation_coefficients = []
                for entry in entry_list[:-1]:
                    val = float(entry.get())
                    equation_coefficients.append(val)
                coefficients.append(equation_coefficients)

                result_val = float(entry_list[-1].get())
                results.append(result_val)

            a = np.array(coefficients)
            b = np.array(results)

            if np.linalg.matrix_rank(a) == np.linalg.matrix_rank(np.column_stack((a, b))) == a.shape[1]:
                x = np.linalg.solve(a, b)

                result.delete(1.0, tk.END)
                result.insert(tk.END, "Kết quả:\n")
                for i, val in enumerate(x):
                    result.insert(tk.END, f"x{i + 1} = {round(val, 2)}\n")

                print("Kết quả:")
                for i, val in enumerate(x):
                    print(f"x{i + 1} = {round(val, 2)}")

                add_to_history(coefficients, results, x)

            elif np.linalg.matrix_rank(a) == np.linalg.matrix_rank(np.column_stack((a, b))) < a.shape[1]:
                result.delete(1.0, tk.END)
                result.insert(tk.END, "Hệ phương trình có vô số nghiệm")

                print("Hệ phương trình có vô số nghiệm")

            else:
                result.delete(1.0, tk.END)
                result.insert(tk.END, "Hệ phương trình vô nghiệm")

                print("Hệ phương trình vô nghiệm")

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def choose_csv_file():
        global equation_entries_list
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            delete_fields()
            try:
                df = pd.read_csv(file_path, header=None)  # Thêm header=None để bỏ qua dòng đầu tiên

                if not all(df.apply(np.isreal).all()):
                    messagebox.showerror("Error", "File chứa dữ liệu không phải kiểu số.")
                    return

                num_equations, num_columns = df.shape

                # Nếu ô nhập số phương trình trống, sử dụng số phương trình từ file CSV
                if n_entry.get() == '':
                    n_entry.insert(tk.END, str(num_equations))

                for i in range(num_equations):
                    frame = tk.Frame(window)
                    frame.pack(side=tk.TOP, padx=10, pady=5)
                    equation_frames.append(frame)

                    equation_entries = []
                    label = tk.Label(frame, text=f"Phương trình {i + 1}:")
                    label.pack(side=tk.LEFT)

                    for j in range(num_columns - 1):
                        entry = tk.Entry(frame)
                        entry.pack(side=tk.LEFT)
                        entry.insert(tk.END, str(df.iloc[i, j]))
                        equation_entries.append(entry)

                    # Thêm entry cho kết quả
                    entry_result = tk.Entry(frame)
                    entry_result.pack(side=tk.LEFT)
                    entry_result.insert(tk.END, str(df.iloc[i, -1]))
                    equation_entries.append(entry_result)

                    equation_entries_list.append(equation_entries)
            except Exception as e:
                messagebox.showerror("Error", f"Error reading CSV file: {str(e)}")

    def save_result_to_csv():
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

            if file_path:
                coefficients = []
                results = []

                for entry_list in equation_entries_list:
                    equation_coefficients = []
                    for entry in entry_list[:-1]:
                        val = float(entry.get())
                        equation_coefficients.append(val)
                    coefficients.append(equation_coefficients)

                    result_val = float(entry_list[-1].get())
                    results.append(result_val)

                a = np.array(coefficients)
                b = np.array(results)

                if np.linalg.matrix_rank(a) == np.linalg.matrix_rank(np.column_stack((a, b))) == a.shape[1]:
                    x = np.linalg.solve(a, b)

                    with open(file_path, 'w', newline='') as csv_file:
                        writer = csv.writer(csv_file)

                        writer.writerow([f'x{i + 1}' for i in range(len(equation_entries_list[0]) - 1)] + ['Result'])
                        for coefficients, result in zip(coefficients, results):
                            writer.writerow(coefficients + [result])

                        writer.writerow(
                            [''] * (len(equation_entries_list[0]) - 1) + [f'x{i + 1}' for i in range(len(x))])
                        writer.writerow([''] * (len(equation_entries_list[0]) - 1) + [round(val, 2) for val in x])

                    messagebox.showinfo("Thông báo", "Hệ phương trình và kết quả đã được lưu vào file CSV.")
                else:
                    messagebox.showwarning("Cảnh báo", "Hệ phương trình không có nghiệm duy nhất.")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def show_history():
        history_window = tk.Toplevel(window)
        history_window.title("Lịch sử kết quả")

        for entry in history:
            tk.Label(history_window,
                     text=f"Coefficients: {entry['coefficients']}, Results: {entry['results']}, Solution: {entry['solution']}").pack()

    def tinh_bac_ma_tran():
        try:
            he_so = []
            for entry_list in equation_entries_list:
                he_so_phuong_trinh = []
                for entry in entry_list[:-1]:
                    val = float(entry.get())
                    he_so_phuong_trinh.append(val)
                he_so.append(he_so_phuong_trinh)

            # Xác định bậc của ma trận bằng cách sử dụng hàm calculate_rank
            bac = calculate_rank(he_so)

            result.delete(1.0, tk.END)
            result.insert(tk.END, f"Bậc của ma trận là: {bac}")

            print(f"Bậc của ma trận là: {bac}")

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def calculate_rank(coefficients):
        # Chuyển list thành mảng NumPy
        matrix = np.array(coefficients)

        # Sử dụng np.linalg.matrix_rank để tính rank của ma trận
        rank = np.linalg.matrix_rank(matrix[:, :-1])  # Lấy tất cả cột trừ cột cuối cùng (cột kết quả)
        return rank

    window = tk.Tk()
    window.title("Giải hệ phương trình tuyến tính")


    equation_entries_list = []
    equation_frames = []
    btn_choose_csv = tk.Button(window, text="Chọn File CSV", command=choose_csv_file)
    btn_choose_csv.pack()

    n_level = tk.Label(window, text="Nhập số phương trình (max = 10)")
    n_level.pack()
    n_entry = tk.Entry(window)
    n_entry.pack()

    btn_create = tk.Button(window, text="Tạo", command=lambda: validate_input(n_entry) and create(n_entry))
    btn_create.pack()

    btn_delete = tk.Button(window, text="Xóa dữ liệu", command=delete_fields)
    btn_delete.pack()

    btn_tinh_bac = tk.Button(window, text="Tính Bậc Ma Trận", command=tinh_bac_ma_tran)
    btn_tinh_bac.pack()

    btn_solve = tk.Button(window, text="Giải", command=solve)
    btn_solve.pack()

    result_label = tk.Label(window, text="Kết quả")
    result_label.pack()

    result = tk.Text(window, height=3, width=30)
    result.pack()

    btn_save_result = tk.Button(window, text="Lưu Kết Quả (CSV)", command=save_result_to_csv)
    btn_save_result.pack()

    btn_show_history = tk.Button(window, text="Xem Lịch Sử", command=show_history)
    btn_show_history.pack()

    # Thêm nút "Back" để quay lại màn hình chính
    back_button = tk.Button(window, text="Back", command=lambda: show_main_function(window))
    back_button.pack()

    window.mainloop()
