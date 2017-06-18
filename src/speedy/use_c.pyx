from libc.stdio cimport printf

def example():
    """
    http://stackoverflow.com/questions/8215265/passing-python-strings-through-cython-to-c
    """
    py_string = """
    a complicated string
    with a few
    newlines.
    """

    cdef bytes py_bytes = py_string.encode()
    cdef char* c_string = py_bytes
    printf(c_string)
    print("we actually got this far! :)")
