"""Tests for ArraySpinBox (PyQt5 port)."""
from PyQt5.QtGui import QValidator
from segyviewlib import ArraySpinBox
from tests.helpers import QtTestCase


class ArraySpinBoxTest(QtTestCase):
    def test_count_indexes_show_values(self):
        box = ArraySpinBox([10, 20, 30, 40])
        self.assertEqual(box.minimum(), 0)
        self.assertEqual(box.maximum(), 3)

    def test_text_from_value_int(self):
        box = ArraySpinBox([10, 20, 30])
        self.assertEqual(box.textFromValue(0), "10")
        self.assertEqual(box.textFromValue(2), "30")

    def test_text_from_value_float(self):
        box = ArraySpinBox([0.123456789, 1.0])
        self.assertEqual(box.textFromValue(0), "0.1235")
        self.assertEqual(box.textFromValue(1), "1.0")

    def test_validate_returns_the_pyqt5_triple(self):
        box = ArraySpinBox([10, 20, 30])
        result = box.validate("20", 2)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
        state, text, pos = result
        self.assertEqual(state, QValidator.Acceptable)

    def test_no_values_must_not_blow_up(self):
        box = ArraySpinBox([])
        # just calling it should not raise
        box.set_index_values([])

    def test_update_view(self):
        box = ArraySpinBox([10, 20, 30])
        box.update_view([100, 200, 300], 2)
        self.assertEqual(box.value(), 2)
        self.assertEqual(box.textFromValue(2), "300")
