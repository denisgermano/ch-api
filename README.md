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
The first time may happen the api fails because the db won't be ready, just wait, stop and start again

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


## Extra notes
- I changed the default Django User to be the Employee model, this was not a good approach, but as I already did this way and the time was running low, I decided to keep this way. Would change to use the same way, but keep the name User and add a flag like `is_employee`, so could keep as a generic User with some extra attributes

- No permission/auth system was used, the next step would be using some approach as token or session to protect the API

- As another step I would change docker-compose to make it more similar to production, adding a webserver to the server instead of built-in django server, environment variable to set `DEBUG` and `DATABASE_URL`, and also add a script to wait for database be ready to the connection before starting the api

- Another step, add coverage to track the test coverage

- Add a CI

- Improve models to fit better on each country, locale, documents
