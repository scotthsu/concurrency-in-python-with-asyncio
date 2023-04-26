import time
import requests


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


start = time.time()
results = [get_status_code('https://www.example.com') for _ in range(1000)]
end = time.time()
for result in results:
        print(result)
print(f'finished requests in {end - start:.4f} second(s)')
