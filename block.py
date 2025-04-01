import json
def write_block(name,amount,to_whom,prev_hash=''):
    data={'name':name,
          'amount':amount,
          'to_whom':to_whom,
          'hash':prev_hash,}
    with open("test",'w') as file:
        json.dump(data,file,indent=4)


def main():
    write_block(name="Ivan",amount=100,to_whom="Ihar")



if __name__=='__main__':
    main()