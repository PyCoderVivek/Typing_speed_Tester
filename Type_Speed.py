import time
import random


def generate_random_text(words):
    text = ' '.join(random.choice(words) for i in range(50))
    return text


def calculate_typing_speed(start_time, end_time, typed_text):
    words_per_minute = len(typed_text.split()) / ((end_time - start_time) / 60)
    return words_per_minute


def typing_speed_test():
    # words = ["python", "programming", "challenge", "keyboard", "practice", "speed", "testing", "accuracy"]
    original_text = ("The Indian Army has the sole objective of protecting the nation from any foreign aggression "
                     "that"
                     "arises, ensuring the nation's security. They also try to prevent the nation from internal \n  "
                     "threats. During natural calamities, the Indian Army conducts humanitarian rescue operations to \n"
                     "save many people's lives")

    print("Type the following:")
    print(original_text)

    input("Press Enter when you are ready to start typing.")

    print("Start typing...")

    start_time = time.time()
    typed_text = input("Type here: ")
    end_time = time.time()

    elapsed_time = end_time - start_time

    words_per_minute = calculate_typing_speed(start_time, end_time, typed_text)

    print(f"\nYour typing speed: {words_per_minute:.2f} words per minute")
    print(f"You spend   : {elapsed_time:.2f} seconds on this typing test ")


if __name__ == "__main__":
    typing_speed_test()
