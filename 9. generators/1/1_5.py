from string import ascii_lowercase as chars
gen=(f"{i}{j}" for i in chars for j in chars)
for i in range(50):
    print(next(gen),end=" ")
