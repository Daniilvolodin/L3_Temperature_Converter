def to_f(from_c):
    fahrenheit = float(from_c * 9/5) + 32
    return fahrenheit

temperatures = [0, 40, 100]
converted = []

for i in temperatures:
    answer = to_f(i)
    ans_statement = "{} degrees to C is {} degrees F".format(i, answer)
    converted.append(ans_statement)

print(converted)
