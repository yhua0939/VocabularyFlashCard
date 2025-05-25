import random

# Flashcard class
class Flashcard:
    def __init__(self, english_words, chinese_translations):
        self.english = english_words
        self.chinese = chinese_translations

    def check_answer(self, user_input):
        return user_input.strip() == self.chinese

# Word bank
word_bank = {
    "apple": "苹果", "banana": "香蕉", "movie": "电影", "computer": "电脑", "dog": "狗",
    "egg": "鸡蛋", "fish": "鱼", "grape": "葡萄", "house": "房子", "ice": "冰",
    "juice": "果汁", "key": "钥匙", "lamp": "灯", "cup": "杯子", "notebook": "笔记本",
    "orange": "橙子", "pen": "钢笔", "queen": "女王", "river": "河流", "pillow": "枕头",
    "moon": "月亮", "bed": "床", "bedroom": "卧室", "king": "国王", "eyebrow": "眉毛",
}

# Create flashcard list
flashcard_list = []
for english_word, chinese_translation in word_bank.items():
    flashcard = Flashcard(english_word, chinese_translation)
    flashcard_list.append(flashcard)

# In-memory mistake list
mistake_list = []

# Learning mode
def start_learning_mode(selected_cards):
    print("\nLearning Mode: English ｜ Chinese")
    for word in selected_cards:
        print(word.english + " ｜ " + word.chinese)
    print("\nEnd of learning!\n")

# Test mode
def start_test_mode(selected_cards):
    print("\nTest Mode: Let's test your translation skills!\n")
    correct_count = 0
    wrong_answers = []
    question_number = 1

    for word_card in selected_cards:
        print("Word " + str(question_number) + ": " + word_card.english)
        user_input = input("Your answer: ").strip()
        if word_card.check_answer(user_input):
            print("Correct!")
            correct_count += 1
        else:
            print("Incorrect! Correct answer: " + word_card.chinese)
            wrong_answers.append({"english": word_card.english, "chinese": word_card.chinese})
        question_number += 1

    print("\nYou got " + str(correct_count) + " / " + str(len(selected_cards)) + " correct.")
    print("Mistakes this round: " + str(len(wrong_answers)))
    mistake_list.extend(wrong_answers)
    return wrong_answers

# Review mistakes
def review_mistakes():
    if len(mistake_list) == 0:
        print("\nNo mistakes to review. Great job!")
        return
    print("\nReview Mode: Let's review your mistakes.\n")
    review_index = 1
    for mistake in mistake_list:
        print("Word " + str(review_index) + ": " + mistake["english"])
        user_retry = input("Your answer: ").strip()
        if user_retry == mistake["chinese"]:
            print("Correct!")
        else:
            print("Incorrect! Correct answer: " + mistake["chinese"])
        review_index += 1

# Main program
def start_flashcard_app():
    print("Welcome to VocabularyFlashCard - Your Vocabulary Study Buddy!")
    name = input("Please enter your name: ").strip()

    while True:
        print(f"\n{name.lower()}, please choose a mode:")
        print("\t1. Learn")
        print("\t2. Test")
        print("\t3. Review Mistakes")
        print("\t4. Exit")

        user_choice = input("Enter your choice (1-4): ").strip()
        user_choice = str(user_choice)

        if user_choice == "1":
            selected_cards = random.sample(flashcard_list, 10)
            start_learning_mode(selected_cards)

        elif user_choice == "2":
            selected_cards = random.sample(flashcard_list, 10)
            wrong_answers = start_test_mode(selected_cards)
            review_now = input("Do you want to review the mistakes from this round? (yes/no): ").lower()
            if review_now == "yes":
                print("\nInstant Review: Let's go through your mistakes again!")
                for i in range(len(wrong_answers)):
                    word = wrong_answers[i]
                    print("Word " + str(i + 1) + ": " + word["english"])
                    answer = input("Your answer: ").strip()
                    if answer == word["chinese"]:
                        print("Correct!")
                    else:
                        print("Incorrect! Correct answer: " + word["chinese"])

        elif user_choice == "3":
            review_mistakes()

        elif user_choice == "4":
            print("\nThanks for using VocabularyFlashCard.\nGoodbye!")
            break

        else:
            print("Invalid input! Please enter 1 to 4.")

# Start the app
if __name__ == "__main__":
    start_flashcard_app()