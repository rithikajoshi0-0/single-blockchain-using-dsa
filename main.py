import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return f"Block {self.index} [Hash: {self.hash}]"
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # First block in the chain (Genesis Block)
        return Block(0, str(datetime.datetime.now()), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), str(datetime.datetime.now()), new_data, latest_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True
if __name__ == "__main__":
    my_chain = Blockchain()

    # Add some blocks
    my_chain.add_block("First transaction: Alice pays Bob 10 BTC")
    my_chain.add_block("Second transaction: Bob pays Charlie 5 BTC")

    # Print the blockchain
    for block in my_chain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print(f"Prev Hash: {block.previous_hash}\n")

    # Check if valid
    print("Blockchain valid?", my_chain.is_chain_valid())

