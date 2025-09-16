from chains.chain_runner import run_chain

def chat():
    print("\n" + "-" * 50)
    print("\nAmeen is here as your personal banking assistant 🏦 (type q to quit).")

    while True:
        user_input = input("\nYOU: ").strip()
        if user_input.lower() == "q":
            print("\nAMEEN🛡️ : Hope I assisted you with everything you need today, goodbye.")
            break
        try:
            output = run_chain(user_input)
            print(f"\nAMEEN🛡️ : {output}")
        except Exception as e:
            print(f"\nAMEEN🛡️ : Sorry, something went wrong >>> ({e})")

if __name__ == "__main__":
    chat()