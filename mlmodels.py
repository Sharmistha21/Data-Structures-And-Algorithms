from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris=load_iris()

x=iris.data
y=iris.target

feature_names=iris.feature_names
target_names=iris.target_names

print("Feature names:",feature_names)
print("Target names:",target_names)

print("\nType of X is:", type(x))
print("\nFirst 5 rows of X:",x[:5])

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=1)
print("X train shape:",X_train.shape)
print("X test shape:",X_test.shape)
print("y train shape:",y_train.shape)
print("y test shape:",y_test.shape)
