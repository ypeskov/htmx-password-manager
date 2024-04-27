import logging


class ColorStreamHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        levelno = record.levelno

        if levelno >= 50:
            color = '\x1b[31m'  # Red for CRITICAL
        elif levelno >= 40:
            color = '\x1b[31m'  # Red for ERROR
        elif levelno >= 30:
            color = '\x1b[33m'  # Yellow for WARNING
        elif levelno >= 20:
            color = '\x1b[32m'  # Green for INFO
        else:
            color = '\x1b[36m'  # Cyan for DEBUG

        record.msg = color + str(record.msg) + '\x1b[0m'  # Append default color after message
        super(ColorStreamHandler, self).emit(record)
