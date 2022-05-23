with open("raw_testcase.txt", "r") as f:
    curr_index = 0
    curr_input = ""
    curr_name = ""
    curr_ext = ""
    for line in f:
        if line.startswith("예제 입력 "):
            curr_name = "input/tc"
            curr_index = line[line.find("예제 입력 ") + len("예제 입력 "):].strip()
            curr_ext = ".in"
        elif line.startswith("예제 출력 "):
            curr_name = "output/tc"
            curr_index = line[line.find("예제 출력 ") + len("예제 출력 "):].strip()
            curr_ext = ".out"
        else:
            with open(curr_name+curr_index+curr_ext, 'a') as w:
                if w.tell() == 0:
                    w.write(line.strip())
                else:
                    w.write("\n"+line.strip())