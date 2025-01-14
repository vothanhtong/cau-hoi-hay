import sqlite3
import bcrypt

# Kết nối tới SQLite database (tạo nếu chưa có)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Tạo bảng người dùng nếu chưa tồn tại
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

def register(username, password):
    """
    Đăng ký người dùng mới.
    """
    # Mã hóa mật khẩu
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
    
    # Kiểm tra mật khẩu
    stored_password = result[0]
    if bcrypt.checkpw(password.encode('utf-8'), stored_password):
        print("Đăng nhập thành công!")
        return True
    else:
        print("Mật khẩu không chính xác.")
        return False

def main():
    while True:
        print("\n=== Hệ Thống Đăng Nhập ===")
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("3. Thoát")
        choice = input("Chọn chức năng (1-3): ").strip()
        
        if choice == "1":
            username = input("Nhập tên đăng nhập: ").strip()
            password = input("Nhập mật khẩu: ").strip()
            register(username, password)
        elif choice == "2":
            username = input("Nhập tên đăng nhập: ").strip()
            password = input("Nhập mật khẩu: ").strip()
            login(username, password)
        elif choice == "3":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()

# Đừng quên đóng kết nối khi hoàn tất
conn.close()
1
