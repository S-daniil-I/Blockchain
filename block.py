import json
import os

def write_block(name,amount,to_whom,prev_hash=''):
    blockchain_dir=os.curdir +'/blocks/'
    files =os.listdir(blockchain_dir)
    files=sorted([int(i) for i in files ] )

    last_file=files[-1]
    filename=str(last_file+1)

    data={'name':name,
          'amount':amount,
          'to_whom':to_whom,
          'hash':prev_hash,}
    with open(blockchain_dir+filename,'w') as file:
        json.dump(data,file,indent=4)


def main():
    write_block(name="Ivan",amount=100,to_whom="Daniil")



if __name__=='__main__':
    main()