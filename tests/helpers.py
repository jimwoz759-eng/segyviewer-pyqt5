"""Shared test helpers for the segyviewlib test suite."""
import os, sys, unittest

# Make sure src/ is on the path (also done by tests/__init__.py, but be defensive)
_SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt5.QtWidgets import QApplication

_app = None  # keep a module-level reference so it is never GC'd

def _get_app():
    global _app
    if _app is None:
        _app = QApplication.instance() or QApplication(sys.argv[:1])
    return _app

# Track Qt slot exceptions via sys.excepthook
_qt_errors = []

def _record_exception(exc_type, exc_value, exc_tb):
    import traceback
    _qt_errors.append("".join(traceback.format_exception(exc_type, exc_value, exc_tb)))

_orig_excepthook = sys.excepthook
sys.excepthook = _record_exception

def _record_unraisable(unraisable):
    _qt_errors.append(
        "unraisable exception in %r: %r" % (unraisable.object, unraisable.exc_value)
    )

sys.unraisablehook = _record_unraisable


class QtTestCase(unittest.TestCase):
    """Base class that provides a QApplication and checks for unhandled Qt errors."""

    def setUp(self):
        _get_app()
        _qt_errors.clear()

    def tearDown(self):
        _get_app().processEvents()
        if _qt_errors:
            errors = "\n".join(_qt_errors)
            _qt_errors.clear()
            self.fail("unhandled exception inside a Qt slot / virtual method:\n" + errors)


def data_path(filename):
    return os.path.join(os.path.dirname(__file__), "testdata", filename)
