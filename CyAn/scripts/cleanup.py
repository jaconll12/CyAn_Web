#cleanup fix

import os
from datetime import datetime
import time

url = "www.sharksec.net"
today = datetime.now()
folder = today.strftime('%Y%m%d') +"_" +str(url)+"/"
if not os.path.exists("CyAn/" + folder):
    os.system("mkdir CyAn/" +folder)
    os.system("cp -rf CyAn/output/* CyAn/" + folder)
    os.system("rm -rf CyAn/output/*")
else:
    os.system("cp -rf CyAn/output/* CyAn/" + folder)
    os.system("rm -rf CyAn/output/*")