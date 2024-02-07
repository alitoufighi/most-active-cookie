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
```bash
docker build -t most-active-cookie-finder .
```
Then to run:
```bash
docker run -v /path/to/input/file.txt:/app/input.txt most-active-cookie-finder -f /app/input.txt -d 2018-12-09
```

Running Tests
---
Tests are located in the `tests/` directory. To run them, use:
```bash
python -m unittest tests/*.py -v
```
Tests will automatically run when building with docker so if any of the test cases fails, the image will not be built.

Configuration
---
Default log level is `INFO`; to change the verbosity, use the `MOST_ACTIVE_COOKIE_LOG_LEVEL` environment variable. For example:
```bash
docker run -e MOST_ACTIVE_COOKIE_LOG_LEVEL=DEBUG -v ./input.txt:/app/input.txt most-active-cookie-finder -f /app/input.txt -d 2018-12-09
```


Notes
---
This implementation focuses on extendability and readability. If performance is of a higher priority and the current implementation does not meet the performance criteria, another version of the code could be to use the assumption \#5 and modify the parser to stop parsing after the requested date have been passed. Or if memory is of a concern and we are dealing with a very large amount of logs, we can reduce memory usage by only keeping the cases for that specific date. However the current implementation focuses on simplicity, in case of extensions that are needed to be implemented later.

Plus, since the sample cases included the dates in the ISO format, I used this format to validate the input dates.

Components
---
There are 3 classes in this implementation:

* The **ArgumentParser** class will read command-line arguments from sys.argv and parse them using Python's native argparse module.
* The **CookieFileParser** class will read the input file and parse it as a dictionary of dictionary of integers, keeping the count of cookies per day. For example:
```python
{
  date(2018, 12, 9): {'AtY0laUfhglK3lC7': 2, 'SAZuXPGUrfbcn5UA': 1, '5UAVanZf6UtGyKVS': 1},
  date(2018, 12, 8): {'SAZuXPGUrfbcn5UA': 1, '4sMM2LxV07bPJzwf': 1, 'fbcn5UAVanZf6UtG': 1},
  date(2018, 12, 7): {'4sMM2LxV07bPJzwf': 1}
}
```
* The **MostActiveCookieApp** class which uses parsed cookies and provides the `get_top_used_cookies` interface to get the top used cookies in a given day.