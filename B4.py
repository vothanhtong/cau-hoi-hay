import sqlite3
import bcrypt
import re
from getpass import getpass

# Khởi tạo database nếu chưa có
def init_db():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            role TEXT DEFAULT 'user'
                          )''')
        conn.commit()

# Kiểm tra tính hợp lệ của username
def is_valid_username(username):
    return re.match(r'^[a-zA-Z0-9_-]{3,20}$', username) is not None

# Đăng ký tài khoản
def register():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        
        username = input("Nhập tên đăng nhập: ").strip()
        if not is_valid_username(username):
            print("Tên đăng nhập không hợp lệ. Chỉ được chứa chữ cái, số, '-' và '_'.")
            return

        password = getpass("Nhập mật khẩu: ").strip()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            print("Đăng ký thành công!")
        except sqlite3.IntegrityError:
            print("Tên đăng nhập đã tồn tại.")

# Danh sách lưu số lần đăng nhập sai
failed_attempts = {}

# Đăng nhập
def login():
    global failed_attempts
    username = input("Nhập tên đăng nhập: ").strip()
    password = getpass("Nhập mật khẩu: ").strip()

    if failed_attempts.get(username, 0) >= 3:
        print("Tài khoản bị khóa tạm thời do nhập sai quá nhiều lần.")
        return False

    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()

        if row and bcrypt.checkpw(password.encode('utf-8'), row[0]):
            print("Đăng nhập thành công!")
            failed_attempts[username] = 0  # Reset đếm thất bại
            return True
        else:
            failed_attempts[username] = failed_attempts.get(username, 0) + 1
            print(f"Sai mật khẩu ({failed_attempts[username]}/3 lần).")
            return False

# Cập nhật mật khẩu
def update_password():
    username = input("Nhập tên đăng nhập: ").strip()
    old_password = getpass("Nhập mật khẩu cũ: ").strip()

    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()

        if row and bcrypt.checkpw(old_password.encode('utf-8'), row[0]):
            new_password = getpass("Nhập mật khẩu mới: ").strip()
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

            cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password, username))
            conn.commit()
            print("Mật khẩu đã được cập nhật.")
        else:
            print("Sai mật khẩu cũ.")

# Xóa tài khoản
def delete_account():
    username = input("Nhập tên đăng nhập cần xóa: ").strip()
    confirm = input(f"Bạn có chắc muốn xóa tài khoản '{username}'? (y/n): ").strip().lower()

    if confirm == "y":
        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE username = ?", (username,))
            conn.commit()
            print("Tài khoản đã được xóa.")
    else:
        print("Hủy thao tác xóa.")

# Hiển thị danh sách người dùng (chỉ Admin)
def list_users():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, role FROM users")
        users = cursor.fetchall()

        print("\nDanh sách người dùng:")
        for user in users:
            print(f"ID: {user[0]} | Username: {user[1]} | Role: {user[2]}")
        print("-" * 40)

# Giao diện menu
def menu():
    init_db()
    while True:
        print("\n=== Hệ Thống Đăng Nhập ===")
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("3. Cập nhật mật khẩu")
        print("4. Xóa tài khoản")
        print("5. Hiển thị danh sách người dùng (Admin)")
        print("6. Thoát")

        choice = input("Chọn chức năng (1-6): ").strip()
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            update_password()
        elif choice == "4":
            delete_account()
        elif choice == "5":
            list_users()
        elif choice == "6":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

# Chạy chương trình
if __name__ == "__main__":
    menu()
