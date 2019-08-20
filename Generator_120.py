import glob
import os
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import datetime


def ret_path():#最新のファイルの入っているディレクトリをreturn?                                                                 
    path = "./testdata"
    files = os.listdir(path)
    files_dir = [i for i in files if os.path.isdir(os.path.join(path, i))]
    files_dir.sort()
    return files_dir

def ret_filename(date, num = 5):#numの日数分のファイル名をreturn                                                                               
    filelist = glob.glob("./testdata/{}/*.dat".format(date))
    filelist = list(map(os.path.basename, filelist))
    filelist.sort()
    return filelist[num*-1:]

data_list = ret_filename(ret_path()[-1],num = 5)
a = len(data_list)

#Oil_pressure
data = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,6))
        file_n, data_n = np.hsplit(d,[6])
        data=np.append(data,data_n)

        l = 0
        b1 = len(file_n)
        for l in range(b1):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,6))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    b2 = len(file_n)
    for l in range(b2):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data)
                                                                                                                                               
ax1.set_ylabel('label')
ax1.set_title("Oil_pressure")
ax1.grid()

plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/Oil_pressure")
#plt.show()

#Coolant temp
data = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,7))
        file_n, data_n = np.hsplit(d,[6])
        data=np.append(data,data_n)

        l = 0
        b1 = len(file_n)
        for l in range(b1):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,7))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    b2 = len(file_n)
    for l in range(b2):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data)

ax1.set_ylabel('label')
ax1.set_title("Coolant_temp")
ax1.grid()

plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/Coolant_temp")

#ChgAltnV
data = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,8))
        file_n, data_n = np.hsplit(d,[6])
        data=np.append(data,data_n)

        l = 0
        b1 = len(file_n)
        for l in range(b1):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s

for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,8))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    b2 = len(file_n)
    for l in range(b2):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data)

ax1.set_ylabel('label')
ax1.set_title("ChgAltnV")
ax1.grid()

plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/ChgAltnV")

#Battery_voltage
data = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,9))
        file_n, data_n = np.hsplit(d,[6])
        data=np.append(data,data_n)

        l = 0
        b1 = len(file_n)
        for l in range(b1):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s



for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,9))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    b2 = len(file_n)
    for l in range(b2):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data)

ax1.set_ylabel('label')
ax1.set_title("Battery_voltage")
ax1.grid()

plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/Battery_voltage")
#Engine_speed
data = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,10))
        file_n, data_n = np.hsplit(d,[6])
        data=np.append(data,data_n)

        l = 0
        b1 = len(file_n)
        for l in range(b1):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s

for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,10))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    b2 = len(file_n)
    for l in range(b2):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data)

ax1.set_ylabel('label')
ax1.set_title("Engine_speed")
ax1.grid()

plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/Engine_speed")
#Frequency
data = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,11))
        file_n, data_n = np.hsplit(d,[6])
        data=np.append(data,data_n)

        l = 0
        b1 = len(file_n)
        for l in range(b1):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s

for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,11))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    b2 = len(file_n)
    for l in range(b2):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data)

ax1.set_ylabel('label')
ax1.set_title("Frequency")
ax1.grid()

plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/Frequency")


#L1-L3voltage
data1 = []
data2 = []
data3 = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,12,13,14))
        file_n, data_n1, data_n2, data_n3 = np.hsplit(d,[6,7,8])
        data1=np.append(data1,data_n1)
        data2=np.append(data2,data_n2)
        data3=np.append(data3,data_n3)
        l = 0
        b1 = len(file_n)
        for l in range(b1):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s

for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,12,13,14))
    file_n, data_n1, data_n2, data_n3 = np.hsplit(d,[6,7,8])
    data1=np.append(data1,data_n1)
    data2=np.append(data2,data_n2)
    data3=np.append(data3,data_n3)
    l = 0
    b2 = len(file_n)
    for l in range(b2):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data1,label='L1 voltage')
ax1.plot(time_list,data2,label='L2 voltage')
ax1.plot(time_list,data3,label='L3 voltage')
ax1.set_ylabel('V')
ax1.set_title("L1-L3voltage")
ax1.grid()
ax1.legend(loc = 'upper right')
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/L1-L3voltage")


