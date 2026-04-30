# Biến và Kiểu Dữ Liệu trong Python - Hướng Dẫn Toàn Diện
# 1. BIẾN (VARIABLES)
# 1.1. Khái niệm
# Biến là vùng nhớ dùng để lưu trữ dữ liệu. Python là ngôn ngữ động, không cần khai báo kiểu dữ liệu trước.
# 1.2. Quy tắc đặt tên biến
# python# Đúng
# ten = "Nam"
# tuoi_hoc_sinh = 18
# _private = 10
# HANG_SO = 100
# camelCase = True
# snake_case = True

# # Sai
# # 2ten = "Nam"        # Không bắt đầu bằng số
# # ten-hoc-sinh = 18   # Không dùng dấu gạch ngang
# # class = "A1"        # Không dùng từ khóa Python
# Quy tắc:

# Bắt đầu bằng chữ cái hoặc dấu gạch dưới _
# Chỉ chứa chữ cái, số và dấu gạch dưới
# Phân biệt hoa thường (name ≠ Name)
# Không dùng từ khóa Python (if, for, class,...)

# 1.3. Gán giá trị cho biến
# python# Gán đơn
# x = 10

# # Gán nhiều biến cùng lúc
# a, b, c = 1, 2, 3

# # Gán cùng giá trị
# x = y = z = 0

# # Hoán đổi giá trị
# a, b = 5, 10
# a, b = b, a  # a=10, b=5
# 1.4. Kiểm tra kiểu dữ liệu
# pythonx = 100
# print(type(x))  # <class 'int'>

# # Kiểm tra kiểu
# isinstance(x, int)  # True
# 1.5. Xóa biến
# pythonx = 10
# del x  # Xóa biến x

# 2. CÁC KIỂU DỮ LIỆU CƠ BẢN
# 2.1. KIỂU SỐ (Numeric Types)
# 2.1.1. Integer (int) - Số nguyên
# pythonx = 10
# y = -5
# z = 0
# big_number = 1_000_000  # Dùng dấu _ để dễ đọc

# # Hệ số khác nhau
# binary = 0b1010      # Hệ nhị phân = 10
# octal = 0o12         # Hệ bát phân = 10
# hexa = 0xA           # Hệ thập lục phân = 10
# 2.1.2. Float - Số thực
# pythonx = 3.14
# y = -0.5
# z = 2.0
# scientific = 1.5e2   # 1.5 * 10^2 = 150.0

# # Lưu ý về độ chính xác
# print(0.1 + 0.2)     # 0.30000000000000004
# 2.1.3. Complex - Số phức
# pythonx = 3 + 4j
# y = complex(2, 5)    # 2 + 5j

# # Truy cập phần thực và phần ảo
# print(x.real)        # 3.0
# print(x.imag)        # 4.0
# Chuyển đổi giữa các kiểu số
# pythonx = 10
# float(x)     # 10.0
# complex(x)   # (10+0j)

# y = 3.7
# int(y)       # 3 (cắt bỏ phần thập phân)

# 2.2. KIỂU CHUỖI (String)
# 2.2.1. Tạo chuỗi
# python# Dấu nháy đơn hoặc kép
# s1 = 'Hello'
# s2 = "World"

# # Chuỗi nhiều dòng
# s3 = '''Dòng 1
# Dòng 2
# Dòng 3'''

# s4 = """Cũng được"""

# # Chuỗi thô (raw string)
# path = r"C:\new\folder"  # Không xử lý ký tự đặc biệt
# 2.2.2. Truy cập ký tự
# pythontext = "Python"
# print(text[0])      # P
# print(text[-1])     # n
# print(text[1:4])    # yth (slicing)
# print(text[:3])     # Pyt
# print(text[3:])     # hon
# print(text[::2])    # Pto (bước nhảy 2)
# print(text[::-1])   # nohtyP (đảo ngược)
# 2.2.3. Các phương thức chuỗi
# pythons = "  Hello World  "

# # Chuyển đổi
# s.upper()           # "  HELLO WORLD  "
# s.lower()           # "  hello world  "
# s.capitalize()      # "  hello world  "
# s.title()           # "  Hello World  "
# s.swapcase()        # "  hELLO wORLD  "

# # Loại bỏ khoảng trắng
# s.strip()           # "Hello World"
# s.lstrip()          # "Hello World  "
# s.rstrip()          # "  Hello World"

# # Tìm kiếm và thay thế
# s.find("World")     # 8 (vị trí tìm thấy, -1 nếu không tìm thấy)
# s.index("World")    # 8 (lỗi nếu không tìm thấy)
# s.count("l")        # 3
# s.replace("World", "Python")  # "  Hello Python  "

# # Kiểm tra
# s.startswith("  H") # True
# s.endswith("d  ")   # True
# "123".isdigit()     # True
# "abc".isalpha()     # True
# "abc123".isalnum()  # True

