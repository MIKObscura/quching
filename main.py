from quching.quching_window import QuchingWindow
from quching.quching_player import QuchingPlayer
from quching.indexer.index import refresh_index
import sys
import os
from pathlib import Path
from multiprocessing import Process
from PySide6.QtWidgets import QApplication

def init_config_dir():
    Path(os.path.join(str(Path("~").expanduser()), ".config/quching/playlists")).mkdir(parents=True, exist_ok=True)
    open(os.path.join(str(Path("~").expanduser()), ".config/quching/blacklist.txt"), "w").close()


if __name__=="__main__":
    app = QApplication()

    if not os.path.exists(os.path.join(str(Path("~").expanduser()), ".config/quching")):
        init_config_dir()
    initial_queue = []
    if len(sys.argv) > 1:
        initial_queue = sys.argv[1:]
    player = QuchingPlayer(initial_queue, 0)
    quching = QuchingWindow(player)
    indexer = Process(target=refresh_index, daemon=True)
    quching.show()
    indexer.start()

    app.exec()

    indexer.join()