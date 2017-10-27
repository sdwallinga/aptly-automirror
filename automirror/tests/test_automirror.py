# test_automirror.py

from automirror import automirror

test_url_mirror = automirror.AutoMirror(
  'wwwdir',
  'mirrorname',
  'testdistro',
  'http://5thc.co/test',
)

test_ppa_mirror = automirror.AutoMirror(
  'wwwdir2',
  'ppamirrorname',
  'ppamirrordistro',
  'ppa:5thc/test',
)

def test_mirror_create():
  assert test_url_mirror.mirror_create() == 'aptly mirror create mirrorname-testdistro http://5thc.co/test testdistro'

def test_ppa_mirror_create():
  assert test_ppa_mirror.mirror_create() == 'aptly mirror create ppamirrorname-ppamirrordistro ppa:5thc/test ppamirrordistro'