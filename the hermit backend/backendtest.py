from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pickle
knn = KNeighborsClassifier(n_neighbors=2)
X_train = [
[84, 77, 80, 83, 83, 94, 94, 94, 88, 81, 67, 77, 88, 93, 97, 97, 97, 78, 69, 69, 63, 64, 57, 57, 57, 56, 66, 70] ,
[44, 70, 77, 77, 93, 69, 83, 88, 80, 100, 81, 87, 100, 83, 100, 91, 94, 94, 84, 90, 75, 77, 66, 74, 78, 84, 90, 88] ,
[91, 78, 63, 51, 53, 64, 57, 56, 67, 63, 83, 81, 44, 43, 27, 44, 56, 54, 51, 51, 57, 74, 77, 63, 69, 64, 75, 96] ,
[78, 70, 50, 50, 50, 50, 50, 57, 66, 54, 63, 67, 40, 61, 63, 63, 94, 90, 90, 90, 88, 94, 94, 69, 69, 69, 77, 78] ,
[63, 64, 51, 53, 43, 34, 29, 35, 38, 47, 43, 38, 43, 29, 35, 35, 24, 38, 47, 43, 48, 53, 50, 60, 57, 51, 37, 37] ,
[61, 67, 48, 50, 50, 48, 51, 35, 35, 35, 35, 35, 48, 61, 63, 63, 63, 75, 64, 54, 54, 54, 60, 53, 56, 56, 56, 56] ,
[50, 44, 40, 37, 41, 37, 48, 48, 66, 60, 57, 61, 51, 35, 27, 17, 8, 35, 44, 44, 40, 53, 56, 57, 78, 84, 63, 66] ,
[48, 48, 47, 44, 50, 48, 44, 37, 34, 24, 27, 37, 30, 43, 41, 40, 34, 29, 29, 29, 34, 41, 57, 43, 40, 43, 35, 48] ,
[96, 100, 94, 100, 91, 84, 81, 66, 57, 57, 44, 53, 53, 53, 53, 54, 43, 47, 37, 37, 41, 41, 41, 50, 48, 48, 47, 53] ,
[63, 63, 53, 53, 51, 53, 77, 90, 77, 66, 50, 48, 61, 67, 78, 77, 81, 90, 83, 80, 66, 57, 57, 50, 69, 75, 77, 78] ,
[63, 69, 43, 14, 41, 26, 34, 56, 47, 47, 35, 26, 16, 10, 26, 26, 21, 23, 16, 14, 30, 21, 35, 41, 41, 41, 24, 24] ,
[10, 14, 26, 14, 14, 20, 34, 41, 67, 67, 60, 56, 44, 48, 37, 47, 35, 29, 41, 50, 57, 61, 48, 43, 44, 41, 41, 26] ,
[69, 75, 63, 54, 75, 88, 87, 91, 69, 35, 53, 54, 67, 97, 90, 100, 100, 100, 100, 100, 84, 74, 61, 56, 63, 84, 84, 83] ,
[84, 57, 67, 44, 61, 63, 51, 40, 27, 29, 24, 41, 53, 37, 21, 40, 29, 56, 69, 44, 47, 56, 64, 61, 61, 61, 53, 44] ,
[44, 48, 69, 74, 54, 54, 57, 43, 54, 70, 74, 75, 91, 63, 44, 35, 4, 13, 29, 37, 41, 29, 13, 17, 10, 29, 40, 57] ,
[54, 17, 23, 44, 47, 74, 56, 37, 35, 37, 54, 78, 70, 70, 70, 54, 64, 43, 26, 35, 35, 43, 54, 63, 81, 54, 78, 78] ,
[66, 78, 88, 69, 75, 75, 56, 70, 84, 67, 70, 63, 43, 41, 53, 64, 77, 64, 69, 51, 60, 67, 53, 60, 67, 74, 61, 66] ,
[30, 37, 63, 84, 66, 83, 83, 87, 100, 100, 100, 96, 88, 75, 48, 56, 56, 50, 34, 37, 37, 37, 37, 43, 43, 43, 43, 50] ,
[53, 56, 69, 66, 69, 61, 50, 61, 75, 77, 81, 94, 80, 78, 87, 80, 80, 87, 77, 78, 77, 84, 93, 90, 97, 83, 80, 78] ,
[50, 53, 53, 51, 47, 40, 35, 40, 38, 48, 57, 54, 63, 50, 43, 53, 57, 74, 70, 69, 60, 48, 47, 40, 40, 48, 48, 51] ,
[77, 100, 100, 94, 84, 83, 83, 81, 81, 78, 78, 69, 69, 69, 69, 87, 87, 87, 81, 100, 94, 100, 100, 90, 78, 80, 84, 87] ,
[3, 1, 3, 41, 13, 23, 47, 29, 29, 29, 41, 30, 26, 40, 21, 26, 48, 47, 57, 51, 29, 27, 34, 37, 37, 29, 27, 27] ,
[69, 64, 64, 53, 53, 51, 57, 57, 44, 44, 50, 60, 64, 63, 67, 47, 43, 50, 51, 51, 69, 56, 35, 40, 48, 56, 67, 56] ,
[26, 27, 41, 66, 94, 100, 75, 47, 24, 20, 23, 26, 38, 50, 60, 63, 63, 78, 91, 100, 94, 80, 40, 17, 43, 23, 57, 67] ,
[24, 24, 48, 50, 47, 50, 41, 35, 41, 27, 26, 23, 16, 21, 30, 37, 38, 41, 24, 37, 41, 41, 51, 37, 23, 23, 11, 20] ,
[74, 53, 63, 69, 84, 84, 67, 66, 69, 57, 57, 63, 48, 61, 56, 51, 27, 20, 35, 34, 44, 70, 54, 47, 63, 48, 53, 43]
]
Y_train =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
knn.fit(X_train , Y_train)
print(knn.predict([
[84, 77, 80, 83, 83, 94, 94, 94, 88, 81, 67, 77, 88, 93, 97, 97, 97, 78, 69, 69, 63, 64, 57, 57, 57, 56, 66, 70] ,
[44, 70, 77, 77, 93, 69, 83, 88, 80, 100, 81, 87, 100, 83, 100, 91, 94, 94, 84, 90, 75, 77, 66, 74, 78, 84, 90, 88] ,
[91, 78, 63, 51, 53, 64, 57, 56, 67, 63, 83, 81, 44, 43, 27, 44, 56, 54, 51, 51, 57, 74, 77, 63, 69, 64, 75, 96] ,
[78, 70, 50, 50, 50, 50, 50, 57, 66, 54, 63, 67, 40, 61, 63, 63, 94, 90, 90, 90, 88, 94, 94, 69, 69, 69, 77, 78] ,
[63, 64, 51, 53, 43, 34, 29, 35, 38, 47, 43, 38, 43, 29, 35, 35, 24, 38, 47, 43, 48, 53, 50, 60, 57, 51, 37, 37] ,
[61, 67, 48, 50, 50, 48, 51, 35, 35, 35, 35, 35, 48, 61, 63, 63, 63, 75, 64, 54, 54, 54, 60, 53, 56, 56, 56, 56] ,
[50, 44, 40, 37, 41, 37, 48, 48, 66, 60, 57, 61, 51, 35, 27, 17, 8, 35, 44, 44, 40, 53, 56, 57, 78, 84, 63, 66] ,
[48, 48, 47, 44, 50, 48, 44, 37, 34, 24, 27, 37, 30, 43, 41, 40, 34, 29, 29, 29, 34, 41, 57, 43, 40, 43, 35, 48] ,
[96, 100, 94, 100, 91, 84, 81, 66, 57, 57, 44, 53, 53, 53, 53, 54, 43, 47, 37, 37, 41, 41, 41, 50, 48, 48, 47, 53] ,
[63, 63, 53, 53, 51, 53, 77, 90, 77, 66, 50, 48, 61, 67, 78, 77, 81, 90, 83, 80, 66, 57, 57, 50, 69, 75, 77, 78] ,
[63, 69, 43, 14, 41, 26, 34, 56, 47, 47, 35, 26, 16, 10, 26, 26, 21, 23, 16, 14, 30, 21, 35, 41, 41, 41, 24, 24] ,
[10, 14, 26, 14, 14, 20, 34, 41, 67, 67, 60, 56, 44, 48, 37, 47, 35, 29, 41, 50, 57, 61, 48, 43, 44, 41, 41, 26] ,
[69, 75, 63, 54, 75, 88, 87, 91, 69, 35, 53, 54, 67, 97, 90, 100, 100, 100, 100, 100, 84, 74, 61, 56, 63, 84, 84, 83] ,
[84, 57, 67, 44, 61, 63, 51, 40, 27, 29, 24, 41, 53, 37, 21, 40, 29, 56, 69, 44, 47, 56, 64, 61, 61, 61, 53, 44] ,
[44, 48, 69, 74, 54, 54, 57, 43, 54, 70, 74, 75, 91, 63, 44, 35, 4, 13, 29, 37, 41, 29, 13, 17, 10, 29, 40, 57] ,
[54, 17, 23, 44, 47, 74, 56, 37, 35, 37, 54, 78, 70, 70, 70, 54, 64, 43, 26, 35, 35, 43, 54, 63, 81, 54, 78, 78] ,
[66, 78, 88, 69, 75, 75, 56, 70, 84, 67, 70, 63, 43, 41, 53, 64, 77, 64, 69, 51, 60, 67, 53, 60, 67, 74, 61, 66] ,
[30, 37, 63, 84, 66, 83, 83, 87, 100, 100, 100, 96, 88, 75, 48, 56, 56, 50, 34, 37, 37, 37, 37, 43, 43, 43, 43, 50] ,
[53, 56, 69, 66, 69, 61, 50, 61, 75, 77, 81, 94, 80, 78, 87, 80, 80, 87, 77, 78, 77, 84, 93, 90, 97, 83, 80, 78] ,
[50, 53, 53, 51, 47, 40, 35, 40, 38, 48, 57, 54, 63, 50, 43, 53, 57, 74, 70, 69, 60, 48, 47, 40, 40, 48, 48, 51] ,
[77, 100, 100, 94, 84, 83, 83, 81, 81, 78, 78, 69, 69, 69, 69, 87, 87, 87, 81, 100, 94, 100, 100, 90, 78, 80, 84, 87] ,
[3, 1, 3, 41, 13, 23, 47, 29, 29, 29, 41, 30, 26, 40, 21, 26, 48, 47, 57, 51, 29, 27, 34, 37, 37, 29, 27, 27] ,
[69, 64, 64, 53, 53, 51, 57, 57, 44, 44, 50, 60, 64, 63, 67, 47, 43, 50, 51, 51, 69, 56, 35, 40, 48, 56, 67, 56] ,
[26, 27, 41, 66, 94, 100, 75, 47, 24, 20, 23, 26, 38, 50, 60, 63, 63, 78, 91, 100, 94, 80, 40, 17, 43, 23, 57, 67] ,
[24, 24, 48, 50, 47, 50, 41, 35, 41, 27, 26, 23, 16, 21, 30, 37, 38, 41, 24, 37, 41, 41, 51, 37, 23, 23, 11, 20] ,
[74, 53, 63, 69, 84, 84, 67, 66, 69, 57, 57, 63, 48, 61, 56, 51, 27, 20, 35, 34, 44, 70, 54, 47, 63, 48, 53, 43]
]))
y_pred = [1 ,1 ,1 ,1, 1, 1, 1, 1, 0, 1 ,1 ,1 ,1 ,1 ,1, 1, 1, 0, 1 ,1 ,1 ,0 ,1 ,1 ,0 ,0]
print(accuracy_score(Y_train, y_pred))

filename = 'finalized_model.sav'
pickle.dump(knn, open(filename, 'wb'))