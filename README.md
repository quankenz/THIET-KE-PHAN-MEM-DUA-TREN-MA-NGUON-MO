# THIET-KE-PHAN-MEM-DUA-TREN-MA-NGUON-MO
# NHOM 10
#1 VŨ ĐÌNH TUẤN

#2 VŨ THU PHƯƠNG

#3 NGUYỄN CÔNG MINH

#4 NGUYỄN ĐỨC QUÂN

Phân tích chức năng của đoạn mã gốc: Giải hệ phương trình tuyến tính hai ẩn x và y

Đoạn mã gốc:
# bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# để có 1 app giải hệ phương trình có n phương trình n ẩn
  - import numpy as np
  - A = np.array([(1,2),(3,4)])
  - B = np.array([5,6])
  - A1  = np.linalg.inv(A) # tạo ma trận nghich đảo
  - print(A)
  - print(B)
  - print(A1)
  - X = np.dot(A1,B)
  - print('Nghiem cua he:',X)
  - print('lam thu')
  - print('aaaaaaaaaaaaaaaaaaaaaaaa')

Phân tích đoạn mã gốc:
- Sử dụng thư viện hỗ trợ numpy để tạo ra ma trận A có kích thước 2x2 và ma trận B có kích thước 2x1 bằng câu lệnh np.arr()
- Tính ma trận nghịch đảo của ma trận A bằng cách sử dụng hàm inv từ module linalg của NumPy. Nếu ma trận không khả nghị, mã sẽ raise một lỗi.
- In ra ma trận A, B, B1
- Tính tích vô hướng (dot product) giữa ma trận nghịch đảo của A và ma trận cột B để tìm nghiệm của hệ phương trình tuyến tính Ax = B bằng lệnh np.dot()
- In ra nghiệm của hệ và 2 chuỗi 'lam thu' và 'aaaaaaaaaaaaaaaaaaaaaaaa'.

Link code gốc: https://github.com/QuynhTrang26/baivenumpy/blob/main/giai_he_PT.py

Ý tưởng cải tiến/ phát triển từ đoạn mã gốc:
Giải tích: tích phân, đạo hàm, khai triển và rút gọn biểu thức, giới hạn
Đại số tuyến tính: Giải hệ phương trình, tính bậc ma trận, xem lịch sử, cho phép nhập số phương trình.

Hướng phát triển:
-Tích hợp thêm hình học
-Giao diện thân thiện và dễ sử dụng hơn
-Kết hợp vẽ biểu đồ và đồ thị
-Hỗ trợ đa ngôn ngữ
