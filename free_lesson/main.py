import os

from web3 import Web3

rpc = 'https://rpc.ankr.com/eth/'
# Подключение
web3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth/'))
# Или
web3_2 = Web3(Web3.HTTPProvider(endpoint_uri=rpc))


# получение параметров из блокчейна

print(f'gas price {web3.eth.gas_price} EHT')

print(f'current block number {web3.eth.block_number}')

print(f'number of current chain {web3.eth.chain_id}')

# проверка баланса

private_key = Web3.to_hex(os.urandom(32)) # Генерация приватника
print(private_key)
address = web3.eth.account.from_key(private_key=private_key).address # Получение адреса из приватника
pr_key = web3.eth.account.from_key(private_key=private_key)._private_key.hex()
print(address)
checksum_address = Web3.to_checksum_address(address)
balance = web3.eth.get_balance(checksum_address)
print(balance)
ether_balance = Web3.from_wei(balance, 'ether')
print(ether_balance)
wei_balance = Web3.to_wei(ether_balance, 'wei')
print(ether_balance)


