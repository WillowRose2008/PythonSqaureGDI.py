#!/usr/bin/env python

import sys

from win32con import PATINVERT
from win32gui import GetDC, PatBlt


def draw_rects(dc, x, y, w, h, count, dx, dy):
    for i in range(count):
        PatBlt(dc, x + i * dx, y + i * dy, w - 2 * i * dx, h - 2 * i * dy, PATINVERT)


def main(*argv):
    dc = GetDC(0)
    draw_rects(dc, 100, 100, 250, 250, 13, 10, 10)


if __name__ == "__main__":
    print("Python {:s} {:03d}bit on {:s}\n".format(" ".join(elem.strip() for elem in sys.version.split("\n")),
                                                   64 if sys.maxsize > 0x100000000 else 32, sys.platform))
    rc = main(*sys.argv[1:])
    print("\nDone.")
    sys.exit(rc)
