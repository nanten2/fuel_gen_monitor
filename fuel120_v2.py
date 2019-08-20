# -*- coding: utf-8 -*-
import glob
import os
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import datetime

def ret_path():#最新のファイルの入っているディレクトリをreturn?                                                                                               
    path = "./Fuel_data/data/testdata"
    files = os.listdir(path)
    files_dir = [i for i in files if os.path.isdir(os.path.join(path, i))]
    files_dir.sort()
    return files_dir

def ret_filename(date, num = 5):#numの日数分のファイル名をreturn                                                                                              
    filelist = glob.glob("./Fuel_data/data/testdata/{}/*.dat".format(date))
    filelist = list(map(os.path.basename, filelist))
    filelist.sort()
    return filelist[num*-1:]

day_list = ret_filename(ret_path()[-1],num = 5)#最新ディレクトリの中に入っている中で新しいものから5つのファイル名からなるリスト    
number_of_days = len(day_list)
data = []
time_list = []

if number_of_days < 5:#一番新しいディレクトリにファイルが4つ以下しかなかった場合 
    day_list2 = ret_filename(ret_path()[-2],num = 5-number_of_days)
    for i in day_list2:
        second_directory = ret_path()[-2]#二番目に新しいディレクトリ名を持ってくる
        file_data = np.loadtxt("./Fuel_data/data/testdata/{}/{}".format(second_directory,i), delimiter=',')
        time_n, data_n = np.hsplit(file_data,[6])#取得したデータを時間とパラメータ値に分割  
        k = len(data)
        if k<1:
            data = data_n
        else:
            data = np.append(data,data_n,axis=0)#二回目以降のループでは取得したデータをリストの後ろに追加する
        b1 = len(time_n)
        for l in range(b1):
            tmp = list(map(int,time_n[l]))#取得した時間それぞれをint化する 
            datetime_list = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]#datetime型の変数にする 
            time_list = time_list + datetime_list
        
for i in day_list:
    latest_directory = ret_path()[-1]
    file_data  = np.loadtxt("./Fuel_data/data/testdata/{}/{}".format(latest_directory,i), delimiter=',')
    time_n, data_n = np.hsplit(file_data,[6])#取得したデータを時間とパラメータ値に分割   
    k = len(data)
    if k<1:
        data = data_n
    else:
        data = np.append(data,data_n,axis=0)#二回目以降のループでは取得したデータをリストの後ろに追加する
    l = 0
    b2 = len(time_n)
    for l in range(b2):
        tmp = list(map(int,time_n[l]))#取得した時間それぞれをint化する   
        datetime_list = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]#datetime型の変数にする 
        time_list = time_list + datetime_list

data19 = data
for i in range(19):
    exec("data{},data19 = np.hsplit(data19,[1])".format(i))#各パラメーターごとにデータを分割

#プロットを行う関数    
def plot_fig1(title,Ylabel,data_1):
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_xticklabels(time_list,rotation=0,size="small")
    xfmt = mdates.DateFormatter("%m-%d\n%H:00")
    ax1.xaxis.set_major_formatter(xfmt)
    ax1.plot(time_list,data_1)
    ax1.set_ylabel("{}".format(Ylabel))
    ax1.set_title("{}".format(title))
    ax1.grid()
    #plt.savefig("//Users/matsueyudai/Desktop/燃料モニター201609/graphics/{}120".format(title))
    plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/{}".format(title))                                                                  
    #plt.show()                                                                                                                                              \
                                                                                                                                                              

def plot_fig2(title,Ylabel,data_1,data_2,label_1,label_2):
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_xticklabels(time_list,rotation=0,size="small")
    xfmt = mdates.DateFormatter("%m-%d\n%H:00")
    ax1.xaxis.set_major_formatter(xfmt)
    ax1.plot(time_list,data_1,label="{}".format(label_1))
    ax1.plot(time_list,data_2,label="{}".format(label_2))
    ax1.set_ylabel("{}".format(Ylabel))
    ax1.set_title("{}".format(title))
    ax1.grid()
    ax1.legend(loc = 'upper right')
    #plt.savefig("/Users/matsueyudai/Desktop/燃料モニター201609/graphics/{}120".format(title))
    plt.savefig("/home/amigos/fuel_generator_monitor/static/img/120h_img/{}".format(title))                                                                  
    #plt.show()                      

#ファイル名とタイトル、軸ラベルの指定を行いプロット関数を起動 
plot_fig1("temp_powersuply","Ylabel",data0)
plot_fig1("temp_box","Ylabel",data1)
plot_fig2("temp_fuelfilter","Ylabel",data2,data3,"65063","65064")
plot_fig1("temp_genhause","Ylabel",data4)
plot_fig1("humidity_genhause","Ylabel",data5)
plot_fig2("flowrate_flowmeter","Ylabel",data6,data8,"65063","65064")
plot_fig2("temp_flowmeter","Ylabel",data7,data9,"65063","65064")
plot_fig2("highlevelalarm","Ylabel",data10,data15,"65063","65064")
plot_fig2("lowlevelalarm","Ylabel",data11,data16,"65063","65064")
plot_fig2("onlevelswitch","Ylabel",data12,data17,"65063","65064")
plot_fig2("offlevelswitch","Ylabel",data13,data18,"65063","65064")
plot_fig2("solenoid","Ylabel",data14,data19,"65063","65064")

