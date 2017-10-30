# test_automirror.py
from unittest import mock

from automirror import core

test_url_mirror = [
  'wwwdir',
  'mirrorname',
  'testdistro',
  'http://5thc.co/test',
]

test_ppa_mirror = [
  'wwwdir',
  'ppamirrorname',
  'ppamirrordistro',
  'ppa:5thc/test',
]

def test_mirror_create():
  assert 0 == 0
