"""Stage-1: verify no PyQt4 remains and all modules import cleanly."""
import os, re, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Things that only exist in PyQt4 / Python 2 era Qt bindings and must not come back.
FORBIDDEN = re.compile(r"PyQt4|qt4agg|QtWebKit|toPyObject|\.toString\(\)")


def _python_sources():
    for folder in ("src", "applications", "examples"):
        base = os.path.join(ROOT, folder)
        if not os.path.isdir(base):
            continue
        for dirpath, _, files in os.walk(base):
            for fname in files:
                if fname.endswith(".py"):
                    yield os.path.join(dirpath, fname)


class ImportTest(unittest.TestCase):
    def test_no_pyqt4_leftovers(self):
        hits = []
        for fpath in _python_sources():
            with open(fpath, encoding="utf-8") as f:
                for number, line in enumerate(f, 1):
                    if line.lstrip().startswith('#'):
                        continue  # comments may mention PyQt4 for historical reference
                    if FORBIDDEN.search(line):
                        hits.append(f"{fpath}:{number}: {line.rstrip()}")
        self.assertEqual(hits, [], "\n".join(hits))

    def test_segyviewlib_imports(self):
        import segyviewlib as sv
        self.assertTrue(hasattr(sv, "SegyViewWidget"))
        self.assertTrue(hasattr(sv, "SegyTabWidget"))

    def test_widgets_are_pyqt5_widgets(self):
        from PyQt5.QtWidgets import QWidget, QComboBox, QSpinBox
        import segyviewlib as sv
        self.assertTrue(issubclass(sv.ArraySpinBox, QSpinBox))
        self.assertTrue(issubclass(sv.ColormapCombo, QComboBox))
        self.assertTrue(issubclass(sv.LayoutCombo, QComboBox))
        self.assertTrue(issubclass(sv.SegyViewWidget, QWidget))
