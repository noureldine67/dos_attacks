# Outil d'attaque réseau éducatif

Cet outil est un script Python conçu à des fins éducatives pour démontrer les principes de deux types d'attaques réseau : **SYN Flood** et **Smurf**. Il vous permet de choisir l'attaque que vous souhaitez lancer en utilisant une interface en ligne de commande.

---

## Pré-requis

- Python 3.x
- Bibliothèques Python :
  - `scapy` : pour manipuler les paquets réseau
  - `colorama` : pour les couleurs dans le terminal

Installez les dépendances avec pip :

```bash
pip install scapy colorama
```

---

## Lancer l'outil

Le fichier `cli.py` vous permet de choisir l'attaque à effectuer et de spécifier les paramètres requis. Vous pouvez choisir entre les attaques `syn` et `smurf`.

```bash
python cli.py [-h] {syn,smurf} ...
```

### Arguments principaux

- **-h, --help** : Affiche l'aide pour l'outil.
- **{syn,smurf}** : Choisir le type d'attaque à lancer :
  - `syn` : Lance une attaque SYN Flood.
  - `smurf` : Lance une attaque Smurf.

---

## Attaque SYN Flood

### Description
L'attaque **SYN Flood** est une attaque de déni de service qui envoie de nombreuses requêtes SYN à une cible dans le but de saturer ses ressources et l'empêcher de répondre aux demandes légitimes.

### Arguments

```bash
python cli.py syn -h
```

#### Arguments pour `syn` :

- **target_ip** : Adresse IP de la cible (ex: 192.168.56.101)
- **target_port** : Port TCP de la cible (ex: 80 pour HTTP)
- **packet_count** : Nombre de paquets SYN à envoyer par thread.
- **thread_count** : Nombre de threads à utiliser pour l'attaque.

#### Exemple d'utilisation

```bash
python cli.py syn 192.168.1.100 80 500 4
```

Cela enverra **500 paquets** SYN par **4 threads** à la cible avec l'adresse IP **192.168.1.100** sur le port **80**.

---

## Attaque Smurf

### Description
L'attaque **Smurf** est un type d'attaque par amplification. Elle consiste à envoyer des paquets ICMP (ping) avec une adresse source falsifiée (spoofée) pointant vers la victime, mais envoyés à un réseau de broadcast pour que tous les hôtes du réseau répondent à la victime en même temps.

### Arguments

```bash
python cli.py smurf -h
```

#### Arguments pour `smurf` :

- **victim_ip** : Adresse IP de la victime (l'adresse à usurper).
- **broadcast_ip** : Adresse de broadcast du réseau cible.
- **packet_count** : Nombre de paquets ICMP à envoyer par thread.
- **thread_count** : Nombre de threads à utiliser pour l'attaque.

#### Exemple d'utilisation

```bash
python cli.py smurf 192.168.1.100 192.168.1.255 500 4
```

Cela enverra **500 paquets ICMP** par **4 threads**, spoofés depuis **192.168.1.100** vers l'adresse de broadcast **192.168.1.255**.

---

## Exemple complet

1. Pour lancer une **attaque SYN Flood** sur l'IP `192.168.1.100` sur le port `80`, avec **500 paquets** par thread et **4 threads** :

```bash
python cli.py syn 192.168.1.100 80 500 4
```

2. Pour lancer une **attaque Smurf** sur la victime `192.168.1.100` avec une adresse de broadcast `192.168.1.255`, en envoyant **500 paquets** par thread et **4 threads** :

```bash
python cli.py smurf 192.168.1.100 192.168.1.255 500 4
```

---

## Sécurité et éthique

**ATTENTION :** Ce script est destiné à des fins **éducatives seulement** et doit être utilisé dans un environnement contrôlé, tel qu'un réseau local ou un laboratoire de test. L'utilisation de ces attaques sur des réseaux ou des machines sans autorisation explicite est illégale et contraire à l'éthique.

---

## Remarque

L'utilisation abusive de cet outil peut entraîner des conséquences légales graves. Soyez toujours responsable et respectueux de la sécurité des réseaux et des systèmes des autres.
