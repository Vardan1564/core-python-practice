def v(vip):

    def mvip():
        print("++++|HI|+++++++++++")
        vip()
        print("++good byyy++")
    return mvip

@v
def i():
    print("hii how r u")   


i()