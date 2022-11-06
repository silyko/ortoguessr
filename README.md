# ortoguessr
Simple game inspired by geoguessr
# How to run locally
Define your token for dataforsyningen:
```shell
export DATAFORSYNINGEN_TOKEN=<your_token>
```
Then:
```shell
make build
make run
```
Run migrations, create a superuser (in another shell)
```shell
docker exec -ti eye_backend bash
python manage.py migrate
python manage.py createsuperuser
```
Access the game at http://localhost:8080
