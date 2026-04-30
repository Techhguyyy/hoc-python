# print("Hello, World!")
# print("2468 + 1234 = ",2468 + 1234)
# print("2468 + 1234 = ",2468 - 1234)
# print("2468 + 1234 = ",2468 * 1234)
# print("2468 + 1234 = ",2468 / 1234)


# print("Area =",7.8 * 6.4)
# print("Perimeter =",(7.8 + 6.4) * 2)


# BIẾN TRONG PYTHON
# Trong py,bạn ko cần khai báo biến một cách tường minh trước khi sử dụng cũng như khai báo kiểu dữ liệu của chúng.Biến được tạo ra khi ra gán giá trị cho nó.
# VD:
# Khai báo biến a và gán giá trị cho a = 5
# a = 5
# Khai báo biến b và gán trá trị cho b = 7
# b = 7
# print("a + b =",a + b)
# Kết quả khi chạy chương trình:a + b = 12

# QUY TẮC

# Bắt đầu bằng chữ cái hoặc dấu gạch dưới _
# Chỉ chứa chữ cái, số và dấu gạch dưới
# Phân biệt hoa thường (name ≠ Name)
# Không dùng từ khóa Python (if, for, class,...)


#1.2. Quy tắc đặt tên biến
# Đúng
# ten = "Nam"
# tuoi_hoc_sinh = 18
# _private = 10
# HANG_SO = 100
# camelCase = True
# snake_case = True

# Sai
# 2ten = "Nam"        # Không bắt đầu bằng số
# ten-hoc-sinh = 18   # Không dùng dấu gạch ngang
# class = "A1"        # Không dùng từ khóa Python


#1.3 Gán giá trị cho biến
# Gán đơn
# x = 10

# Gán nhiều biến cùng lúc
# a, b, c = 1, 2, 3

# Gán cùng giá trị
# x = y = z = 0

# Hoán đổi giá trị
# a, b = 5, 10
# a, b = b, a  # a=10, b=5


#1.4. Kiểm tra kiểu dữ liệu
# x = 100
# print(type(x)) # <class 'int'>

# Kiểm tra kiểu
#isinstance(x, int) #True


#1.5. Xóa biến
#x = 10
#del x # Xóa biến x

#2.CÁC KIỂU DỮ LIỆU CƠ BẢN
#2.1. KIỂU SỐ (Numeric Types)

# 2.1.1. Integer (int) - Số nguyên
# x = 10
# y = -5
# z = 0
# big_number = 1_000_000  # Dùng dấu _ để dễ đọc

# # Hệ số khác nhau
# binary = 0b1010      # Hệ nhị phân = 10
# octal = 0o12         # Hệ bát phân = 10
# hexa = 0xA           # Hệ thập lục phân = 10


# 2.1.2. Float - Số thực
# x = 3.14
# y = -0.5
# z = 2.0
# scientific = 1.5e2   # 1.5 * 10^2 = 150.0

# # Lưu ý về độ chính xác
# print(0.1 + 0.2)     # 0.30000000000000004


#2.1.3. Complex - Số phức
# x = 3 + 4j
# y = complex(2, 5)    # 2 + 5j

# # Truy cập phần thực và phần ảo
# print(x.real)        # 3.0
# print(x.imag)        # 4.0


# so_nguyen = 5000
# so_thap_phan = 1.2345
# string_var = 'Codelearn.io'
# boolean_var = False

# print(so_nguyen)
# print(so_thap_phan)
# print(string_var)
# print(boolean_var)

# name = "Codelearn"
# date_of_birth = 2019
# print("Name:",name)
# print("Date of birth:",date_of_birth)


# a = 438
# b = 636
# print("a + b = " + str(a+b))
# print("a + b = " + str(a-b))
# print("a + b = " + str(a*b))
# print("a + b = " + str(a/b))


# length = 7.8
# width = 3.5
# print("Area: " + str(length * width))
# print("Perimeter: " + str((length + width) * 2))



# Sử dụng hàm input() để nhập dữ liệu cho biến từ bàn phím:
# name = input()
# print("Hello " + name)
# Bạn cần lưu ý rằng khi nhập dữ liệu cho một biến từ bàn phím thì kiểu dữ liệu của biến đó luôn là str (kể cả bạn có nhập giá trị số cho biến đó).
# VD
# age = input()
# print(type(age))


#Baitap:Bạn hãy viết chương trình nhập vào tên của mình từ bàn phím và thực hiện hiển thị ra màn hình dòng chữ:
# Hello {P}
# Với {P} là tên bạn vừa nhập từ bàn phím.

# name = input()
# print("Hello " + name)





# Trong Python,dữ liệu nhập từ bàn phím luôn có kiểu là str (hàm input() trả về kiểu str),mà biến kiểu str thì ko thể tính toán được.Do đó cần chuyển kiểu dũ liệu của biến age về kiểu dữ liệu int,để làm việc này bạn cần sử dụng hàm int().
# Ví dụ
# age = int(input())
# age = age + 10
# print(age)
# print(type(age))

