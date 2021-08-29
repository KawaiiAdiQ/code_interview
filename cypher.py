#!/usr/bin/python3

import os, sys

def c_cypher(n, overwrite):
    n %= 26
    if os.path.isfile(f"zasifrovana({n}).txt") and not overwrite:
        print("File already exists. If you want to overwrite, run the command with --force-overwrite or -f")
        sys.exit(1)

    lower_case = range(ord('a'), ord('z')+1)
    upper_case = range(ord('A'), ord('Z')+1)
    try:
        with open(f"zasifrovana({n}).txt", "w") as out_file:
            for line in sys.stdin:
                result = ""
                for char in line:
                    if ord(char) in lower_case:
                        result += chr((ord(char) + n - ord('a')) % 26 + ord('a'))
                    elif ord(char) in upper_case:
                        result += chr((ord(char) + n - ord('A')) % 26 + ord('A'))
                    else:
                        result += char
                print(result, end='')
                out_file.write(result)
    except:
        print("Error has occured.")
    finally:
        out_file.close()

def print_help():
    print("Usage:")
    print("a) python3 cypher.py YOUR_INT [OPTION] < YOUR_FILE_TO_ENCRYPT")
    print("b) python3 cypher.py YOUR_SOURCE_CHAR YOUR_DESTINATION_CHAR [OPTION] < YOUR_FILE_TO_ENCRYPT\n")
    print("[OPTION]:")
    print("-h --help")
    print("   prints usage (this).\n")
    print("-f --force-overwrite")
    print("   if destination file exists, overwrites it.")
    sys.exit(2)

def recommend_help():
    print("Bad arguments.")
    print("Type: \"python3 cypher.py -h\" for help.")
    sys.exit(2)

def in_alphabet(c):
    return (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z'))
    
def main():
    overwrite = False
    for arg in sys.argv:
        if "-h" == arg or "--help" == arg:
            print_help()
        if "-f" == arg or "--force-overwrite" == arg:
            overwrite = True

    argv_size = len(sys.argv) if not overwrite else len(sys.argv) -1
    argv = sys.argv[1:argv_size]
    if len(argv) < 1 or len(argv) > 2:
        recommend_help()

    n = 0
    if len(argv) == 1:
        if not str(argv[0]).isdecimal() and not (argv[0][0] == '-' and str(argv[0][1:]).isdecimal()):
            recommend_help()
        n = int(argv[0])
    else:
        if len(argv[0]) != 1 or len(argv[1]) != 1:
            recommend_help()
        if not in_alphabet(argv[0]) or not in_alphabet(argv[1]):
            recommend_help()
        n = ord(str(argv[1]).lower()) - ord(str(argv[0]).lower())
    c_cypher(n, overwrite)

if __name__ == "__main__":
   main()