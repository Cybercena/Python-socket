import socket
import threading
from queue import Queue

def port_scan(target_host, target_port, verbose=False):
    try:
        scanner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner_socket.settimeout(1)
        result = scanner_socket.connect_ex((target_host, target_port))
        scanner_socket.close()

        if result == 0:
            print(f"Port {target_port} is open")
            if verbose:
                try:
                    service = socket.getservbyport(target_port)
                    print(f"Service running on port {target_port}: {service}")
                except OSError:
                    print("Failed to identify service.")
        else:
            if verbose:
                print(f"Port {target_port} is closed")
    except Exception as e:
        if verbose:
            print(f"Error scanning port {target_port}: {str(e)}")

def port_scan_worker(target_host, ports, verbose, results):
    while not ports.empty():
        port = ports.get()
        port_scan(target_host, port, verbose)
        results.put(port)
        ports.task_done()

def main():
    target_host = input("Enter the target host IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    verbose = input("Enable verbose mode? (y/n): ").lower() == 'y'

    ports = Queue()
    results = Queue()

    for port in range(start_port, end_port + 1):
        ports.put(port)

    print(f"Scanning ports {start_port} to {end_port} on host {target_host}")
    num_threads = min(100, end_port - start_port + 1)  # Limiting the number of threads
    for _ in range(num_threads):
        worker = threading.Thread(target=port_scan_worker, args=(target_host, ports, verbose, results))
        worker.start()

    ports.join()
    while not results.empty():
        results.get()
        results.task_done()

    print("Scan complete.")

if __name__ == "__main__":
    main()
