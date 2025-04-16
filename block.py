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
    files = get_sorted_files(blockchain_dir)
    results = []
    corruption_detected = False

    for i in range(1, len(files)):
        current_file = str(files[i])
        previous_file = str(files[i - 1])

        with open(blockchain_dir + current_file) as f:
            current_data = json.load(f)

        actual_prev_hash = get_hash(previous_file)

        if corruption_detected or current_data['hash'] != actual_prev_hash:
            res = 'Corrupted'
            corruption_detected = True
        else:
            res = 'Everything is fine. No changes. 😊'

        results.append({'block': previous_file, 'result': res})

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