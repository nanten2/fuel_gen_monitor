import glob
import os
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import datetime


def ret_path():#最新のファイルの入っているディレクトリをreturn?                 
    path = "./data"
    files = os.listdir(path)
    files_dir = [i for i in files if os.path.isdir(os.path.join(path, i))]
    files_dir.sort()
    return files_dir

def ret_filename(date, num = 5):#numの日数分のファイル名をreturn                
    filelist = glob.glob("./data/{}/*.dat".format(date))
    filelist = list(map(os.path.basename, filelist))
    filelist.sort()
    return filelist[num*-1:]

data_list = ret_filename(ret_path()[-1],num = 5)
print(data_list)
a = len(data_list)
data = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,6))
        file_n, data_n = np.hsplit(d,[6])
        data=np.append(data,data_n)

        l = 0
        a = len(file_n)
        for l in range(a):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s

for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,6))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    a = len(file_n)
    for l in range(a):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

print(time_list)


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data)#label='Oil_pressure')                                                                                                                                                              
ax1.set_ylabel('label')
ax1.set_title("Oil_pressure")
ax1.grid()

#plt.subplots_adjust(hspace=0.7,bottom=0.2)                                                                                                                                                                 

plt.savefig('./static/img/Oil_pressure.jpg')
plt.show()
