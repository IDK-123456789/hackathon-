import msvcrt #(use AI to generate the code)
import subprocess
import cv2
import os
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from playsound import playsound
from gtts import gTTS

# Set the folder where you want to save images
save_folder = os.path.join(os.getcwd(), "captured")

# Create the folder if it doesn't exist
os.makedirs(save_folder, exist_ok=True)
img_path = os.path.join(save_folder, "captured_image.jpg")

# Ensure you have the required libraries installed: (used AI to generate the code)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# This script runs a Python script in a subprocess and captures keyboard input.
# This script captures keyboard input in a loop and prints the pressed key.
while True:
    key = msvcrt.getch()
    print(f"You pressed: {key.decode('utf-8', errors='ignore')}")
    if key.lower() == b'q':
        print("Exiting loop.")
        break
    elif key.lower() == b'a':
        print("You pressed 'a'. Running see.py...")
        subprocess.run(["python", "see.py"])
    elif key.lower() == b'b':
        print("You pressed 'b'. Running say.py...")
        # subprocess.run(["python", "say.py"])
        # Load the image captured by the previous script
        img = Image.open(img_path)
        inputs = processor(img, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)
        print("Caption:", caption)

        # Convert the caption to speech and save it as an audio file
        caption = "i-can-c says: " + caption
        tts = gTTS(text=caption, lang='en')
        tts.save("description.mp3")
        print("Audio saved as description.mp3")
        playsound("description.mp3")