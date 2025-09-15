import openpyxl
import pandas as pd
from pandas import DataFrame
import os
from tqdm import tqdm

DATA_PATH = '...'
DATA_LABEL_PATH = '...'


def combine():    
    for i in range(1,4):
        for j in tqdm(range(1,101)):
            name = 'Q' + str(i) + '_' + str(j) + '.xlsx'
            if os.access(DATA1_PATH + name, os.F_OK) and os.access(DATA2_PATH + name, os.F_OK):
                df1 = pd.DataFrame(pd.read_excel(DATA1_PATH + name, index_col=None, header=None))
                df2 = pd.DataFrame(pd.read_excel(DATA2_PATH + name, index_col=None, header=None))
                data = pd.concat([df1,df2])
                data.to_excel(DATA_SAVE_PATH + 'Q' + str(i) + '_' + str(j) + '.xlsx', index=False, header=False)
            else:
                if os.access(DATA2_PATH + name, os.F_OK):
                    data = pd.DataFrame(pd.read_excel(DATA2_PATH + name, header = None))
                    data.to_excel(DATA_SAVE_PATH + 'Q' + str(i) + '_' + str(j) + '.xlsx', index=False, header=False)
                elif os.access(DATA1_PATH + name, os.F_OK):
                    data = pd.DataFrame(pd.read_excel(DATA1_PATH + name, header = None))
                    data.to_excel(DATA_SAVE_PATH + 'Q' + str(i) + '_' + str(j) + '.xlsx', index=False,header=False)                   
                else:
                    continue

