-include .env
export

build:
	docker-compose -f docker-compose.yml build

start-local:
	docker-compose -f docker-compose.yml up -d

start-prod:
	docker-compose -f docker-compose.yml up -d

stop:
	docker-compose down --remove-orphans

delete:
	docker-compose -f docker-compose.yml down