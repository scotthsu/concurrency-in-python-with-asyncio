import time
import requests
from threading import Thread

def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


start = time.time()
threads = []
for _ in range(1000):
    thread = Thread(target=get_status_code, args=['https://www.example.com'])
    threads.append(thread)
    thread.start()

for thread in threads:
     thread.join()

end = time.time()
print(f'finished requests in {end - start:.4f} second(s)')
