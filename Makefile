-include .env
export

dev:
	docker-compose -f docker-compose.yml -f docker-compose.local.yml build
	docker-compose -f docker-compose.yml -f docker-compose.local.yml up 

build:
	docker build .

start-local:
	docker-compose -f docker-compose.yml -f docker-compose.local.yml up 

start-prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

stop:
	docker-compose down --remove-orphans

delete:
	docker-compose down --remove-orphans
	docker-compose -f docker-compose.yml down