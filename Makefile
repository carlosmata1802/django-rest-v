
install: 
	docker-compose build

up:
	docker-compose up -d

debug:
	docker-compose up

migrations:
	docker exec -it ventu_test bash -c "python manage.py makemigrations"

migrate:
	docker exec -it ventu_test bash -c "python manage.py migrate" 

create-super-user:
	docker exec -it ventu_test bash -c "python manage.py createsuperuser"

shell:
	docker exec -it ventu_test bash -c "python manage.py shell"

start:	up migrations migrate

start-with-admin-user:	up migrations migrate create-super-user
