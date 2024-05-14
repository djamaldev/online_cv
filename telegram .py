import requests

def req_chat_id():
    TOKEN = "token"
    url =  
"https://api.telegram.org/bot{token}/getUpdates"
    print(requests.get(url).json())

def telegram_bot_sendtext():
    
    bot_token = 'token'
    bot_chatID = req_chat_id()
    send_text = 
"https://api.telegram.org/bot{token}/sendMessage?chat_id=bot_chatID&text=your mssage text here....!"

    response = requests.get(send_text)

    return response.json()
