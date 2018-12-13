blockchain = [[1]]


def addValue(value):
    blockchain.append([blockchain[-1], value])
    print(blockchain)

addValue(3.1)
addValue(8.7)
addValue(5.0)
