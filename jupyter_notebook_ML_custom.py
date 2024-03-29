#This AI bot will respond to most common questions about the tech gadget

# Define a dictionary with predefined responses
responses = {
    "hi": "Hello there! How can I assist you today?",
    "tell me about the product" : "The high end worstation is capable of running 256 processes at the same time thanks to the latest Intel Core i9 processor",
    "shipping details": "If you finilize the purchase and pay for the item before 4PM, we guarantee same day shipping and depending on your location delivery will take 1-3 business days",
    "return policy": "We accept for returns for up to 30 days",
    "my computer won't turn on": "Make sure you switch on the power supplywith the I/O button",
    "my pc turns on but nothing shows on the screen": "Remove all but 1 RAM stick and see if the computer will post",
    "how do I reset the pc": "Hold down shift and click on the windows logo on the bottom of the screen and then click Restart",
    "help": "Sure, I can help you. What do you need assistance with?",
}

# Function to get the bot response
def get_bot_response(user_input):
    # Make the input lowercase to match the dictionary keys
    user_input = user_input.lower()

    # Return the matching response if it exists, otherwise return a default response
    return responses.get(user_input, "I'm not sure how to respond to that. Can you try asking something else?")

# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    response = get_bot_response(user_input)
    print(f"Bot: {response}")