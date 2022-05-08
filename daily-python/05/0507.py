s1 = "God only konws"
s2 = "       God only konws 123123123    "
s3 = "the sky is blue"

# r = [""]
# for i in s:
#     if i != " ":
#         r[-1] += i
#     elif r[-1] != "":
#         r.append("")

def reverseWords(s):
    r = [""]
    for i in s:
        if i != " ":
            r[-1] += i
        elif r[-1] != "":
            r += [""]
    if r[-1] == "":
        r.pop()

    left, right = 0, len(r) - 1
    while left < right:
        r[left], r[right] = r[right], r[left]
        left += 1
        right -= 1

    return " ".join(r)

# print(r)
# print(s.split())
# print(s)
# print(s.strip())
# def reverse(s):
#     return (" ").join(s.split()[::-1])

# print(reverse(s))


if __name__ == "__main__":
    print(reverseWords(s1))
    print(reverseWords(s2))
    print(reverseWords(s3))

