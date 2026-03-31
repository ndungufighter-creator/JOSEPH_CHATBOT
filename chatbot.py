import random

def chatbot(): 
    print("🤖 AI Course Assistant Bot")
    print("Type 'bye' to exit.\n")
    
    while True:
        user = input("You: ").lower()

        if "hello" in user or "hi" in user:
            responses = [
                "Hello Joseph! How can I assist you today?",
                "Hi there! Ready to learn some AI?",
                "Hey Joseph! What can I help you with?"
            ]
            print("Bot:", random.choice(responses))
        
        elif "ai" in user:
            responses = [
                "AI stands for Artificial Intelligence. It allows machines to think and learn like humans.",
                "Artificial Intelligence helps computers perform tasks that usually require human intelligence.",
                "AI is all about making machines smart and capable of learning."
            ]
            print("Bot:", random.choice(responses))
        
        elif "python" in user:
            responses = [
                "Python is a popular programming language for AI.",
                "Python is widely used in AI because it's simple and powerful.",
                "You can use Python libraries like NumPy, Pandas, and Scikit-learn for AI."
            ]
            print("Bot:", random.choice(responses))
        
        elif "machine learning" in user:
            responses = [
                "Machine Learning allows systems to learn from data.",
                "It’s a branch of AI that improves automatically through experience.",
                "Machine Learning helps computers make predictions without being explicitly programmed."
            ]
            print("Bot:", random.choice(responses))
        
        elif "pass" in user or "exam" in user:
            responses = [
                "Focus on practice and understanding concepts.",
                "Revise consistently and complete your assignments on time.",
                "Practice past papers and stay consistent — you’ll pass!"
            ]
            print("Bot:", random.choice(responses))
        
        elif "thanks" in user:
            responses = [
                "You're welcome! 😊",
                "Happy to help!",
                "Anytime, Joseph!"
            ]
            print("Bot:", random.choice(responses))
        
        elif "bye" in user:
            responses = [
                "Goodbye Joseph! All the best 👋",
                "See you next time! Keep learning!",
                "Bye! Don’t forget to practice AI 😊"
            ]
            print("Bot:", random.choice(responses))
            break
        
        else:
            responses = [
                "Sorry, I didn't understand that.",
                "Can you try asking that differently?",
                "Hmm… I’m not sure about that yet."
            ]
            print("Bot:", random.choice(responses))

chatbot()

print("Welcome to AI Bot")

print("This is my simple ai and efficient chatbot")