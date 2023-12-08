# logging — Report Status, Error, and Informational Messages

* http://pymotw.com/3/logging/index.html

Purpose: Report status, error, and informational messages.
目的：报告状态、错误和信息性消息。

The `logging` module defines a standard API for reporting errors and status information from applications and libraries. The key benefit of having the logging API provided by a standard library module is that all Python modules can participate in logging, so an application’s log can include messages from third-party modules.
日志记录模块定义了一个标准 API，用于报告来自应用程序和库的错误和状态信息。使用标准库模块提供的日志记录 API 的主要好处是所有 Python 模块都可以参与日志记录，因此应用程序的日志可以包含来自第三方模块的消息。

## Logging Components
记录组件

The logging system is made up of four interacting types of objects. Each module or application that wants to log uses a `Logger` instance to add information to the logs. Invoking the logger creates a `LogRecord`, which is used to hold the information in memory until it is processed. A `Logger` may have a number of `Handler` objects configured to receive and process log records. The `Handler` uses a `Formatter` to turn the log records into output messages.
日志系统由四种交互类型的对象组成。每个想要记录日志的模块或应用程序都使用 Logger 实例向日志添加信息。调用记录器会创建一个 LogRecord，用于将信息保存在内存中直到被处理。 Logger 可以具有多个配置为接收和处理日志记录的 Handler 对象。处理程序使用格式化程序将日志记录转换为输出消息。

## Logging in Applications vs. Libraries

Application developers and library authors can both use `logging`, but each audience has different considerations to keep in mind.
应用程序开发人员和库作者都可以使用日志记录，但每个受众都有不同的注意事项需要牢记。

Application developers configure the `logging` module, directing the messages to appropriate output channels. It is possible to log messages with different verbosity levels or to different destinations. Handlers for writing log messages to files, HTTP GET/POST locations, email via SMTP, generic sockets, or OS-specific logging mechanisms are all included, and it is possible to create custom log destination classes for special requirements not handled by any of the built-in classes.
应用程序开发人员配置日志记录模块，将消息定向到适当的输出通道。 可以将消息记录到不同的详细级别或记录到不同的目的地。 用于将日志消息写入文件、HTTP GET/POST 位置、通过 SMTP 发送电子邮件、通用套接字或特定于操作系统的日志记录机制的处理程序都包含在内，并且可以为任何未处理的特殊要求创建自定义日志目标类。

Developers of libraries can also use `logging` and have even less work to do. Simply create a logger instance for each context, using an appropriate name, and then log messages using the standard levels. As long as a library uses the logging API with consistent naming and level selections, the application can be configured to show or hide messages from the library, as desired.
库的开发人员还可以使用日志记录，并且要做的工作甚至更少。 只需使用适当的名称为每个上下文创建一个记录器实例，然后使用标准级别记录消息。 只要库使用具有一致命名和级别选择的日志记录 API，就可以根据需要将应用程序配置为显示或隐藏库中的消息。

## Logging to a File

Most applications are configured to log to a file. Use the `basicConfig()` function to set up the default handler so that debug messages are written to a file.

```python
# logging_file_example.py

import logging

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)

logging.debug('This message should go to the log file')

with open(LOG_FILENAME, 'rt') as f:
    body = f.read()

print('FILE:')
print(body)
```

After running the script, the log message is written to `logging_example.out`:

```bash
$ python3 logging_file_example.py
FILE:
DEBUG:root:This message should go to the log file
```

## Rotating Log Files
轮换日志文件

Running the script repeatedly causes more messages to be appended to the file. To create a new file each time the program runs, pass a `filemode` argument to `basicConfig()` with a value of `'w'`. Rather than managing the creation of files this way, though, it is better to use a `RotatingFileHandler`, which creates new files automatically and preserves the old log file at the same time.
重复运行该脚本会导致更多消息附加到文件中。要在程序每次运行时创建一个新文件，请将 filemode 参数传递给 basicConfig()，其值为“w”。不过，与其以这种方式管理文件的创建，不如使用 RotatingFileHandler，它会自动创建新文件并同时保留旧的日志文件。

