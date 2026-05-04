# Bài 1: Xin chào!
# Yêu cầu: Viết chương trình in ra màn hình dòng chữ: "Xin chao Python!"
# Mở rộng: In ra trên 3 dòng khác nhau họ tên, tuổi, và nghề nghiệp của bạn (dùng 1 lệnh print duy nhất, xuống dòng bằng \n).

# print('Xin chao Python!\nTechguy\n18\nSinh vien ')




# Bài 2: Tính tổng hai số
# Yêu cầu: Nhập hai số nguyên a và b từ bàn phím. Tính tổng, hiệu, tích, thương của chúng và in kết quả ra màn hình.

# a = int(input("Nhap so nguyen: "))
# b = int(input("Nhap so nguyen: "))
# tong = a + b
# hieu = a - b
# tich = a * b
# thuong = a / b
# print("Tong:",tong)
# print("Hieu:",hieu)
# print("Tich:",tich)
# print("Thuong:",thuong)




# Bài 3: Tính tuổi
# Yêu cầu: Nhập năm sinh của bạn. Tính và in ra số tuổi hiện tại (giả sử năm hiện tại là 2026). Chương trình không cần xét đến ngày tháng cụ thể.

# nam_sinh = int(input("Nhap nam sinh: "))
# tuoi = 2026 - nam_sinh
# print("Ban",tuoi,"tuoi.")



# Bài 4: Đổi độ C sang độ F
# Yêu cầu: Nhập nhiệt độ theo độ C (Celsius) là một số thực. Chuyển đổi sang độ F (Fahrenheit) theo công thức: F = C * 9/5 + 32. In kết quả ra màn hình.

# do_c = float(input("Nhap do c: "))
# do_f = do_c * 9/5 + 32
# print("F =",do_f)





# Bài 5: Tính chỉ số BMI
# Yêu cầu: Nhập cân nặng (kg) và chiều cao (mét). Tính chỉ số BMI theo công thức BMI = can_nang / (chieu_cao ** 2). In ra BMI đã được làm tròn đến 1 chữ số thập phân.

# can_nang = int(input("Nhap can nang:"))
# chieu_cao = float(input("Nhap chieu cao:"))
# Bmi = can_nang / (chieu_cao ** 2)
# print(f"BMI = {Bmi:.1f}")




# Bài 6: Tách số
# Yêu cầu: Nhập một số có 4 chữ số (ví dụ: 2468). Hãy in ra từng chữ số trên một dòng riêng biệt.
# Gợi ý: Kết hợp toán tử chia lấy nguyên // và chia lấy dư %.

# n = int(input("Nhap so co 4 chu so: "))
# nghin = n // 1000
# tram = (n % 1000) // 100
# chuc = (n % 100) // 10
# don_vi = n % 10

# print(nghin)
# print(tram)
# print(chuc)
# print(don_vi)





# Bài 7: Tính trung bình cộng
# Yêu cầu: Nhập vào 5 số thực bất kỳ từ bàn phím. Tính tổng và trung bình cộng của 5 số đó. In kết quả chính xác đến 2 chữ số thập phân.

# so_thu_nhat = float(input("Nhap so thuc bat ky: "))
# so_thu_hai = float(input("Nhap so thuc bat ky: "))
# so_thu_ba = float(input("Nhap so thuc bat ky: "))
# so_thu_tu = float(input("Nhap so thuc bat ky: "))
# so_thu_nam = float(input("Nhap so thuc bat ky: "))

# so_tb_cong = (so_thu_nhat + so_thu_hai + so_thu_ba + so_thu_tu + so_thu_nam) / 5
# print("Trung binh cong:",so_tb_cong)






# Bài 8: Đổi giây ra giờ, phút, giây
# Yêu cầu: Nhập vào một số nguyên t là số giây. Chuyển đổi t thành dạng Gio:Phut:Giay. Mỗi thành phần hiển thị 2 chữ số (có thể dùng zfill hoặc f-string).
t = int(input("Nhap so giay: "))
gio = t // 3600
giay_con_lai = t % 3600
phut = giay_con_lai // 60
giay = giay_con_lai % 60
print(f"{gio: 02d}:{phut:02d}:{giay:02d}")
