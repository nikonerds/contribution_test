from os import system
for i in range(100):
    with open("a.txt", "a") as f:
        f.write(str(i))
    system(f"git add --all && git commit -m {i}")
    print(i)
