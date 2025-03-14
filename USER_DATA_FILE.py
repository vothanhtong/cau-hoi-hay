import json
import os

# File để lưu trữ thông tin người dùng
USER_DATA_FILE = "users.json"

# Hàm kiểm tra xem file dữ liệu người dùng có tồn tại không
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Hàm lưu thông tin người dùng
def save_user_data(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file)

# Hàm đăng ký tài khoản
def register():
    users = load_user_data()
    username = input("Nhập tên đăng nhập: ")
    if username in users:
        print("Tên đăng nhập đã tồn tại!")
        return
    password = input("Nhập mật khẩu: ")
    users[username] = password
    save_user_data(users)
    print("Đăng ký thành công!")

# Hàm đăng nhập
def login():
    users = load_user_data()
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")
    if username in users and users[username] == password:
        print("Đăng nhập thành công!")
    else:
        print("Tên đăng nhập hoặc mật khẩu không đúng!")

# Menu chính
def main():
    while True:
        print("\n1. Đăng ký")
        print("2. Đăng nhập")
        print("3. Thoát")
        choice = input("Chọn một tùy chọn: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()