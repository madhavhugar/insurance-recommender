# Insurance Recommender

API that recommends an insurance policy based on a questionnaire answers

## Setup

- python 3.8
- postgres
- docker & docker-compose

### Locally

- Install the dependencies within a virtual environment
    ```
    pip install -r requirements.txt
    ```

- Create .env file (using .env.example) and update environment and export them. Any modifications to existing environment variables should be reflected to both .env and .env.docker files.
    ```
    cp .env.example .env
    export $(cat .env | grep -v ^# | xargs)
    ```

- Start the database container
    ```
    docker-compose up --no-start postgres
    docker-compose start postgres
    ```

- Initialise database and migrate
    ```
    python manage.py db init
    python manage.py db migrate
    ```

- Start the web application server
    ```
     python manage.py runserver
    ```

### Docker

- Start the docker containers (environment variables are pre-configured in .env.docker and need not be changed)

    ```
    docker-compose up
    ```

## Tests

After setting up your local dev environment use the following command to run the tests:

```
pytest -v
```

#### Troubleshooting running tests

To run tests you might need to install `postgresql` and `postgresql-contrib`

```
<package-manager> install postgresql postgresql-contrib
```

## API endpoints

### Insomnia

Load the [`httpie/insomnia.json`](httpie/insomnia.json) file into your workspace

### HTTPie

Install [HTTPie](https://httpie.org/docs#installation)

- Following are the available API endpoints
    - POST http://localhost:5000/auth/signup
        ```
        http POST http://localhost:5000/auth/signup username=xyz password=xyz
        ```
    - POST http://localhost:5000/auth/login
        ```
        http POST http://localhost:5000/auth/login username=xyz password=xyz
        ```
    - POST http://localhost:5000/insurance/questionnare
        ```
        http POST http://localhost:5000/insurance/questionnare 'Authorization: JWT <jwt_token>' < httpie/questionnare.json
        ```
    - POST http://localhost:5000/insurance/recommendation
        ```
        http POST http://localhost:5000/insurance/recommendation 'Authorization: JWT <jwt_token>' < httpie/questionnare.json
        ```
