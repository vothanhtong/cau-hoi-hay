import json

# Danh sách câu hỏi (dữ liệu mẫu)
questions_db = []


def input_with_default(prompt, default=None):
    """Nhập dữ liệu với giá trị mặc định."""
    user_input = input(f"{prompt} ({'để trống để giữ nguyên' if default else ''}): ").strip()
    return user_input if user_input else default


def display_menu():
    """Hiển thị menu chức năng."""
    menu = """
=== Quản lý câu hỏi thi Tin học trẻ ===
1. Thêm câu hỏi mới
2. Xem danh sách câu hỏi
3. Xuất câu hỏi ra file JSON
4. Nhập câu hỏi từ file JSON
5. Xóa câu hỏi
6. Chỉnh sửa câu hỏi
7. Thoát
"""
    print(menu)


def view_questions():
    """Hiển thị danh sách câu hỏi."""
    if not questions_db:
        print("Chưa có câu hỏi nào trong danh sách.")
        return

    for idx, q in enumerate(questions_db, start=1):
        print(f"\nCâu hỏi {idx}: {q['question']}")
        for i, option in enumerate(q["options"], start=65):  # 65 là mã ASCII của 'A'
            print(f"  {chr(i)}. {option}")
        print(f"Đáp án đúng: {q['correct_answer']}")
        if q['explanation']:
            print(f"Giải thích: {q['explanation']}")


def add_or_edit_question(question=None):
    """Thêm hoặc chỉnh sửa câu hỏi."""
    is_edit = question is not None
    question = question or {}
    
    question["question"] = input_with_default("Nhập câu hỏi", question.get("question"))
    question["options"] = [
        input_with_default(f"Nhập đáp án {chr(65 + i)}", question.get("options", [None] * 4)[i])
        for i in range(4)
    ]
    correct_answer = input_with_default("Nhập đáp án đúng (A, B, C, D)", question.get("correct_answer"))
    if correct_answer not in ["A", "B", "C", "D"]:
        print("Đáp án không hợp lệ! Vui lòng thử lại.")
        return

    question["correct_answer"] = correct_answer
    question["explanation"] = input_with_default("Giải thích (nếu có)", question.get("explanation", ""))
    
    if not is_edit:
        questions_db.append(question)
        print("Câu hỏi đã được thêm thành công!")
    else:
        print("Câu hỏi đã được cập nhật!")


def export_to_json():
    """Xuất câu hỏi ra file JSON."""
    filename = input("Nhập tên file để xuất (mặc định: questions.json): ").strip() or "questions.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(questions_db, file, ensure_ascii=False, indent=4)
    print(f"Dữ liệu đã được xuất ra file {filename}.")


def import_from_json():
    """Nhập câu hỏi từ file JSON."""
    global questions_db
    filename = input("Nhập tên file để nhập (mặc định: questions.json): ").strip() or "questions.json"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            imported_questions = json.load(file)
        
        if not isinstance(imported_questions, list):
            print(f"File {filename} không chứa danh sách hợp lệ.")
            return

        if input("Bạn có muốn ghi đè danh sách hiện tại? (y/n): ").strip().lower() == "y":
            questions_db = imported_questions
            print(f"Dữ liệu đã được nhập từ file {filename}.")
        else:
            print("Dữ liệu hiện tại không bị thay đổi.")
    except FileNotFoundError:
        print(f"Không tìm thấy file {filename}.")
    except json.JSONDecodeError:
        print(f"File {filename} không hợp lệ.")


def delete_question():
    """Xóa một câu hỏi khỏi danh sách."""
    if not questions_db:
        print("Danh sách câu hỏi hiện đang trống.")
        return

    view_questions()
    try:
        question_idx = int(input("Nhập số thứ tự câu hỏi cần xóa: ").strip())
        if 1 <= question_idx <= len(questions_db):
            deleted_question = questions_db.pop(question_idx - 1)
            print(f"Đã xóa câu hỏi: {deleted_question['question']}")
        else:
            print("Số thứ tự không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")


def main():
    """Chương trình chính."""
    while True:
        display_menu()
        choice = input("Chọn chức năng (1-7): ").strip()

        if choice == "1":
            add_or_edit_question()
        elif choice == "2":
            view_questions()
        elif choice == "3":
            export_to_json()
        elif choice == "4":
            import_from_json()
        elif choice == "5":
            delete_question()
        elif choice == "6":
            if questions_db:
                view_questions()
                try:
                    question_idx = int(input("Nhập số thứ tự câu hỏi cần chỉnh sửa: ").strip())
                    if 1 <= question_idx <= len(questions_db):
                        add_or_edit_question(questions_db[question_idx - 1])
                    else:
                        print("Số thứ tự không hợp lệ.")
                except ValueError:
                    print("Vui lòng nhập số hợp lệ.")
            else:
                print("Danh sách câu hỏi hiện đang trống.")
        elif choice == "7":
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng thử lại.")


if __name__ == "__main__":
    main()
