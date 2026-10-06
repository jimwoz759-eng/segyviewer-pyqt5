from PyQt5.QtGui import QValidator
from PyQt5.QtWidgets import QSpinBox


class ArraySpinBox(QSpinBox):
    def __init__(self, values, parent=None):
        QSpinBox.__init__(self, parent)
        self.setKeyboardTracking(False)
        self._values = []
        """ :type: list[int]"""
        self.set_index_values(values)
        self.setMinimum(0)

    def update_view(self, indexes, index):
        self.blockSignals(True)
        self.set_index_values(indexes)
        self.setValue(index)
        self.blockSignals(False)

    def set_index_values(self, values):
        self._values = values
        if self.maximum() != len(values) - 1:
            self.setMaximum(len(values) - 1)

    def setValue(self, value):
        QSpinBox.setValue(self, value)

    def valueFromText(self, text):
        text = str(text)
        if text.strip() == "":
            index = 0
        else:
            value = int(text)
            index = self._values.index(value)
        return index

    def textFromValue(self, index):
        if not self._values or index < 0 or index >= len(self._values):
            return ''
        val = self._values[index]
        if isinstance(val, float):
            val = round(val, 4)
        return str(val)

    def validate(self, text, pos):
        # PyQt5 requires validate() to return a (QValidator.State, str, int) triple
        s = str(text)
        if s.strip() == "":
            return QValidator.Acceptable, s, pos

        try:
            value = int(s)
        except ValueError:
            return QValidator.Invalid, s, pos

        try:
            self._values.index(value)
        except ValueError:
            for v in self._values:
                if str(v).startswith(s[:pos]):
                    return QValidator.Intermediate, s, pos
            return QValidator.Invalid, s, pos

        return QValidator.Acceptable, s, pos
