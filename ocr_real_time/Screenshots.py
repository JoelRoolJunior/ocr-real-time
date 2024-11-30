from pathlib import Path

from mss import mss
from mss.models import Monitor
from mss.screenshot import ScreenShot


class RealTimeScreenShot:
    def __init__(self, folder_path: Path) -> None:
        self.folder_path = folder_path

    def screenshot(self):
        file_name = self.folder_path / 'screenshot.png'
        with mss() as sct:
            sct.shot(output=str(file_name))
