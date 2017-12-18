#!/usr/bin/python3
import jieba
import os
import sys
import logging

def seg():
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)

    logger.info("Openning file -wiki.text ...\n\n")

    jieba.load_userdict('./data/user.dict')

    with open("./output/wiki.data", "w+") as outf:
        with open("./output/wiki.text") as inf:
            i = 0
            for line in inf.readlines():
                i = i + 1
                if(i%100 == 0):
                    logger.info("Processing line " + str(i) + "\n")
                line.replace("\t","").replace("\n","").replace(" ","")
                newline = " ".join(jieba.cut(line, cut_all=False))
                outf.write(newline + " ")

    logger.info("\n\nFinished processing See the result in --wiki.data\n\n")

if __name__ == "__main__":
    seg()

