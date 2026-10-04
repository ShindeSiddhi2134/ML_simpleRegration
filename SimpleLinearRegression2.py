import numpy as np 
from sklearn.linear_model import LinearRegression

def main():
    X=np.array([[1],[2],[3],[4],[5]])

    Y=np.array([50,55,60,70])

    model=model.fit(X,Y)
    print(model.predict([[6]]))

    print("coefficient :",model.coef())
    print()
if __name__=="__main__":
    main()