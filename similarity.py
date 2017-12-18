#!/usr/bin/python3
from gensim.models import Word2Vec
import logging
import configparser
import os
import sys


def sim_txt():
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("Running program " + program)

    config = configparser.ConfigParser()
    config.read("./config/w2v.conf", encoding="utf-8")
    tags = "." + str(config.get("similarity", "tags_file"))

    out_similarity = "./result/similarity_words.txt"

    logger.info("Loading model from file data.model...")

    model = Word2Vec.load('./models/data.model')

    with open(out_similarity, "w+") as os1:
        with open(tags) as tags:
            for tag in tags.readlines():
                tag = tag.strip();
                logger.info("Processing tag : " + tag)
                items = ""
                try:
                    ms_names = model.most_similar(tag)
                except Exception as e:
                    items =  "\tWord not contained"
                    os1.write(tag + " : " + "\n" + items + "\n\n")
                else:
                    for (name, value) in ms_names:
                        items = items + "\t" + name + ", " + str(value) + "\n" 
                    os1.write(tag + " : " + "\n" + items + "\n\n")

    logger.info("Process finished, see " + out_similarity)

if __name__ == "__main__":
    sim_txt()

