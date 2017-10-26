#!/usr/bin/env python
# Automirror.py
import json
import datetime

class Mirror:
  def __init__(self, endpoint, name, dist, uri):
    self.endpoint = endpoint
    self.name = name
    self.dist = dist
    self.uri  = uri
    self.cname = name + '-' + dist

  def mirror_create(self):
    print('aptly mirror create ' + self.cname + ' ' + self.uri + ' ' + self.dist)

  def mirror_update(self):
    print('aptly mirror update ' + self.cname)

  def snapshot_create(self):
    datestamp = datetime.date.today()
    datestamp = datestamp.strftime('%m.%d')
    snapshot = self.cname + '-' + datestamp
    print('aptly snapshot create ' + snapshot + ' from mirror ' + self.cname)

  def snapshot_publish(self):
    fs_endpoint = 'filesystem:' + self.endpoint + ':' + self.name
    print("aptly publish snapshot -passphrase VAULT_VERY_SECRET_HERE -batch=true " + self.cname + " " + fs_endpoint)

  def build_mirror(self):
    self.mirror_create()
    self.mirror_update()
    self.snapshot_create()
    self.snapshot_publish()

with open('mirror.json') as mirror_file:
  data = json.load(mirror_file)
  for repo in data['repositories']:
    print("Mirroring " + repo['name'] + ' (' + repo['description'] + ')')
    for item in repo['dists']:
      #print('|- Distribution: ' + item['distribution'])
      #print('|-- Endpoint: filesystem:' + data['endpoint'] + ':' + repo['name'])
      a = Mirror(data['endpoint'], repo['name'], item['distribution'], item['uri'])
      a.build_mirror()