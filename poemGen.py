import pandas as pd
from bs4 import BeautifulSoup
from Tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
file = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#pick a .csv, otherwise this will probably fail
df = pd.DataFrame(file)
