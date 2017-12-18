#!/usr/bin/python3

if __name__ == "__main__":
    inp = "./config/tags.conf"
    outp = "./data/user.dict"

    with open(outp, 'a') as op:
        with open(inp) as ip:
            for tag in ip:
                op.write(tag.strip("\n").strip() + " 10 \n")

