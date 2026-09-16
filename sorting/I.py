def check_anagram(str1, str2):
    if len(str1) != len(str2):
        return 'NO'

    ord_str1 = [0] * 256

    for i in range(len(str1)):
        ord_str1[ord(str1[i])] += 1

    for i in range(len(str2)):
        ord_str1[ord(str2[i])] -= 1

        if ord_str1[ord(str2[i])] < 0:
            return 'NO'

    return 'YES'


str1 = input()
str2 = input()

print(check_anagram(str1, str2))