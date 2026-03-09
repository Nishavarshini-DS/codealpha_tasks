import random
import time
import sys

def type_text(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def play_rps(user_choice):
   
    choices = ['rock', 'paper', 'scissors']
    user_choice = user_choice.lower().strip()
    if user_choice not in choices:
        return "Please choose rock, paper, or scissors! 🎮"
    bot_choice = random.choice(choices)
    if user_choice == bot_choice:
        return f"🤝 Tie! Both chose {user_choice}!"
    elif (user_choice == 'rock' and bot_choice == 'scissors') or (user_choice == 'paper' and bot_choice == 'rock') or (user_choice == 'scissors' and bot_choice == 'paper'):
        return f"🎉 You win! {user_choice} beats {bot_choice}!"
    else:
        return f"🤖 I win! {bot_choice} beats {user_choice}!"

def chatbot():
    type_text("ChatBot: Hi! Type 'bye' to exit. Type 'prompts' for more commands!", 0.02)
    
    while True:
        user = input("You: ").lower()
        
        if user == "bye":
            type_text("ChatBot: Goodbye!", 0.02)
            break
        elif user.startswith('play ') or user.startswith('rps '):
            choice = user.split()[-1]
            type_text(f"ChatBot: {play_rps(choice)}", 0.02)
        elif "hello" in user or "hi" in user:
            type_text("ChatBot: Hello!", 0.02)
        elif "how are you" in user:
            type_text("ChatBot: I'm fine, thanks!", 0.02)
        elif "your name" in user:
            type_text("ChatBot: I'm ChatBot.", 0.02)
        elif "joke" in user:
            type_text("ChatBot: Why do programmers prefer dark mode? Light attracts bugs!", 0.02)
        elif "weather" in user:
            type_text("ChatBot: I don't know, I'm inside a computer.", 0.02)
        elif "prompts" in user:
            type_text("Here are the interesting commands you can try:", 0.02)
            time.sleep(0.3)
            type_text(" joke - tells a joke", 0.02)
            type_text(" weather - talks about weather", 0.02)
            type_text(" your name - tells its name", 0.02)
            type_text(" how are you - tells about itself", 0.02)
            type_text(" play rock/paper/scissors - play RPS game! \nBut make sure to use the prefix play before your choice in rps", 0.02)
        else:
            type_text("ChatBot: I'm not sure what you mean.", 0.02)

chatbot()