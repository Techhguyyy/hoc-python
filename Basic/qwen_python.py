#Bai 1:Bien va kieu du lieu co ban


# Bài tập 1: Thông tin cá nhân
# Tạo 3 biến: ho_ten (chuỗi), nam_sinh (số nguyên), diem_tb (số thực).
# Gán giá trị tùy thích cho 3 biến này.
# In ra màn hình dòng: Xin chào [ho_ten], bạn sinh năm [nam_sinh] và có điểm trung bình là [diem_tb].

# ho_ten = "Tien thoi"
# nam_sinh = 2007
# diem_tb = 9.0
# print("Ten:",ho_ten)
# print("Sinh nam:",nam_sinh)
# print("Diem trung binh la:",diem_tb)



# Bài tập 2: Tính diện tích hình chữ nhật
# Khai báo 2 biến chieu_dai và chieu_rong (gán số tùy ý, ví dụ 5 và 3).
# Tính diện tích (dien_tich = chieu_dai * chieu_rong).
# In ra kết quả.

# chieu_dai = 4
# chieu_rong = 5
# dien_tich = chieu_dai * chieu_rong
# print("Dien tich hinh chu nhat la:",dien_tich)




# Bài tập 3: Đổi tiền (Khó hơn chút xíu)
# Hỏi người dùng nhập vào so_usd (số đô la Mỹ) bằng lệnh input().
# Biết tỷ giá: 1 USD = 25.000 VND (giả sử).
# Tính số tiền VND tương ứng.
# In ra màn hình: [so_usd] USD tương đương với [so_vnd] VND.
# Gợi ý: Nhớ dùng float() hoặc int() để ép kiểu dữ liệu từ input() nhé!


# so_usd = int(input("Nhap so tien usd: "))
# ty_gia = 25000
# so_vnd = so_usd * ty_gia
# print(so_usd,"USD tuong duong voi",so_vnd,"VND")
# print(f"{so_usd} USD tuong duong voi {so_vnd:,.0f} VND")




# Bài 4: Số chẵn hay lẻ?
# Hỏi người dùng nhập một số nguyên.
# Dùng toán tử chia lấy dư % (ví dụ: 5 % 2 sẽ ra 1 vì 5 chia 2 dư 1).
# Nếu số đó chia hết cho 2 (dư 0) thì in ra "Số chẵn".
# Ngược lại in ra "Số lẻ".


# so_nguyen = int (input("Nhap so nguyen: "))
# if so_nguyen % 2 == 0:
#     print("So chan")
# else:
#     print("So le")



# Bài 5: Máy tính đơn giản
# Hỏi người dùng nhập 2 số: a và b.
# Hỏi người dùng chọn phép tính: +, -, *, /.
# Dùng if/elif/else để kiểm tra phép tính người dùng chọn và in ra kết quả tương ứng.
# Gợi ý: Nếu người dùng chọn / mà b bằng 0, hãy in ra "Không thể chia cho 0" để tránh lỗi nhé!


a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))
phep_toan = input ("Chon phep tinh (+ ,-,*, /): ")

if phep_toan == "+":
    ket_qua = a + b
    print(f"ket qua: {a} + {b} = {ket_qua}")

elif phep_toan == "-":
    ket_qua = a - b
    print(f"Ket qua: {a} - {b} = {ket_qua}")

elif phep_toan == "*":
    ket_qua = a - b
    print(f"Ket qua: {a} * {b} = {ket_qua}")

elif phep_toan == "/":
    if b == 0:
        print("Loi: Khong the chia cho 0!")
    else:
        ket_qua = a / b 
        print(f"Ket qua: {a} / {b} = {ket_qua}")
else:
    print("Phep toan khong hop le! vui long chon +,-,*,/")
    



