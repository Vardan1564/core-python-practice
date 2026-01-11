def vip(vp):
    def mvip(*args,**kwargs):
        print("hollo good morning")
        vp(*args,**kwargs)
        print("thanks for use for my code")
    return mvip


@vip
def hello():
    print("HOW R U")

hello()
