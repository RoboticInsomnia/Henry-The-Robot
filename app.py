import speech_recognition as sr
import time

# Initialize the speech recognition object
r = sr.Recognizer()

# Define the function for the robot's movements
def move(direction):
    print("Moving " + direction)
    # Code for actual movement goes here

# Set up the microphone
mic = sr.Microphone()

# Calibrate the microphone to ambient noise
with mic as source:
    r.adjust_for_ambient_noise(source)

# Start listening for speech
while True:
    with mic as source:
        print("Hi.... please say a command!")
        audio = r.listen(source)

    # Attempt to recognize speech
    try:
        command = r.recognize_google(audio)
        print("You said: " + command)

        # Determine which direction the user wants to move the robot
        if "forward" in command:
            move("forward")
        elif "backward" in command:
            move("backward")
        elif "left" in command:
            move("left")
        elif "right" in command:
            move("right")
        else:
            print("Invalid command. Try again.")

    # Handle errors with speech recognition
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Wait for a moment before listening again
    time.sleep(1)