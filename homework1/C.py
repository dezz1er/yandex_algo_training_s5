def read_file(filename="input.txt"):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except IOError:
        return []

from_file = read_file()
_ = int(from_file[0])
arrL = [int(x) for x in from_file[1].split()]

maxL = max(arrL)
sumL = sum(arrL)
if sumL - maxL == maxL:
    print(maxL * 2)
else:
    ans = maxL * 2 - sumL
    print(ans if ans > 0 else sumL)