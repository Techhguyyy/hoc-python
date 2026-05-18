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

# t = int(input("Nhap so giay: "))
# gio = t // 3600
# giay_con_lai = t % 3600
# phut = giay_con_lai // 60
# giay = giay_con_lai % 60
# print(f"{gio: 02d}:{phut:02d}:{giay:02d}")






# Bài 9: Hoán đổi 3 biến (Theo vòng tròn)
# Yêu cầu: Cho 3 biến x, y, z được gán giá trị bất kỳ. Hoán đổi giá trị của chúng theo vòng tròn: Giá trị của x chuyển sang y, y sang z, z sang x.

# Ví dụ: Ban đầu x=5, y=10, z=15 -> Sau khi đổi: x=15, y=5, z=10.

# Gợi ý: Trong Python có thể làm đơn giản bằng x, y, z = z, x, y


# x = float(input("Nhap so bat ky: "))
# y = float(input("Nhap so bat ky: "))
# z = float(input("Nhap so bat ky: "))
# x,y,z = z,y,x
# print("x = ",x)
# print("y = ",y)
# print("z = ",z)




# Bài 10: Tính tổng các ước số (cơ bản)
# Yêu cầu: Nhập một số nguyên dương n. Hãy tính tổng các ước số thực sự của n. Ước số thực sự là các số tự nhiên nhỏ hơn n chia hết cho n (không tính chính nó).

# n = int(input("Nhap vao so nguyen duong: "))
# sum = 0
# for i in range(1,n):
#     if n % i == 0:
#         sum += i
# print("Tong cua so nhap vao la: ",sum)















# Bài 1: In dãy số tự nhiên
# Yêu cầu: Nhập số nguyên dương n. In ra các số từ 1 đến n, mỗi số cách nhau bởi dấu cách.

# for

# n = int(input("Nhap vao mot so nguyen: "))
# for i in range(1,n + 1):
#     print(i,end=" ")

#While
# n = int(input("Nhap vao mot so nguyen: "))
# i = 1
# while i <= n:
#     print(i,end= " ")
#     i += 1




# Bài 2: Tính tổng từ 1 đến n
# Yêu cầu: Nhập số nguyên dương n. Tính tổng S = 1 + 2 + 3 + ... + n.
# Thực hiện: Dùng cả for và while.

#for 
# n = int(input("Nhap so nguyen duong: "))
# tong = 0
# for i in range(1,n + 1):
#     tong += i
# print(tong)

#while
# n = int(input("Nhap so nguyen duong: "))
# tong = 0
# i = 1
# while i <= n:
#     tong += i
#     i += 1
# print(tong)



# Bài 3: In bảng cửu chương
# Yêu cầu: Nhập số nguyên n (từ 1 đến 9). Dùng vòng lặp for in ra bảng cửu chương của n.

# n = int(input("Nhap so ban muon: "))
# if n < 2 or n > 9:
#     print("Yeu cau ban nhap lai so!")
# else:
#     for i in range(1,11):
#         ket_qua = n * i
#         print(f"{n} x {i:2d} = {ket_qua}")



# Bài 4: In toàn bộ bảng cửu chương
# Yêu cầu: Dùng 2 vòng lặp lồng nhau in ra tất cả bảng cửu chương từ 1 đến 10. Mỗi bảng cách nhau một dòng trống.

# for i in range(2,10):
#     for j in range(1,11):
#         ket_qua = i * j
#         print(f"{i:2d} x {j:2d} = {ket_qua:3d}")

#     print()




# Bài 5: Đếm số chữ số của một số
# Yêu cầu: Nhập số nguyên dương n. Dùng vòng lặp while đếm xem n có bao nhiêu chữ số.

# n = int(input("Nhap so mong muon: "))
# dem = 0
# while n > 0:
#     n = n // 10
#     dem += 1
# print(dem)







# Bài 6: Kiểm tra số nguyên tố
# Yêu cầu: Nhập số nguyên dương n. Dùng vòng lặp for kiểm tra xem n có phải số nguyên tố không.

# n = int(input("Nhap so nguyen duong: "))

# la_nguyen_to = True

# if n < 2:
#     la_nguyen_to = False
# else:
#     for i in range(2,n):
#         if n % i == 0:
#             la_nguyen_to = False
#             break

# if la_nguyen_to:
#     print(f"{n} la so nguyen to")
# else:
#     print(f"{n} ko phai so nguyen to")



# n = int(input("Nhap so nguyen duong bat ki: "))

# la_nguyen_to = True

# if n < 2:
#     la_nguyen_to = False
# else:
#     for i in range(2,n):
#         if n % i == 0:
#             la_nguyen_to = False
#             break
# if la_nguyen_to:
#     print(f"{n} la so nguyen to")
# else:
#     print(f"{n} ko phai la so nguyen to")





# Bài 7: In dãy Fibonacci
# Yêu cầu: Nhập số nguyên dương n. In ra n số Fibonacci đầu tiên.
# Quy luật: Số đầu tiên = 1, số thứ hai = 1, số tiếp theo = tổng 2 số trước đó.

