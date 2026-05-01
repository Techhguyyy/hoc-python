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

can_nang = int(input("Nhap can nang:"))
chieu_cao = float(input("Nhap chieu cao:"))
Bmi = can_nang / (chieu_cao ** 2)
print(f"BMI = {Bmi:.1f}")