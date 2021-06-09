import hashlib
    
def making_hash(word):
        hashdata=hashlib.sha256(word.encode()).hexdigest()
        return hashdata
def proof_of_work(nounce,block):
    hashed_nounce=making_hash(nounce)
    hashed_block=making_hash(block)
    if hashed_nounce<hashed_block:
        True