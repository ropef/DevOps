import re
import os

from collections import Counter

import requests



LOG_FILE = "C:\devops\Второе полугодие\Задание 2.1\access.log"

TELEGRAM_TOKEN = "8669038062:AAGf0tDnPtph0hrqNjBkist98Tp9bc4eInQ"

CHAT_ID = "your_chat_id"



# Поиск IP адресов с ошибками 404

with open(LOG_FILE, "r") as f:

    log_content = f.read()

    # Ищем IP и код ответа 404

    ips = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?" 404', log_content)



# Если какой-то IP совершил более 50 ошибок 404

for ip, count in Counter(ips).items():

    if count > 50:

        msg = f"Обнаружена подозрительная активность! IP {ip} получил {count} ошибок 404."

        requests.post(f"https://telegram.org{TELEGRAM_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg})
