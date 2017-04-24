Install Docker
([Linux](https://docs.docker.com/engine/installation/),
[Windows/Mac](https://www.docker.com/products/docker-toolbox)), then

``` bash
docker-compose up --build
chrome http://localhost:3333
```

will bring up a web application stack for experimentation, including a
couple reverse proxies to serve the app and two different API
endpoints in separate Docker containers at different URLs.

Nothing really to see in the frontend so far, just an
off-the-shelf
[React/Redux starter kit](https://github.com/davezuko/react-redux-starter-kit).
At `/api/todos` you can access a Python endpoint with some in-memory
storage of JSON objects. At `/api/tasks` you can find a Node endpoint
which
uses [jsonapi-server](https://github.com/holidayextras/jsonapi-server)
to provide a [{json:api}](http://jsonapi.org) compliant endpoint
backed by MySQL via Sequelize.
