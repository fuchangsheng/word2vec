#!/usr/bin/python3
import pickle
import logging
import sys
import os
import multiprocessing
import configparser

from gensim.models import Word2Vec

class Word2vec(object):
    
    def __init__(self):
        self.__init_logger()
        self.__set_path()
        self.__load()
        self.__model = Word2Vec.load(self.__modelPath)
    
    def __iter__(self):
        # scan all dict
        return self
    
    def __next__(self):
        try:
            data = pickle.load(self.__dictionary)
        except Exception as e:
            self.__dictionary.close()
            raise StopIteration()
        else:
            return data

    def get_similarity(self, tag, word):
        # return float
        return self.__model.similarity(tag, word)
    
    def dump(self):
        # save
        self.__logger.info("Reading tags ...")
        tags = list()
        with open(self.__tagsPath) as f:
            for tag in f.readlines():
                tags.append(tag.strip("\n").strip())
        self.__logger.info(str(tags))
        self.__logger.info("Openning file " + self.__path)
        with open(self.__path, "wb+") as outf:
            with open(self.__wordsPath) as words:
                count = -1
                for item in words:
                    obj = dict()
                    count = count + 1
                    if count==0 :
                        continue
                    else:
                        word = item.split()[0]
                        obj['word'] = word
                        obj['values'] = dict()
                        self.__logger.info("Processing word " + str(count) + " : " + word)
                        for tag in tags:
                            try:
                                value = self.__model.similarity(tag, word)
                            except Exception as e:
                                continue
                            else:
                                obj['values'][tag] = value
                    pickle.dump(obj, outf)
        self.__logger.info("Finished dump action")
    
    def __load(self):
        # read from self.path 
        self.__dictionary = open(self.__path, 'wb+')
    
    def __set_path(self):
        # set dump/load path as self.path
        self.__pyPath = os.path.split(os.path.realpath(__file__))[0]
        self.__config = configparser.ConfigParser()
        self.__config.read("./config/w2v.conf", encoding="utf-8")
        self.__path = self.__pyPath + "/result/data.dictionary"
        self.__tagsPath = self.__pyPath + str(self.__config.get('similarity', 'tags_file'))
        self.__wordsPath = self.__pyPath + "/models/data.vector"
        self.__modelPath = self.__pyPath + "/models/data.model"
    
    def __init_logger(self):
        self.__logger = logging.getLogger("Word2Vec")
        logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s")
        logging.root.setLevel(level=logging.INFO)

