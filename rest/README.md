

## In order to run the rest service, user docker-compose from the root folder:
```bash
cd engineering-test
docker-compose up -d
```

## The service will be avaliable at port 8080

# Implemented features:

*  List all id's avaliable in the database at /id
*  "Display": Download and render the image by id at /<id>
*  "Statistics": Provide statistics on a given id at /stats/<string:id>/<int:distance>
*  "Find": Return a list of ids within a radius of a given point.
```python
import requests
data = {"type": "Point", "coordinates": [-73.748751, 40.9185483]}
r = requests.post(url+'/find/100', json=json.dumps(data))
r.content
```

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