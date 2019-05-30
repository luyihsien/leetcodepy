def a():
    print('a')
    return a()
a()
#RecursionError: maximum recursion depth exceeded while calling a Python object