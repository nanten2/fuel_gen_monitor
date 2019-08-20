import glob
import os
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import datetime


def ret_path():#最新のファイルの入っているディレクトリをreturn?                                                                 
    path = "./Fuel_data/data"
    files = os.listdir(path)
    files_dir = [i for i in files if os.path.isdir(os.path.join(path, i))]
    files_dir.sort()
    return files_dir

def ret_filename(date, num = 1):#numの日数分のファイル名をreturn                                                                               
    filelist = glob.glob("./Fuel_data/data/{}/*.dat".format(date))
    filelist = list(map(os.path.basename, filelist))
    filelist.sort()
    return filelist[num*-1:]

data_list = ret_filename(ret_path()[-1],num = 1)

#temp.powersuply
data = []
time_list = []
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./Fuel_data/data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,6))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    a = len(file_n)
    for l in range(a):
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
ax1.set_title("temp.powersuply")
ax1.grid()

plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/temp_powersuply")
#plt.show()

#temp.box
data = []
time_list = []
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./Fuel_data/data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,7))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    a = len(file_n)
    for l in range(a):
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
ax1.set_title("temp.box")
ax1.grid()

plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/temp_box")

#temp.fuelfilter
data1 = []
data2 = []
time_list = []
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./Fuel_data/data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,8,9))
    file_n, data_n1, data_n2 = np.hsplit(d,[6,7])
    data1=np.append(data1,data_n1)
    data2=np.append(data2,data_n2)
    l = 0
    a = len(file_n)
    for l in range(a):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data1,label='65063')
ax1.plot(time_list,data2,label='65064')
ax1.set_ylabel('V')
ax1.set_title("temp.fuelfilter")
ax1.grid()
ax1.legend(loc = 'upper right')
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/temp_fuelfilter")

#temp.genhause
data = []
time_list = []
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./Fuel_data/data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,10))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    a = len(file_n)
    for l in range(a):
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
ax1.set_title("temp.genhause")
ax1.grid()

plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/temp_genhause")


#humidity.genhause
data = []
time_list = []
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./Fuel_data/data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,11))
    file_n, data_n = np.hsplit(d,[6])
    data=np.append(data,data_n)

    l = 0
    a = len(file_n)
    for l in range(a):
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
ax1.set_title("humidity.genhause")
ax1.grid()
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/humidity_genhause")

#flowrate.flowmeter
data1 = []
data2 = []
time_list = []
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./Fuel_data/data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,12,14))
    file_n, data_n1, data_n2 = np.hsplit(d,[6,7])
    data1=np.append(data1,data_n1)
    data2=np.append(data2,data_n2)
    l = 0
    a = len(file_n)
    for l in range(a):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data1,label='65063')
ax1.plot(time_list,data2,label='65064')
ax1.set_ylabel('V')
ax1.set_title("flowrate.flowmeter")
ax1.grid()
ax1.legend(loc = 'upper right')
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/flowrate_flowmeter")

#temp.flowmeter                                                                                     
data1 = []
data2 = []
time_list = []
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./Fuel_data/data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,13,15))
    file_n, data_n1, data_n2 = np.hsplit(d,[6,7])
    data1=np.append(data1,data_n1)
    data2=np.append(data2,data_n2)
    l = 0
    a = len(file_n)
    for l in range(a):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data1,label='65063')
ax1.plot(time_list,data2,label='65064')
ax1.set_ylabel('V')
ax1.set_title("temp.flowmeter")
ax1.grid()
ax1.legend(loc = 'upper right')
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/temp_flowmeter")

#temp.flowmeter                                                                                    
data1 = []
data2 = []
time_list = []
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./Fuel_data/data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,13,15))
    file_n, data_n1, data_n2 = np.hsplit(d,[6,7])
    data1=np.append(data1,data_n1)
    data2=np.append(data2,data_n2)
    l = 0
    a = len(file_n)
    for l in range(a):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data1,label='65063')
ax1.plot(time_list,data2,label='65064')
ax1.set_ylabel('V')
ax1.set_title("temp.flowmeter")
ax1.grid()
ax1.legend(loc = 'upper right')
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/temp_flowmeter")

#highlevelalarm
data1 = []
data2 = []
time_list = []
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./Fuel_data/data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,16,21))
    file_n, data_n1, data_n2 = np.hsplit(d,[6,7])
    data1=np.append(data1,data_n1)
    data2=np.append(data2,data_n2)
    l = 0
    a = len(file_n)
    for l in range(a):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data1,label='65063')
ax1.plot(time_list,data2,label='65064')
ax1.set_ylabel('V')
ax1.set_title("highlevelalarm")
ax1.grid()
ax1.legend(loc = 'upper right')
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/highlevelalarm")

#lowlevelalarm
data1 = []
data2 = []
time_list = []
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./Fuel_data/data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,17,22))
    file_n, data_n1, data_n2 = np.hsplit(d,[6,7])
    data1=np.append(data1,data_n1)
    data2=np.append(data2,data_n2)
    l = 0
    a = len(file_n)
    for l in range(a):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data1,label='65063')
ax1.plot(time_list,data2,label='65064')
ax1.set_ylabel('V')
ax1.set_title("lowlevelalarm")
ax1.grid()
ax1.legend(loc = 'upper right')
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/lowlevelalarm")

#onlevelswitch
data1 = []
data2 = []
time_list = []
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./Fuel_data/data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,18,23))
    file_n, data_n1, data_n2 = np.hsplit(d,[6,7])
    data1=np.append(data1,data_n1)
    data2=np.append(data2,data_n2)
    l = 0
    a = len(file_n)
    for l in range(a):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data1,label='65063')
ax1.plot(time_list,data2,label='65064')
ax1.set_ylabel('V')
ax1.set_title("onlevelswitch")
ax1.grid()
ax1.legend(loc = 'upper right')
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/onlevelswitch")

#offlevelswitch
data1 = []
data2 = []
time_list = []
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./Fuel_data/data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,19,24))
    file_n, data_n1, data_n2 = np.hsplit(d,[6,7])
    data1=np.append(data1,data_n1)
    data2=np.append(data2,data_n2)
    l = 0
    a = len(file_n)
    for l in range(a):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data1,label='65063')
ax1.plot(time_list,data2,label='65064')
ax1.set_ylabel('V')
ax1.set_title("offlevelswitch")
ax1.grid()
ax1.legend(loc = 'upper right')
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/offlevelswitch")

#solenoid
data1 = []
data2 = []
time_list = []
for i in data_list:
    c = ret_path()[-1]
    d  = np.loadtxt("./Fuel_data/data/{}/{}".format(c,i), delimiter=',', usecols=(0,1,2,3,4,5,20,25))
    file_n, data_n1, data_n2 = np.hsplit(d,[6,7])
    data1=np.append(data1,data_n1)
    data2=np.append(data2,data_n2)
    l = 0
    a = len(file_n)
    for l in range(a):
        tmp = list(map(int,file_n[l]))
        list_s = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]
        time_list = time_list + list_s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xticklabels(time_list,rotation=0,size="small")
xfmt = mdates.DateFormatter("%m-%d\n%H:00")
ax1.xaxis.set_major_formatter(xfmt)
ax1.plot(time_list,data1,label='65063')
ax1.plot(time_list,data2,label='65064')
ax1.set_ylabel('V')
ax1.set_title("solenoid")
ax1.grid()
ax1.legend(loc = 'upper right')
plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/solenoid")
