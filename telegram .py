import requests

def req_chat_id():
    TOKEN = "your token"
    url =  
"https://api.telegram.org/bot{your token}/getUpdates"
    print(requests.get(url).json())

def telegram_bot_sendtext():
    
    bot_token = 'your token'
    bot_chatID = req_chat_id()
    send_text = 
"https://api.telegram.org/bot
{bot_token}
/sendMessage?chat_id=bot_chatID&text=your mssage text here....!"

    response = requests.get(send_text)

    return response.json()