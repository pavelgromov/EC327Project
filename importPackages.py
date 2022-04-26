
import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yfinance'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tweepy'])