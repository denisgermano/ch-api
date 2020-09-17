# ch-api

Live API documentation can be accessed with [swagger](https://chapi.herokuapp.com/swagger/) and [redoc](https://chapi.herokuapp.com/redoc/) flavors

Admin page can be accessed [here](https://chapi.herokuapp.com/admin/login/) with

```
username: ch
password: ch
```

For local development it is being used [docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/), so
make sure they are installed to easly run the project.

Inside docker-compose we run a service with postgre database and a service with our application

To start the service locally run

```console
$ docker-compose up
```

Then access `http://0.0.0.0:8000/` to see the results
In this moment you can also see the documentation at `/redocs/` or `/swagger/`

The auth for the API is not enabled, so you can start right the way creating the companies and employees using the tools of your choice, `curl`, `postman`, `insomnia`, or even directly from the `swagger` link

If you want to use the admin locally, just run the following command and fill the steps to create the first super user

```console
$ docker-compose run api python manage.py createsuperuser
```

Run unit tests with

```console
$ docker-compose run api python manage.py test
```
