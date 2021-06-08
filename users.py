chain = []
# 블록을 만들어주는 클래스 
# 만들고 보니까 걍 튜플 이나 딕셔너리 형식으로 만드는게 더 나을거같음 
class block:
    def setdata(self, data, hash_, previoushash, time):
        self.data = data
        self.hash_ = hash_
        self.previoushash = previoushash
        self.time = time

# 작업증명을 해주는 함수
def proof_of_work(hash,data):
    pass

# 블록을 만들어주는 함수
import datetime
def chaining_block(data, hash_, previoushash):
    currunt_block = block()
    currunt_block.setdata(data, hash_, previoushash, datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S'))
    return currunt_block

# 해시 만들어주는 함수
import hashlib
def making_hash(word):
    return hashlib.sha256(word.encode()).hexdigest()
# word넣으면 해시 나옴 

if __name__ == '__main__':
    # if proof_of_work() == True:
    data = 'data'
    prehash = 'prehash'
    nowhash =  making_hash(data+prehash)
    block = chaining_block(data, prehash, nowhash)
    output = '%s%s%s%s'%(block.hash_, block.previoushash, block.data, block.time)
    chain.append(output)

