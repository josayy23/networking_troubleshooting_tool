from network_utils import ping_host, traceroute, get_network_config

def main():
    print("Network Troubleshooting Tool")

    while True:
        print("\nOptions:")
        print("1. Ping a host")
        print("2. Traceroute a host")
        print("3. Display network configuration")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            host = input("Enter host to ping: ")
            print(ping_host(host))
        elif choice == "2":
            host = input("Enter host to traceroute: ")
            print(traceroute(host))
        elif choice == "3":
            print(get_network_config())
        elif choice == "4":
            break
        else:
            print("Invalid option")
            print("Try again")

    if __name__ == "__main__":
        main()

