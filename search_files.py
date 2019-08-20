#!/usr/bin/env python
import glob
import os

def ret_path(path="./testdata"):#最新のファイルの入っているディレクトリをreturn
    files = os.listdir(path)
    files_dir = [i for i in files if os.path.isdir(os.path.join(path, i))]
    files_dir.sort()
    return files_dir[-1]

def ret_filename(date, path_name="testdata" ,num = 5):#numの日数分のファイル名をreturn
    filelist = glob.glob("./{}/{}/*.dat".format(path_name, date))
    filelist = list(map(os.path.basename, filelist))
    filelist.sort()
    return filelist[num*-1:]


data_list = ret_filename(ret_path("./Generator_data/data"))
print(data_list)