#L1-L2,L2-L3,L3-L1voltage
data1 = []
data2 = []
data3 = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,15,16,17))
        file_n, data_n1, data_n2, data_n3 = np.hsplit(d,[6,7,8])
        data1=np.append(data1,data_n1)
        data2=np.append(data2,data_n2)
        data3=np.append(data3,data_n3)
        l = 0
        b1 = len(file_n)
        for l in range(b1):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s

for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,15,16,17))
    file_n, data_n1, data_n2, data_n3 = np.hsplit(d,[6,7,8])
    data1=np.append(data1,data_n1)
    data2=np.append(data2,data_n2)
    data3=np.append(data3,data_n3)
    l = 0
    b2 = len(file_n)
    for l in range(b2):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data1,label='L1-L2 voltage')
ax1.plot(time_list,data2,label='L2-L3 voltage')
ax1.plot(time_list,data3,label='L3-L1 voltage')
ax1.set_ylabel('A')
ax1.set_title("relative voltage")
ax1.grid()
ax1.legend(loc = 'upper right')
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/relative_voltage")


#L1~L3ampare
data1 = []
data2 = []
data3 = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,18,19,20))
        file_n, data_n1, data_n2, data_n3 = np.hsplit(d,[6,7,8])
        data1=np.append(data1,data_n1)
        data2=np.append(data2,data_n2)
        data3=np.append(data3,data_n3)
        l = 0
        b1 = len(file_n)
        for l in range(b1):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s

for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,18,19,20))
    file_n, data_n1, data_n2, data_n3 = np.hsplit(d,[6,7,8])
    data1=np.append(data1,data_n1)
    data2=np.append(data2,data_n2)
    data3=np.append(data3,data_n3)
    l = 0
    b2 = len(file_n)
    for l in range(b2):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data1,label='L1 ampare')
ax1.plot(time_list,data2,label='L2 ampare')
ax1.plot(time_list,data3,label='L3 ampare')
ax1.set_ylabel('A')
ax1.set_title("L1-L3ampare")
ax1.grid()
ax1.legend(loc = 'upper right')
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/L1-L3ampare")


#Earth_current
data = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,21))
        file_n, data_n = np.hsplit(d,[6])
        data=np.append(data,data_n)

        l = 0
        b1 = len(file_n)
        for l in range(b1):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s

for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,21))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    b2 = len(file_n)
    for l in range(b2):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data)

ax1.set_ylabel('label')
ax1.set_title("Earth current")
ax1.grid()

plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/Earth_current")
#L1~L3wattage
data1 = []
data2 = []
data3 = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,22,23,24))
        file_n, data_n1, data_n2, data_n3 = np.hsplit(d,[6,7,8])
        data1=np.append(data1,data_n1)
        data2=np.append(data2,data_n2)
        data3=np.append(data3,data_n3)
        l = 0
        b1 = len(file_n)
        for l in range(b1):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s

for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,22,23,24))
    file_n, data_n1, data_n2, data_n3 = np.hsplit(d,[6,7,8])
    data1=np.append(data1,data_n1)
    data2=np.append(data2,data_n2)
    data3=np.append(data3,data_n3)
    l = 0
    b2 = len(file_n)
    for l in range(b2):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data1,label='L1 wattage')
ax1.plot(time_list,data2,label='L2 wattage')
ax1.plot(time_list,data3,label='L3 wattage')
ax1.set_ylabel('A')
ax1.set_title("L1-L3wattage")
ax1.grid()
ax1.legend(loc = 'upper right')
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/L1-L3wattage")


#Total_wattage
data = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,25))
        file_n, data_n = np.hsplit(d,[6])
        data=np.append(data,data_n)

        l = 0
        b1 = len(file_n)
        for l in range(b1):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s

for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,25))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    b2 = len(file_n)
    for l in range(b2):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data)

ax1.set_ylabel('W')
ax1.set_title("Total_wattage")
ax1.grid()

plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/Total_wattage")
#running_generator
data = []
time_list = []
if a < 5:
    data_list2 = ret_filename(ret_path()[-2],num = 5-a)
    for i in data_list2:
        c = ret_path()[-2]
        d = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,26))
        file_n, data_n = np.hsplit(d,[6])
        data=np.append(data,data_n)

        l = 0
        b1 = len(file_n)
        for l in range(b1):
            tmp = list(map(int,file_n[l]))
            list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
            time_list = time_list + list_s

for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./testdata/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,26))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    b2 = len(file_n)
    for l in range(b2):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data)

ax1.set_ylabel('label')
ax1.set_title("running generator")
ax1.grid()

plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/running_generator")
