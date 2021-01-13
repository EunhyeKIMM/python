import pickle

def save(fpath, data):
    with open(fpath, 'wb') as f:
        pickle.dump(f, data)