```python
# logging_rotatingfile_example.py

import glob
import logging
import logging.handlers

LOG_FILENAME = 'logging_rotatingfile_example.out'

# Set up a specific logger with our desired output level

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger

handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME,
    maxBytes=20,
    backupCount=5,
)
my_logger.addHandler(handler)

# Log some messages

for i in range(20):
    my_logger.debug('i = %d' % i)

# See what files are created

logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in sorted(logfiles):
    print(filename)
```

The result is six separate files, each with part of the log history for the application.

```bash
$ python3 logging_rotatingfile_example.py
logging_rotatingfile_example.out
logging_rotatingfile_example.out.1
logging_rotatingfile_example.out.2
logging_rotatingfile_example.out.3
logging_rotatingfile_example.out.4
logging_rotatingfile_example.out.5
```

The most current file is always `logging_rotatingfile_example.out`, and each time it reaches the size limit it is renamed with the suffix `.1`. Each of the existing backup files is renamed to increment the suffix (`.1` becomes `.2`, etc.) and the `.5` file is erased.
最新的文件始终是logging_rotatingfile_example.out，并且每次达到大小限制时，都会使用后缀.1 对其进行重命名。 每个现有备份文件都被重命名以增加后缀（.1 变为 .2 等），并且 .5 文件被删除。

> Note
> Obviously, this example sets the log length much too small as an extreme example. Set `maxBytes` to a more appropriate value in a real program.
> 显然，这个例子作为一个极端的例子，将日志长度设置得太小了。 在实际程序中将 maxBytes 设置为更合适的值。

## Verbosity Levels
详细程度

Another useful feature of the `logging` API is the ability to produce different messages at different *log levels*. This means code can be instrumented with debug messages, for example, and the log level can be set so that those debug messages are not written on a production system. the table below lists the logging levels defined by `logging`.
日志记录 API 的另一个有用功能是能够在不同的日志级别生成不同的消息。 例如，这意味着可以使用调试消息来检测代码，并且可以设置日志级别，以便这些调试消息不会写入生产系统。 下表列出了logging定义的日志级别。

| Level | Value |
| --- | --- |
| CRITICAL | 50  |
| ERROR | 40  |
| WARNING | 30  |
| INFO | 20  |
| DEBUG | 10  |
| UNSET | 0   |

The log message is only emitted if the handler and logger are configured to emit messages of that level or higher. For example, if a message is `CRITICAL`, and the logger is set to `ERROR`, the message is emitted (50 > 40). If a message is a `WARNING`, and the logger is set to produce only messages set to `ERROR`, the message is not emitted (30 < 40).
仅当处理程序和记录器配置为发出该级别或更高级别的消息时，才会发出日志消息。 例如，如果消息为“CRITICAL”，并且记录器设置为“ERROR”，则会发出该消息 (50 > 40)。 如果消息是警告，并且记录器设置为仅生成设置为错误的消息，则不会发出该消息 (30 < 40)。

```python
# logging_level_example.py

import logging
import sys

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL,
}

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical error message')
```

Run the script with an argument like ‘debug’ or ‘warning’ to see which messages show up at different levels:

```bash
$ python3 logging_level_example.py debug
DEBUG:root:This is a debug message
INFO:root:This is an info message
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical error message

$ python3 logging_level_example.py info
INFO:root:This is an info message
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical error message
```

## Naming Logger Instances

All of the previous log messages all have ‘root’ embedded in them because the code uses the root logger. An easy way to tell where a specific log message comes from is to use a separate logger object for each module. Log messages sent to a logger include the name of that logger. Here is an example of how to log from different modules so it is easy to trace the source of the message.
之前的所有日志消息都嵌入了“root”，因为代码使用根记录器。 判断特定日志消息来自何处的一种简单方法是为每个模块使用单独的记录器对象。 发送到记录器的日志消息包括该记录器的名称。 以下是如何从不同模块进行日志记录的示例，以便轻松跟踪消息的来源。

