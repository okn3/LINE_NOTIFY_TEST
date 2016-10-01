#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
LINE NotifyをPythonから使う
"""
from __future__ import absolute_import
import urllib2, urllib
import urllib2, urllib, urlparse
import urllib2, urllib
import urllib2, urllib, urlparse
import urllib2, urllib
import urllib2, urllib
import os,sys

url = u"https://notify-api.line.me/api/notify"
message = sys.argv[1]
params = {u"message":message}
params = urllib.urlencode(params)

req = urllib2.Request(url)
# ヘッダ設定
req.add_header(u"Authorization",u"Bearer "+os.environ[u"LINE_ACCESS_TOKEN"])
# パラメータ設定
req.add_data(params)


res = urllib2.urlopen(req)
r = res.read()
print r

