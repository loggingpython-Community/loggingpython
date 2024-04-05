# loggingpython
## Version 1.3

`loggingpython` is a Python package which provides a simple and extensible way to integrate logging into your applications. The package starts with a basic logger and can be extended with additional functions to meet the requirements of your application.

Please always use the most current version
---

## Installation

### With pip

For a simple installation via pip, run the following command:
``` bash
pip install loggingpython
```

### With GitHub

To install the latest development of `loggingpython` directly from the GitHub repository, follow these steps:

1. Clone the repository:
``` bash
git clone https://github.com/loggingpython-Community/loggingpython.git
```

2. Change into the cloned directory:
``` bash
cd loggingpython
```

3. Install the package:
``` bash
pip install .
```

---

## Simple Example

In this section, we show how to configure and use a basic logger with `loggingpython`. First, we import the package and create a logger:
``` python
import loggingpython as lp

# Create a basic logger
logger = lp.getBasicLogger()
```

This creates a logger with a Filehandler and a Consolehandler, the Consolehandler has colors in the message.

Now, we can use the logger to generate various types of log messages:

``` python
# Logging messages at different levels
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning.")
logger.error("This is an error.")
logger.critical("This is a critical error.")

# Log message with an exception
try:
    1 / 0 
except ZeroDivisionError as e:
    logger.error(f"An exception occurred: {e}")
```

The file handler saves the logs in the `logs/file.log` directory.

This example shows how to configure and use a basic logger to generate various types of log messages.

---

We welcome your contributions to the development of loggingpython. If you have feedback, suggestions or would like to contribute to the development, please visit our [GitHub repository](https://github.com/loggingpython-Community/loggingpython) for more information. You can also find more details in our [wiki](https://github.com/loggingpython-Community/loggingpython/wiki) or in the folder `Docs`. For more detailed information, please also visit our package page on [PyPi](https://pypi.org/project/loggingpython).

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