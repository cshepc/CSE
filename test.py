tester = ["primero", "segundo", "primero", "segundo"]
test2 = []
for num in tester:
    test = [tester[-2], tester[-1]]

    test2.append(test)
    tester.remove(tester[-1])


print(tester)
print(test2)
