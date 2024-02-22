#!/usr/bin/env python3
print("Content-type:text/html\r\n\r\n")
import cgi, cgitb; cgitb.enable()

# Import modules for CGI handling 
import random
import re

# Dictionary of sample responses with regular expressions
responses = {
    r"hello.*": ["Hello!", "Hi there!", "Hey!"],
    r"how are you.*": ["I'm doing well, thank you!", "I'm good, how about you?", "Pretty good!"],
    r"goodbye.*": ["Goodbye!", "See you later!", "Bye!"],
    r".*name.*": ["My name is Chatbot.", "You can call me Chatbot.", "I'm Chatbot!"],
    r".*(how old|age).*": ["I'm just a computer program, so I don't have an age.", "Age is just a number for me!"],
    r".*(where|location|located).*": ["I exist in the digital realm, so I'm everywhere and nowhere at the same time.", "I'm located wherever I'm needed, usually on servers."],
    "default": ["I'm not sure what you mean...", "Can you please rephrase that?", "I didn't understand that."]
}

# Function to generate bot response using regular expressions
def generate_bot_response(user_input):
    if user_input is not None:  # Check if user input exists
        # Check if input matches any predefined responses with regular expressions
        for pattern, responses_list in responses.items():
            if re.match(pattern, user_input, re.IGNORECASE):
                return random.choice(responses_list)

    # If no predefined response matches or user_input is None, return a default response
    return random.choice(responses["default"])

def parse_form_data():
    form = cgi.FieldStorage()
    user_input = form.getvalue('user_input')
    return user_input

# Function to generate HTML response
def generate_response(bot_response):
    print("Content-type:text/html\r\n\r\n")
    print(f"""
    <html>
    <head>
        <title>Chatbot Response</title>
    </head>
    <body>
        <h1>Chatbot Response</h1>
        <p>{bot_response}</p>
    </body>
    </html>
    """)

# Main function
if __name__ == "__main__":
    user_input = parse_form_data()
    bot_response = generate_bot_response(user_input)
    generate_response(bot_response)
