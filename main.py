import socket
from lets_common_log import logUtils as log

def tcp(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    res = sock.connect_ex((ip, port))
    print("")
    if res == 0:
        log.info(f"TCP | HOST : {ip} - PORT : {port} >>> CONNECTED")
    else:
        log.warning(f"TCP | HOST : {ip} - PORT : {port} >>> NOT CONNECTED")

def udp(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    res = sock.connect_ex((ip, port))
    print("")
    if res == 0:
        log.info(f"UDP | HOST : {ip} - PORT : {port} >>> CONNECTED")
    else:
        log.warning(f"UDP | HOST : {ip} - PORT : {port} >>> NOT CONNECTED")

#TCP_or_UDP = input("\nChoose Protocol! \nTCP = 1 \nUDP = 2 \n")
TCP_or_UDP  = "1"
ip = input("\nIP Address : ")
port = int(input("PORT : "))

if TCP_or_UDP == "1" or TCP_or_UDP.upper() == "TCP":
    tcp(ip, port)
elif TCP_or_UDP == "2" or TCP_or_UDP.upper() == "UDP":
    #udp(ip, port)
    log.error("UDP Blocked")
else:
    log.error("ERROR")
