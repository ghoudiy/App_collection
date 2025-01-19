def palindrome(n):
    return n == n[::-1] and len(n) > 1

def check(n, l):
    i = 1
    testg = True
    testl = True
    while i < l and (testl or testg):
      testg = testg and (n[i] > n[i - 1])
      testl = testl and n[i] < n[i - 1]
      i += 1
    return testl or testg

def test(s, l, awesome_phrases, n):
    # print((s[1:] == '0' * (l - 1), check(s, l), s[0] * l == s), l - 1 != 0 or palindrome(s), n in awesome_phrases)
    return (s[1:] == '0' * (l - 1) or check(s, l) or s[0] * l == s) and l - 1 != 0 or palindrome(s) or n in awesome_phrases
def is_interesting(number, awesome_phrases):
    s = str(number)
    s1 = str(number + 1)
    s2 = str(number + 2)
    if test(s, len(s), awesome_phrases, number) or number in awesome_phrases:
        return 2
    elif test(s1, len(s1), awesome_phrases, number + 1) or test(s2, len(s2), awesome_phrases, number + 2):
        return 1
    return 0

tests = [
    (3, [1337, 256]),
    (1336, [1337, 256]),
    (1337, [1337, 256]),
    (11208, [1337, 256]),
    (11209, [1337, 256]),
    (11211, [1337, 256])
]
for t in tests:
    print(is_interesting(*t))