import sys
from os import system
from platform import system as operating_system

x = '''
clipboard==0.0.4
ffpyplayer==4.3.2
numpy==1.19.5
opencv-python==4.5.1.48
pyglet==1.5.15
pyperclip==1.8.2
PyQt5==5.15.4
PyQt5-Qt5==5.15.2
PyQt5-sip==12.8.1
youtube-dl==2021.2.10
'''.replace('\n', ' ')


system(f'{sys.executable} -m pip install {x}')
