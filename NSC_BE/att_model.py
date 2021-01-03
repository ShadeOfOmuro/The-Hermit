import pickle
filename = 'Beta/NSC_BE/model_dump_save/att_model.sav'
knn = pickle.load(open(filename, 'rb'))
def predict(data) :
    return knn.predict(data)[0]
