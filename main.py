from quching.quching_window import QuchingWindow
from quching.quching_player import QuchingPlayer
from quching.indexer.index import refresh_index
import sys
from multiprocessing import Process
from PySide6.QtWidgets import QApplication

if __name__=="__main__":
    app = QApplication()

    player = QuchingPlayer(sys.argv[1:], 0)
    quching = QuchingWindow(player)
    indexer = Process(target=refresh_index, daemon=True)
    quching.show()
    indexer.start()

    app.exec()

    indexer.join()