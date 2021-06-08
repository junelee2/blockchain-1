# 블록을 만들어주는 클래스 
class block:
    def setdata(self, data, hash_, previoushash, time):
        self.data = data
        self.hash_ = hash_
        self.inprevioushashdex = previoushash
        self.time = time
        self.data = data

# 작업증명을 해주는 함수
def proof_of_work(hash,data):
    pass

# 블록을 연결해주는 함수
import datetime
def chaining_block(data, hash_, previoushash):
    currunt_block = block()
    currunt_block.setdata(data, hash_, previoushash, datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S'))
    return currunt_block

# 해시 만들어주는 함수
import hashlib
def making_hash(word):
    return hashlib.sha256(word.encode()).hexdigest()

if __name__ == '__main__':
    pass