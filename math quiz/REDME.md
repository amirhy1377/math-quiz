This code implements a simple math quiz game where random arithmetic questions are presented to the user, who must answer them within a limited time. Let's break down each part of the code:





1. Importing Libraries
import random
import time
random: This library is used to generate random numbers.
time: This library is used for measuring time and controlling the time limit for answering questions.



2. Function to Convert Persian Digits to English
def convert_farsi_digits_to_english(input_str):
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    translation_table = str.maketrans(persian_digits, english_digits)
    return input_str.translate(translation_table)
This function takes a string input of Persian digits and converts them to their English equivalents.
It uses str.maketrans to create a translation table and then applies this translation with translate.




3. Question Generator Function
def question_generator():
    a = random.randint(1, 9)
    b = random.randint(1, 9)

    operator_list = ["+", "-", "*"]
    selected_operator = random.choice(operator_list)

    if selected_operator == "+":
        operator_farsi = "به‌علاوه"
    elif selected_operator == "-":
        operator_farsi = "منها"
    else:
        operator_farsi = "ضربدر"

    print(f"{a} {operator_farsi} {b} = ?")

    if selected_operator == "+":
        return a + b
    elif selected_operator == "-":
        return a - b
    else:
        return a * b
This function generates two random integers between 1 and 9, then randomly selects an arithmetic operator (addition, subtraction, or multiplication).
The selected operator is translated to Persian for display purposes, and the question is printed in the format (e.g., 5 به‌علاوه 3 = ?).
The result of the arithmetic operation is calculated and returned.



4. Initial Settings
question_number_limit = 5
question_number = 0
score = 0
time_limit = 10
question_number_limit: This variable sets the maximum number of questions in the game (in this case, 5).
question_number: This variable keeps track of the current question number (initialized to 0).
score: This variable tracks the user's score (initialized to 0).
time_limit: This variable defines the time limit for answering each question (set to 10 seconds).


5. Main Game Loop
while question_number < question_number_limit:
    result = question_generator()  # Generate a new question
    start_time = time.time()

    user_answer = input("لطفاً جواب خود را وارد کنید: ")
    
    user_answer = convert_farsi_digits_to_english(user_answer)
    
    end_time = time.time()
    time_dif = end_time - start_time

    if time_dif < time_limit:
        try:
            if int(user_answer) == result:  # Check if the answer is correct
                score += 1 
                print(f"صحیح! امتیاز فعلی: {score}")
            else:
                print(f"اشتباه! جواب صحیح {result} بود.")
        except ValueError:
            print("لطفاً یک عدد صحیح وارد کنید.")
    else:
        print("متاسفانه زمان شما تمام شد.")

    question_number += 1          
In this loop, questions are presented to the user, who must answer them within the specified time limit:

A new question is generated using the question_generator function, and the start time is recorded.
The user is prompted to enter their answer.
If the user enters Persian digits, they are converted to English using the convert_farsi_digits_to_english function.
The end time is recorded, and the time taken to answer is calculated.
If the user answers within the 10-second limit:

The answer is checked to see if it's correct.
If the answer is correct, the score is incremented, and a success message is displayed.
If the answer is incorrect, the correct answer is shown.
If the user does not enter a valid integer, a message is displayed asking them to enter a valid integer.
If the user exceeds the 10-second limit, a message saying "متاسفانه زمان شما تمام شد." (Unfortunately, your time is up.) is displayed.

6. Final Score Display
print(f"بازی به پایان رسید. امتیاز نهایی شما: {score} از {question_number_limit} سوال.")
Once the number of questions reaches the limit, the loop ends, and the user's final score is displayed.
Conclusion
This code implements a fun and educational math quiz game that allows users to test their arithmetic skills and practice their response speed. The use of Persian for
the questions makes it accessible for Persian-speaking users, enhancing their experience while engaging with basic math concepts.




این کد یک بازی ساده ریاضی است که به کاربر سوالات ریاضی تصادفی می‌دهد و از او می‌خواهد در زمان محدود به آن‌ها پاسخ دهد. در ادامه به تفصیل هر بخش کد را بررسی می‌کنیم:

1. وارد کردن کتابخانه‌ها
import random
import time
random: برای تولید اعداد تصادفی استفاده می‌شود.
time: برای محاسبه زمان و کنترل زمان پاسخ‌دهی کاربر به سوالات استفاده می‌شود.
2. تابع تبدیل اعداد فارسی به انگلیسی
def convert_farsi_digits_to_english(input_str):
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    translation_table = str.maketrans(persian_digits, english_digits)
    return input_str.translate(translation_table)
