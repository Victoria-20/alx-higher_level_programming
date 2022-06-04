#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    len_args = len(sys.argv)
    sum = 0

    for i in range(1, len_args):
        sum = sum + int(sys.argv[i])
    print("{}".format(sum))
