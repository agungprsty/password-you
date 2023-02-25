## PASSWORD YOU

The Password-You password generator creates random passwords based on parameters set by you.

### Requirement

This application is being developed in following requirement :
- Python 3.10.x

### Installation 
- clone project
- pip install -U pip & pip install -r requirements.txt
- set env variable : 

```
FLASK_APP_NAME=password-you
FLASK_DEBUG=<0 | 1>

```

- copy ``config/config.py.example`` to ``config/config.py``
- set configuration as your needs 
- for ``SECURITY`` section, acquire a new one (if you don't have one) by run : 

```
python3 generate_key.py
```

### Running

#### API service  
```
./run.sh
```

### Unit testing

```
./unit_test.sh
```

### Unit test report

After run unit test command, run following command

```
coverage report
```