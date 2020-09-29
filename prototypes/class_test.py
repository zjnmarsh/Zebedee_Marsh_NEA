class hello:
    def __init__(self):
        print("hello")
        print(self.hello.var)


class bye:
    def __init__(self, in):
        print(in)
        hello.var = "assigned outside"

bye = bye("hello")

