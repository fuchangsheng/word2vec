#!/usr/bin/python3

import wikiBz_to_wikiText as wiki
import filter_en as filt
import jieba_process as seg
import train
import similarity
from word import Word2vec
from os import popen as excute

if __name__ == "__main__":
    wiki.process_wiki_xml() 
    command = "opencc -i ./output/wiki.zh.text -o ./output/wiki.jianti.text -c zht2zhs.ini"
    print(str(excute(command).readlines()))
    print(command)
    filt.filter_english_chars()
    seg.seg()
    command = "iconv -c -t UTF-8<./output/wiki.data> ./output/wiki.data.utf8.txt"
    print(str(excute(command).readlines()))
    print(command)
    train.train() 
    similarity.sim_txt() 
    word = Word2vec()
    word.dump()
