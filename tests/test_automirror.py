# test_automirror.py
import unittest
from unittest.mock import patch

from automirror import core

test_url_mirror = (
  'test',
  'test',
  'xenial',
  'http://5thc.co/test',
)

test_ppa_mirror = (
  'wwwdir',
  'ppatest',
  'xenial',
  'ppa:5thc/test',
)

url_mirror = core.AutoMirror(*test_url_mirror)
ppa_mirror = core.AutoMirror(*test_ppa_mirror)
''' 
Create some test objects
'''

def test_url_obj_create():
  assert url_mirror.name == 'test'
  assert url_mirror.dist == 'xenial'
  assert url_mirror.uri == 'http://5thc.co/test'
  assert url_mirror.cname == 'test-xenial'

def test_ppa_obj_create():
  assert ppa_mirror.name == 'ppatest'
  assert ppa_mirror.dist == 'xenial'
  assert ppa_mirror.uri == 'ppa:5thc/test'
  assert ppa_mirror.cname == 'ppatest-xenial'

