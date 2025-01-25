import sqlite3
import bcrypt
import re

# Kết nối tới SQLite database (tạo nếu chưa có)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Sửa bảng để lưu thêm thông tin
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
)
""")
conn.commit()

def is_password_strong(password):
    """
    Kiểm tra độ mạnh mật khẩu.
    Mật khẩu phải có ít nhất 8 ký tự, chứa chữ hoa, chữ thường, số và ký tự đặc biệt.
    """
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[@$!%*?&#]', password)):
        return True
    return False

def register(username, password):
    """
    Đăng ký người dùng mới.
    """
    if not is_password_strong(password):
        print("Mật khẩu yếu. Mật khẩu cần có ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt.")
        return

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print("Đăng ký thành công!")
    except sqlite3.IntegrityError:
        print("Tên đăng nhập đã tồn tại. Vui lòng chọn tên khác.")

def login(username, password):
    """
    Đăng nhập người dùng.
    """
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result is None:
        print("Tên đăng nhập không tồn tại.")
        return False

    stored_password = result[0]
    if bcrypt.checkpw(password.encode('utf-8'), stored_password):
        cursor.execute("UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE username = ?", (username,))
        conn.commit()
        print("Đăng nhập thành công!")
        return True
    else:
        print("Mật khẩu không chính xác.")
        return False

def update_password(username, old_password, new_password):
    """
    Cập nhật mật khẩu cho người dùng.
    """
    if login(username, old_password):
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password, username))
        conn.commit()
        print("Cập nhật mật khẩu thành công!")
    else:
        print("Không thể cập nhật mật khẩu. Thông tin không chính xác.")

def delete_account(username, password):
    """
    Xóa tài khoản người dùng.
    """
    if login(username, password):
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        conn.commit()
        print("Xóa tài khoản thành công!")
    else:
        print("Không thể xóa tài khoản. Thông tin không chính xác.")

def list_users():
    """
    Hiển thị danh sách người dùng.
    """
    cursor.execute("SELECT id, username, created_at, last_login FROM users")
    users = cursor.fetchall()
    print("\nDanh sách người dùng:")
    for user in users:
        print(f"ID: {user[0]}, Tên: {user[1]}, Ngày tạo: {user[2]}, Lần đăng nhập cuối: {user[3]}")

def main():
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
            username = input("Nhập tên đăng nhập: ").strip()
            password = input("Nhập mật khẩu: ").strip()
            register(username, password)
        elif choice == "2":
            username = input("Nhập tên đăng nhập: ").strip()
            password = input("Nhập mật khẩu: ").strip()
            login(username, password)
        elif choice == "3":
            username = input("Nhập tên đăng nhập: ").strip()
            old_password = input("Nhập mật khẩu cũ: ").strip()
            new_password = input("Nhập mật khẩu mới: ").strip()
            update_password(username, old_password, new_password)
        elif choice == "4":
            username = input("Nhập tên đăng nhập: ").strip()
            password = input("Nhập mật khẩu: ").strip()
            delete_account(username, password)
        elif choice == "5":
            list_users()
        elif choice == "6":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()

# Đừng quên đóng kết nối khi hoàn tất
conn.close()

