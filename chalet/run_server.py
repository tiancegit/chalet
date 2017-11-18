# coding: utf-8

import sys

from chalet.app import app


def main():
    try:
        port = int(sys.argv[1])
    except:
        port = None
    app.run(host='0.0.0.0', port=port or 8000)


if __name__ == "__main__":
    main()
