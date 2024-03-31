from collections import Counter

st1 = input()
st2 = input()
print('Yes' if Counter(st1) == Counter(st2) else 'No')