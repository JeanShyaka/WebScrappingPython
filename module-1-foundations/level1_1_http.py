import requests
from requests.exceptions import RequestException, Timeout

# High-availability target platform for scraping practice
URL = "http://books.toscrape.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def run_http_lab():
    print("[*] Sending Masked HTTP GET Request to stable target...")
    
    try:
        # Send GET request with a 10-second connection timeout
        response = requests.get(URL, headers=HEADERS, timeout=10)
        
        # Check status code
        print(f"[+] HTTP Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("[+] Connection Successful!")
            print(f"[+] Server Response Length: {len(response.text)} bytes")
            print(f"[+] Server Content-Type: {response.headers.get('Content-Type')}")
        else:
            print(f"[-] Server returned unexpected status: {response.status_code}")

    except Timeout:
        print("[-] Error: Request timed out. The server took too long to respond.")
    except RequestException as e:
        print(f"[-] Network Error encountered: {e}")

if __name__ == "__main__":
    run_http_lab()