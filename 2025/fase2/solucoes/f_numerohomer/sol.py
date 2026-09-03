def bestEstimate(nd, a, b):
    while True:
        estimate = (a+b)/2
        diff = nd - estimate**estimate

        if (abs(diff) <= 0.001):
            return estimate
        
        if diff < 0:
            b = round(estimate, 8)
        elif diff > 0:
            a = round(estimate, 8)
        else:
            return estimate

def calcHS(nd):
    # Base cases
    if nd == 1:
        return 1
    if nd == 4:
        return 2

    # Get bounds or response
    a = 1
    b = 2
    while True:
        if b**b == nd:
            return b

        if b**b > nd:
            break

        a += 1
        b += 1

    return bestEstimate(nd, a, b)

def formatTime(num):
    ms = num * 60 * 1000
    minutes = ms // 60000
    seconds = (ms // 1000) % 60
    remainder = ms - (minutes * 60000) - (seconds * 1000)
    return "{0}:{1:02}:{2:03}".format(int(minutes), int(seconds), int(remainder))
    
def main():
    while True:
        n = int(input())
        if n == 0:
            break
        print(formatTime(calcHS(n)), flush=True)

if __name__ == '__main__':
    main()
