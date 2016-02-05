#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Shihang'
SITENAME = u'Hello World'
SITEURL = 'http://dev.shihang.me'

PATH = 'content'
TIMEZONE = 'Asia/Shanghai' 
DATE_FORMATS = {'zh_CN': '%Y-%m-%d %H:%M', } 
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M' 
DEFAULT_DATE = 'fs'  # use filesystem's mtime 
LOCALE = ('zh_CN',) 
DEFAULT_LANG = u'zh_CN' 
FILENAME_METADATA = '(?P<slug>.*)'

THEME = 'pelican-clean-blog'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'images': {'path': 'images'}}

HEADER_COVER = 'images/cover.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/myprofile'),
          ('github', 'https://github.com/myprofile'),
          ('facebook','https://facebook.com/myprofile'),
          ('flickr','https://www.flickr.com/myprofile/'),
          ('envelope','mailto:my@mail.address'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
