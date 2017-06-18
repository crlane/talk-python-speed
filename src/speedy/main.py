def collatz(n=27):
    length = 0
    while n > 1:
        if not n % 2:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length


def longest_collatz(limit=10 ** 6):
    start = 1
    length = 0
    start_of_seq = 0
    longest = 0
    for i in range(start, limit):
        length = collatz(i)
        if length > longest:
            longest = length
            start_of_seq = i
    return start_of_seq
