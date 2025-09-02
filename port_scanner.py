import socket

def scan_host(host, ports):
    print(f"Scanning {host}...")
    open_ports = []
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            s.connect((host, port))
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
            s.close()
        except:
            pass
    return open_ports

if __name__ == "__main__":
    target = input("Enter target host (IP): ")
    ports = range(20, 1025)  # Common ports
    results = scan_host(target, ports)
    with open("sample_report.txt", "a") as f:
        f.write(f"Open ports on {target}: {results}\n")
