#coding :utf8
from flask import request
from  relase import app

if __name__ == "__main__":
    app.__call__
    app.request_class
    app.wsgi_app()
    app.run()

from _thread import _local
from threading import local
from _threading_local import local