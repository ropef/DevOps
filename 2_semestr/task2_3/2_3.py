import requests
from bs4 import BeautifulSoup


url = "https://www.cbr.ru/currency_base/daily/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/150.0.0.0 Safari/537.36 YaBrowser/26.8.0.0"
    )
}

def get_rates(url):
    """Возврат списка с курсами валют."""
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()  # ошибка, если статус не 200

    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", class_="data")

    rates = []
    rows = table.find_all("tr")[1:]  # пропускаем заголовок
    for row in rows:
        cols = [c.get_text(strip=True) for c in row.find_all("td")]

        if len(cols) >= 5:
            rates.append({
                "letter": cols[1],   # Буквенный код
                "units":  cols[2],   # Количество валюты
                "name":   cols[3],   # Полное имя валюты
                "rate":   cols[4],   # Стоимость валюты
            })
    return rates


try:
    rates = get_rates(url)
    print(f"Получено курсов: {len(rates)}\n")
    for r in rates:
        print(f'за {r["units"]} единиц(у) валюты{r["letter"]:>5} — {r["name"]} -  {r["rate"]} ₽')
except Exception as e:
    print(f"Ошибка парсинга: {e}")
input("\nНажмите Enter, чтобы выйти...")
