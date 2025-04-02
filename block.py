import json
import os
import hashlib



def get_blockchain_dir():
    return os.curdir + '/blocks/'

def get_sorted_files(blockchain_dir):
    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])
    return files

def get_hash(filename):
    blockchain_dir = get_blockchain_dir()
    file=open(blockchain_dir + filename,"rb").read()
    return hashlib.sha256(file).hexdigest()

def check_integrity():
    blockchain_dir = get_blockchain_dir()
    files=get_sorted_files(blockchain_dir)
    results=[]
    for file in files[1:]:
        h=json.load(open(blockchain_dir + str(file)))['hash']
        prev_file=str(file-1)
        actual_hash = get_hash(prev_file)
        if h==actual_hash:
            res='Ok'
        else:
            res='Corrupted'
        results.append({'block':prev_file,'result':res})
    return results

def write_block(name,amount,to_whom,prev_hash=''):
    blockchain_dir = get_blockchain_dir()
    blockchain_dir = get_blockchain_dir()
    files = get_sorted_files(blockchain_dir)

    prev_file=files[-1]
    filename=str(prev_file+1)

    data={'name':name,
          'amount':amount,
          'to_whom':to_whom,
          'hash':get_hash(str(prev_file))}
    with open(blockchain_dir+filename,'w') as file:
        json.dump(data,file,indent=4)


def main():
    # write_block(name="Alex",amount=78,to_whom="Milana")
    print(check_integrity())

if __name__=='__main__':
    main()