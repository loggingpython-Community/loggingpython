Create your own handlers in `loggingpython`
=============================================

`loggingpython` provides a flexible and extensible architecture that allows developers to create their own handlers to fulfill specific logging functionalities. This documentation will guide you through the process of creating your own handler, including the basics, a practical example and a summary of the benefits.

Why create your own handlers?
----------------------------

Creating your own handlers allows you to customize the logging functionality of `loggingpython` to the specific requirements of your application. This can be particularly useful if the predefined handlers do not exactly meet your needs or if you want to implement a unique logging strategy.

Basics
------

A handler in `loggingpython` is a class that inherits from the base class `handler`. You need to override the `emit(self, record)` method, which is called when a log entry is generated. Within this method you can implement the logic to send the log entry to the desired destination.

Example
-------

Here is a simple example of a custom handler that writes log entries to a file:

.. code-block:: python

    from loggingpython.handler import Handler
    
    class MyCustomHandler(Handler):
        def __init__(self, filename):
            self.filename = filename
    
        def emit(self, record):
            with open(self.filename, 'a') as file:
                file.write(f"{record.levelname}: {record.msg}\n")

Use of your own handler
----------------------

To use the created handler, you must add it to a logger:

.. code-block:: python

    from loggingpython import getLogger
    
    logger = getLogger()
    my_handler = MyCustomHandler('my_log_file.log')
    logger.addHandler(my_handler)
    
    logger.info("This is an info message.")

Summary
-------

By creating your own handlers, you can customize the logging functionality of `loggingpython` to the specific requirements of your application. This allows you to process and store log entries in a way that best suits your project.

This section is intended to provide clear guidance and examples for developers who wish to extend `loggingpython`.

Contribute to `loggingpython`
---------------------------

We invite you to contribute your own handlers to `loggingpython`. By sharing your creative solutions and innovations, we can continue to improve the library and make it accessible to the entire community.

For detailed information on the contribution process, including how to adhere to our code style guidelines and how to create pull requests, please visit our `contribution guidelines <../contributing.md>`.

We look forward to your contributions and thank you in advance for your support!

License
-------

`loggingpython` is licensed under the `MIT License <https://opensource.org/licenses/MIT>`.

Further resources
-----------------

- `GitHub Repository <https://github.com/loggingpython-Community/loggingpython>`_
- `Issue Tracker <https://github.com/loggingpython-Community/loggingpython/issues>`_
- `Changelog <https://github.com/loggingpython-Community/loggingpython/blob/main/CHANGELOG.md>`_
- `PyPi <https://pypi.org/project/loggingpython/>`_

Social media
-------------

- `GitHub <https://github.com/loggingpython-Community>`_