run:
	@python main.py

test:
	@python test_wiring.py

install:
	git clone https://github.com/taku910/cabocha
	cd cabocha
	pip install python/
	pip install git+https://github.com/kenkov/cabocha@0.1.4