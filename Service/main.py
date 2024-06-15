import os
import subprocess

subprocess.call('python /Users/younsy6/Desktop/sparta/Service/recognition.py', shell= True)
subprocess.call('conda activate sparta', shell= True)
subprocess.call('streamlit run app-2.py', shell= True)