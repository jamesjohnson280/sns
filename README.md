# sns
Swords and Sorcery

## Installing & Running the App
Create a virtual environment
```
$ mkdir env
$ python3 -m venv env
```

Install required Python modules
```
$ pip install -r requirements.txt
```

Run the app
```
$ python3 -m goblin
```

## Testing
### Run all tests
```
$ python3 -m unittest discover -s goblin/tests
```

### Generate coverage report
```
$ coverage run -m unittest discover -s goblin/tests
```

### View coverage report
```
$ coverage report
```