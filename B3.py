import json

# Danh sách câu hỏi (dữ liệu mẫu)
questions_db = []

def add_question():
    """
    Thêm câu hỏi mới vào danh sách.
    """
    question = input("Nhập câu hỏi: ").strip()
    options = [input(f"Nhập đáp án {chr(65+i)}: ").strip() for i in range(4)]
    correct_answer = input("Nhập đáp án đúng (A, B, C, D): ").strip().upper()
    explanation = input("Giải thích (nếu có, nhấn Enter để bỏ qua): ").strip()
    
    if correct_answer not in ["A", "B", "C", "D"]:
        print("Đáp án không hợp lệ! Vui lòng nhập lại.")
        return
    
    questions_db.append({
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "explanation": explanation
    })
    print("Câu hỏi đã được thêm thành công!")

def view_questions():
    """
    Hiển thị danh sách câu hỏi.
    """
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

def export_to_json(filename="questions.json"):
    """
    Xuất câu hỏi ra file JSON.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(questions_db, file, ensure_ascii=False, indent=4)
    print(f"Dữ liệu đã được xuất ra file {filename}.")

def import_from_json(filename="questions.json"):
    """
    Nhập câu hỏi từ file JSON.
    """
    global questions_db
    try:
        with open(filename, "r", encoding="utf-8") as file:
            questions_db = json.load(file)
        print(f"Dữ liệu đã được nhập từ file {filename}.")
    except FileNotFoundError:
        print(f"Không tìm thấy file {filename}.")
    except json.JSONDecodeError:
        print(f"File {filename} không hợp lệ.")

def main():
    """
    Chương trình chính.
    """
    while True:
        print("\n=== Quản lý câu hỏi thi Tin học trẻ ===")
        print("1. Thêm câu hỏi mới")
        print("2. Xem danh sách câu hỏi")
        print("3. Xuất câu hỏi ra file JSON")
        print("4. Nhập câu hỏi từ file JSON")
        print("5. Thoát")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            add_question()
        elif choice == "2":
            view_questions()
        elif choice == "3":
            export_to_json()
        elif choice == "4":
            import_from_json()
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng thử lại.")

if __name__ == "__main__":
    main()
