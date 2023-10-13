import socket

def scan_ports(target, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error as e:
            print(f"Error scanning port {port}: {str(e)}")

    if open_ports:
        print("Portas abertas:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("Nenhuma porta aberta encontrada.")

if __name__ == "__main__":
    target_host = input("Digite o host alvo: ")
    target_ports = input("Digite as portas a serem verificadas (separadas por vírgulas ou 'TODAS' para escanear todas as portas): ")

    if target_ports.upper() == 'TODAS':
        ports = list(range(1, 65536))  # Escaneia todas as portas disponíveis
    else:
        ports = [int(p) for p in target_ports.split(',')]

    if not ports:
        print("Nenhuma porta válida fornecida. Encerrando o scanner.")
    else:
        try:
            socket.inet_aton(target_host)  # Verifica se o host é um endereço IP válido.
            scan_ports(target_host, ports)
        except socket.error:
            print("Host alvo inválido. Encerrando o scanner.")