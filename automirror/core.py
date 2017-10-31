#!/usr/bin/env python3
import json
import datetime
import os
import subprocess

class AutoMirror:
  """ Defines the AutoMirror object
  """
  def __init__(self, endpoint, name, dist, uri):
    """ instantiates a new ``AutoMirror``
    :param endpoint: the root directory of the mirror archive
    :param name: Name of the repository to mirror, directory name located within @endpoint
    :param dist: Distribution to mirror (e.g. xenial, trusty)
    :param uri: URL, unless it's a PPA in which case use `ppa:author/package`
    """
    self.endpoint = endpoint
    self.name = name
    self.dist = dist
    self.uri  = uri
    self.cname = name + '-' + dist
    self.datestamp = datetime.date.today()
    self.datestamp = self.datestamp.strftime('%m.%d')

  def run_aptly(self, args):
    """ Handles execution of `aptly` commands
    .. TODO:: Actual error handling
    :param args: generated aptly command string in list format
    """
    try:
      subprocess.call(args)
      return 0
    except OSError as e:
      print(e)
      return 1

  def mirror_create(self):
    """ prepares the `aptly mirror create` command
    .. TODO:: Add PPA handling
    """
    args = [
      'aptly',
      'mirror',
      'create',
      self.cname,
      self.uri,
      self.dist,
    ]
    if (self.uri[:3] == 'ppa'):
      args.remove(self.dist)
    return args

  def mirror_update(self):
    """ prepares the `aptly mirror update` command
    """
    args = [
      'aptly',
      'mirror',
      'update',
      self.cname,
    ]
    return args

  def snapshot_create(self):
    """ prepares `aptly snapshot create` command
    """
    snapshot = self.cname + '-' + self.datestamp
    args = [
      'aptly',
      'snapshot',
      'create',
      snapshot,
      'from',
      'mirror',
      self.cname,
    ]
    return args
  
  def snapshot_publish(self, signing):
    """ prepares the `aptly snapshot publish` command
    """
    fs_endpoint = 'filesystem:' + self.endpoint + ':' + self.name
    signing_key_passphrase = signing
    snapshot = self.cname + '-' + self.datestamp
    args = [
      'aptly',
      'publish',
      'snapshot',
      '-passphrase',
      signing_key_passphrase,
      '-batch=true',
      snapshot,
      fs_endpoint,
    ]
    return args

  def build_mirror(self, signing):
    """ Conveniently executes all the functions for a fresh mirror release.
    """
    self.run_aptly(self.mirror_create())
    self.run_aptly(self.mirror_update())
    self.run_aptly(self.snapshot_create())
    self.run_aptly(self.snapshot_publish(signing))