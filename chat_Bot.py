import os
import google.generativeai as genai
from colorama import init, Fore, Style

# Initialize colorama (Windows friendly)
init(autoreset=True)

# --- API Key Configuration ---
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print(Fore.RED + "FATAL ERROR: GEMINI_API_KEY environment variable not set.")
    print(Fore.YELLOW + "➡️ Set it before running:\n   setx GEMINI_API_KEY \"your-api-key-here\"")
    exit()

genai.configure(api_key=API_KEY)

# --- Initialize Gemini model ---
try:
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception as e:
    print(Fore.RED + f"FATAL ERROR: Could not initialize model: {e}")
    exit()

# --- Welcome Message ---
print(Fore.CYAN + Style.BRIGHT + "\n=======================================")
print(Fore.CYAN + Style.BRIGHT + "🤖 Gemini Chatbot is ready! (type 'bye' to exit)")
print(Fore.CYAN + Style.BRIGHT + "=======================================\n")

# --- Chat Loop ---
while True:
    user_input = input(Fore.BLUE + "🧑 You: " + Style.RESET_ALL)

    if user_input.lower() in ["bye", "exit", "quit"]:
        print(Fore.YELLOW + "\n🤖 Bot: Goodbye Master! 👋")
        break

    try:
        # Generate response from Gemini
        response = model.generate_content(user_input)

        # Print bot reply nicely
        print(Fore.CYAN + "🤖 Bot: " + Style.BRIGHT + response.text + "\n")

    except Exception as e:
        print(Fore.RED + f"⚠️ Error: {e}\n")