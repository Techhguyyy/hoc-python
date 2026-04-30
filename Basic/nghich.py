import os
import time
import random
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Màu sắc RGB
def rgb_text(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def rgb_bg(r, g, b, text):
    return f"\033[48;2;{r};{g};{b}m{text}\033[0m"

def create_gradient_bg(height=10, width=40):
    gradient = []
    for i in range(height):
        # Tạo gradient từ xanh dương -> tím -> hồng
        r = int(100 + (155 * i / height))
        g = int(50 + (50 * i / height))
        b = int(200 - (100 * i / height))
        line = " " * width
        gradient.append(rgb_bg(r, g, b, line))
    return gradient

def falling_hearts():
    hearts = ["❤️", "💕", "💖", "💗", "💓"]
    return random.choice(hearts)

def animate_love_message():
    message = "ANH YÊU EM"
    
    try:
        while True:  # Chạy vô hạn
            clear_screen()
            
            # Tạo nền gradient
            gradient_bg = create_gradient_bg(12, 50)
            
            # Hiển thị từng dòng với nền gradient
            for i, bg_line in enumerate(gradient_bg):
                if i == 5:  # Dòng giữa để hiển thị chữ
                    # Tạo màu RGB ngẫu nhiên cho chữ
                    r, g, b = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
                    colored_message = rgb_text(r, g, b, f"   {message}   ")
                    
                    # Thêm trái tim rơi
                    heart = falling_hearts()
                    print(f"{bg_line[:15]}{colored_message}{bg_line[15+len(message)+6:]} {heart}")
                else:
                    # Thêm trái tim rơi ngẫu nhiên ở các dòng khác
                    if random.random() > 0.7:
                        heart_pos = random.randint(0, 45)
                        print(f"{bg_line[:heart_pos]}{falling_hearts()}{bg_line[heart_pos+1:]}")
                    else:
                        print(bg_line)
            
            # Thêm hiệu ứng sao băng ở dưới
            print("\n" + "✨" * 25)
            
            # Hiệu ứng nhấp nháy cho dòng phụ
            colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255), (0,255,255)]
            for _ in range(3):
                r, g, b = random.choice(colors)
                print(rgb_text(r, g, b, " " * 10 + "💝 I LOVE YOU FOREVER 💝"), end='\r')
                time.sleep(0.2)
            
            time.sleep(0.3)  # Tốc độ nhấp nháy
            
    except KeyboardInterrupt:
        clear_screen()
        print(rgb_text(255, 255, 255, "\n💖 Cảm ơn em! Anh yêu em mãi mãi! 💖\n"))

# Phiên bản đơn giản hơn nhưng vẫn đẹp
def simple_love_animation():
    message = "ANH YÊU EM"
    heart_patterns = [
        "  ❤️❤️  ❤️❤️  ",
        "❤️❤️❤️❤️❤️❤️❤️",
        "  ❤️❤️❤️❤️❤️  ",
        "    ❤️❤️❤️    ",
        "      ❤️      "
    ]
    
    try:
        while True:
            clear_screen()
            
            # Tạo khung trang trí
            print("╔" + "═" * 50 + "╗")
            
            # Hiển thị pattern trái tim với màu sắc thay đổi
            for pattern in heart_patterns:
                r, g, b = random.randint(150, 255), random.randint(100, 200), random.randint(150, 255)
                colored_hearts = rgb_text(r, g, b, pattern)
                print(f"║{colored_hearts:^50}║")
            
            print("╠" + "═" * 50 + "╣")
            
            # Hiển thị message với màu RGB ngẫu nhiên
            for _ in range(3):
                r, g, b = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
                colored_message = rgb_text(r, g, b, f"💝 {message} 💝")
                print(f"║{colored_message:^50}║")
                time.sleep(0.3)
            
            print("╚" + "═" * 50 + "╝")
            
            # Hiệu ứng phụ
            colors = [(255,0,0), (255,165,0), (255,255,0), (0,255,0), (0,0,255), (128,0,128)]
            for _ in range(5):
                r, g, b = random.choice(colors)
                print(rgb_text(r, g, b, "✨" * 20 + " MÃI MÃI BÊN NHAU " + "✨" * 20), end='\r')
                time.sleep(0.2)
            
    except KeyboardInterrupt:
        clear_screen()
        print("\n💖 Yêu em nhiều lắm! 💖\n")

if __name__ == "__main__":
    clear_screen()
    print("Chọn hiệu ứng:")
    print("1. Hiệu ứng nâng cao (Gradient + trái tim rơi)")
    print("2. Hiệu ứng đơn giản (Khung + pattern)")
    
    choice = input("Nhập lựa chọn (1 hoặc 2): ")
    
    clear_screen()
    print("Bắt đầu hiệu ứng... (Nhấn Ctrl+C để dừng)")
    time.sleep(2)
    
    if choice == "1":
        animate_love_message()
    else:
        simple_love_animation()