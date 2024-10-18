import random
import time

def question_generator():
    # پردازش اعداد تصادفی
    a = random.randint(1, 9)
    b = random.randint(1, 9)

    # انتخاب تصادفی عملگر
    operator_list = ["+", "-", "*"]
    selected_operator = random.choice(operator_list)

    print(f"{a} {selected_operator} {b} = ?")

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
    user_answer = input("Enter your answer: ")
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
