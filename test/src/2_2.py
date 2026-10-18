
import requests

input_file = "link.txt"
output_file = "report.txt"
TIMEOUT = 10

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/150.0.0.0 Safari/537.36 YaBrowser/26.8.0.0"
    )
    }
def check_url(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        if 200 <= response.status_code < 400:
            return "Ok"
        return "Error"
    except requests.RequestException:
        return "Error"


with open(input_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

with open(output_file, "w", encoding="utf-8") as f:
    for url in urls:
        status = check_url(url)
        f.write(f"{url} -> {status}\n")
        print(f"{url} -> {status}")

print(f"\nРезультат сохранён в {output_file}")
