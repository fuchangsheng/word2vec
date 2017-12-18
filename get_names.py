#!/usr/bin/python3

import re


if __name__ == "__main__":
    inp = "./data/20170907"
    outp = "./data/names.dict"

    names = list()

    with open(outp, "w+") as o:
        with open(inp) as i:
            for line in i.readlines():
                items = line.split(",")
                if len(items) > 2:
                    item = items[2][1:-1]
                    pattern = re.compile(u"[\u4e00-\u9fa5]+")
                    for name in re.findall(pattern, item):
                        if len(name) > 2:
                            if name not in names:
                                print(name)
                                o.write(name+" 10 "+"\n")
                                names.append(name)
