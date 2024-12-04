"""
This script allows user to read CSV files which are prepared from anonymized structured eventlogs.
The data should have CaseID, ActivityID and Timestamp. Other resources are optional.
"""

#Importing Libraries

import pandas as pd
import os


class Datahandler:

    """
    Data handler Class

    ...

    This class takes the CSV files as input and returns data after preprocessing.


    Attributes
    --------------
    
        spamread: obj
            pandas object to store the input eventlog.
        
        name: str
            name of the file
        
        ext: str
            extension of the file
 
   Methods

    ---------------
        read_data(self, filename):  
            Reads pandas CSV files as per user defined name and path of the file from main.    
        
        log2np(self,):
           Finds out number of Unique Activities
           Returns an array of values for further preprocessing.
           
    """
   

    def __init__(self,spamread=0,
                 spamreader=0,
                 name='',
                 ext=''):

        self.spamread = spamread
        self.spamreader= spamreader
        self.name= name
        self.ext= ext
    
    
    #import anonymized data
    import os
import pandas as pd

class Datahandler:
    def read_data(self, filename):
        """
        Reads the Data from a CSV file and returns the name of the file.

        Parameters
        --------------
        filename: str
            Name or relative/absolute path of the input file.

        Returns
        ----------------------
        self.name: str
            Name of the file.
        """
        # 파일 이름과 확장자 분리
        self.name, self.ext = os.path.splitext(os.path.basename(filename))

        # 현재 스크립트의 디렉토리를 기준으로 경로 생성
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "../../data/processed", filename)

        # 경로에서 백슬래시를 슬래시로 변환
        file_path = file_path.replace("\\", "/")

        # CSV 파일 읽기
        try:
            self.spamread = pd.read_csv(
                file_path,
                error_bad_lines=False,
                delimiter=',',
                quotechar='|',
                index_col=False
            )
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at {file_path}")

        return self.name




    # Preprocess the event log data to form sequences    
    def log2np(self):
        """This function converts the pandas dataframe into a numpy array like object and returns it.

        *****Helper Variable*****

        self.spamread: obj
            pandas object to store the input eventlog.

        Returns
        ------------
        spamreader: obj
            values of the pandas input table
        max_task: int
            number of unique tasks
        """
        #Number of Unique Tasks
        max_task=len(self.spamread['ActivityID'].unique())
        print('Number of Unique Activities',max_task)
        spamreader=self.spamread.values
        return spamreader,max_task
        
    
  





    
    
    
    

