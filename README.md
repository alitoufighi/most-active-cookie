Most Active Cookie Finder
==
Usage
---
```
usage: python main.py [-h] -f FILENAME -d DATE

options:
  -h, --help   show this help message and exit
  -f FILENAME  Path to a CSV file
  -d DATE      Requested date in ISO format
```

Or to use with Docker, first build it using:
```
docker build -t most-active-cookie-finder .
```
Then to run:
```
docker run -v /path/to/input/file.txt:/app/input.txt most-active-cookie-finder -f /app/input.txt -d 2018-12-09
```

Running Tests
---
Tests are located in the `tests/` directory. To run them, use:
```
python -m unittest tests/*.py -v
```
Tests will automatically run when building with docker so if any of the test cases fails, the image will not be built.

Configuration
---
Default log level is `INFO`; to change the verbosity, use the `MOST_ACTIVE_COOKIE_LOG_LEVEL` environment variable. For example:
```
docker run -e MOST_ACTIVE_COOKIE_LOG_LEVEL=DEBUG -v ./input.txt:/app/input.txt most-active-cookie-finder -f /app/input.txt -d 2018-12-09
```


Notes
---
This implementation focuses on extendability and readability. If performance is of a higher priority and the current implementation does not meet the performance criteria, another version of the code could be to use the assumption \#5 and modify the parser to stop parsing after the requested date have been passed. Or if memory is of a concern and we are dealing with a very large amount of logs, we can reduce memory usage by only keeping the cases for that specific date. However the current implementation focuses on simplicity, in case of extensions that are needed to be implemented later.