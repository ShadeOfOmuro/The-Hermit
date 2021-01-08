import pickle
filename = 'model_dump_save/att_model.sav'
knn = pickle.load(open(filename, 'rb'))
def predict(data) :
    return knn.predict(data)[0]
