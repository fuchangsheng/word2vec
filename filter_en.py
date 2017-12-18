#!/usr/bin/python3


import logging
import os
import sys
import re


def filter_english_chars():
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
 
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    infile = "./output/wiki.jianti.text"
    outfile = "./output/wiki.text"
    logger.info("Openning file : " + infile + "\n\n\n")
    
    with open(outfile,"w+") as outf:
        with open(infile) as inf:
            i = 0
            for line in inf.readlines():
                i = i + 1
                logger.info("Line " + str(i) + ": " + line)
                pattern = re.compile(u"[\u4e00-\u9fa5]+")
                newline = " ".join(re.findall(pattern, line))
                logger.info("NewLine " + str(i) + ": " + newline + "\n\n")
                outf.write(newline + "+\n")
    logger.info("Finished process text, see the output file --" + outfile)

if __name__ == "__main__":
    filter_english_chars()

