import pickle

def storedata():
    omkar = {'nickname':'omya','name':'omprakash mundkar','age':'27','vllge':'suntagi'}
    baswaraj = {'nickname':'shubham','name':'baswaraj mundkar','age': '29','vllage':'suntagi fata'}

    db = {}
    db['omkar']=omkar
    db['baswaraj']= baswaraj

    dbfile = open('examplepickle1','ab')
    pickle.dump(db,dbfile)
    dbfile.close()

def looaddata():
    dbfile = open('examplepickle1','rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys,db[keys])
    dbfile.close()

if  __name__=='__main__':
    storedata()
    looaddata()






storedata()