# # Tách và nối
# "a,b,c".split(",")  # ['a', 'b', 'c']
# "-".join(['a','b']) # "a-b"
# 2.2.4. Format chuỗi
# pythonname = "Nam"
# age = 20

# # f-string (Python 3.6+) - Khuyên dùng
# print(f"Tên: {name}, Tuổi: {age}")
# print(f"Tính: {5 + 3}")

# # format()
# print("Tên: {}, Tuổi: {}".format(name, age))
# print("Tên: {n}, Tuổi: {a}".format(n=name, a=age))

# # % formatting (cũ)
# print("Tên: %s, Tuổi: %d" % (name, age))

# # Format số
# pi = 3.14159
# print(f"{pi:.2f}")    # 3.14
# print(f"{pi:10.2f}")  # "      3.14" (rộng 10 ký tự)

# 2.3. KIỂU BOOLEAN (Bool)
# pythonx = True
# y = False

# # Giá trị falsy (được coi là False)
# bool(0)          # False
# bool("")         # False
# bool(None)       # False
# bool([])         # False
# bool({})         # False
# bool(())         # False

# # Giá trị truthy (được coi là True)
# bool(1)          # True
# bool("text")     # True
# bool([1,2])      # True

# # So sánh
# 5 > 3            # True
# 10 == 10         # True
# "a" in "abc"     # True

# 2.4. NONE TYPE
# pythonx = None

# # Kiểm tra None
# if x is None:
#     print("x là None")

# # None khác với False và 0
# None == False    # False
# None == 0        # False
# None is None     # True

# 3. CÁC KIỂU DỮ LIỆU TẬP HỢP
# 3.1. LIST - Danh sách (có thứ tự, thay đổi được)
# python# Tạo list
# numbers = [1, 2, 3, 4, 5]
# mixed = [1, "hai", 3.0, True, [5, 6]]
# empty = []
# empty2 = list()

# # Truy cập
# print(numbers[0])      # 1
# print(numbers[-1])     # 5
# print(numbers[1:4])    # [2, 3, 4]

# # Thêm phần tử
# numbers.append(6)       # Thêm cuối
# numbers.insert(0, 0)    # Thêm vào vị trí 0
# numbers.extend([7,8])   # Thêm nhiều phần tử

# # Xóa phần tử
# numbers.remove(3)       # Xóa phần tử có giá trị 3
# del numbers[0]          # Xóa phần tử vị trí 0
# popped = numbers.pop()  # Xóa và trả về phần tử cuối
# numbers.clear()         # Xóa tất cả

# # Các phương thức khác
# numbers = [3, 1, 4, 1, 5]
# numbers.sort()          # Sắp xếp tăng dần
# numbers.reverse()       # Đảo ngược
# numbers.count(1)        # Đếm số lần xuất hiện
# numbers.index(4)        # Tìm vị trí đầu tiên

# # List comprehension
# squares = [x**2 for x in range(10)]
# evens = [x for x in range(20) if x % 2 == 0]

# 3.2. TUPLE - Bộ (có thứ tự, KHÔNG thay đổi được)
# python# Tạo tuple
# t1 = (1, 2, 3)
# t2 = 1, 2, 3           # Không cần dấu ngoặc
# single = (5,)          # Tuple 1 phần tử phải có dấu phấy
# empty = ()

# # Truy cập (giống list)
# print(t1[0])           # 1
# print(t1[1:3])         # (2, 3)

# # Không thể thay đổi
# # t1[0] = 10           # Lỗi!

# # Giải nén tuple
# a, b, c = (1, 2, 3)
# x, *y, z = (1, 2, 3, 4, 5)  # x=1, y=[2,3,4], z=5

# # Phương thức
# t1.count(2)            # Đếm
# t1.index(3)            # Tìm vị trí

# 3.3. SET - Tập hợp (KHÔNG có thứ tự, KHÔNG trùng lặp)
# python# Tạo set
# s1 = {1, 2, 3, 4, 5}
# s2 = set([1, 2, 2, 3, 3])  # {1, 2, 3}
# empty = set()              # Không dùng {} vì đó là dict

# # Thêm và xóa
# s1.add(6)              # Thêm phần tử
# s1.update([7, 8, 9])   # Thêm nhiều phần tử
# s1.remove(5)           # Xóa (lỗi nếu không tồn tại)
# s1.discard(5)          # Xóa (không lỗi nếu không tồn tại)
# s1.pop()               # Xóa phần tử ngẫu nhiên
# s1.clear()             # Xóa tất cả

# # Các phép toán tập hợp
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# a | b                  # Hợp: {1, 2, 3, 4, 5, 6}
# a & b                  # Giao: {3, 4}
# a - b                  # Hiệu: {1, 2}
# a ^ b                  # Đối xứng: {1, 2, 5, 6}

