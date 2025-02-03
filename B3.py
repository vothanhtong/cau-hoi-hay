import json

# Danh sách câu hỏi giả định (có thể được load từ JSON)
questions_db = [
    {
        "question": "Thủ đô của Việt Nam là gì?",
        "options": ["Hà Nội", "TP. Hồ Chí Minh", "Đà Nẵng", "Cần Thơ"],
        "correct_answer": "A",
        "explanation": "Hà Nội là thủ đô của Việt Nam."
    }
]

def view_questions():
    """Hiển thị danh sách câu hỏi hiện có."""
    if not questions_db:
        print("Danh sách câu hỏi hiện đang trống.")
        return
    
    print("\n Danh sách câu hỏi:")
    for idx, q in enumerate(questions_db, start=1):
        print(f"{idx}. {q['question']}")
        for i, option in enumerate(q["options"], start=65):
            print(f"  {chr(i)}. {option}")
        print(f" Đáp án đúng: {q['correct_answer']}")
        if q.get("explanation"):
            print(f"ℹ️ Giải thích: {q['explanation']}")
        print("-" * 50)

def delete_question():
    """Xóa một câu hỏi khỏi danh sách."""
    if not questions_db:
        print("Danh sách câu hỏi hiện đang trống.")
        return

    view_questions()
    try:
        question_idx = int(input(" Nhập số thứ tự câu hỏi cần xóa: ").strip())
        if 1 <= question_idx <= len(questions_db):
            deleted_question = questions_db.pop(question_idx - 1)
            print(f" Đã xóa câu hỏi: \"{deleted_question['question']}\"")
        else:
            print(" Số thứ tự không hợp lệ.")
    except ValueError:
        print(" Vui lòng nhập một số hợp lệ.")

def search_questions():
    """Tìm kiếm câu hỏi theo từ khóa."""
    keyword = input("🔍 Nhập từ khóa để tìm kiếm: ").strip().lower()
    results = [q for q in questions_db if keyword in q["question"].lower()]
    
    if results:
        print("\n🔎 Kết quả tìm kiếm:")
        for idx, q in enumerate(results, start=1):
            print(f"{idx}. {q['question']}")
            for i, option in enumerate(q["options"], start=65):
                print(f"  {chr(i)}. {option}")
            print(f" Đáp án đúng: {q['correct_answer']}")
            if q.get("explanation"):
                print(f"ℹ️ Giải thích: {q['explanation']}")
            print("-" * 50)
    else:
        print(" Không tìm thấy câu hỏi nào.")

def import_from_json():
    """Nhập câu hỏi từ file JSON."""
    global questions_db
    filename = input(" Nhập tên file để nhập (mặc định: questions.json): ").strip() or "questions.json"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            imported_questions = json.load(file)
        
        if not isinstance(imported_questions, list):
            print(f" File {filename} không chứa danh sách hợp lệ.")
            return

        action = input(" Bạn có muốn gộp dữ liệu hay ghi đè danh sách hiện tại? (gộp: y, ghi đè: n): ").strip().lower()
        if action == "y":
            questions_db.extend(imported_questions)
            print(f" Dữ liệu đã được gộp từ file {filename}.")
        elif action == "n":
            questions_db = imported_questions
            print(f" Danh sách câu hỏi đã được ghi đè từ file {filename}.")
        else:
            print(" Hủy thao tác nhập dữ liệu.")
    except FileNotFoundError:
        print(f" Không tìm thấy file {filename}.")
    except json.JSONDecodeError:
        print(f" File {filename} không hợp lệ.")

def export_to_json():
    """Xuất câu hỏi ra file JSON."""
    filename = input(" Nhập tên file để xuất (mặc định: questions.json): ").strip() or "questions.json"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(questions_db, file, ensure_ascii=False, indent=4)
        print(f" Dữ liệu đã được xuất ra file {filename}.")
    except Exception as e:
        print(f" Đã xảy ra lỗi khi xuất file: {e}")

def update_question():
    """Cập nhật nội dung của một câu hỏi."""
    if not questions_db:
        print("Danh sách câu hỏi hiện đang trống.")
        return

    view_questions()
    try:
        question_idx = int(input(" Nhập số thứ tự câu hỏi cần cập nhật: ").strip())
        if 1 <= question_idx <= len(questions_db):
            question = questions_db[question_idx - 1]
            
            print(f"\n Câu hỏi hiện tại: \"{question['question']}\"")
            new_question = input(" Nhập nội dung câu hỏi mới (bỏ trống để giữ nguyên): ").strip()
            if new_question:
                question['question'] = new_question

            for idx, option in enumerate(question['options'], start=1):
                print(f"  {idx}. {option}")
                new_option = input(f" Nhập nội dung lựa chọn {idx} mới (bỏ trống để giữ nguyên): ").strip()
                if new_option:
                    question['options'][idx - 1] = new_option

            new_correct_answer = input(" Nhập đáp án đúng mới (A, B, C, D - bỏ trống để giữ nguyên): ").strip().upper()
            if new_correct_answer in ["A", "B", "C", "D"]:
                question['correct_answer'] = new_correct_answer
            elif new_correct_answer:
                print(" Đáp án không hợp lệ, giữ nguyên giá trị cũ.")

            new_explanation = input("ℹ️ Nhập giải thích mới (bỏ trống để giữ nguyên): ").strip()
            if new_explanation:
                question['explanation'] = new_explanation

            print(" Câu hỏi đã được cập nhật thành công.")
        else:
            print(" Số thứ tự không hợp lệ.")
    except ValueError:
        print(" Vui lòng nhập số hợp lệ.")

# Chạy chương trình
if __name__ == "__main__":
    while True:
        print("\n MENU:")
        print("1. Xem danh sách câu hỏi")
        print("2. Thêm/xóa/cập nhật câu hỏi")
        print("3. Tìm kiếm câu hỏi")
        print("4. Nhập/Xuất JSON")
        print("5. Thoát")
        choice = input(" Chọn chức năng: ").strip()
        
        if choice == "1":
            view_questions()
        elif choice == "2":
            update_question()
        elif choice == "3":
            search_questions()
        elif choice == "4":
            import_from_json()
            export_to_json()
        elif choice == "5":
            print(" Tạm biệt!")
            break
        else:
            print(" Lựa chọn không hợp lệ.")
