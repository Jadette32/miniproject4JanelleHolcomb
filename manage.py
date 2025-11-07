# Author: Janelle Holcomb
# Class: INF 601 Mini Project 4
# Project: Creative Systems Support

import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Could not import Django. Make sure it is installed and your virtual environment is active."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
