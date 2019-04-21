def find_last(s, a):
    last_occur = -1

    while last_occur < (len(s) - len(a)):
        last_occur = s.find(a, last_occur + 1)
        if s.find(a) == -1:
            break

    return last_occur


print(find_last('aaaa', 'a'))
#>>> 3

print(find_last('aaaaa', 'aa'))
#>>> 3

print(find_last('aaaa', 'b'))
#>>> -1

print(find_last("111111111", "1"))
#>>> 8

print(find_last("222222222", ""))
#>>> 9
