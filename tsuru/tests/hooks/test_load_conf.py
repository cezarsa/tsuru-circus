# Copyright 2013 tsuru-circus authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from unittest import TestCase
import os

from tsuru.hooks import load_config


class LoadConfTest(TestCase):
    def setUp(self):
        self.data = u"""hooks:
pre-restart:
  - testdata/pre.sh
post-restart:
  - testdata/pos.sh"""

    def test_load_app_yaml(self):
        with open("app.yaml", "w") as f:
            f.write(self.data)
        config = load_config()
        expected = {
            'hooks': None,
            'pre-restart': ['testdata/pre.sh'],
            'post-restart': ['testdata/pos.sh'],
        }
        self.assertDictEqual(config, expected)
        os.remove("app.yaml")

    def test_load_app_yml(self):
        with open("app.yml", "w") as f:
            f.write(self.data)
        config = load_config()
        expected = {
            'hooks': None,
            'pre-restart': ['testdata/pre.sh'],
            'post-restart': ['testdata/pos.sh'],
        }
        self.assertDictEqual(config, expected)
        os.remove("app.yml")

    def test_load_without_app_files(self):
        config = load_config()
        expected = {
            'pre-restart': [],
            'post-restart': [],
        }
        self.assertDictEqual(config, expected)
