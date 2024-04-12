# loggingpython

`loggingpython` is a Python package that provides a simple and extensible way to integrate logging into your applications. The package starts with a basic logger and can be extended with additional functions to meet the requirements of your application.

## Features

- **Simple Logger**: Begin with a basic logger and extend it with additional functions.
- **Extensible**: Easily add more functionality to meet your application's logging needs.
- **Customizable**: Tailor the logging system to your specific requirements.

## Installation

You can install `loggingpython` using pip:
```bash
pip install loggingpython
```

Alternatively, you can install the latest development version directly from GitHub:
```bash
git clone https://github.com/loggingpython-Community/loggingpython.git
cd loggingpython
pip install .
```

## Usage

To use `loggingpython`, you first need to import the package and create a logger:
```python
import loggingpython as lp

# Create a simple logger with a file handler and a console handler
logger = lp.getBasicLogger()
```

You can add various handlers to your logger to customize how log messages are handled:
```python
# Log messages at different levels
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning.")
logger.error("This is an error.")
logger.critical("This is a critical error.")
```

## Contributing

We welcome contributions to `loggingpython`. If you have feedback, suggestions, or would like to contribute, please visit our [GitHub repository](https://github.com/loggingpython-Community/loggingpython).

## License

`loggingpython` is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Further Resources

- [Documentation](https://github.com/loggingpython-Community/loggingpython/wiki)
- [GitHub Repository](https://github.com/loggingpython-Community/loggingpython)
- [Issue Tracker](https://github.com/loggingpython-Community/loggingpython/issues)
- [Changelog](https://github.com/loggingpython-Community/loggingpython/blob/main/CHANGELOG.md)
- [PyPi](https://pypi.org/project/loggingpython/)

## Social Media

- [GitHub](https://github.com/loggingpython-Community)
