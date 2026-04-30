# Phần 1: Biến, Kiểu dữ liệu và Nhập/Xuất cơ bản

# Bài 1: Lời chào cá nhân hóa
# Viết chương trình yêu cầu người dùng nhập tên của họ, sau đó in ra màn hình lời chào "Xin chào, [tên]!".

# Bài 2: Tính tuổi
# Yêu cầu người dùng nhập năm sinh của họ. Tính và in ra tuổi của họ trong năm hiện tại (giả sử năm hiện tại là 2024).

# Bài 3: Tính điểm trung bình
# Viết chương trình yêu cầu người dùng nhập điểm của 3 môn học (Toán, Văn, Anh). Tính điểm trung bình cộng và in kết quả ra màn hình.



#Bai 1
# ten = input("Nhập tên:")
# print("Xin chào",ten)



#Bai 2
# namsinh = int(input("Nhap nam sinh cua ban: "))
# namhientai = 2026
# tuoi = namhientai - namsinh
# print(tuoi)


#Bai 3
# toan =int(input(""))
# van =int(input(""))
# anh =int(input(""))
# trungbinh = (toan + van + anh) / 3
# print(trungbinh)




# Phần 2: Câu lệnh rẽ nhánh (if-elif-else)
# Bài 4: Kiểm tra số chẵn lẻ
# Nhập vào một số nguyên từ bàn phím. Kiểm tra xem số đó là số chẵn hay số lẻ và in kết quả.

# Bài 5: Tìm số lớn nhất
# Nhập vào 3 số nguyên từ bàn phím. Tìm và in ra số lớn nhất trong 3 số đó.

# Bài 6: Xếp loại học lực
# Nhập vào điểm trung bình của một học sinh. Xếp loại học lực theo tiêu chuẩn:

# Giỏi: điểm >= 8.0

# Khá: 6.5 <= điểm < 8.0

# Trung bình: 5.0 <= điểm < 6.5

# Yếu: điểm < 5.0


#Bai 4
# n = int(input())
# if n % 2 == 0:
#     print("Day la so chan")
# else:
#     print("Day la so le")




#Bai 5
# x = int(input())
# y = int(input())
# z = int(input())
# if x > y and x > z:
#     print("x la so lon nhat")
# if y > x and y > z:
#     print("y la so lon nhat")
# if z > x and z > y:
#     print("z la so lon nhat")



#Bai 6
# diemtrungbinh = float(input())
# if diemtrungbinh >= 8.0:
#     print("Gioi")
# if diemtrungbinh >= 6.5 and diemtrungbinh < 8.0:
#     print("Kha")
# if diemtrungbinh >= 5.0 and diemtrungbinh < 6.5:
#     print("trung binh")
# if diemtrungbinh < 5.0:
#     print("Yeu")




#Bai 7
#For
# n = int(input())
# for j in range(1,11):
#     print(f"{n} * {j} = {n * j}")


#While
# n = int(input())
# i = 1
# while i <= 10:
#     print(f"{n} * {i} = {n * i}")
#     i += 1


#Bai 8
n = int(input())
gia_thua = 1
for i in range(1,n + 1):
    gia_thua += i
print(f"{gia_thua}")





