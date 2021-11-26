class Person:
    apples = 0
    ideas = 0


X = Person()
X.apples = 7
Y = Person()
Y.apples = 2


def Print_apple(you, me):
    store = 0
    store = you.apples
    you.apples = me.apples
    me.apples = store
    return (you.apples, me.apples)


Print_apple(Y, X)
print("X= {}, Y = {}".format(X.apples, Y.apples))
