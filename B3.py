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
            overwrite = input("Bạn có muốn ghi đè danh sách hiện tại bằng dữ liệu mới? (y/n): ").strip().lower()
            if overwrite == "y":
                questions_db = imported_questions
                print(f"Danh sách câu hỏi đã được ghi đè từ file {filename}.")
            else:
                print("Hủy thao tác nhập dữ liệu.")
    except FileNotFoundError:
        print(f"Không tìm thấy file {filename}.")
    except json.JSONDecodeError:
        print(f"File {filename} không hợp lệ.")

# Bổ sung các chức năng để nâng cao trải nghiệm

def export_to_json():
    """Xuất câu hỏi ra file JSON."""
    filename = input("Nhập tên file để xuất (mặc định: questions.json): ").strip() or "questions.json"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(questions_db, file, ensure_ascii=False, indent=4)
        print(f"Dữ liệu đã được xuất ra file {filename}.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi xuất file: {e}")

def update_question():
    """Cập nhật nội dung của một câu hỏi."""
    if not questions_db:
        print("Danh sách câu hỏi hiện đang trống.")
        return

    view_questions()
    try:
        question_idx = int(input("Nhập số thứ tự câu hỏi cần cập nhật: ").strip())
        if 1 <= question_idx <= len(questions_db):
            question = questions_db[question_idx - 1]
            print(f"Nội dung hiện tại: {question['question']}")
            new_question = input("Nhập nội dung câu hỏi mới (bỏ trống để giữ nguyên): ").strip()
            if new_question:
                question['question'] = new_question

            for idx, option in enumerate(question['options'], start=1):
                print(f"  {idx}. {option}")
                new_option = input(f"Nhập nội dung lựa chọn {idx} mới (bỏ trống để giữ nguyên): ").strip()
                if new_option:
                    question['options'][idx - 1] = new_option

            new_correct_answer = input(f"Nhập đáp án đúng mới (bỏ trống để giữ nguyên): ").strip()
            if new_correct_answer:
                question['correct_answer'] = new_correct_answer

            new_explanation = input(f"Nhập giải thích mới (bỏ trống để giữ nguyên): ").strip()
            if new_explanation:
                question['explanation'] = new_explanation

            print("Câu hỏi đã được cập nhật thành công.")
        else:
            print("Số thứ tự không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")