# name = input()
# age = int(input())
# agee = age + 15
# print("In 15 years, age of",name,"will be",agee)



# Bạn hãy viết chương trình nhập vào từ bàn phím 2 số nguyên a và b. Sau đó hiển thị ra màn hình thông tin sau:
# a % b = {P}
# Với {P} là phần dư của phép chia a/b.

# a = int(input())
# b = int(input())
# print("a % b =",a % b)

# Bạn hãy viết chương trình nhập vào từ bàn phím 2 biến kiểu số nguyên a và b. Sau đó hiển thị ra các phép tính trên 2 số này giống như sau:
# a + b = {P1}
# a - b = {P2}
# a * b = {P3}
# a / b = {P4}
# a % b = {P5}
# Trong đó:

# {P1} là tổng của a và b.
# {P2} là hiệu của a và b.
# {P3} là tích của a và b.
# {P4} là thương của a và b.
# {P5} là phần dư của phép chia a/b.

# a = int(input())
# b = int(input())
# print("a + b =",a + b)
# print("a - b =",a - b)
# print("a * b =",a * b)
# print("a / b =",a / b)
# print("a % b =",a % b)



# Cho 2 biến lưu trữ các số nguyên a và b được nhập từ bàn phím, bạn hãy viết chương trình hoán đổi giá trị của biến a và biến b. Sau đó hiển thị ra màn hình:
# after swap a = {P1}, b = {P2}
# Với {P1} và {P2} lần lượt là giá trị của a và b sau khi đã hoán đổi.

# a = int(input())
# b = int(input())
# c = a
# a = b
# b = c
# print("after swap a = " + str(a) + ", b = " + str(b))



# Viết chương trình nhập từ bàn phím bán kính r của một hình tròn và hiển thị ra màn hình chu vi của hình tròn đó giống như sau:
# Circumference = {P}

# r = float(input())
# pi = 3.14
# print("Circumference = " , 2 * r * pi )







# Viết chương trình tính diện tích hình tam giác có chiều cao h và độ dài cạnh đáy a được nhập từ bàn phím (chiều cao và độ dài cạnh đáy của hình tam giác này là một số nguyên). Sau đó, in ra màn hình "The area of triangle is {P}" với {P} là diện tích của hình tam giác.

# chieucao = int(input())
# canhday = int(input())
# dientich = 1/2 * canhday * chieucao
# print("The area of triangle is" , dientich)


# Viết chương trình nhập từ bàn phím hai số nguyên x và y. Sau đó, kiểm tra giá trị của x có lớn hơn giá trị y hay không. Nếu có (x lớn hơn y) thì in ra x > y: True, ngược lại in ra x > y: False.

# x = int(input())
# y = int(input())
# print("x > y:",x > y)


# a = int(input())
# Total = int(input())
# Total += a
# print("The Value of the Total after using += Operator is:",Total)
# Total -= a
# print("The Value of the Total after using -= Operator is:",Total)
# Total *= a
# print("The Value of the Total after using *= Operator is:",Total)
# Total //= a
# print("The Value of the Total after using //= Operator is:",Total)
# Total **= a
# print("The Value of the Total after using **= Operator is:",Total)
# Total /= a
# print("The Value of the Total after using /= Operator is:",Total)
# Total %= a
# print("The Value of the Total after using %= Operator is:",Total)


# Viết chương trình nhập từ bàn phím xâu x và kiểm tra xem trong xâu x có chứa ký tự 'H' hay không, nếu có thì hiển thị ra màn hình True, ngược lại hiển thị False.

# x = input()
# print("H" in x)

#Viết chương trình nhập từ bàn phím 2 số nguyên a và b. Sau đó kiểm tra xem số a và b có cùng giá trị hay không, nếu có thì hiển thị ra màn hình True, ngược lại hiển thị False.
# a = int(input())
# b = int(input())
# print(a is b)


# Cho 4 số nguyên x, y, z và t được nhập từ bàn phím. Bạn hãy viết chương trình để kiểm tra 4 giá trị này có thoả mãn điều kiện x > y và z < t hay không. In ra màn hình "Result evaluation is True" nếu 4 số thoả mãn điều kiện; nếu không, in ra "Result evaluation is False".
# x = int(input())
# y = int(input())
# z = int(input())
# t = int(input())
# print("Result evaluation is",x > y and z < t)

# Cho số nguyên age chỉ tuổi của một con mèo được nhập vào từ bàn phím. Bạn hãy viết chương trình để kiểm tra xem con mèo của bạn là già hay còn trẻ. Nếu tuổi của con mèo dưới 5 (age <5), thì hiển thị ra màn hình dòng chữ Your cat is young, ngược lại nếu tuổi của con mèo lớn hơn hoặc bằng 5 tuổi thì hiển thị ra Your cat is old.

