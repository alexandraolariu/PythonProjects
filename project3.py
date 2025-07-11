import subprocess
import platform
import socket
import time


MONITOR_INTERVAL_SECONDS = 10 # Check every 10 seconds

# List of hosts and their ports to monitor
TARGETS_TO_MONITOR = [
    {
        "name": "Google DNS",
        "ip": "8.8.8.8",
        "ports": [53] # Standard DNS port
    },
    {
        "name": "Example Web Server",
        "ip": "example.com",
        "ports": [80, 443] # HTTP and HTTPS ports
    },
    {
        "name": "Localhost SSH (if running)",
        "ip": "127.0.0.1",
        "ports": [22] # Standard SSH port
    },
    {
        "name": "Non-existent Host (expect failure)",
        "ip": "192.0.2.1", # Reserved for documentation, unlikely to exist
        "ports": [80]
    }
]

# --- Functions for Network Checks ---

# Pings a host once and returns True if reachable, False otherwise.
def ping_host(host):

    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', str(host)]

    try:
        # 0 usually means success, non-zero means failure
        result = subprocess.run(command, capture_output=True, text=True, timeout=2)
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False
    except Exception as e:
        print(f"Error pinging {host}: {e}")
        return False

#Checks if TCP port is open
def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # 1-second timeout for connection
        result = sock.connect_ex((str(host), int(port))) # connect_ex returns 0 on success
        sock.close()
        return result == 0
    except Exception as e:
        print(f"Error checking port {port} on {host}: {e}")
        return False

def start_simple_monitoring():
    print(f"--- Starting Simple Network Monitor (checking every {MONITOR_INTERVAL_SECONDS} seconds) ---")

    while True:
        print("\n--- New Monitoring Cycle ---")
        for target in TARGETS_TO_MONITOR:
            name = target["name"]
            ip = target["ip"]
            ports = target["ports"]

            print(f"  Checking {name} ({ip})...")

            # 1. Ping the host
            if ping_host(ip):
                print(f"    🟢 {name} is REACHABLE.")
                # 2. If reachable, check specified ports
                for port in ports:
                    if check_port(ip, port):
                        print(f"      ✅ Port {port} is OPEN.")
                    else:
                        print(f"      ❌ Port {port} is CLOSED or UNREACHABLE.")
            else:
                print(f"    🔴 {name} is UNREACHABLE.")

                for port in ports:
                    print(f"      (Skipping Port {port} check as host is down.)")

        print(f"\nMonitoring cycle complete. Waiting {MONITOR_INTERVAL_SECONDS} seconds...")
        time.sleep(MONITOR_INTERVAL_SECONDS)

# --- Run the monitor ---
if __name__ == "__main__":
    start_simple_monitoring()