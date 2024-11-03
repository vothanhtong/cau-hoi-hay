# import turtle

# # Hàm vẽ cây Giáng Sinh
# def draw_tree():
#     turtle.fillcolor("green")
#     turtle.begin_fill()
#     turtle.setheading(0)
    
#     # Vẽ phần lá cây
#     turtle.forward(100)
#     turtle.left(120)
#     turtle.forward(100)
#     turtle.left(120)
#     turtle.forward(100)
#     turtle.left(120)
#     turtle.forward(50)
    
#     turtle.right(90)
#     turtle.forward(20)
    
#     turtle.left(90)
#     turtle.forward(50)
    
#     turtle.right(90)
#     turtle.forward(20)
    
#     turtle.left(90)
#     turtle.forward(50)
    
#     turtle.right(90)
#     turtle.forward(20)
    
#     turtle.left(90)
#     turtle.forward(50)
    
#     turtle.right(90)
#     turtle.forward(20)
    
#     turtle.left(90)
#     turtle.forward(50)
    
#     turtle.end_fill()

# # Hàm hiển thị thông điệp
# def draw_message():
#     turtle.penup()
#     turtle.goto(-70, -150)
#     turtle.pendown()
#     turtle.color("red")
#     turtle.write("Chúc Mừng Giáng Sinh!", font=("Arial", 16, "bold"))

# # Thiết lập màn hình
# turtle.speed(1)
# turtle.bgcolor("lightblue")

# # Vẽ cây
# draw_tree()

# # Hiển thị thông điệp
# draw_message()

# # Hoàn thành
# turtle.hideturtle()
# turtle.done()



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Không thể chia cho 0"

def calculator():
    print("Chọn phép toán:")
    print("1 - Cộng")
    print("2 - Trừ")
    print("3 - Nhân")
    print("4 - Chia")
    
    choice = input("Nhập phím (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Nhập số thứ nhất: "))
            num2 = float(input("Nhập số thứ hai: "))
            
            if choice == '1':
                print(f"Kết quả: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Kết quả: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Kết quả: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Kết quả: {num1} / {num2} = {divide(num1, num2)}")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
    else:
        print("Vui lòng chọn một phép toán hợp lệ (1, 2, 3 hoặc 4).")

# Chạy chương trình
calculator()
