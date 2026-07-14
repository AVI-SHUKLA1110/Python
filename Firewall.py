import random;

# defining a function to generate a random ip address 
#function to check if the ip address belongs to our set blocked ip addresses or not
#simulating network traffic by generating random ip addresses and checking if they are blocked or not

def generate_random_ip():
    return f"192.168.1.{random.randint(1, 254)}"

def is_ip_blocked(ip ,rules):
  for rule_ip, action in rules.items():
    if ip == rule_ip:
      return action
  return "allow"

def main():
    # defining a set of blocked ip addresses
    blocked_ips = {
        "192.168.1.1": "block",
        "192.168.1.3": "block",
        "192.168.1.7": "block"
    }

    # simulating network traffic    
    for _ in range(10):
        ip = generate_random_ip()
        action = is_ip_blocked(ip, blocked_ips)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip}, Action: {action}")
        print(f"Random Number: {random_number}")

if __name__ == "__main__":
    main()

