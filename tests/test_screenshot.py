from pathlib import Path

from ocr_real_time.Screenshots import RealTimeScreenShot


def single_screenshoot():
    path = Path.cwd()
    rts = RealTimeScreenShot(path)
    rts.screenshot()


if __name__ == '__main__':
    single_screenshoot()
