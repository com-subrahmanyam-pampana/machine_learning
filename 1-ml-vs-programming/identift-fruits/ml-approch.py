# We don't write rules we provide examples

from sklearn.tree import DecisionTreeClassifier


# Features:[color_code,shape_code]
# red=0,yellow=1,round=0,long=1
X=[[0,0] ,#red,round->Apple
[1,1],#yellow,long->banana
[0,0],#red,round->apple
[1,1] # yellow,long->banana
]


Y=["Apple","Banana","Apple","Banana"] # labels

#Train model
model=DecisionTreeClassifier()
model.fit(X,Y)


#Predict a new fruit

new_fruit=[[0,0]]

print(model.predict(new_fruit))