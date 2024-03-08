# loggingpython

`loggingpython` is a Python package that provides a simple and extensible way to integrate logging into your applications. The package starts with a basic logger and can be extended with additional functions to meet the requirements of your application.

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

This creates a logger with a Filehandler and a Consolehandler, the Consolehandler has colors at message.

This creat a logger without handlers.
```python
import loggingpython as lp

# Create a logger
logger = lp.getLogger()

# Creat a FileHandler
filehandler = lp.FileHandler(logger.name)
logger.addHandler(filehandler)

# Creat a Consolehandler
consolehandler = lp.Consolehandler()
logger.addHandler(consolehandler)
```

Now, we can use the logger to generate various types of log messages:

python
``` python
# Logging messages at different levels
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning.")
logger.error("This is an error.")
logger.critical("This is a critical error.")

#Log message with an exception
try:
    1 / 0 
except ZeroDivisionError as e:
    logger.error("An exception occurred: %s", e)
```

The file handler saves the logs in the `logs/file.log directory`.

This example shows how to configure and use a basic logger to generate various types of log messages.

---

We welcome your contributions to the development of loggingpython. If you have feedback, suggestions or would like to contribute to the development, please visit our [GitHub repository](https://github.com/loggingpython-Community/loggingpython) for more information. You can also find more details in our [wiki](https://github.com/loggingpython-Community/loggingpython/wiki) or in the folder `Docs`. For more detailed information, please also visit our package page on [PyPi](https://pypi.org/project/loggingpython).

---

## License

`loggingpython` is licensed under the [MIT License](https://opensource.org/licenses/MIT).