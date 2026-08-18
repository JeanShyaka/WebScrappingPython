import requests
from requests.exceptions import RequestException, Timeout

# Stable target site
URL = "http://books.toscrape.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def inspect_http_response():
    print("[*] Module 1.2: Inspecting HTTP Response Metadata...")
    
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        
        # 1. Evaluate Status Code
        print(f"[+] Response Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("[+] Status 200 OK: Target server accessible.")
            
            # 2. Inspect Server Response Headers
            content_type = response.headers.get("Content-Type", "")
            server_type = response.headers.get("Server", "Unknown")
            
            print(f"[+] Header Content-Type: {content_type}")
            print(f"[+] Header Server:       {server_type}")
            
            if "text/html" in content_type:
                print("[+] HTML payload verified. Ready for DOM parsing.")
            else:
                print("[-] Non-HTML payload received.")
                
        elif response.status_code == 403:
            print("[-] Status 403 Forbidden: Request flagged by anti-bot firewall.")
        elif response.status_code == 429:
            print("[-] Status 429 Rate Limit: Too many requests sent in short interval.")
        else:
            print(f"[-] Received unexpected HTTP status: {response.status_code}")

    except Timeout:
        print("[-] Error: Connection timed out.")
    except RequestException as err:
        print(f"[-] Network Exception: {err}")

if __name__ == "__main__":
    inspect_http_response()