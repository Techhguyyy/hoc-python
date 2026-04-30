# Bài 1: Kiểm tra số chẵn lẻ
# Viết chương trình nhập vào một số nguyên và kiểm tra xem số đó là chẵn hay lẻ

# n = int(input())
# if n % 2 == 0:
#     print("So chan")
# else:
#     print("So le")


# Bài 2: So sánh hai số
# Nhập vào hai số và in ra số nào lớn hơn, hoặc thông báo nếu hai số bằng nhau.
# a = float(input())
# b = float(input())
# if a > b:
#     print("a lon hon b")
# else:
#     if a < b:
#        print("a nho hon b")
#     else:
#         print("a bang b")



# Cho trước 3 số nguyên x, y, z được từ bàn phím. Bạn hãy viết chương trình hiển thị ra màn hình theo yêu cầu sau:
# Nếu x là số chẵn, kiểm tra xem y có lớn hơn hoặc bằng 20 hay không. Nếu y >= 20, in ra dòng chữ y is greater than or equal to 20; ngược lại, in ra dòng chữ y is less than 20.
# Nếu x là số lẻ, kiểm tra xem z có lớn hơn hoặc bằng 30 hay không. Nếu z >= 30, in ra dòng chữ z is greater than or equal to 30; ngược lại, in ra dòng chữ z is less than 30.

# x = int(input())
# y = int(input())
# z = int(input())

# if x % 2 == 0:
#     if y >= 20:
#         print("y is greater than or equal to 20")
#     else:
#         print("y is less than 20")
# else:
#     if z >= 30:
#         print("z is greater than or equal to 30")
#     else:
#         print("z is less than 30")


# Viết chương trình Python tính giá trị trung bình (avg) của ba biến a, b, c nhập từ bàn phím (a, b, c là ba số tự nhiên) với điều kiện như sau:
# Nếu avg > a và avg > b thì hiển thị The average value is greater than both a and b
# Nếu avg > a và avg > c thì hiển thị The average value is greater than both a and c
# Nếu avg > b và avg > c thì hiển thị The average value is greater than both b and c
# Nếu avg chỉ lớn hơn a thì hiển thị The average value is greater than a
# Nếu avg chỉ lớn hơn b thì hiển thị The average value is greater than b
# Nếu avg chỉ lớn hơn c thì hiển thị The average value is greater than c

# a = int(input())
# b = int(input())
# c = int(input())
# avg = (a + b + c) / 3

# if avg > a and avg > b:
#     print("The average value is greater than both a and b")
# elif avg > a and avg > c:
#     print("The average value is greater than both a and c")
# elif avg > b and avg > c:
#     print("The average value is greater than both b and c")
# elif avg > a:
#     print("The average value is greater than a")
# elif avg > b:
#     print("The average value is greater than b")
# elif avg > c:
#     print("The average value is greater than c")


#Bai tap:
# Cho số nguyên age chỉ tuổi của vật nuôi được nhập từ bàn phím, bạn hãy hiển thị ra màn hình theo yêu cầu sau:
# Nếu age <= 0 thì hiển thị "This can hardly be true"
# Nếu age == 1 thì hiển thị "About 1 human year"
# Nếu age == 2 thì hiển thị "About 2 human years"
# Nếu age > 2 thì hiển thị "Over 5 human years.

# age = int(input())
# if age <= 0:
#     print("This can hardly be true")
# elif age == 1:
#     print("About 1 human year")
# elif age == 2:
#     print("About 2 human years")
# elif age > 2:
#     print("Over 5 human years")





# Vòng lặp FOR và WHILE
#Vi du:Cho số nguyên dương n được nhập từ bàn phím, bạn hãy viết chương trình hiển thị ra màn hình tổng các số từ 1 tới n.
#Với vòng lặp while
# n = int(input())
# i = 1
# answer = 0
# while i <= n:
#     answer += i
#     i += 1
# print(answer)

# Với vòng lặp for
# n = int(input())
# answer = 0
# for i in range (1,n + 1):
#     answer += i
# print(answer)




# Cho 2 số nguyên a và b được nhập từ bàn phím, bạn hãy viết chương trình hiển thị ra tổng các số lẻ từ a tới b.

# a = int(input())
# b = int(input())
# tongcacsole = 0

# for i in range(a, b + 1):
#     if i % 2 != 0:  # Kiểm tra số lẻ
#         tongcacsole += i

# if tongcacsole % 3 == 0:
#     print(tongcacsole)






#Bài 1: Cho chuỗi s được nhập từ bàn phím, hãy viết chương trình đếm số lần xuất hiện của ký tự 'a' trong chuỗi s.
# s = input()
# print(s.count('a'))

# s = input() # (dùng vòng lặp đếm)
# dem = 0
# for c in s:
#     if c == 'a':
#         dem += 1
# print(dem)



# Bài 2: Cho chuỗi s được nhập từ bàn phím, hãy viết chương trình hiển thị ra màn hình chuỗi s sau khi thay thế tất cả ký tự 'e' thành ký tự '3'.


