import requests

def req_chat_id():
    TOKEN = "7054721511:AAH-iPHLPmjFikcWD9CfbKkZk5JfkrFE6PE"
    url =  
"https://api.telegram.org/bot7054721511:AAH-iPHLPmjFikcWD9CfbKkZk5JfkrFE6PE/getUpdates"
    print(requests.get(url).json())

def telegram_bot_sendtext():
    
    bot_token = '7054721511:AAH-iPHLPmjFikcWD9CfbKkZk5JfkrFE6PE'
    bot_chatID = req_chat_id()
    send_text = 
"https://api.telegram.org/bot7054721511:AAH-iPHLPmjFikcWD9CfbKkZk5JfkrFE6PE/sendMessage?chat_id=bot_chatID&text=your mssage text here....!"

    response = requests.get(send_text)

    return response.json()
