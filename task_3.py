import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

patterns_responses = [
    (r'Hi|Hello|Hey', ["Greetings, seeker. How may I assist you today?", 
                      "Hello! How can I help you on your journey?"]),
    
    (r'What is your name', ["I am RUMI, a humble guide in the world of words and wisdom."]),
    
    (r'How are you', ["I am but a reflection of your thoughts. Tell me, how does your heart feel today?"]),
    
    (r'What can you do', ["I can share wisdom, answer your queries, and walk alongside you on your journey of knowledge."]),
    
    (r'Bye|Goodbye', ["Farewell, dear seeker. May your journey be filled with wisdom and light.",
                      "Goodbye! May your path be ever bright."])
]

chatbot = Chat(patterns_responses, reflections)

def chatbot_conversation():
    print("RUMI: Greetings, wanderer of thoughts! Type 'Bye' to part ways.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye']:
            print("RUMI: Farewell, dear seeker. May your heart always find its path.")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print(f"RUMI: {response}")
            else:
                print("RUMI: The universe holds many mysteries; perhaps rephrase your question, and we shall seek together.")

if __name__ == "__main__":
    chatbot_conversation()
