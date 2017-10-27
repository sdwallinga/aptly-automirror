#!/usr/bin/env python3
# __init__.py
# It's automirror!
import json
import datetime
import os

class AutoMirror:
  def __init__(self, endpoint, name, dist, uri):
    self.endpoint = endpoint
    self.name = name
    self.dist = dist
    self.uri  = uri
    self.cname = name + '-' + dist

  def mirror_create(self):
    print(f'aptly mirror create {self.cname} {self.uri} {self.dist}')

  def mirror_update(self):
    print(f'aptly mirror update {self.cname}')

  def snapshot_create(self):
    datestamp = datetime.date.today()
    datestamp = datestamp.strftime('%m.%d')
    snapshot = self.cname + '-' + datestamp
    print(f'aptly snapshot create {snapshot} from mirror {self.cname}')

  def snapshot_publish(self):
    fs_endpoint = 'filesystem:' + self.endpoint + ':' + self.name
    print(f'aptly publish snapshot -passphrase VAULT_VERY_SECRET_HERE -batch=true {self.cname} {fs_endpoint}')

  def build_mirror(self):
    self.mirror_create()
    self.mirror_update()
    self.snapshot_create()
    self.snapshot_publish()