from sklearn import  tree

Features=[[35,'Rough'],[47,'Rough'],[90,'Smooth'],[48,'Rough'],[90,'Smooth'],[35,'Rough'],[92,'Smooth'],[35,'Rough'],[35,'Rough'],[35,'Rough'],[96,'Smooth'],[43,'Rough'],[110,'Smooth'],[35,'Rough'],[95,'Smooth'],]
Lables=['Tennis','Tennis','Cricket','Tennis','Cricket','Tennis','Cricket','Tennis','Tennis','Tennis','Cricket','Tennis','Cricket','Tennis','Cricket']

obj=tree.DecisionTreeClassifier()
obj=obj.fit(Features,Lables)
print(obj.predict([[97,'Smooth']]))

