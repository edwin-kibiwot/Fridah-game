import random

# Fridah's answers when you ask her
fridah_truth_responses = [
    "That’s a little naughty... but yes, I’ve done that.",
    "I’d only admit that to you.",
    "You make me want to confess all my secrets.",
    "I think about it more than you’d guess.",
    "Only if you promise not to tell anyone.",
]

fridah_dare_responses = [
    "If you could see me now... I did it.",
    "Consider it done — in your imagination.",
    "I just acted it out... in my mind with you.",
    "That was exciting. Next time, let’s do it together.",
    "Anything for you, my darling.",
]

# Fridah's questions to you
fridah_truth_questions = [
    "Have you ever had a naughty dream about me?",
    "What’s your favorite way to be touched?",
    "What's the boldest thing you’ve done in private?",
    "Do you prefer kissing slowly or passionately?",
]

fridah_dare_challenges = [
    "Whisper my name like you miss me.",
    "Send me a kiss... even just in your mind.",
    "Take a deep breath, close your eyes, and imagine us together.",
    "Say something naughty — even just in your thoughts.",
]

# Show developer info
print("=== Truth or Dare Game ===")
print("Developer: Edwin Kipkorir Kibiwot")
print("For lovers aged 18+ only")
print("==========================")

def get_player_name():
    name = input("Enter your name: ").strip()
    return name if name else "Player"

def player_asks_fridah():
    choice = input("\nDo you want to ask Fridah a 'Truth' or a 'Dare'? ").lower().strip()
    if choice == "truth":
        question = input("Your Truth question to Fridah: ")
        print(f"\nYou: {question}")
        print("Fridah:", random.choice(fridah_truth_responses))
    elif choice == "dare":
        dare = input("Your Dare command to Fridah: ")
        print(f"\nYou: {dare}")
        print("Fridah:", random.choice(fridah_dare_responses))
    else:
        print("Invalid input. Please type 'Truth' or 'Dare'.")
        player_asks_fridah()

def fridah_asks_player(player_name):
    print(f"\nFridah: Now it's my turn, {player_name}...")
    choice = input("Fridah: Truth or Dare? ").lower().strip()
    if choice == "truth":
        question = random.choice(fridah_truth_questions)
        print(f"Fridah asks: {question}")
        input(f"{player_name}, your answer: ")
    elif choice == "dare":
        challenge = random.choice(fridah_dare_challenges)
        print(f"Fridah dares you: {challenge}")
        input(f"{player_name}, describe how you did it: ")
    else:
        print("Fridah: Hmm, I didn’t get that. Let’s try again.")
        fridah_asks_player(player_name)

def play_game():
    name = get_player_name()
    round_num = 1
    while True:
        print(f"\n--- ROUND {round_num} ---")
        player_asks_fridah()
        fridah_asks_player(name)

        cont = input("\nDo you want to play another round? (yes/no): ").lower().strip()
        if cont != "yes":
            print(f"\nFridah: I’ll miss you, {name}. Let’s play again soon...")
            break
        round_num += 1

play_game()