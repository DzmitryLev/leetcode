import collections

if __name__ == '__main__':
    s = input()
    count = collections.Counter(sorted(s))
    result = count.most_common(3)
    for letter, number in result:
        print(letter, number)