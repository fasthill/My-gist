import sys
import os

module_path = os.path.abspath(os.path.join('..')) # 상위 폴더로 이동
if module_path not in sys.path:
    sys.path.append(module_path+"\\folder_name") #  상위 폴더에서 하위 폴더('folder_name') 지정. import하려는 파일이 있는 폴더명. 

from file_name import file_module   # import하려는 파일명(file_name), import file_module

#---------------------------------------------------------

sys.path.append(module_path)  #상위 폴더 지정 module_path = ('..')

import filetest2 # 상위 폴더에 있는 filename
