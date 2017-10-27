#!/usr/bin/env python3
# __init__.py
# It's automirror!
import json
import datetime
import os
import subprocess

class AutoMirror:
  def __init__(self, endpoint, name, dist, uri):
    self.endpoint = endpoint
    self.name = name
    self.dist = dist
    self.uri  = uri
    self.cname = name + '-' + dist

  def mirror_create(self):
    args = [
      'aptly',
      'mirror',
      'create',
      self.cname,
      self.uri,
      self.dist,
    ]
    return subprocess.call(args)

  def mirror_update(self):
    args = [
      'aptly',
      'mirror',
      'update',
      self.cname,
    ]
    return subprocess.call(args)

  def snapshot_create(self):
    datestamp = datetime.date.today()
    datestamp = datestamp.strftime('%m.%d')
    snapshot = self.cname + '-' + datestamp
    args = [
      'aptly',
      'snapshot',
      'create',
      snapshot,
      'from',
      'mirror',
      self.cname,
    ]
    return subprocess.call(args)

  def snapshot_publish(self, signing):
    fs_endpoint = 'filesystem:' + self.endpoint + ':' + self.name
    signing_key_passphrase = signing
    args = [
      'aptly',
      'publish',
      'snapshot',
      '-passphrase',
      signing_key_passphrase,
      '-batch=true',
      self.cname,
      fs_endpoint,
    ]
    return subprocess.call(args)

  def build_mirror(self, signing):
    self.mirror_create()
    self.mirror_update()
    self.snapshot_create()
    self.snapshot_publish(signing)