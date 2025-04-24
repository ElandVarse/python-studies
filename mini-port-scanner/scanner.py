import socket

def scan_all_ports(host):
    print(f"\n[🔍] Escaneando {host} de 1 a 65535...\n")
    for port in range(1, 65536):
        sock = socket.socket()
        sock.settimeout(0.01)  # tempo curtíssimo pra acelerar
        try:
            sock.connect((host, port))
            print(f"[✅] Porta {port} ABERTA")
        except:
            pass
        finally:
            sock.close()

if __name__ == "__main__":
    alvo = input("Digite o host ou IP para escanear: ")
    scan_all_ports(alvo)
