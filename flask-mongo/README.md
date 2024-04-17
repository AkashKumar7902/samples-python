This version of Flask-Mongo is intended to demonstrate the collection of coverage data for each incoming request and storing it in a file.

There are already 2 tests in `keploy`` directory.

To replay those and collect coverage data, follow the below instructions:

1. create & activate a virtual environment
  ```bash
  python -m venv coverage
  source coverage/bin/activate
  ```

2. install the dependencies
  ```bash
  pip install -r requirements.txt
  ```

3. Replay the tests
  ```bash
  keploy test -c "python app.py"
  ```

Upon successful execution of the keploy command, a dedupdata.yaml file will be created. This file will contain details of the executed files, including the lines covered, for each test case.

This is how it will look like:
```yaml
- id: test-1
  executedLinesByFile:
    /home/akash/Desktop/githubrepo/samples-python/flask-mongo/app.py:
    - 33
    - 34
    - 35
- id: test-2
  executedLinesByFile:
    /home/akash/Desktop/githubrepo/samples-python/flask-mongo/app.py:
    - 24
    - 23
```