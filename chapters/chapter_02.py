blockchain = [[1]]


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(value):
    blockchain.append([get_last_blockchain_value(), value])


tx_amount = float(input('Your transaction amount please: '))
add_value(tx_amount)

tx_amount = float(input('Your transaction amount please: '))
add_value(tx_amount)

tx_amount = float(input('Your transaction amount please: '))
add_value(tx_amount)

print(blockchain)
