version="2.0.0"
from lets_common_log import logUtils as log
import socket
import requests
import traceback
import threading
import time

try:
    newVersion = requests.get("https://raw.githubusercontent.com/skchqhdpdy/port/main/main.py").text.split("\n")[0]
    if version != newVersion:
        log.warning(f"업데이트 있음!\n현재버전 : {version}\n최신버전 : {newVersion}")
        log.chat("https://github.com/skchqhdpdy/port")
        if input("Press Enter to exit...") != "ignore":
            exit()
except Exception as e:
    log.warning(e)
    log.error(f"\n{traceback.format_exc()}")
    log.warning("버전확인 실패!!")
    log.chat("https://github.com/skchqhdpdy/port/issues")

def tcp(ip, port, scan=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = sock.connect_ex((ip, port))
    if res == 0:
        log.info(f"TCP | HOST : {ip} - PORT : {port} >>> CONNECTED")
        with open("TCP-scan-list.txt", "a") as f:
            f.write(f"TCP | HOST : {ip} - PORT : {port} >>> CONNECTED\n")
    elif not scan:
        log.warning(f"TCP | HOST : {ip} - PORT : {port} >>> NOT CONNECTED")

def udp(ip, port, scan=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    res = sock.connect_ex((ip, port))
    if res == 0:
        log.info(f"UDP | HOST : {ip} - PORT : {port} >>> CONNECTED")
        with open("UDP-scan-list.txt", "a") as f:
            f.write(f"UDP | HOST : {ip} - PORT : {port} >>> CONNECTED\n")
    elif not scan:
        log.warning(f"UDP | HOST : {ip} - PORT : {port} >>> NOT CONNECTED")

while True:
    #TCP_or_UDP = input("\nChoose Protocol! \nTCP = 1 \nUDP = 2 \n")
    TCP_or_UDP  = "1"
    ip = input("\nIP Address : ")
    port = input("PORT : ")
    port = int(port) if port.lower() != "scan" else list(range(65536))
    print("")
    st = time.time()

    if type(port) == int:
        if TCP_or_UDP == "1" or TCP_or_UDP.upper() == "TCP":
            tcp(ip, port)
        elif TCP_or_UDP == "2" or TCP_or_UDP.upper() == "UDP":
            #udp(ip, port)
            log.error("UDP Blocked")
        else:
            log.error("ERROR")
    elif type(port) == list:
        if TCP_or_UDP == "1" or TCP_or_UDP.upper() == "TCP":
            tt = tcp
        elif TCP_or_UDP == "2" or TCP_or_UDP.upper() == "UDP":
            tt = udp
            log.error("UDP Blocked")
        else:
            tt = None
            log.error("ERROR")

        threads = []
        for p in port:
            thread = threading.Thread(target=tt, args=(ip, p, True))
            threads.append(thread)
            thread.start()
        # 모든 스레드의 작업이 완료될 때까지 대기
        for thread in threads:
            thread.join()

    log.chat(f"{time.time() - st} Sec")
    if input("Press exit to EXIT...").lower() == "exit":
        break