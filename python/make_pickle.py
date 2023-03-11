import pickle

def save_to_pickle(path, filename):
    open_file = open(path, "wb")
    pickle.dump(filename, open_file)
    open_file.close()

def load_from_pickle(path):
    open_file = open(path, "rb")
    loaded_list = pickle.load(open_file)
    open_file.close()
    return loaded_list
