#!/usr/bin/env python
from flask import *
from datetime import datetime
import glob
import os
import pandas
import search_files as sf

template_html = """                                                                                                        
<html>                                                                                                                     
  <head><title>Generator Monitor</title></head>                                                                                     
  <meta http-equiv="refresh" content="10" >                                                                                
  <link rel="stylesheet" type="text/css" href="/static/style.css"/>                                                        
  <body>                                                                                                                   
    最終更新時間[UTC]：{last_update}<br>                                                                                   
    {table}
  <br>
  </body>                                                                                                                  
</html>                                                                                                                    
"""

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generator")
def return_html():#test code
    #今のyyyymmは
    now = datetime.now()
    str_date = now.strftime("%Y%m")
    str_date = "201609"
    ###最新ファイルを調べます
    filelist = glob.glob("./testdata/{}/*.dat".format(str_date))
    filelist = list(map(os.path.basename, filelist))
    filelist = [i[:-4] for i in filelist]
    filelist.sort()
    filelist[-1]#最新ファイル名
    make_table_html()
    with open("./templates/df1.html") as f:
        html = f.read()
    return render_template("gen_monitor24h.html", in_html = html)

@app.route("/fuel_monitor")
def return_html2_1():
    return render_template("fuel_monitor24h_2.html")

@app.route("/fuel_monitor2")
def return_html2():#test code
    #今のyyyymmは
    now = datetime.now()
    str_date = now.strftime("%Y%m")
    print(str_date)
    ###最新ファイルを調べます
    filelist = glob.glob("./Fuel_data/data/{}/*.dat".format(str_date))
    print("##$", filelist)
    filelist = list(map(os.path.basename, filelist))
    print("###", filelist)
    filelist = [i[:-4] for i in filelist]
    filelist.sort()
    filelist[-1]#最新ファイル名
    make_table_html2()
    with open("./templates/df2.html") as f:
        html = f.read()
    return render_template("fuel_monitor24h.html", in_html = html)

@app.route("/generator120h")
def return_html3():#test code
    #今のyyyymmは
    now = datetime.now()
    str_date = now.strftime("%Y%m")
    str_date = "201609"
    ###最新ファイルを調べます
    filelist = glob.glob("./testdata/{}/*.dat".format(str_date))
    filelist = list(map(os.path.basename, filelist))
    filelist = [i[:-4] for i in filelist]
    filelist.sort()
    filelist[-1]#最新ファイル名
    make_table_html()
    with open("./templates/df1.html") as f:
        html = f.read()
    return render_template("gen_monitor120h.html", in_html = html)

@app.route("/fuel_monitor120h")
def return_html4():#test code
    return render_template("fuel_monitor120h_2.html")

@app.route("/fuel_monitor14days")
def return_html5():#test code
    return render_template("fuel_monitor14days.html")

#最新のデータを読み込み、htmlを生成する。
def make_table_html():#test code
    ret = sf.ret_path()
    ret_f = sf.ret_filename(ret)
    path = "./testdata/{}/{}".format(ret, ret_f[0])
    print(path)
    read_file(path)

#最新のデータを読み込み、htmlを生成する。                                                                  
def make_table_html2():#test code
    ret = sf.ret_path(path="./testdata")
    print("%$%", ret)
    ret_f = sf.ret_filename(ret, path_name = "testdata")
    path = "./testdata/{}/{}".format(ret, ret_f[0])
    print("%%%",path)
    read_file2(path)

def read_file(path):#df.htmlを生成
    header_list = ["year", "month", "day", "hour", "minute", "second", "Oil pressure", "Coolant temp", " ChgAltnV", "Battery voltage", " Engine speed", "Frequency" , "L1-N voltage", "L2-N voltage", "L3-N voltage", "L1-L2 voltage", "L2-L3 voltage", "L3-L1 voltage", "L1 ampare", "L2 ampare", "L3 ampare", "Earth current", "L1 wattage", "L2 wattage", "L3 wattage", "Total wattage", "running generator"]
    ###
    df = pandas.read_csv(path, sep=",", header = 8, names = header_list)#不完全なデータを読み込むことでエラーが出る
    _df = df.iloc[-2]#-1はNunになることあるから-2にしている。雑だが
    dflist = _df.values.tolist()#indexの確認
    _df = pandas.DataFrame(_df).reset_index()
    _df = _df[6:]#datetime部分は表には不要なのでcut
    ###
    dflist = list(map(int, dflist))
    data_dtime = datetime(dflist[0], dflist[1], dflist[2], dflist[3], dflist[4], dflist[5])
    print(data_dtime)
    with open("./templates/df1.html", "w") as f:
        f.write(template_html.format(table = _df.to_html(classes="mystyle", index = False, header = False), last_update = data_dtime))
    pass

def read_file2(path):#df.htmlを生成
    header_list = ["Year", "Month", "Day", "Hour", "Min", "Sec", "temp.powersuply", "temp.box", "temp.fuelfilter65063", "temp.fuelfilter65064", "temp.genhouse", "humidity.genhause", "flowrate.flowmeter65063", "temp.flowmeter65063", "flowrate.flowmeter65064", "temp.flowmeter65064", "temp.heater65063", "temp.heater65064", "highlevelalarm.gen65063", "lowlevelalarm.gen65063", "solenoid.gen65063", "highlevelalarm.gen65064", "lowlevelalarm.gen65064", "solenoid.gen65064", "NC", "NC"]
    ###
    df = pandas.read_csv(path, sep=",", header = 8, names = header_list)#不完全なデータを読み込むことでエラーが出る
    _df = df.iloc[-2]#-1はNunになることあるから-2にしている。雑だが
    dflist = _df.values.tolist()#indexの確認
    _df = pandas.DataFrame(_df).reset_index()
    _df = _df[6:]#datetime部分は表には不要なのでcut
    ###
    dflist = list(map(int, dflist))
    data_dtime = datetime(dflist[0], dflist[1], dflist[2], dflist[3], dflist[4], dflist[5])
    print(data_dtime)
    with open("./templates/df2.html", "w") as f:
        f.write(template_html.format(table = _df.to_html(classes="mystyle", index = False, header = False), last_update = data_dtime))
    pass


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True, port = 12300, threaded = True)
    pass
