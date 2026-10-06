"""Tests for LayoutCombo (PyQt5 port)."""
from segyviewlib import LayoutCombo
from tests.helpers import QtTestCase


class LayoutComboTest(QtTestCase):
    def test_has_items(self):
        combo = LayoutCombo()
        self.assertGreater(combo.count(), 0)

    def test_layouts_have_icons(self):
        from PyQt5.QtGui import QIcon
        combo = LayoutCombo()
        for i in range(combo.count()):
            icon = combo.itemIcon(i)
            self.assertIsInstance(icon, QIcon)

    def test_changing_layout_emits_signal(self):
        combo = LayoutCombo()
        received = []
        combo.layout_changed.connect(lambda spec: received.append(spec))
        # Change to a different index to trigger the signal
        combo.setCurrentIndex(1)
        self.app_process_events()
        self.assertGreater(len(received), 0)

    def app_process_events(self):
        from PyQt5.QtWidgets import QApplication
        QApplication.processEvents()

    def test_get_current_layout_returns_dict(self):
        combo = LayoutCombo()
        layout = combo.get_current_layout()
        self.assertIsInstance(layout, dict)
