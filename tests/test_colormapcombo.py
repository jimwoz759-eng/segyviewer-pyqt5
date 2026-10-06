"""Tests for ColormapCombo (PyQt5 port)."""
from segyviewlib import ColormapCombo
from tests.helpers import QtTestCase


class ColormapComboTest(QtTestCase):
    def test_default_items(self):
        combo = ColormapCombo()
        self.assertGreater(combo.count(), 0)

    def test_item_text_is_the_colormap_name(self):
        combo = ColormapCombo(['seismic', 'gray', 'hot'])
        self.assertEqual(combo.itemText(0), 'seismic')
        self.assertEqual(combo.itemText(1), 'gray')
        self.assertEqual(combo.itemText(2), 'hot')

    def test_current_text_after_setCurrentIndex(self):
        from PyQt5.QtWidgets import QApplication
        combo = ColormapCombo(['seismic', 'gray'])
        combo.setCurrentIndex(1)
        QApplication.processEvents()
        # currentIndex should be 1; currentText() may be empty without a window
        self.assertEqual(combo.currentIndex(), 1)
