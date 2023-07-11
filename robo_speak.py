import pyttsx3

print("Welcome to RoboSpeak 1.1 Created By Fasih ul Hassan Baig")
while(True):
    x = input("Enter What You Want Me To Speak: ")
    if(x == "q"):
        break
    # Initialize the text-to-speech engine
    text = pyttsx3.init()
    
    # Get the current speed rate
    current_rate = text.getProperty('rate')
    print("Current speech rate:", current_rate)

    # Set the new speed rate (change the value as desired)
    new_rate = 150  # Adjust the rate value as per your preference
    text.setProperty('rate', new_rate)
    
    # Speak the provided text
    text.say(x)
    text.runAndWait()
