# Usage

In this section you will learn how to use `loggingpython` in your project.

## Simple example

First, import the package and create a logger:
```python
import loggingpython as lp

# Create a simple logger with a file handler and a console handler
logger = lp.getBasicLogger()
```

``` python
# Create a logger
logger = lp.getLogger()

# Add a FileHandler
filehandler = lp.FileHandler(logger.name)
logger.addHandler(filehandler)

# Add a ConsoleHandler
consolehandler = lp.ConsoleHandler()
logger.addHandler(consolehandler)

# Creat a JSONhandler
jsonhandler = lp.JSONHandler()
logger.addHandler(jsonhandler)

# Creat a SQLHandler
sqlhandler = lp.SQLHandler()
logger.addHandler(sqlhandler)
```

Now you can use the logger to generate different types of log messages:

``` python
# Log messages at different levels
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning.")
logger.error("This is an error.")
logger.critical("This is a critical error.")
```

## Further examples

Further examples and instructions for using `loggingpython` can be found in the [API reference](api_reference.md).

---

## License

`loggingpython` is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Further resources

- [GitHub Repository](https://github.com/loggingpython-Community/loggingpython)
- [Issue Tracker](https://github.com/loggingpython-Community/loggingpython/issues)
- [Changelog](https://github.com/loggingpython-Community/loggingpython/blob/main/CHANGELOG.md)
- [PyPi](https://pypi.org/project/loggingpython/)

## Social media

- [GitHub](https://github.com/loggingpython-Community)

---