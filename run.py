#!/usr/bin/env python3
import os
from roop import core
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
if __name__ == '__main__':
    core.run()
