.PHONY: build run

build:
	docker build -t uflist .

run: build
	docker run --rm -it -p 80:8080 uflist
