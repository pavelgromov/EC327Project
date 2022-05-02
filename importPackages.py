import os
os.system('cmd /c "python -m pip install --upgrade --force-reinstall pip"')
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yfinance'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tweepy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'vaderSentiment'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'wordcloud'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyqt5'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'matplotlib'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'datetime'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])