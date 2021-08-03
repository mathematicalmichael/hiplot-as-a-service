build:
	docker build -t hiplot-service .

run:
	docker run --rm -ti -p 8081:8081 hiplot-service
