# cython: profile=True

cdef int collatzx(long n=27):
    cdef int length = 0
    while n > 1:
        if not n % 2:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length


cpdef int longest_collatzx(int limit=10 ** 6):
    cdef int start = 1
    cdef int length = 0
    cdef int start_of_seq = 0
    cdef int longest = 0
    cdef int i
    for i in range(start, limit):
        length = collatzx(i)
        if length > longest:
            longest = length
            start_of_seq = i
    return start_of_seq
