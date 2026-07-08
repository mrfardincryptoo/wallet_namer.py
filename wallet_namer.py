# Simple tool to generate safe user aliases for testnet addresses
def generate_wallet_alias(address, username):
    if not address.startswith("0x") or len(address) < 10:
        return "Invalid Address"
    
    short_addr = f"{address[:5]}...{address[-3:]}"
    return f"{username} ({short_addr})"

user_wallet = "0x95222290DD7278Aa3Dddd389Cc1E1d165CC4BAfe"
display_name = generate_wallet_alias(user_wallet, "Fardin_Tester")

print(f"Profile Destination Display: {display_name}")