# age = int(input())
# if age < 5:
#     print("Your cat is young")
# else:
#     print("Your cat is old")








# Câu lệnh Break
# Câu lệnh break được dùng để thoái khỏi vòng lặp,khi chương trình gặp câu lệnh break thì vòng lặp sẽ không được thực thi tiếp
#Ví dụ
# for i in range(1,11):
#     if i == 6:
#         break
#     print(i)

# Câu lệnh Continue
# Khi gặp câu lệnh continue trong vòng lặp, các đoạn code bên dưới câu lênh này trong vòng lặp sẽ không được thực thi.
#Ví dụ
# for i in range(1,20):
#     if i % 2 == 0:
#         continue
#     print(i)




# Cho chuỗi s được nhập từ bàn phím, bạn hãy viết chương trình hiển thị ra màn hình các kí tự khác kí tự 'y' trong chuỗi s
# s = input()
# for c in s:
#     if c == 'y':
#         continue
#     print("Current character:", c)




# Cho số nguyên a được nhập từ bàn phím, bãn hãy viết chương trình hiển thị ra kết quả khi nhân a với các số từ 1 đến 5.
# a = int(input())
# for i in range(1,6):
#     print(a,"*",i,"=", a * i)

         

# Cho hai số nguyên a và b được nhập từ bàn phím, bạn hãy viết chương trình đếm số các số chẵn và số các số lẻ trong khoảng từ a tới b. Sau đó hiển thị ra màn hình thông tin sau:
# Number of even numbers: {P1}
# Number of odd numbers: {P2}
# Trong đó {P1} và {P2} lần lượt là số các số chẵn và số các số lẻ trong khoảng [a, b].

# a = int(input())
# b = int(input())
# chan = 0
# le = 0
# for i in range(a,b + 1):
#     if i % 2 == 0:
#         chan += 1
#     else:
#         le += 1
# print("Number of even number:",chan)
# print("Number of odd number:",le)







# Sử dụng hàm round để làm tròn các số thực
# Cú pháp hàm round:
# round(number,ndigits)(Trong đó number là số cần làm tròn,ndigits là số chữ số sau dấu phẩy cần làm tròn)
#print(round(1.23, 1))
# print(round(2.665, 2))
# print(round(2.673567, 4))

# Bài tập:Cho số nguyên n được nhập vào từ bàn phím, bạn hãy viết chương trình hiển thị ra tổng của dãy số 1/2 + 2/3 + ... + n/n+1.
# Lưu ý: chỉ hiển thị 2 chữ số thập phân sau dấu phẩy.

# n = int(input())
# ans = 0
# for i in range(1,n+1):
#     ans += i / (i + 1)
# print(round(ans,2))








# LIST
#List trong py là một kiểu dữ liệu cho phép lưu trữ nhiều kiểu dữ liệu khác.
#Để khởi tạo một list trong py bạn có thể sử dụng cặp dấu [].Ví dụ

# Tạo ra list để lưu trữ các số nguyên
# list1 = [1, 2, 3]
# Tạo ra list để lưu trữ các xâu ký tự
# list2 = ["Viet", "Tuan", "Duong"]
# Bạn cũng có thể tạo ra một list lưu trữ các kiểu dữ liệu khác nhau
# list3 = [7, 3.5, "Codelearn"]

#Để truy xuất tới các phần tử trong list bạn dùng toán tử [].Ví dụ
# names = ["Viet" , "Dung", "Huong"]
# print(names[0])
# print(names[1])
# print(names[2])


# Lưu ý: names[1] không phải là phần tử đầu tiên của list mà phải là names[0] (do chỉ số của list được bắt đầu từ 0).

# Bạn cũng có thể dùng vòng lặp for để duyệt qua các phần tử của list. Ví dụ:

# names = ["Viet", "Dung", "Huong"]
# for name in names:
#     print(name)
# Để thêm một phần tử vào cuối của list bạn dùng hàm append():

# lst = []
# lst.append(4)
# lst.append(3)
# lst.append(6)
# print(lst)




#Bai tap:Cho một list các số nguyên n phần tử lst được nhập từ bàn phím. Bạn hãy viết chương trình hiển thị ra màn hình số nhỏ nhất trong list vừa nhập.
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# min_value = lst[0]
# for i in lst:
#     if i < min_value:
#         min_value = i
# print(min_value)


#Bai tap:Cho một list các số nguyên n phần tử được nhập từ bàn phím. Hãy viết chương trình hiển thị ra màn hình số lớn nhất trong list vừa nhập.
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# max = lst[0]
# for i in lst:
#     if i > max:
#         max = i
# print(max)


#Bai tap:Cho một list các số nguyên n phần tử được nhập từ bàn phím. Hãy viết chương trình tính và hiển thị tổng của tất cả các số chẵn trong list.
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
tongsochan = 0
for i in lst:
    if i % 2 == 0:
        tongsochan += i 
print(tongsochan)