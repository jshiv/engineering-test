


## Build command
```bash
docker build -t jshiv/zestyai-engineering-test:latest .
```

## Running the container in development
```bash
docker run -it jshiv/zestyai-engineering-test bash
```

## Run tests
```bash
pip install pytest --user
cd engineering-test/rest/
pytest -v
```