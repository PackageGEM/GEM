import numpy as np
import pandas as pd
import xlrd
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'



gaze_path = '...'
output_behavior_dir = '...'
task_num = 453
behavior_num = 3

class ReCalculate():
    def __init__(self):
        super(ReCalculate, self).__init__()

    def read_excel(self, file_name):
        xls = pd.ExcelFile(file_name)
        self.df = pd.read_excel(xls)

    def recalculate(self):
        words = [str(item) for item in list(self.df["ID"])]
        word_dict_sorted = {}
        behavior_new = np.zeros((task_num,behavior_num))
        for line in words:
            line = line.replace(',',' ').replace('\n',' ').lower()
            for word in line.split():
                if word in word_dict_sorted:
                    word_dict_sorted[word] += 1
                else:
                    word_dict_sorted[word] = 1
        i=0
        for key in word_dict_sorted:
            
            df1 = self.df[self.df["ID"]==int(key)]
            df1.reset_index(drop=True, inplace=True)
            choice = np.array(df1["Choice"])
            target = np.array(df1["T_Package"][0])
            choice_length = len(choice)
            revisit = 0
            refix = 0
            search = 1
            for n in range(choice_length):
                if n==1:
                        current_gaze = choice[n]
                        pre_gaze = choice[n-1]
                        if current_gaze == pre_gaze:
                            refix +=1
                        else:
                            search +=1
                if n > 1:
                    current_gaze = choice[n]
                    pre_gaze = choice[n-1]
                    if current_gaze == pre_gaze:
                        refix +=1
                    elif current_gaze in choice[:n-1] and current_gaze != pre_gaze:
                        revisit +=1
                    else:
                        search +=1
            
            total_behavior = int(search) + int(refix) + int(revisit)
           
            behavior_new[i,0]=int(search) / total_behavior
            behavior_new[i,1]=int(refix) / total_behavior
            behavior_new[i,2]=int(revisit) / total_behavior
            i+=1
        # df_len = pd.DataFrame(len_new)
        # df_len.to_excel(output_len_dir, index=False)
        df_behavior = pd.DataFrame(behavior_new)
        df_behavior.to_excel(output_behavior_dir, index=False)


        

            
if __name__ == '__main__':
    ReCalculate = ReCalculate()
    ReCalculate.read_excel(gaze_path)
    ReCalculate.recalculate() 

