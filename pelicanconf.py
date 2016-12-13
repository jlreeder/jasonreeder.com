#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Jason Reeder"
SITENAME = "Jason Reeder"
SITEURL = "http://www.jasonreeder.com"

PATH = "content"
STATIC_PATHS = ["files"]

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (("linkedin", "https://www.linkedin.com/in/jason-reeder-07481b52"),
          ("github", "https://github.com/jlreeder"),
          ("mail-s", "mailto:info@jasonreeder.com"),
         )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Configure plugins
PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["org_reader"]
ORG_READER_EMACS_LOCATION = "/Applications/Emacs.app/Contents/MacOS/Emacs"

# Configure theme
THEME = "../pelican-themes/pelican-blue-modified"
SIDEBAR_DIGEST = "Linguist, Musician, Programmer, Punslinger"
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (("Home", "/"),
             ("Projects", "/pages/projects.html"),
             ("Language", "/pages/language.html"),
             ("Songbook", "http://whsongbook.jasonreeder.com/")
            )
# TWITTER_USERNAME = "jlreeder"
DISPLAY_SUMMARY = True

# Set "home" and not blog page as home page
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True
PATH = 'content'
ARTICLE_PATHS = ['articles',]
PAGE_PATHS = ['pages',]
