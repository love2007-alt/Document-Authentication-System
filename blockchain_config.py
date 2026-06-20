from web3 import Web3
import json

# Connect to Ganache

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

# Load compiled contract

with open("compiled_code.json", "r") as file:

    compiled_sol = json.load(file)

# ABI

abi = compiled_sol["contracts"]["contract.sol"]["DocumentVerification"]["abi"]

# Contract Address

contract_address = "0x214396e54DCa3787233A10d38B5cd09be1DF7979"

# Connect contract

contract = web3.eth.contract(

    address=contract_address,

    abi=abi

)