# n = int(input("Nhap n: "))

# a = 1
# b = 1

# if n >= 1:
#     print(a,end=" ")
# if n >= 2:
#     print(b,end=" ")

# for i in range(3,n + 1):
#     c = a + b
#     print(c ,end=" ")
#     a = b
#     b = c

    





# Bài 9: Tính giai thừa
# Yêu cầu: Nhập số nguyên dương n. Tính n! (giai thừa của n).
# Công thức: n! = 1 * 2 * 3 * ... * n
# Thực hiện: Dùng for và while (cả 2 cách).

# n = int(input("Nhap so nguyen duong: "))

# giaithua = 1

# if n < 0:
#     print("Ko tinh duoc giai thua so am!")
# else:
#     for i in range(1,n + 1):
# giaithua *= i
# print(giaithua)









# =========================
# PHẦN LUYỆN FOR / WHILE (dễ - trung bình)
# =========================


# Bài 10 (FOR): In dãy số cách nhau 2
# Yêu cầu: Nhập số nguyên dương n. In ra các số: 1, 3, 5, ..., (số lớn nhất <= n).
# Ví dụ: n=7 => 1 3 5 7

# Gợi ý:
# - Dùng vòng lặp for: duyệt i từ 1 đến n theo bước 2 (range(1, n+1, 2))
# - In i ra màn hình (có thể dùng print(i, end=" "))


# n = int(input("Nhap vao so nguyen duong: "))

# for i in range(1,n + 1,2):
#     print(i,end=" ")





# Bài 11 (WHILE): Đảo ngược chữ số của một số nguyên
# Gợi ý:
# - Khởi tạo rev = 0
# - Trong khi n > 0:
#     + digit = n % 10
#     + rev = rev * 10 + digit
#     + n = n // 10
# - In rev

# Yêu cầu: Nhập số nguyên dương n. In ra số đảo ngược của n.
# Gợi ý: dùng % 10 lấy chữ số cuối và // 10 bỏ chữ số cuối.
# Ví dụ: n=1234 => 4321

# n = int(input("Nhap vao mot so nguyen duong:"))
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# print(rev)







# Bài 12 (FOR): Tính tổng các số chẵn trong đoạn [1..n]
# Yêu cầu: Nhập n. Tính và in ra tổng các số chẵn từ 1 đến n.
# Ví dụ: n=10 => 2+4+6+8+10
# Gợi ý:
# - Duyệt bằng for với range(2, n+1, 2)
# - Khởi tạo tong = 0, mỗi lần cộng i vào
# - In tong

# n = int(input("Nhap vao mot so bat ky:"))

# sum = 0
# for i in range(2,n + 1,2):
#     sum += i
# print(sum)






# Bài 13 (WHILE): Kiểm tra số nguyên tố (tối giản)
# Yêu cầu: Nhập số nguyên dương n. Dùng while để kiểm tra n có phải số nguyên tố không.
# Gợi ý: chỉ cần thử chia đến khi i*i > n.

n = int(input("Nhap vao so bat ky: "))

i = 2
so_nguyen_to = True

if n < 2:
    so_nguyen_to = False

while i * i <= n:
    if n % i == 0:
        so_nguyen_to = False
        break
    i += 1

if so_nguyen_to:
    print(n,"la so nguyen to")
else:
    print(n,"Ko phai so nguyen to")



# Bài 14 (FOR): In tam giác số
# Yêu cầu: Nhập n. In ra tam giác theo mẫu:
# Với n=4:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# Dùng for để in theo từng dòng.


# Bài 15 (WHILE): Tìm ước chung của hai số (dạng cơ bản)
# Yêu cầu: Nhập hai số nguyên dương a và b. Tìm ước chung lớn nhất theo cách cơ bản:
# Dùng while giảm từ min(a,b) xuống tìm số chia hết cho cả a và b.


# Bài 16 (FOR): Đếm chữ số chẵn trong một số
# Yêu cầu: Nhập số nguyên dương n. Đếm xem trong n có bao nhiêu chữ số chẵn.
# Ví dụ: n=2487 => có 2,4 => 2 chữ số chẵn.


# Bài 17 (WHILE): Tính tổng chữ số của một số
# Yêu cầu: Nhập số nguyên dương n. Tính tổng các chữ số của n.
# Ví dụ: n=508 => 5+0+8 = 13.


# Bài 18 (FOR): In danh sách các số nguyên tố nhỏ hơn n
# Yêu cầu: Nhập n (n>2). In ra tất cả số nguyên tố < n, mỗi số cách nhau bởi dấu cách.
# Ví dụ: n=20 => 2 3 5 7 11 13 17 19


# Bài 19 (WHILE): Vẽ hình chữ nhật bằng ký tự '*'
# Yêu cầu: Nhập chiều cao h và chiều rộng w. Dùng while để in ra hình chữ nhật h dòng, mỗi dòng có w ký tự '*'.
# Ví dụ: h=3, w=5:
# *****
# *****
# *****


# (Không có đáp án) Chúc bạn luyện tập vui vẻ!













