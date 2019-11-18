#!flask/bin/python
from flask import Flask, jsonify,abort,request,render_template
from flask_cors import CORS


app = Flask(__name__);
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

filename = 'dailyweather.csv'



data =[]
fk = open(filename)
for line in fk:
    commands = {}
    dateVal,tMax,tMin  = line.strip().split(',')
    commands['DATE'] = dateVal
    commands['TMAX'] = tMax;
    commands['TMIN'] = tMin;
    data.append(commands)     
fk.close();

@app.route('/',methods =['GET'])
def index():
    return render_template("ajax.html");


@app.route('/historical/', methods=['GET'])
def get_dates():
    datesList = [];
    for elements in data:
        for key,value in elements.items():
            if(key == 'DATE'):
                dict ={}
                dict[key] = value
        datesList.append(dict)
    return jsonify(datesList)


@app.route('/historical/<dateYYYYMMDD>', methods=['GET'])
def getDateInfo(dateYYYYMMDD):
    datelist=[]
    init = {}
    flag = 0
    for dates in data:
        flag =0
        for key,value in dates.items():
            if key=='DATE':
                if value==dateYYYYMMDD:
                    init ={}
                    flag = 1

            if flag:
                init[key]=value
                datelist.append(init)
    if len(datelist)==0:
        abort(404)
    return jsonify(datelist[0]),200
	
	
@app.route('/historical/<dateYYYYMMDD>', methods=['DELETE'])
def deleteDate(dateYYYYMMDD):
    flag=0
    for info in data:
        for key,value in info.items():
            if key=='DATE':
                if value==dateYYYYMMDD:
                    flag=1
            if flag:
                data.remove(info)
                break
    return jsonify('Response','Success'),204


@app.route('/historical/', methods=['POST'])
def newdata():
    new_list =[]
    info={
    'DATE':request.json['DATE'],
    'TMIN':request.json['TMIN'],
    'TMAX':request.json['TMAX']
    }
    data.append(info)
    return jsonify(info),201


@app.route('/forecast/<dateYYYYMMDD>',methods=['GET'])
def forecast7days(dateYYYYMMDD):
    given_date = dateYYYYMMDD
    
    all_dates = [];
    for info in data:
        for key,value in info.items():
            if(key == 'DATE'):
                dates_dict ={}
                dates_dict[key] = value
        all_dates.append(dates_dict)
    list_year = [2013,2014,2015,2016,2017]
    y = given_date[:4]
    m = given_date[4:6]
    d = given_date[6:8]
    list1 = []
    for i in range(0,7):    
        tmax = ""
        tmin = ""
        for year in list_year:
            add_date = y+m+d
            for dates in data:
                datelist = []
                flag =0
                for key,value in dates.items():
                    if key=='DATE':
                        if value==add_date:
                            init ={}
                            flag = 1
                    if flag:
                        if key == 'TMAX':
                            tmax = value;
                        if key == 'TMIN':
                            tmin = value
                    dic ={"DATE":add_date,"TMAX":tmax,"TMIN":tmin}
        list1.append(dic)
        if(int(d)<10):
            d = "0" + str(int(d)+1)
        else:
            d = str(int(d)+1)
        if(int(d)>30):
            d="01"
            if(int(m)<10):
                m = "0"+str(int(m)+1)
            else:
                m = str(int(m)+1)
    return jsonify(list1)               



if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 80)

