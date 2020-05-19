import json
from urllib import parse,request

class JSMS_SMS_API:
    '江苏美圣短信接口，官网：http://www.jsmsxx.com'
    __instance=None#此变量非短信接口参数，用于控制短信类的单例

	#以下4个参数可联系江苏美圣客服获取
    __username ="JSM43002"#短信帐号
    __password ="clyckisz"#帐号密码
    __veryCode="3r46kr9swsp3"#通讯认证Key
    __apiurl="http://112.74.76.186:8030/service/httpService/httpInterface.do" #服务器接口路径

    #单例模式
    def __init__(self):
        pass

    #如短信帐号较多， 可每次调用接口前先初始化短信参数
    #def __init__(self,username="",password="",veryCode=""):
    #    JSMS_SMS_API.count=1
    #    if username!="" and  password!="" and  veryCode!="":
    #        self.__username=username
    #        self.__password=password
    #        self.__veryCode=veryCode


    #单例模式
    def get_instance():
        if JSMS_SMS_API.__instance  is None:
             JSMS_SMS_API.__instance=JSMS_SMS_API()
        return JSMS_SMS_API.__instance


    #发送模板短信 
    def sendTplSms(self,tempid,mobile,smstext):
        paras=self.getCommonParas()
        paras['method'] = 'sendMsg'
        paras['mobile'] = mobile;
        paras['content']=smstext;
        paras['msgtype']= '2'
        paras["tempid"]=tempid
        paras['code']= 'utf-8'
        apiresult=self.httpPost(self.__apiurl,paras)
        return apiresult

    #发送普通短信 
    def sendSms(self,mobile,smstext):
        paras=self.getCommonParas()
        paras['method'] = 'sendMsg'
        paras['mobile'] = mobile;
        paras['content']=smstext;
        paras['msgtype']= '1'
        paras['code']= 'utf-8'
        apiresult=self.httpPost(self.__apiurl,paras)
        return apiresult

    #获取余额
    def getAmount(self):
        paras=self.getCommonParas()
        paras['method'] = 'getAmount'
        apiresult=self.httpPost(self.__apiurl,paras)
        return apiresult

    #获得状态报告
    def queryReport(self):
        paras=self.getCommonParas()
        paras['method'] = 'queryReport'
        apiresult=self.httpPost(self.__apiurl,paras)
        return apiresult

    #获得上行短信
    def queryMo(self):
        paras=self.getCommonParas()
        paras['method'] = 'queryMo'
        apiresult=self.httpPost(self.__apiurl,paras)
        return apiresult


    #post请求
    def httpPost(self,url,paras):
        #json串数据使用#
        #postdata = json.dumps(paras).encode(encoding='utf-8')
        #print(postdata)
        #普通数据使用
        postdata2 = parse.urlencode(paras).encode(encoding='utf-8')
        header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
        req = request.Request(url=url,data=postdata2)#,headers=header_dict
        res = request.urlopen(req)
        text = res.read()
        #print(text.decode("utf8"))
        return text
        #输出内容:b'{"jsonrpc":"2.0","result":"37d991fd583e91a0cfae6142d8d59d7e","id":1}'
        #return res.decode(encoding='utf-8')

    #get请求
    def get(url,paras):
        return ""


    #公共参数
    def getCommonParas(self):
        return {"username":self.__username,"password":self.__password,"veryCode":self.__veryCode}