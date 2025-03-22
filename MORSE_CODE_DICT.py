MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K',
    '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'
}
def morse_to_text(morse_code):
    return ' '.join(
        ''.join(MORSE_CODE_DICT.get(letter, '') for letter in word.split())
        for word in morse_code.split('   ')
    )
# Nhận đầu vào từ người dùng
user_input = input("Nhập mã Morse: ")
print("Kết quả: ", morse_to_text(user_input))
