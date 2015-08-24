from functools import partial
import json

from tornado.httpclient import AsyncHTTPClient

URL = 'https://www.archlinux.org/packages/search/json/?name='

def get_version(name, conf, callback):
  pkg = conf['archpkg']
  strip_release = conf.getboolean('strip-release', False)
  url = URL + pkg
  AsyncHTTPClient().fetch(
    url, partial(_pkg_done, name, strip_release, callback))

def _pkg_done(name, strip_release, callback, res):
  if res.error:
    raise res.error

  data = json.loads(res.body.decode('utf-8'))

  if not data['results']:
    logger.error('Arch package not found: %s', name)
    callback(name, None)
    return

  version = [r['pkgver'] for r in data['results'] if r['repo'] != 'testing'][0]
  if strip_release and '-' in version:
    version = version.rsplit('-', 1)[0]
  callback(name, version)
