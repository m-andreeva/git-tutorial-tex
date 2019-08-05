def lunch(edibles):
    for food in edibles:
        if food == "spam":
            print("No more spam please!")
            continue
        print("Great, delicious " + food)
        else:
            print("I am so glad: No spam!")
    print("Finally, I finished stuffing myself")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def fast_fibonacci(n):
    memo = {0:0, 1:1}
    if not n in memo:
        memo[n] = fast_fibonacci(n-1) + fast_fibonacci(n-2)
    return memo[n]

def celsius2fahrenheit(T_in_celsius):
    return (T_in_celsius * 9 / 5) + 32

def celsius2kelvin(T_in_celsius):
    return T_in_celsius+273.15

def permutations(xs,ys):
    res = []
    for x in xs:
        for y in ys:
            res.append((x,y))
    return res

def calculate(xs, ys):
    result = []
    pairs = permutations(xs, ys)
    for pair in pairs:
        result.append(sum(pair))
    return result
