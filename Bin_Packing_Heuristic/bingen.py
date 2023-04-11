#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randint

# MAIN
if __name__ == "__main__":
    with open("bin_r.txt", "w+") as ofile:
        ofile.write("20\n")
        for x in range(10, 911, 100):
            for y in range(2):
                capacity = randint(10, 51)
                ofile.write("{}\n".format(capacity))
                ofile.write("{}\n".format(x))

                rand_ints = [str(randint(1, capacity)) for x in range(x)]
                ofile.write("{}\n".format(" ".join(rand_ints)))
