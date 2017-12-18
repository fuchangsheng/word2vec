#!/usr/bin/python3

import logging
import os
import sys
import multiprocessing
import configparser

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


def train():
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s")
    logging.root.setLevel(level=logging.INFO)

    logger.info("Running %s" % " ".join(sys.argv))

    inp = "./output/wiki.data.utf8.txt"
    out1 = "./models/data.model"
    out2 = "./models/data.vector"

    config = configparser.ConfigParser()
    config.read("./config/w2v.conf", encoding="utf-8")

    train_size = int(config.get("train", "size"))
    train_window = int(config.get("train", "window"))
    train_min_count = int(config.get("train", "min_count"))

    model = Word2Vec(LineSentence(inp), size=train_size, window=train_window,
                       min_count=train_min_count,workers=multiprocessing.cpu_count())

    model.save(out1)
    model.wv.save_word2vec_format(out2, binary=False)

if __name__ == "__main__":
    train()

