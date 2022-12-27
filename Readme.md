# Credit Card Validator #

### Supported Providers ###
 - American Express
 - Master Card
 - Visa


### Usage ###
```bash
$ python validator.py <ccn>
```

### Example: American Express ###
```bash
$ python validator.py 378282246310005
valid
```

### Development ###
```bash
$ make create-virtualenv # creates env and installs requirements
$ make all-checks # lint and unit tests
$ make requirements-dev.txt # updates requirements file
```