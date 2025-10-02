import google.generativeai as genai

# 🔑 Configure API key (replace with your key)
genai.configure(api_key="YOUR_API_KEY_HERE")

# Initialize Gemini model (use "gemini-1.5-flash" or "gemini-1.5-pro")
model = genai.GenerativeModel("gemini-1.5-flash")

print("🤖 Gemini Chatbot is ready! (type 'bye' to exit)\n")

# Chat loop
while True:
    user_input = input("You: ")

    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye Master! 👋")
        break

    # Generate response from Gemini
    response = model.generate_content(user_input)

    print("Bot:", response.text)