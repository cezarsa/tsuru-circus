from unittest import TestCase
from mock import Mock

from tsuru.plugins import ProcfileWatcher


class ProcfileWatcherTest(TestCase):
    def test_add_watcher(self):
        plugin = ProcfileWatcher("", "", 1)
        plugin.call = Mock()
        options = {
            "cmd": "ls",
            "name": "name",
        }
        plugin.add_command(name=options["name"], cmd=options["cmd"])
        plugin.call.assert_called_with("add", **options)