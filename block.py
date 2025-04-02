import json
import os
import hashlib

def get_hash(filename):
    blockchain_dir = os.curdir + '/blocks/'
    file=open(blockchain_dir + filename,"rb").read()
    return hashlib.sha256(file).hexdigest()

def write_block(name,amount,to_whom,prev_hash=''):
    blockchain_dir=os.curdir +'/blocks/'
    files =os.listdir(blockchain_dir)
    files=sorted([int(i) for i in files ] )

    last_file=files[-1]
    filename=str(last_file+1)

    data={'name':name,
          'amount':amount,
          'to_whom':to_whom,
          'hash':get_hash(str(last_file))}
    with open(blockchain_dir+filename,'w') as file:
        json.dump(data,file,indent=4)


def main():
    write_block(name="Alex",amount=78,to_whom="Milana")



if __name__=='__main__':
    main()