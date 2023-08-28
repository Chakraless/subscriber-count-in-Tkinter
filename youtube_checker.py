# AIzaSyAlUu_yOdm-YwNzu5k1dG9utmM8lkCWqKU
from tkinter import *
import requests

window = Tk()
window.geometry('500x500')
window.title('YouTube Subscriber Count')

def subscriber_count(channel_name):
    api_key = 'AIzaSyAlUu_yOdm-YwNzu5k1dG9utmM8lkCWqKU'  # Replace with your own API key
    url = f'https://www.googleapis.com/youtube/v3/channels'
    
    params = {
        'part': 'statistics',
        'forUsername': channel_name,
        'key': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        subscriber_count = data['items'][0]['statistics']['subscriberCount']
        return f"Subscriber Count: {subscriber_count}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_subscriber_count():
    input_channel = channel_name.get()
    result = subscriber_count(input_channel)
    result_label.config(text=result)

channel_label = Label(window, text="Enter channel name:")
channel_label.pack()

channel_name = Entry(window)
channel_name.pack()

check_button = Button(window, text="Check Subscriber Count", command=get_subscriber_count)
check_button.pack()

result_label = Label(window, text="")
result_label.pack()

window.mainloop()
