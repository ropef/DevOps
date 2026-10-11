
print("start")
from config import TELEGRAM_TOKEN
import re
from collections import Counter
import requests

LOG_FILE = "ip_adress.txt"
CHAT_ID = "8752874549"

# Поиск IP-адресов с ошибками 404
with open(LOG_FILE, "r", encoding="utf-8") as f:
    log_content = f.read()

    # Ищем IP-адреса и код ответа 404
    ips = re.findall(
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?"\s+404\b',
        log_content
    )

# Считаем количество ошибок для каждого IP
ip_count = Counter(ips)

# Если какой-то IP совершил более 50 ошибок 404
for ip, count in ip_count.items():
    print(f"IP: {ip} — ошибок 404: {count}")
    if count >5:
        msg = (
            f"Обнаружена подозрительная активность! "
            f"IP {ip} получил {count} ошибок 404."
        )

        print(msg)

        # Отправляем сообщение в Telegram
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

        response = requests.post(
            url,
            json={
                "chat_id": CHAT_ID,
                "text": msg
            }

        )

        print("Ответ Telegram:", response.text)
