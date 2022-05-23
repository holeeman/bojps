import sys
if len(sys.argv) < 3:
    print("not enough arguments")
    exit(0)
with open(sys.argv[1], "r") as f:
    with open(sys.argv[2], "r") as f2:
        for line1, line2 in zip(f, f2):
            if line1.strip() != line2.strip():
                print("\x1b[0;37;41m fail \x1b[0m: the output does not match the expected output")
                print()
                print("output: ")
                print("\033[91m"+line1.strip()+"\x1b[0m")
                print()
                print("expected: ")
                print("\033[92m"+line2.strip()+"\x1b[0m")
                exit()
        
        print("\x1b[0;37;42m pass \x1b[0m: the output is the same as expected")