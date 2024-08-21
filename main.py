from quching.quching_window import QuchingWindow
from quching.quching_player import QuchingPlayer
import sys
from PySide6.QtWidgets import QApplication

if __name__=="__main__":
    app = QApplication()

    player = QuchingPlayer(sys.argv[1:], 0.5)
    quching = QuchingWindow(player)
    quching.show()

    sys.exit(app.exec())