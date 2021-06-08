import random
chain = {}

class block:
    def setdata(self, data, hash_, previoushash, time):
        self.data = data
        self.hash_ = hash_
        self.inprevioushashdex = previoushash
        self.time = time
        self.data = data

import datetime
def Making_node(data, hash_, previoushash):
    time = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    currunt_block = block()
    currunt_block.setdata(data, hash_, previoushash, time)
    return currunt_block

if __name__ == '__main__':
    data = 'data'
    hashdata = 'hashdata'
    prehash = 'prehash'
    print(Making_node(data, hashdata, prehash))