def label():
    for i in range(1,4):
        for j in tqdm(range(1,101)):
            name = 'Q' + str(i) + '_' + str(j) + '.xlsx'
            if os.access(DATA_PATH + name, os.F_OK):
                Package =[]
                if i == 1:
                    if x_coordinate in range(1,153) and y_coordinate in range(153, 602):
                        Package.append(1)
                    elif x_coordinate in range(153,305) and y_coordinate in range(153, 602):
                        Package.append(2)
                    elif x_coordinate in range(305,457) and y_coordinate in range(153, 602):
                        Package.append(3)
                    elif x_coordinate in range(457,610) and y_coordinate in range(153, 602):
                        Package.append(4)
                    elif x_coordinate in range(610,763) and y_coordinate in range(153, 602):
                        Package.append(5)
                    elif x_coordinate in range(763,916) and y_coordinate in range(153, 602):
                        Package.append(6)
                    elif x_coordinate in range(916,1069) and y_coordinate in range(153, 602):
                        Package.append(7)
                    elif x_coordinate in range(1069,1222) and y_coordinate in range(153, 602):
                        Package.append(8)
                    elif x_coordinate in range(1222,1375) and y_coordinate in range(153, 602):
                        Package.append(9)
                    elif x_coordinate in range(1375,1528) and y_coordinate in range(153, 602):
                        Package.append(10)
                    elif x_coordinate in range(1528,1681) and y_coordinate in range(153, 602):
                        Package.append(11)
                    elif x_coordinate in range(1,153) and y_coordinate in range(603, 1051):
                        Package.append(12)
                    elif x_coordinate in range(153,305) and y_coordinate in range(603, 1051):
                        Package.append(13)
                    elif x_coordinate in range(305,457) and y_coordinate in range(603, 1051):
                        Package.append(14)
                    elif x_coordinate in range(457,610) and y_coordinate in range(603, 1051):
                        Package.append(15)
                    elif x_coordinate in range(610,763) and y_coordinate in range(603, 1051):
                        Package.append(16)
                    elif x_coordinate in range(763,916) and y_coordinate in range(603, 1051):
                        Package.append(17)
                    elif x_coordinate in range(916,1069) and y_coordinate in range(603, 1051):
                        Package.append(18)
                    elif x_coordinate in range(1069,1222) and y_coordinate in range(603, 1051):
                        Package.append(19)
                    elif x_coordinate in range(1222,1375) and y_coordinate in range(603, 1051):
                        Package.append(20)
                    elif x_coordinate in range(1375,1528) and y_coordinate in range(603, 1051):
                        Package.append(21)
                    elif x_coordinate in range(1528,1681) and y_coordinate in range(603, 1051):
                        Package.append(22)
                    else:
                        Package.append(0)

                elif i == 2:
                    if x_coordinate in range(1,187) and y_coordinate in range(166, 461):
                        Package.append(1)
                    elif x_coordinate in range(187,373) and y_coordinate in range(166, 461):
                        Package.append(2)
                    elif x_coordinate in range(373,559) and y_coordinate in range(166, 461):
                        Package.append(3)
                    elif x_coordinate in range(559,746) and y_coordinate in range(166, 461):
                        Package.append(4)
                    elif x_coordinate in range(746,933) and y_coordinate in range(166, 461):
                        Package.append(5)
                    elif x_coordinate in range(933,1120) and y_coordinate in range(166, 461):
                        Package.append(6)
                    elif x_coordinate in range(1120,1307) and y_coordinate in range(166, 461):
                        Package.append(7)
                    elif x_coordinate in range(1307,1494) and y_coordinate in range(166, 461):
                        Package.append(8)
                    elif x_coordinate in range(1494,1681) and y_coordinate in range(166, 461):
                        Package.append(9)
                    elif x_coordinate in range(1,187) and y_coordinate in range(461, 756):
                        Package.append(10)
                    elif x_coordinate in range(187,373) and y_coordinate in range(461, 756):
                        Package.append(11)
                    elif x_coordinate in range(373,559) and y_coordinate in range(461, 756):
                        Package.append(12)
                    elif x_coordinate in range(559,746) and y_coordinate in range(461, 756):
                        Package.append(13)
                    elif x_coordinate in range(746,933) and y_coordinate in range(461, 756):
                        Package.append(14)
                    elif x_coordinate in range(933,1120) and y_coordinate in range(461, 756):
                        Package.append(15)
                    elif x_coordinate in range(1120,1307) and y_coordinate in range(461, 756):
                        Package.append(16)
                    elif x_coordinate in range(1307,1494) and y_coordinate in range(461, 756):
                        Package.append(17)
                    elif x_coordinate in range(1494,1681) and y_coordinate in range(461, 756):
                        Package.append(18)
                    elif x_coordinate in range(1,187) and y_coordinate in range(757, 1051):
                        Package.append(19)
                    elif x_coordinate in range(187,373) and y_coordinate in range(757, 1051):
                        Package.append(20)
                    elif x_coordinate in range(373,559) and y_coordinate in range(757, 1051):
                        Package.append(21)
                    elif x_coordinate in range(559,746) and y_coordinate in range(757, 1051):
                        Package.append(22)
                    elif x_coordinate in range(746,933) and y_coordinate in range(757, 1051):
                        Package.append(23)
                    elif x_coordinate in range(933,1120) and y_coordinate in range(757, 1051):
                        Package.append(24)
                    elif x_coordinate in range(1120,1307) and y_coordinate in range(757, 1051):
                        Package.append(25)
                    elif x_coordinate in range(1307,1494) and y_coordinate in range(757, 1051):
                        Package.append(26)
                    elif x_coordinate in range(1494,1681) and y_coordinate in range(757, 1051):
                        Package.append(27)
                    else:
                        Package.append(0)
                
                elif i == 3:
                    if x_coordinate in range(1,187) and y_coordinate in range(136, 441):
                        Package.append(1)
                    elif x_coordinate in range(187,373) and y_coordinate in range(136, 441):
                        Package.append(2)
                    elif x_coordinate in range(373,559) and y_coordinate in range(136, 441):
                        Package.append(3)
                    elif x_coordinate in range(559,746) and y_coordinate in range(136, 441):
                        Package.append(4)
                    elif x_coordinate in range(746,933) and y_coordinate in range(136, 441):
                        Package.append(5)
                    elif x_coordinate in range(933,1120) and y_coordinate in range(136, 441):
                        Package.append(6)
                    elif x_coordinate in range(1120,1307) and y_coordinate in range(136, 441):
                        Package.append(7)
                    elif x_coordinate in range(1307,1494) and y_coordinate in range(136, 441):
                        Package.append(8)
                    elif x_coordinate in range(1494,1681) and y_coordinate in range(136, 441):
                        Package.append(9)
                    elif x_coordinate in range(1,187) and y_coordinate in range(441, 746):
                        Package.append(10)
                    elif x_coordinate in range(187,373) and y_coordinate in range(441, 746):
                        Package.append(11)
                    elif x_coordinate in range(373,559) and y_coordinate in range(441, 746):
                        Package.append(12)
                    elif x_coordinate in range(559,746) and y_coordinate in range(441, 746):
                        Package.append(13)
                    elif x_coordinate in range(746,933) and y_coordinate in range(441, 746):
                        Package.append(14)
                    elif x_coordinate in range(933,1120) and y_coordinate in range(441, 746):
                        Package.append(15)
                    elif x_coordinate in range(1120,1307) and y_coordinate in range(441, 746):
                        Package.append(16)
                    elif x_coordinate in range(1307,1494) and y_coordinate in range(441, 746):
                        Package.append(17)
                    elif x_coordinate in range(1494,1681) and y_coordinate in range(441, 746):
                        Package.append(18)
                    elif x_coordinate in range(1,187) and y_coordinate in range(746, 1051):
                        Package.append(19)
                    elif x_coordinate in range(187,373) and y_coordinate in range(746, 1051):
                        Package.append(20)
                    elif x_coordinate in range(373,559) and y_coordinate in range(746, 1051):
                        Package.append(21)
                    elif x_coordinate in range(559,746) and y_coordinate in range(746, 1051):
                        Package.append(22)
                    elif x_coordinate in range(746,933) and y_coordinate in range(746, 1051):
                        Package.append(23)
                    elif x_coordinate in range(933,1120) and y_coordinate in range(746, 1051):
                        Package.append(24)
                    elif x_coordinate in range(1120,1307) and y_coordinate in range(746, 1051):
                        Package.append(25)
                    elif x_coordinate in range(1307,1494) and y_coordinate in range(746, 1051):
                        Package.append(26)
                    elif x_coordinate in range(1494,1681) and y_coordinate in range(746, 1051):
                        Package.append(27)
                    else:
                        Package.append(0)

                if m == 0:
                    Behavior.append(1)
                    Delta_x.append(0)
                    Delta_y.append(0)

                elif m == last:
                    Behavior.append(5)
                    x_pre_coordinate = int(df1.loc[m-1, 2])
                    y_pre_coordinate = int(df1.loc[m-1, 3])
                    delta_x = (x_coordinate - x_pre_coordinate) / 1680
                    delta_y = (y_coordinate - y_pre_coordinate) / 1050
                    Delta_x.append(delta_x)
                    Delta_y.append(delta_y)
                else:
                    
                    if Package[m] == Package[m-1]:
                        Behavior.append(3) 
                    elif Package[m] in Package[:-1]:
                        Behavior.append(4)
                    else:
                        Behavior.append(2)
                    # x_pre_coordinate = int(df1.loc[m-1, 2])
                    # y_pre_coordinate = int(df1.loc[m-1, 3])
                    # delta_x = (x_coordinate - x_pre_coordinate) / 1680
                    # delta_y = (y_coordinate - y_pre_coordinate) / 1050
                    # Delta_x.append(delta_x)
                    # Delta_y.append(delta_y)
                package.extend(Package)

                Delta = [package,Behavior]
                Delta = DataFrame(Delta)
                Delta = Delta.T
                Delta.reset_index().drop(['index'],axis=1)
                Delta.columns.name = None
                Dataframe = pd.concat([df, Delta],axis=1)
                
                Dataframe.to_excel(DATA_LABEL_PATH + 'Q' + str(i) + '_' + str(j) + '.xlsx', index=False, header=False)

            else:
                continue
            


label()

