import json
from typing import List, Dict

# Danh sách câu hỏi
questions_db: List[Dict[str, str | List[str]]] = [
    {
        "question": "Thủ đô của Việt Nam là gì?",
        "options": ["Hà Nội", "TP. Hồ Chí Minh", "Đà Nẵng", "Cần Thơ"],
        "correct_answer": "A",
        "explanation": "Hà Nội là thủ đô của Việt Nam."
    }
]

def display_menu() -> None:
    """Hiển thị menu chính với các tùy chọn."""
    print("\n=== QUẢN LÝ CÂU HỎI ===")
    print("1. Xem danh sách câu hỏi")
    print("2. Thêm câu hỏi mới")
    print("3. Xóa câu hỏi")
    print("4. Cập nhật câu hỏi")
    print("5. Tìm kiếm câu hỏi")
    print("6. Nhập từ JSON")
    print("7. Xuất ra JSON")
    print("8. Thoát")

def view_questions() -> None:
    """Hiển thị danh sách câu hỏi hiện có."""
    if not questions_db:
        print("Danh sách câu hỏi hiện đang trống.")
        return
    
    print("\nDanh sách câu hỏi:")
    for idx, q in enumerate(questions_db, 1):
        print(f"{idx}. {q['question']}")
        for i, opt in enumerate(q['options'], 65):
            print(f"  {chr(i)}. {opt}")
        print(f"Đáp án đúng: {q['correct_answer']}")
        if q.get("explanation"):
            print(f"Giải thích: {q['explanation']}")
        print("-" * 60)

def add_question() -> None:
    """Thêm một câu hỏi mới vào danh sách."""
    print("\nThêm câu hỏi mới:")
    question = input("Nhập câu hỏi: ").strip()
    if not question:
        print("Câu hỏi không được để trống.")
        return

    options = []
    for i in range(4):
        opt = input(f"Nhập lựa chọn {chr(65 + i)}: ").strip()
        if not opt:
            print("Lựa chọn không được để trống.")
            return
        options.append(opt)

    correct_answer = input("Nhập đáp án đúng (A, B, C, D): ").strip().upper()
    if correct_answer not in "ABCD":
        print("Đáp án phải là A, B, C hoặc D.")
        return

    explanation = input("Nhập giải thích (Enter để bỏ qua): ").strip()

    questions_db.append({
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "explanation": explanation if explanation else ""
    })
    print("Câu hỏi đã được thêm thành công!")

def delete_question() -> None:
    """Xóa một câu hỏi khỏi danh sách."""
    if not questions_db:
        print("Danh sách câu hỏi hiện đang trống.")
        return

    view_questions()
    try:
        idx = int(input("Nhập số thứ tự câu hỏi cần xóa: ")) - 1
        if 0 <= idx < len(questions_db):
            deleted = questions_db.pop(idx)
            print(f"Đã xóa câu hỏi: \"{deleted['question']}\"")
        else:
            print("Số thứ tự không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")

def update_question() -> None:
    """Cập nhật nội dung của một câu hỏi."""
    if not questions_db:
        print("Danh sách câu hỏi hiện đang trống.")
        return

    view_questions()
    try:
        idx = int(input("Nhập số thứ tự câu hỏi cần cập nhật: ")) - 1
        if 0 <= idx < len(questions_db):
            q = questions_db[idx]
            print(f"\nCâu hỏi hiện tại: \"{q['question']}\"")

            new_q = input("Nhập câu hỏi mới (Enter để giữ nguyên): ").strip()
            if new_q:
                q['question'] = new_q

            for i, opt in enumerate(q['options']):
                new_opt = input(f"Nhập lựa chọn {chr(65 + i)} mới (Enter để giữ nguyên '{opt}'): ").strip()
                if new_opt:
                    q['options'][i] = new_opt

            new_ans = input(f"Nhập đáp án đúng mới (A-D, Enter để giữ '{q['correct_answer']}'): ").strip().upper()
            if new_ans in "ABCD":
                q['correct_answer'] = new_ans
            elif new_ans:
                print("Đáp án không hợp lệ, giữ nguyên.")

            new_exp = input("Nhập giải thích mới (Enter để giữ nguyên): ").strip()
            if new_exp:
                q['explanation'] = new_exp

            print("Câu hỏi đã được cập nhật thành công!")
        else:
            print("Số thứ tự không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")

def search_questions() -> None:
    """Tìm kiếm câu hỏi theo từ khóa."""
    keyword = input("Nhập từ khóa để tìm kiếm: ").strip().lower()
    results = [q for q in questions_db if keyword in q["question"].lower()]
    
    if results:
        print("\nKết quả tìm kiếm:")
        for idx, q in enumerate(results, 1):
            print(f"{idx}. {q['question']}")
            for i, opt in enumerate(q['options'], 65):
                print(f"  {chr(i)}. {opt}")
            print(f"Đáp án đúng: {q['correct_answer']}")
            if q.get("explanation"):
                print(f"Giải thích: {q['explanation']}")
            print("-" * 60)
    else:
        print("Không tìm thấy câu hỏi nào.")

def import_from_json() -> None:
    """Nhập câu hỏi từ file JSON."""
    global questions_db
    filename = input("Nhập tên file để nhập (mặc định: questions.json): ").strip() or "questions.json"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            imported_questions = json.load(file)
        
        if not isinstance(imported_questions, list):
            print(f"File {filename} không chứa danh sách hợp lệ.")
            return

        action = input("Bạn muốn gộp dữ liệu hay ghi đè danh sách hiện tại? (gộp: y, ghi đè: n): ").strip().lower()
        if action == "y":
            questions_db.extend(imported_questions)
            print(f"Dữ liệu đã được gộp từ file {filename}.")
        elif action == "n":
            questions_db = imported_questions
            print(f"Danh sách câu hỏi đã được ghi đè từ file {filename}.")
        else:
            print("Hủy thao tác nhập dữ liệu.")
    except FileNotFoundError:
        print(f"Không tìm thấy file {filename}.")
    except json.JSONDecodeError:
        print(f"File {filename} không hợp lệ.")

def export_to_json() -> None:
    """Xuất câu hỏi ra file JSON."""
    filename = input("Nhập tên file để xuất (mặc định: questions.json): ").strip() or "questions.json"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(questions_db, file, ensure_ascii=False, indent=4)
        print(f"Dữ liệu đã được xuất ra file {filename}.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi xuất file: {e}")

# Chạy chương trình
if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Chọn chức năng: ").strip()
        
        if choice == "1":
            view_questions()
        elif choice == "2":
            add_question()
        elif choice == "3":
            delete_question()
        elif choice == "4":
            update_question()
        elif choice == "5":
            search_questions()
        elif choice == "6":
            import_from_json()
        elif choice == "7":
            export_to_json()
        elif choice == "8":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

# === QUẢN LÝ CÂU HỎI ===
# 1. Xem danh sách câu hỏi
# 2. Thêm câu hỏi mới
# 3. Xóa câu hỏi
# 4. Cập nhật câu hỏi
# 5. Tìm kiếm câu hỏi
# 6. Nhập từ JSON
# 7. Xuất ra JSON
# 8. Thoát
# Chọn chức năng: 1

# Danh sách câu hỏi:
# 1. Thủ đô của Việt Nam là gì?
#   A. Hà Nội
#   B. TP. Hồ Chí Minh
#   C. Đà Nẵng
#   D. Cần Thơ
# Đáp án đúng: A
# Giải thích: Hà Nội là thủ đô của Việt Nam.
