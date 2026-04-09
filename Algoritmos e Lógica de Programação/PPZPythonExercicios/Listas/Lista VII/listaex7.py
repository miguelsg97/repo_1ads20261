def multstring(s, n):
    return s * n


def string_splosion(s):
    return ''.join([s[0:x] for x in range(1, len(s)+1)])


def array_count9(nums):
    return nums.count(9)


def array_front9(nums):
    return 9 in nums[:4]


def hello_name(name):
    return f'Hello {name}!'


def make_tags(tab, word):
    return f'<{tab}>{word}</{tab}>'


def extra_end(s):
    return 3 * s[-2:]


def first_half(s):
    return s[:len(s)//2]


def sem_pontas(s):
    return s[1:-1]


def roda2(s):
    return s[2:] + s[:2]