# 블록을 만들어주는 클래스 
# 만들고 보니까 걍 튜플 이나 딕셔너리 형식으로 만드는게 더 나을거같음 
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
    # 블록 만들기
    currunt_block = block()
    currunt_block.setdata(data, hash_, previoushash, datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S'))
    # 블록 연결 안썼음

# 해시 만들어주는 함수
import hashlib
def making_hash(word):
    return hashlib.sha256(word.encode()).hexdigest()
# word넣으면 해시 나옴 

if __name__ == '__main__':
    # 여기다 실행할거 쓰면댐
    pass