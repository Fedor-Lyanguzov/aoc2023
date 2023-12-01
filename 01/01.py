digits = dict(zip(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], map(str, range(1, 10))))

inp = open("input.txt").readlines()

print(sum(int(x[0]+x[-1]) for line in inp if (x:=list(filter(str.isdigit, line)))))

def rep(line):
    left, right = None, None
    for word, num in digits.items():
        l = line.find(word)
        if l!=-1:
            if left is None:
                left = l
                lword = word
            elif l<left:
                left = l
                lword = word
        r = line.rfind(word)
        if r!=-1:
            if right is None:
                right = r
                rword = word
            elif r>right:
                right = r
                rword = word
    if left is None or right is None:
        return line
    line = line[:left]+digits[lword]+line[left:]
    line = line[:right+len(rword)]+digits[rword]+line[right+len(rword):]
    return line

print(sum(int(x[0]+x[-1]) for line in inp if (x:=list(filter(str.isdigit, rep(line))))))

