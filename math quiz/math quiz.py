import random
import time

# تابع تبدیل اعداد فارسی به انگلیسی
def convert_farsi_digits_to_english(input_str):
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    translation_table = str.maketrans(persian_digits, english_digits)
    return input_str.translate(translation_table)

def question_generator():
    # پردازش اعداد تصادفی
    a = random.randint(1, 9)
    b = random.randint(1, 9)

    # انتخاب تصادفی عملگر
    operator_list = ["+", "-", "*"]
    selected_operator = random.choice(operator_list)

    # تبدیل عملگر به فارسی
    if selected_operator == "+":
        operator_farsi = "به‌علاوه"
    elif selected_operator == "-":
        operator_farsi = "منها"
    else:
        operator_farsi = "ضربدر"

    print(f"{a} {operator_farsi} {b} = ?")

    # محاسبه نتیجه
    if selected_operator == "+":
        return a + b
    elif selected_operator == "-":
        return a - b
    else:
        return a * b

# تنظیمات اولیه
question_number_limit = 5
question_number = 0
score = 0
time_limit = 10

while question_number < question_number_limit:
    # تولید سوال و شروع زمان
    result = question_generator()  # دریافت نتیجه سوال
    start_time = time.time()

    # دریافت پاسخ کاربر
    user_answer = input("لطفاً جواب خود را وارد کنید: ")

    # تبدیل اعداد فارسی به انگلیسی (در صورت نیاز)
    user_answer = convert_farsi_digits_to_english(user_answer)
    
    end_time = time.time()
    time_dif = end_time - start_time

    # بررسی زمان و پاسخ کاربر
    if time_dif < time_limit:
        try:
            if int(user_answer) == result:  # تبدیل ورودی کاربر به عدد صحیح
                score += 1 
                print(f"صحیح! امتیاز فعلی: {score}")
            else:
                print(f"اشتباه! جواب صحیح {result} بود.")
        except ValueError:
            print("لطفاً یک عدد صحیح وارد کنید.")
    else:
        print("متاسفانه زمان شما تمام شد.")

    question_number += 1          

# نمایش امتیاز پایانی
print(f"بازی به پایان رسید. امتیاز نهایی شما: {score} از {question_number_limit} سوال.")
1
