run:
	@python main.py

test:
	@python -m unittest discover ./ -p '*Spec.py'

install:
	git clone https://github.com/taku910/cabocha
	cd cabocha
	pip install python/
	pip install git+https://github.com/kenkov/cabocha@0.1.4