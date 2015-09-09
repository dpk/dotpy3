import base64
import chardet
import codecs
import collections
import copy
import csv
import datetime
import encodings
import feedparser
import functools
import getopt
import glob
import gzip
import hashlib
import html
import io
import itertools
import lxml.etree
import lxml.html
import mailbox
import math
import mimetypes
import operator
import os
import pytz
import quopri
import random
import re
import requests
import json
import socket
import string
import sys
import textwrap
import time
import unicodedata
import urllib.parse
import urllib.request
import xml
import zlib
import lxml.etree as etree
from lxml.html import html5parser

def run(code):
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    
    output = io.StringIO()
    sys.stdout = output
    sys.stderr = output
    
    try:
        try:
            output.write(str(eval(code)))
        except SyntaxError:
            exec(code)
        
        output.seek(0)
        return output.readline()
    except Exception as error:
        if str(error):
            return "%s: %s" % (type(error).__name__, str(error))
        else:
            return type(error).__name__
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
