from web3 import Web3
from solcx import compile_standard, install_solc
import json


ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))


print("Connected:", web3.is_connected())



wallet_address = "0x883e4CC617853dbAEfF69E599A1303F9329535Ac"

private_key = 0xb78c709f665b03ca34a7ed105aecefebfd04ba80d749fff1c4de7f531bd657d1


with open("contract.sol", "r") as file:

    contract_file = file.read()


install_solc("0.8.0")


compiled_sol = compile_standard(

    {

        "language": "Solidity",

        "sources": {

            "contract.sol": {

                "content": contract_file

            }

        },

        "settings": {

            "outputSelection": {

                "*": {

                    "*": [

                        "abi",

                        "metadata",

                        "evm.bytecode",

                        "evm.sourceMap"

                    ]

                }

            }

        },

    },

    solc_version="0.8.0",

)



with open("compiled_code.json", "w") as file:

    json.dump(compiled_sol, file)



bytecode = compiled_sol["contracts"]["contract.sol"]["DocumentVerification"]["evm"]["bytecode"]["object"]


abi = compiled_sol["contracts"]["contract.sol"]["DocumentVerification"]["abi"]



contract = web3.eth.contract(

    abi=abi,

    bytecode=bytecode

)



nonce = web3.eth.get_transaction_count(wallet_address)


transaction = contract.constructor().build_transaction(

    {

        "chainId": 1337,

        "gas": 2000000,

        "gasPrice": web3.to_wei("20", "gwei"),

        "nonce": nonce,

    }

)


signed_txn = web3.eth.account.sign_transaction(

    transaction,

    private_key=private_key

)



tx_hash = web3.eth.send_raw_transaction(

    signed_txn.raw_transaction

)



tx_receipt = web3.eth.wait_for_transaction_receipt(

    tx_hash

)

print("Contract deployed!")

print("Contract Address:", tx_receipt.contractAddress)