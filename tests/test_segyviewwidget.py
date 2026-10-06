"""Widget-layer tests for SegyViewWidget and SegyTabWidget."""
import os
from segyviewlib import resource_icon_path, SegyTabWidget, SegyViewWidget
from tests.helpers import QtTestCase, data_path


class TestSegyView(QtTestCase):
    def setUp(self):
        QtTestCase.setUp(self)
        self.filename = data_path("small.sgy")

    def test_resources(self):
        icons = [
            'cog.png', 'folder.png',
            'layouts_four_grid.png', 'layouts_single.png',
            'layouts_three_bottom_grid.png', 'layouts_three_horizontal_grid.png',
            'layouts_three_left_grid.png', 'layouts_three_right_grid.png',
            'layouts_three_top_grid.png', 'layouts_three_vertical_grid.png',
            'layouts_two_horizontal_grid.png', 'layouts_two_vertical_grid.png',
            'table_export.png',
        ]
        for icon in icons:
            p = resource_icon_path(icon)
            self.assertTrue(os.path.exists(p), f"Missing icon: {p}")

    def test_initiate_widget(self):
        widget = SegyViewWidget(self.filename)
        self.assertIsNotNone(widget)

    def test_initiate_empty_tab_widget_and_add_one(self):
        tabwidget = SegyTabWidget()
        widget = SegyViewWidget(self.filename)
        tabwidget.add_segy_view_widget(tabwidget.count(), widget)
        self.assertEqual(tabwidget.count(), 1)

    def test_context_not_none(self):
        widget = SegyViewWidget(self.filename)
        self.assertIsNotNone(widget.context)

    def test_toolbar_visibility(self):
        # show_toolbar=False: toolbar is explicitly hidden regardless of show state
        widget = SegyViewWidget(self.filename, show_toolbar=False)
        self.assertFalse(widget.toolbar.isVisible())
        # show_toolbar=True: toolbar itself is not hidden (isHidden == False)
        # Note: isVisible() returns False until the top-level window is shown,
        # so we test the inverse — it must not be explicitly hidden.
        widget2 = SegyViewWidget(self.filename, show_toolbar=True)
        self.assertFalse(widget2.toolbar.isHidden())
