from flask import Flask , request,render_template
import json
from flask_cors import CORS
from save import savedata
app = Flask(__name__)
CORS(app)
@app.route("/findgender", methods=["GET", "POST"])
def findGender():
     sdata=savedata()
     man,woman,others=sdata.find_gennder()
     responce={'sexdata': [{'name':'男', 'value':man},{'name':'女', 'value':woman},{'name':'未知', 'value':others}]}
     return  responce

@app.route("/findvideo", methods=["GET", "POST"])
def findVideo():
     sdata=savedata()
     res=sdata.find_likenum()
     likename=[]
     likelist=[]
     for ri in res:
          likename.append(ri[0])
          likelist.append(ri[1])
     responce={'likename':likename,'likelist':likelist}
     return  responce




# if __name__ == '__main__':
#    app.run(host="localhost",port=9529)
findVideo()