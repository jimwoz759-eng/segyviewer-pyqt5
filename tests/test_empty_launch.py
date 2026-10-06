"""Regression: the viewer must start without a file (e.g. double-clicked app)."""
from tests.helpers import QtTestCase


class EmptyLaunchTest(QtTestCase):
    def test_widget_without_file(self):
        from segyviewlib import SegyViewWidget
        widget = SegyViewWidget(None)
        widget.show()
        widget.grab()

    def test_open_file_after_empty_start(self):
        from segyviewlib import SegyViewWidget
        from tests.helpers import data_path
        widget = SegyViewWidget(None)
        widget.set_source_filename(data_path("small.sgy"))
        widget.set_default_layout()
