An uptime module for the Python.

Unlike the [original project](https://github.com/Cairnarvon/uptime), this fork
is linux-only. It doesn't require a C compiler to be installed. It is useful
in case you need, say, to build a multiarch debian package (like i do).

Just use it like this:

```python
from uptime import uptime

print uptime()
```

Or run the module as a script:

```
$ python -m uptime
Uptime: 109 days, 33.84 seconds.
$ python -m uptime -b
Booted: Wed Oct 10 06:28:24 2012 CET.
```

(You may need to use `uptime.__main__`, depending on your version of Python.)

Full documentation [here](http://pythonhosted.org/uptime/). Works with any version of Python from 2.5 on, including Python 3.
