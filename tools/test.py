import sys
if len(sys.argv) < 3:
    print("not enough arguments")
    exit(0)
with open(sys.argv[1], "r") as f:
    with open(sys.argv[2], "r") as f2:
        out = f.read().strip()
        ans = f2.read().strip()
        if out == ans:
            print("\x1b[0;37;42m pass \x1b[0m: the output is the same as expected")
        else:
            print("\x1b[0;37;41m fail \x1b[0m: the output does not match the expected output")
            print("output: ")
            print(out)
            print("expected: ")
            print(ans)