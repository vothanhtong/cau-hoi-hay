def delete_question():
    """Xóa một câu hỏi khỏi danh sách."""
    if not questions_db:
        print("Danh sách câu hỏi hiện đang trống.")
        return

    view_questions()
    try:
        question_idx = int(input("Nhập số thứ tự câu hỏi cần xóa: ").strip())
        if 1 <= question_idx <= len(questions_db):
            deleted_question = questions_db[question_idx - 1]
            confirm = input(f"Bạn có chắc chắn muốn xóa câu hỏi này không? (y/n): ").strip().lower()
            if confirm == 'y':
                questions_db.pop(question_idx - 1)
                print(f"Đã xóa câu hỏi: {deleted_question['question']}")
            else:
                print("Hủy thao tác xóa.")
        else:
            print("Số thứ tự không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")
def search_questions():
    """Tìm kiếm câu hỏi theo từ khóa."""
    keyword = input("Nhập từ khóa để tìm kiếm: ").strip().lower()
    results = [q for q in questions_db if keyword in q["question"].lower()]
    if results:
        for idx, q in enumerate(results, start=1):
            print(f"\nKết quả {idx}: {q['question']}")
            for i, option in enumerate(q["options"], start=65):
                print(f"  {chr(i)}. {option}")
            print(f"Đáp án đúng: {q['correct_answer']}")
            if q['explanation']:
                print(f"Giải thích: {q['explanation']}")
    else:
        print("Không tìm thấy câu hỏi nào.")
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

        if input("Bạn có muốn gộp danh sách hiện tại với dữ liệu mới? (y/n): ").strip().lower() == "y":
            questions_db.extend(imported_questions)
            print(f"Dữ liệu đã được gộp từ file {filename}.")
        else:
            print("Hủy thao tác nhập dữ liệu.")
    except FileNotFoundError:
        print(f"Không tìm thấy file {filename}.")
    except json.JSONDecodeError:
        print(f"File {filename} không hợp lệ.")
