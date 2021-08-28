#!/usr/bin/python3

import os, sys

def c_cypher(n):
    lower_case = range(ord('a'), ord('z')+1)
    upper_case = range(ord('A'), ord('Z')+1)
    n = n % 26
    overwrite = "--force-overwrite" in sys.argv or "-f" in sys.argv
    if os.path.isfile(f"zasifrovana({n}).txt") and not overwrite:
        print("File already exists. If you want to overwrite, run the command with --force-overwrite or -f")
        sys.exit(1)
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
                print(result)
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
    
def main():
    if "-h" in sys.argv or "--help" in sys.argv:
        print_help()
        sys.exit(1)

    overwrite = "--force-overwrite" in sys.argv or "-f" in sys.argv
    argv_size = len(sys.argv) if not overwrite else len(sys.argv) -1
    argv = sys.argv[1:argv_size]
    if len(argv) < 1 or len(argv) > 2:
        print("Wrong number of arguments.")
        print("Type: \"python3 cypher.py -h\" for help.")
        sys.exit(2)

    n = 0
    if len(argv) == 1:
        if not str(argv[0]).isdecimal() and not (argv[0][0] == '-' and str(argv[0][1:]).isdecimal()):
            print(f"Wrong format of argument: {argv[0]}")
            print("Type: \"python3 cypher.py -h\" for help.")
            sys.exit(2)
        n = int(argv[0])
    else:
        if len(argv[0]) != 1:
            print(f"Wrong parameter: \"{argv[0]}\", single character required.")
            print("Type: \"python3 cypher.py -h\" for help.")
            sys.exit(2)
        if len(argv[1]) != 1:
            print(f"Wrong parameter: \"{argv[1]}\", single character required.")
            print("Type: \"python3 cypher.py -h\" for help.")
            sys.exit(2)
        lower_case = range(ord('a'), ord('z')+1)
        upper_case = range(ord('A'), ord('Z')+1)
        if not str(argv[0]).isalpha() or (ord(argv[0]) not in lower_case and ord(argv[0]) not in upper_case):
            print(f"Expected character from english alphabet. Got: {argv[0]}")
            sys.exit(2)
        if not str(argv[1]).isalpha() or (ord(argv[1]) not in lower_case and ord(argv[1]) not in upper_case):
            print(f"Expected character from english alphabet. Got: {argv[1]}")
            sys.exit(2)
        n = ord(str(argv[1]).lower()) - ord(str(argv[0]).lower())
    c_cypher(n)

if __name__ == "__main__":
   main()