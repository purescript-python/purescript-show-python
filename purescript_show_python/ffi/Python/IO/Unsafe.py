def printLn(s):
    return lambda: print(s)

def show(s):
    return lambda: str(s)

def repr(s, *, r=repr):
    return lambda: r(s)

def assertMsg(cond, msg):
    def ap():
        assert cond, msg
        return ()
    return ap

def assert_(cond):
    def ap():
        assert cond
        return ()
    return ap
