#!/usr/bin/python3

import logging
import os.path
import six
import sys
 
from gensim.corpora import WikiCorpus

def process_wiki_xml():
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
 
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
 
    inp = "./data/wiki.xml.bz2"
    outp = "./output/wiki.zh.text"
    space = " "
    i = 0
 
    with open(outp, 'w+') as output:
        wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
        for text in wiki.get_texts():
            if six.PY3:
                output.write(
                space.join(map(lambda x:x.encode().decode("utf-8"), text)) + '\n')
            else:
                output.write(space.join(text) + "\n")
            i = i + 1
            if (i % 500 == 0):
                logger.info("Saved " + str(i) + " articles")
 
        logger.info("Finished Saved " + str(i) + " articles")


if __name__ == "__main__":
    process_wiki_xml()

