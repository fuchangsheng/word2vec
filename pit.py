#!/usr/bin/python3

import pickle
import logging
import os
import sys
import multiprocessing
import configparser

from gensim.models import Word2Vec

def dump():
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s")
    logging.root.setLevel(level=logging.INFO)
    logger.info("Running %s" % " ".join(sys.argv))
    config = configparser.ConfigParser()
    config.read("./config/w2v.conf", encoding="utf-8")

    tags_filename = "." + str(config.get("similarity", "tags_file"))
    dictionary = "./models/data.vector"
    model_file = "./models/data.model"
    obj_file = "./result/data.dictionary"

    model = Word2Vec.load(model_file)

    logger.info("Reading tags ...")
    tags = list()
    with open(tags_filename) as f:
        for tag in f.readlines():
            tags.append(tag.strip('\n').strip())
    logger.info(str(tags))

    logger.info("Openning file " + obj_file)
    with open(obj_file, "wb+") as outf:
        logger.info("Openning file " + dictionary)
        with open(dictionary) as words:
            count = -1
            for item in words:
                obj = dict()
                count = count + 1
                if(count == 0):
                    continue
                else:
                    word = item.split()[0]
                    obj['word'] = word
                    obj['values'] = dict()
                    logger.info("Processing word " + str(count) + " : " + word)
                    for tag in tags:
                        try:
                            value = model.similarity(tag, word)
                        except Exception as e:
                            continue
                        else:
                            obj['values'][tag] = value
                pickle.dump(obj, outf)
                logger.info(str(obj))
                    # logger.info("====================================================================\n")
    logger.info("Finished pickle objs")


if __name__ == "__main__":
    dump()


