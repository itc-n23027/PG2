import random
import time

def ask_question(a, b):
    correct_answer = a * b
    attempts = 3
    for attempt in range(attempts):
        start_time = time.time()
        answer = input(f'{a} × {b} = ')
        end_time = time.time()
        
        if end_time - start_time > 8:
            print("時間切れ！")
            return False
        
        try:
            if int(answer) == correct_answer:
                print("正解！")
                time.sleep(1)
                return True
            else:
                print("間違いです。")
        except ValueError:
            print("数値を入力してください。")

    print(f"正解は {correct_answer} でした。")
    return False

def multiplication_quiz():
    questions = [(random.randint(0, 9), random.randint(0, 9)) for _ in range(10)]
    score = 0
    
    for i, (a, b) in enumerate(questions):
        print(f"問題 {i+1}")
        if ask_question(a, b):
            score += 1

    print(f"クイズ終了！ あなたのスコアは {score} / 10 です。")

if __name__ == "__main__":
    multiplication_quiz()
