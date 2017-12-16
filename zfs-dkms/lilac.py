#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

build_prefix = 'extra-x86_64'

depends = [
  ('spl-dkms', 'spl-utils'),
  ('spl-dkms', 'spl-dkms'),
]

def pre_build():
  _, newver = _G.newver.split("-")
  pkgver, pkgrel = get_pkgver_and_pkgrel()

  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgver=') and pkgver != newver:
        line = f'pkgver={newver}'
    elif line.startswith('pkgrel='):
      if pkgver != newver:
        line = 'pkgrel=1'
      else:
        line = f'pkgrel={int(pkgrel)+1}'

    print(line)

  run_cmd(["updpkgsums"])

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
