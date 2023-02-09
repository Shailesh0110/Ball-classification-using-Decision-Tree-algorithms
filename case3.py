from sklearn import  tree

#rough=1
#smoth=0

#Tennis=1
#Cricket=2

def Ballpredictior(weight,surface):

    Features=[[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0],]
    Lables=[1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    obj=tree.DecisionTreeClassifier()
    obj=obj.fit(Features,Lables)
    ret=(obj.predict([[weight,surface]]))
    if ret== 1:
        print("your obj looks like Tennis ball")
    else:
        print("your obj looks like Cricket ball")


def main():
    print("-----------Ball predicatior case study--------------")
    print("plese enter the weight of your obj in grams")
    weight=int(input())
    print("plese enter the type of Surface your obj in (Smooth/rough)")
    surface = (input())
    if surface.lower()=='rough':
        surface=1
    elif surface.lower()=='smooth':
        surface=0
    else:
        print("invalide tye of surface")
        exit()

    Ballpredictior(weight,surface)


if __name__ == '__main__':
    main()
