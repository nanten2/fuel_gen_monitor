# -*- coding: utf-8 -*-
import glob
import os
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import datetime
import sys

sys.setrecursionlimit(2000)#for文等の繰り返しの上限値を上げる

def ret_path():#最新のファイルの入っているディレクトリをreturn?                                                                                                                                                                                                                                                         
    path = "./Fuel_data/data"
    files = os.listdir(path)
    files_dir = [i for i in files if os.path.isdir(os.path.join(path, i))]
    files_dir.sort()
    return files_dir

def ret_filename(date, num = 5):#numの日数分のファイル名をreturn                                                                                                                                                                                                                                                         
    filelist = glob.glob("./Fuel_data/data/{}/*.dat".format(date))
    filelist = list(map(os.path.basename, filelist))
    filelist.sort()
    return filelist[num*-1:]

day_list = ret_filename(ret_path()[-1],num = 2)#最新ディレクトリの中に入っている中で新しいものから2つのファイル名からなるリスト
number_of_days = len(day_list)#最新ディレクトリから取得できたファイル名の数
data = []
time_list = []
t_all = []

if number_of_days < 2:#一番新しいディレクトリにファイルが１つしかない、または全くなかった場合  
    day_list2 = ret_filename(ret_path()[-2],num = 2-number_of_days)
    for i in day_list2:
        second_directory = ret_path()[-2]#二番目に新しいディレクトリ名を持ってくる    
        file_data = np.loadtxt("./Fuel_data/data/{}/{}".format(second_directory,i), delimiter=',')
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
            k2 = len(t_all)
            if k2 < 1:#取得した時間のリストtime_nをint化したリストt_allを作成
                t_all = [tmp]#取得した時間のリストtime_nをint化したリストt_allを作成
            else:
                t_all = t_all+[tmp]
            
for i in day_list:
    latest_directory = ret_path()[-1]
    file_data  = np.loadtxt("./Fuel_data/data/{}/{}".format(latest_directory,i), delimiter=',')
    time_n, data_n = np.hsplit(file_data,[6])#取得したデータを時間とパラメータ値に分割      
    k = len(data)
    if k<1:
        data = data_n
    else:
        data = np.append(data,data_n,axis=0)#二回目以降のループでは取得したデータをリストの後ろに追加する
    b2 = len(time_n)
    for l in range(b2):
        tmp = list(map(int,time_n[l]))#取得した時間それぞれをint化する 
        datetime_list = [datetime.datetime(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])]#datetime型の変数にする
        time_list = time_list + datetime_list
        k2 = len(t_all)
        if k2 < 1:#取得した時間のリストtime_nをint化したリストt_allを作成        
            t_all = [tmp]
        else:
            t_all =t_all+[tmp]

tmax = t_all[-1]#最新のデータ取得時間を調べる
tmax_datetime = datetime.datetime(tmax[0],tmax[1],tmax[2],tmax[3],tmax[4],tmax[5])
tmax_timestamp = tmax_datetime.timestamp()
tmin_timestamp = tmax_timestamp-86400#最新のデータ取得時間より24時間前のUNIXtime
num = 0

#最新のデータ取得時間から24時間前までの間に何回データを取得したかを数える 
for t in t_all:
    t_datetime = datetime.datetime(t[0],t[1],t[2],t[3],t[4],t[5])
    t_timestamp = t_datetime.timestamp()
    if tmin_timestamp <= t_timestamp:
        num = num+1
offset = len(data) - num
data_plot = data[offset:]#24時間より新しいデータの切り出し   
timelist_plot = time_list[offset:]#24時間より新しい時間データの切り出し  
data19 = data_plot
for i in range(19):
    exec("data{},data19 = np.hsplit(data19,[1])".format(i))#各パラメーターごとにデータを分割

#プロットを行う関数  
def plot_fig1(title,Ylabel,data_1):
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_xticklabels(timelist_plot,rotation=0,size="small")
    xfmt = mdates.DateFormatter("%m-%d\n%H:00")
    ax1.xaxis.set_major_formatter(xfmt)
    ax1.plot(timelist_plot,data_1)
    ax1.set_ylabel("{}".format(Ylabel))
    ax1.set_xlabel("UTC")
    ax1.set_title("{}".format(title))
    ax1.grid()
    plt.subplots_adjust(bottom=0.2)
    #plt.savefig("//Users/matsueyudai/Desktop/燃料モニター201609/graphics/{}24".format(title))                                                                
    plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/{}".format(title))
    #plt.show()                                                                                                                                               

def plot_fig2(title,Ylabel,data_1,data_2,label_1,label_2):
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_xticklabels(timelist_plot,rotation=0,size="small")
    xfmt = mdates.DateFormatter("%m-%d\n%H:00")
    ax1.xaxis.set_major_formatter(xfmt)
    ax1.plot(timelist_plot,data_1,label="{}".format(label_1))
    ax1.plot(timelist_plot,data_2,label="{}".format(label_2))
    ax1.set_ylabel("{}".format(Ylabel))
    ax1.set_xlabel("UTC")
    ax1.set_title("{}".format(title))
    ax1.grid()
    ax1.legend(loc = 'upper right')
    plt.subplots_adjust(bottom=0.2)
    #plt.savefig("/Users/matsueyudai/Desktop/燃料モニター201609/graphics/{}24".format(title))                                                                 
    plt.savefig("/home/amigos/fuel_generator_monitor/static/img/24h_img/{}".format(title))
    #plt.show()                                                                                                                                               

#ファイル名とタイトル、軸ラベルの指定を行いプロット関数を起動          
plot_fig1("temp_powersuply","Celsius temperature",data0)
plot_fig1("temp_box","Celsius temperature",data1)
plot_fig2("temp_fuelfilter","Celsius temperature",data2,data3,"65063","65064")
plot_fig1("temp_genhause","Celsius temperature",data4)
plot_fig1("humidity_genhause","%",data5)
plot_fig2("flowrate_flowmeter","L/min",data6,data8,"65063","65064")
plot_fig2("temp_flowmeter","Celsius temperature",data7,data9,"65063","65064")
plot_fig2("temp_heater","Celsius temperature",data10,data11,"65063","65064")
plot_fig2("highlevelalarm","V",data12,data15,"65063","65064")
plot_fig2("lowlevelalarm","V",data13,data16,"65063","65064")
plot_fig2("solenoid","V",data14,data17,"65063","65064")