# # Kiểm tra
# 3 in a                 # True
# a.issubset(b)          # a có phải tập con của b?
# a.issuperset(b)        # a có phải tập cha của b?

# 3.4. DICTIONARY - Từ điển (cặp key-value)
# python# Tạo dictionary
# person = {
#     "name": "Nam",
#     "age": 20,
#     "city": "Hanoi"
# }
# empty = {}
# empty2 = dict()

# # Truy cập
# print(person["name"])       # "Nam"
# print(person.get("age"))    # 20
# print(person.get("job", "Không có"))  # Giá trị mặc định

# # Thêm/sửa
# person["job"] = "Developer"
# person["age"] = 21
# person.update({"phone": "0123456789"})

# # Xóa
# del person["city"]
# job = person.pop("job")
# person.clear()

# # Duyệt dictionary
# person = {"name": "Nam", "age": 20}

# for key in person:
#     print(key, person[key])

# for key, value in person.items():
#     print(key, value)

# for key in person.keys():
#     print(key)

# for value in person.values():
#     print(value)

# # Các phương thức khác
# person.keys()           # dict_keys(['name', 'age'])
# person.values()         # dict_values(['Nam', 20])
# person.items()          # dict_items([('name', 'Nam'), ('age', 20)])

# # Dictionary comprehension
# squares = {x: x**2 for x in range(5)}

# 4. CHUYỂN ĐỔI KIỂU DỮ LIỆU (TYPE CONVERSION)
# python# Sang int
# int("123")         # 123
# int(3.7)           # 3
# int(True)          # 1

# # Sang float
# float("3.14")      # 3.14
# float(5)           # 5.0

# # Sang str
# str(123)           # "123"
# str(3.14)          # "3.14"
# str([1,2,3])       # "[1, 2, 3]"

# # Sang list
# list("abc")        # ['a', 'b', 'c']
# list((1,2,3))      # [1, 2, 3]
# list({1,2,3})      # [1, 2, 3]

# # Sang tuple
# tuple([1,2,3])     # (1, 2, 3)

# # Sang set
# set([1,2,2,3])     # {1, 2, 3}

# # Sang dict
# dict([(1,'a'), (2,'b')])  # {1: 'a', 2: 'b'}

# 5. KIỂM TRA VÀ XÁC ĐỊNH KIỂU
# pythonx = [1, 2, 3]

# # Kiểm tra kiểu
# type(x)                    # <class 'list'>
# isinstance(x, list)        # True
# isinstance(x, (list, tuple))  # True (kiểm tra nhiều kiểu)

# # Kiểm tra khả năng thay đổi
# from collections.abc import Hashable
# isinstance(x, Hashable)    # False (list không hashable)
# isinstance((1,2), Hashable)  # True (tuple hashable)

# 6. CÁC KHÁI NIỆM QUAN TRỌNG
# 6.1. Mutable vs Immutable
# Immutable (Không thay đổi được):

# int, float, complex, bool, str, tuple, frozenset

# Mutable (Thay đổi được):

# list, dict, set

# python# Immutable
# x = 10
# y = x
# x = 20
# print(y)  # 10 (y không thay đổi)

# # Mutable
# list1 = [1, 2, 3]
# list2 = list1
# list1.append(4)
# print(list2)  # [1, 2, 3, 4] (list2 cũng thay đổi!)

# # Copy để tránh
# list3 = list1.copy()
# # hoặc
# list3 = list1[:]
# 6.2. Shallow Copy vs Deep Copy
# pythonimport copy

# # Shallow copy
# original = [[1, 2], [3, 4]]
# shallow = original.copy()
# shallow[0][0] = 999
# print(original)  # [[999, 2], [3, 4]] - Bị ảnh hưởng!

# # Deep copy
# original = [[1, 2], [3, 4]]
# deep = copy.deepcopy(original)
# deep[0][0] = 999
# print(original)  # [[1, 2], [3, 4]] - Không bị ảnh hưởng

# 7. TIPS VÀ LƯU Ý
# python# 1. Kiểm tra biến tồn tại
# if 'x' in locals() or 'x' in globals():
#     print("Biến x tồn tại")

# # 2. Xóa nhiều biến
# x = y = z = 10
# del x, y, z

# # 3. Toán tử Walrus
# if (n := len([1,2,3])) > 2:
#     print(f"List có {n} phần tử")

# # 4. Unpacking nâng cao
# first, *middle, last = [1, 2, 3, 4, 5]

# # 5. So sánh nối tiếp
# x = 5
# if 1 < x < 10:
#     print("x trong khoảng 1 đến 10")

# # 6. Dùng _ cho giá trị không quan tâm
# for _ in range(5):
#     print("Hello")

# # 7. Enumerate và zip
# for i, value in enumerate(['a', 'b', 'c']):
#     print(i, value)

# for x, y in zip([1,2,3], ['a','b','c']):
#     print(x, y)