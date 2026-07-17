def outer():
    def inner():
        global n
        n=20
        print("Inner",n)
    def inner2():
        print("Inner2", n)
    inner()
    inner2()
name="LL"
outer()