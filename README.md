# Simple Standalone HTTP Server

Compiled standalone simple HTTP server. Automatically runs on modern Windows, no dependence required.

## How to use

Download the repository as zip file, copy all files in `dist` into folders where server root should be, double-click `simple_server.exe`

## How the executables are generated

The source files are simply `setup.py` and `simple_server.py`. The executables are generated via `py2exe` and the following command:

```
python setup.py py2exe
```

## License

No specific license to my source file, free to use and without warranty. However you might want to check [py2exe](http://www.py2exe.org/LICENSE.txt) license.