این تابع ورودی رشته‌ای از اعداد فارسی می‌گیرد و آن‌ها را به معادل انگلیسی‌شان تبدیل می‌کند.
با استفاده از str.maketrans یک جدول ترجمه ایجاد می‌شود و سپس با translate این تبدیل اعمال می‌شود.
3. تابع تولید سوالات
def question_generator():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    
    operator_list = ["+", "-", "*"]
    selected_operator = random.choice(operator_list)

    if selected_operator == "+":
        operator_farsi = "به‌علاوه"
    elif selected_operator == "-":
        operator_farsi = "منها"
    else:
        operator_farsi = "ضربدر"

    print(f"{a} {operator_farsi} {b} = ?")

    if selected_operator == "+":
        return a + b
    elif selected_operator == "-":
        return a - b
    else:
        return a * b
این تابع دو عدد تصادفی بین 1 تا 9 تولید می‌کند و یک عملگر ریاضی (جمع، تفریق، یا ضرب) به طور تصادفی انتخاب می‌کند.
سپس سوال را به زبان فارسی نمایش می‌دهد (با استفاده از عملگرهای فارسی) و نتیجه آن را محاسبه و برمی‌گرداند.
4. تنظیمات اولیه
question_number_limit = 5
question_number = 0
score = 0
time_limit = 10
question_number_limit: حداکثر تعداد سوالات بازی (در اینجا ۵).
question_number: شمارنده سوالات فعلی (ابتدا ۰).
score: امتیاز کاربر (ابتدا ۰).
time_limit: محدودیت زمانی برای پاسخ‌دهی به هر سوال (در اینجا ۱۰ ثانیه).
5. حلقه اصلی بازی
   
while question_number < question_number_limit:
    result = question_generator()  # دریافت نتیجه سوال
    start_time = time.time()

    user_answer = input("لطفاً جواب خود را وارد کنید: ")
    
    user_answer = convert_farsi_digits_to_english(user_answer)
    
    end_time = time.time()
    time_dif = end_time - start_time

    if time_dif < time_limit:
        try:
            if int(user_answer) == result:
                score += 1 
                print(f"صحیح! امتیاز فعلی: {score}")
            else:
                print(f"اشتباه! جواب صحیح {result} بود.")
        except ValueError:
            print("لطفاً یک عدد صحیح وارد کنید.")
    else:
        print("متاسفانه زمان شما تمام شد.")

    question_number += 1          
در این حلقه، سوالات به کاربر نمایش داده می‌شود و او باید در زمان معین به آن‌ها پاسخ دهد:

سوال جدید تولید می‌شود و زمان شروع ثبت می‌شود.
کاربر از او خواسته می‌شود که پاسخ خود را وارد کند.
اگر کاربر از اعداد فارسی استفاده کند، پاسخ به اعداد انگلیسی تبدیل می‌شود.
زمان پایان پاسخ‌دهی ثبت می‌شود و زمان اختلاف محاسبه می‌شود.
اگر کاربر در کمتر از ۱۰ ثانیه پاسخ دهد:

پاسخ او بررسی می‌شود که آیا صحیح است یا خیر.
اگر پاسخ صحیح باشد، امتیاز کاربر افزایش می‌یابد و پیام "صحیح!" نمایش داده می‌شود.
اگر پاسخ اشتباه باشد، جواب صحیح به کاربر نشان داده می‌شود.
اگر کاربر عدد صحیح وارد نکند، پیامی مبنی بر این که "لطفاً یک عدد صحیح وارد کنید" نمایش داده می‌شود.
اگر زمان بیش از ۱۰ ثانیه باشد، پیام "متاسفانه زمان شما تمام شد." نمایش داده می‌شود.

6. نمایش امتیاز پایانی
print(f"بازی به پایان رسید. امتیاز نهایی شما: {score} از {question_number_limit} سوال.")
پس از پایان بازی، امتیاز نهایی کاربر به او نمایش داده می‌شود.
نتیجه‌گیری
این کد یک بازی ریاضی سرگرم‌کننده و آموزشی است که به کاربر امکان می‌دهد تا توانایی‌های ریاضی خود را تست کند و سرعت پاسخ‌دهی خود را تمرین کند. همچنین با توجه به تعامل به زبان فارسی، کاربرانی که به این زبان صحبت می‌کنند می‌توانند به راحتی از این برنامه استفاده کنند.

