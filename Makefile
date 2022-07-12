.PHONY: build run tailwind-watch

build:
	docker build -t uflist .

run: build
	docker run --rm -it -p 80:8080 -v ${CURDIR}/app:/app \
	uflist uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload --reload-dir /app --reload-include *.html.j2 --reload-include *.css

tailwind-watch:
	tailwindcss -i ./app/static/css/input.css -o ./app/static/css/main.css --watch
