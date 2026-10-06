from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTextBrowser
from PyQt5.QtCore import Qt

from segyviewlib import resource_html, resource_html_path


class HelpWindow(QWidget):
    # QtWebKit (QWebView) is not part of PyQt5. QTextBrowser renders the small help
    # page well enough and has no extra dependencies.

    def __init__(self, parent=None):
        QWidget.__init__(self, parent, Qt.WindowStaysOnTopHint | Qt.Window)
        self.setVisible(False)

        self._view_help = QTextBrowser(self)
        self._view_help.setOpenExternalLinks(True)
        # resource_html() returns a QUrl; setSource() accepts QUrl directly
        self._view_help.setSource(resource_html("helppage.html"))
        self._view_help.show()

        f_layout = QHBoxLayout()
        f_layout.addWidget(self._view_help)
        self.setLayout(f_layout)
