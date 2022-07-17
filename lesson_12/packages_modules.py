"""
1. текущий каталог
2. PYTHONPATH=
3. каталог установки Python
4. venv
"""

import sys
import examples
print(sys.path)
print(examples.lst)
print(dir())
print(__doc__)
print(__file__)
print(__name__)
examples.func(345)
