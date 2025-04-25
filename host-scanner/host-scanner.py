import subprocess
import ipaddress
import platform

# Verifica o sistema operacional
param = '-n' if platform.system().lower() == 'windows' else '-c'

# Define a rede a ser escaneada
rede = ipaddress.ip_network('192.168.0.0/24', strict=False)

print("Escaneando hosts ativos na rede...")

# Laço para pingar todos os IPs na rede
for ip in rede.hosts():
    ip = str(ip)
    comando = ['ping', param, '1', ip]

    try:
        output = subprocess.check_output(comando, stderr=subprocess.DEVNULL, universal_newlines=True)
        print(f"[+] Host ativo: {ip}")
    except subprocess.CalledProcessError:
        pass  # Ignora os hosts que não responderem

print("Escaneamento finalizado!")
