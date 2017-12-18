all : process_bz jianti filter_en seg utf train similar pickle

process_bz : ./data/wiki.xml.bz2 wikiBz_to_wikiText.py
	python3 wikiBz_to_wikiText.py

jianti : ./output/wiki.zh.text
	opencc -i ./output/wiki.zh.text -o ./output/wiki.jianti.text -c zht2zhs.ini

filter_en : ./output/wiki.jianti.text filter_en.py
	python3 filter_en.py

seg : ./output/wiki.text jieba_process.py
	python3 jieba_process.py

utf : ./output/wiki.data
	iconv -c -t UTF-8<./output/wiki.data> ./output/wiki.data.utf8.txt

train : ./output/wiki.data.utf8.txt train.py
	python3 train.py

similar : ./models/data.model
	python3 similarity.py

pickle : ./models/data.model ./models/data.vector
	python3 pit.py

from-seg : seg utf train similar pickle

result : similar pickle

clean : output result
	rm -rf output
	mkdir output
	rm -rf result
	mkdir result

clean-model : models
	rm -rf models
	mkdir models