```python
# logging_modules_example.py

import logging

logging.basicConfig(level=logging.WARNING)

logger1 = logging.getLogger('package1.module1')
logger2 = logging.getLogger('package2.module2')

logger1.warning('This message comes from one module')
logger2.warning('This comes from another module')
```

The output shows the different module names for each output line.

```bash
$ python3 logging_modules_example.py
WARNING:package1.module1:This message comes from one module
WARNING:package2.module2:This comes from another module
```

## The Logging Tree

The `Logger` instances are configured in a tree structure, based on their names, as illustrated in the figure. Typically each application or library defines a base name, with loggers for individual modules set as children. The root logger has no name.
Logger 实例根据其名称以树形结构进行配置，如图所示。 通常，每个应用程序或库都会定义一个基本名称，并将各个模块的记录器设置为子项。 根记录器没有名称。

![](http://pymotw.com/3/_images/graphviz-2e39f0529306c11f75a099d1fb3e3bc455c8b6e5.png)

The tree structure is useful for configuring logging because it means each logger does not need its own set of handlers. If a logger does not have any handlers, the message is handed to its parent for processing. This means that for most applications it is only necessary to configure handlers on the root logger, and all log information will be collected and sent to the same place, as shown in the figure.
树结构对于配置日志记录非常有用，因为这意味着每个记录器不需要自己的一组处理程序。 如果记录器没有任何处理程序，则消息将传递给其父级进行处理。 这意味着对于大多数应用程序来说，只需要在根记录器上配置处理程序，所有日志信息都将被收集并发送到同一个地方，如图所示。

![](http://pymotw.com/3/_images/graphviz-6284db203afa8a3d139270d7a642cfb0a72eec43.png)

The tree structure also allows different verbosity levels, handlers, and formatters to be set for different parts of the application or library to control which messages are logged and where they go, as in the figure.
树结构还允许为应用程序或库的不同部分设置不同的详细级别、处理程序和格式化程序，以控制记录哪些消息以及它们的去向，如图所示。

![](http://pymotw.com/3/_images/graphviz-ae79e97c1e28266e0cfac5ae087a01eea5e70d61.png)

## Integration with the warnings Module
与警告模块集成

The logging module integrates with [`warnings`](http://pymotw.com/3/warnings/index.html#module-warnings "warnings: Non-fatal alerts") through `captureWarnings()`, which configures `warnings` to send messages through the logging system instead of outputting them directly.
日志模块通过 captureWarnings() 与警告集成，它将警告配置为通过日志系统发送消息，而不是直接输出消息。

```python
# logging_capture_warnings.py

import logging
import warnings

logging.basicConfig(
    level=logging.INFO,
)

warnings.warn('This warning is not sent to the logs')

logging.captureWarnings(True)

warnings.warn('This warning is sent to the logs')
```

The warning message is sent to a logger named `py.warnings` using the `WARNING` level.

```bash
$ python3 logging_capture_warnings.py
logging_capture_warnings.py:13: UserWarning: This warning is not
 sent to the logs
  warnings.warn('This warning is not sent to the logs')
WARNING:py.warnings:logging_capture_warnings.py:17: UserWarning:
 This warning is sent to the logs
  warnings.warn('This warning is sent to the logs')
```

See also

- [Standard library documentation for logging](https://docs.python.org/3.7/library/logging.html) – The documentation for `logging` is extensive, and includes tutorials and reference material that goes beyond the exmaples presented here.

- [Python 2 to 3 porting notes for logging](http://pymotw.com/3/porting_notes.html#porting-logging)

- [`warnings`](http://pymotw.com/3/warnings/index.html#module-warnings "warnings: Non-fatal alerts") – Non-fatal alerts.

- [logging_tree](https://pypi.python.org/pypi/logging_tree) – Third-party package by Brandon Rhodes for showing the logger tree for an application.

- [Logging Cookbook](https://docs.python.org/3.5/howto/logging-cookbook.html) – Part of the standard library documentation, with examples of using `logging` for different tasks.

