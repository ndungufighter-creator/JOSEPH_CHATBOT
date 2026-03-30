def chatbot():
    print("🤖 AI Course Assistant Bot")
    print("Type 'bye' to exit.\n")
    
    while True:
        user = input("You: ").lower()

        if "hello" in user or "hi" in user:
            print("Bot: Hello Joseph! How can I assist you today?")
        
        elif "ai" in user:
            print("Bot: AI stands for Artificial Intelligence. It allows machines to think and learn like humans.")
        
        elif "python" in user:
            print("Bot: Python is a popular programming language for AI. Libraries include NumPy, Pandas, and Scikit-learn.")
        
        elif "machine learning" in user:
            print("Bot: Machine Learning is a part of AI that enables systems to learn from data without being explicitly programmed.")
        
        elif "pass" in user or "exam" in user:
            print("Bot: To pass, focus on practice, understand concepts, and complete your assignments on time.")
        
        elif "thanks" in user:
            print("Bot: You're welcome! Happy to help 😊")
        
        elif "bye" in user:
            print("Bot: Goodbye Joseph! All the best in your AI course 👋")
            break
        
        else:
            print("Bot: Sorry, I didn't understand that. Please try another question.")

chatbot()