# Flask Workshop Template

## Dev Environment

- Implemented using **Python3.8**
- virtual environment (venv)
- Dependencies with versions listed in [`./requirements.txt`](./requirements.txt)

## Database and Database Manager (UI)

### Postgres
This project comes with the **docker stack** configuration.

- https://www.ronaldjamesgroup.com/article/docker-stack#:~:text=Docker%20Stack%20sits%20at%20a,grouped%20together%2C%20essentially%20pooling%20resources.
- https://docs.docker.com/engine/reference/commandline/stack/


Configuration file: [./stack.yaml](./stack.yaml)

Execute with: 

`docker stack deploy -c stack.yaml <process-name>`

The database data will only persist if you use the same `<process-name>`.

### Adminer

Adminer is a web based database manager.

When running the docker `stack.yaml` config, Adminer will be open on port: `localhost:8080`

- https://www.adminer.org/


## Project Structure

### Models

[`./models/`](./models/)

Interaction with the database

### Controller
[`./controllers/`](./controllers/)

Uses models to operate and shape returned data from DB

### Routes

[`./routes/`](./routes/)

The routes folder is divided in two. (Inspired by [NextJS](https://nextjs.org/) project structure.) 

#### API
- Validates user input
  - Query params
  - Post Body
- Uses the controllers to access data

#### Other files and folders inside `/routes`

This other files are meant to serve **HTML** files for server side rendering (SSR).