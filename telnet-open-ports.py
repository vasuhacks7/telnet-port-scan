import telnetlib
import sys

def check_all_ports(ip):

    for port in range(1, 65535):
        try:
            connection = telnetlib.Telnet(ip, port, timeout=1)
            print(f"Port {port} is open on {ip}")

            connection.close()

        except Exception as e:
        
            pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <target_ip>")
        sys.exit(1)

    target_ip = sys.argv[1]

    check_all_ports(target_ip)
    