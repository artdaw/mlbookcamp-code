# Cats & Dogs TF-Lite

## Prerequisites

- We use Python 3
- Install [Docker](https://www.docker.com/get-started)
- Install [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
- Initialise virtualenv using either `venv` or `.venv` folder name: `virtualenv .venv`
- Activate virtualenv: `source .venv/bin/activate`
- Install all dependencies: `pip3 install -r requirements.txt`

## Run Docker Locally

You can test AWS Lambda locally by running the Docker image:

1. Build the image
    ```bash
    ./bin/docker-build.sh
    ```
2. Run the image. Make sure you don't have anything else on port 8080:
    ```bash
    ./bin/docker-run.sh
    ```
3. Use cURL to send a test request:
    ```bash
     curl \
        -H "Content-Type: application/json" \
        -d '{"url": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Pug_600.jpg"}' \
        http://localhost:8080/2015-03-31/functions/function/invocations
    ```

