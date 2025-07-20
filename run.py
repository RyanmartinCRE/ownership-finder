from superagent import Agent
import sys

def main():
    # Allow CLI address or interactive prompt
    address = sys.argv[1] if len(sys.argv) > 1 else input("Address: ")
    result = Agent.from_file("flows/ownership.yaml").run(address=address)
    print(result)

if __name__ == "__main__":
    main()
