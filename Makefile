build:
	docker build -t hiplot-service .


run: serve

serve:
	docker run --rm -ti \
	--name hiplot \
	-p 1234:8081 \
	hiplot-service

test:
	./invoke_local.sh test.csv
