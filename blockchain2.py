import hashlib
import json
from time import time
import requests
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []
        self.new_block(previous_hash=1,proof=100)
    def new_block(self):
        pass
    def new_transaction(self):
        pass
    def hash(block):
        pass
    def last_block(self):
        pass 
def new_block(self,proof,previous_hash=None):
    #블록생성정보나오는거
    block = {
            'index': len(self.chain)+1,
            'timestamp': time(),
            'transactions': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
    }
    self.current_transaction = []
    self.chain.append(block)
    return block
def new_transaction(self,sender,recipient,amount):
    #거래정보나오는거
    self.current_transaction.append(
        {
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount
        }
    )
    return self.last_block['index']+1
def hash(block):
    block_string = json.dumps(block, sort_keys=True).encode
    return hashlib.sha256(block_string).hexdigest()
def proof_of_work(self, last_proof):
    proof=0
    while self.valid_proof(last_proof,proof)is False:
        proof+=1
    return proof
def valid_proof(last_proof,proof):
    guess = str(last_proof + proof).encode()
    guess_hash = hashlib.sha256(guess).hexigest()
    return guess_hash[:4] == "0000"
    #작업증명 << 수정가능 응응