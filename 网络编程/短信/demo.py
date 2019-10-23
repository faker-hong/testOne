import random
from xml.etree import ElementTree 
from smsapi import JSMS_SMS_API #引入江苏美圣短信接口类


"""
公司 ：江苏美圣信息技术有限公司
电话 ：400-600-0599
开发文档：http://www.jsmsxx.com/api/http_doc
python版本：3.x+
说明：JSMS_SMS_API是接口类的封装，供开发者参考使用，以下演示如何调用短信接口：
"""
if ( __name__ == "__main__"):
   
    sms=JSMS_SMS_API.get_instance();
    api_result_xml=""#接口返回值


    #发送模板短信，此处用短信验证码演示 ，模板短信不需要审核
    rand=random.randint(1000, 9999)
    rand2 = 123
    api_result_xml=sms.sendTplSms("JSM43002-0002","18757179539","@1@=%d,@2@=%d" % (rand, rand2))
    '''
    致开发者：如果您开发的短信功能对外开发，则需要在短信发送页加图形验证码 和 短信发送频率的控制，否则您的程序可能被恶意利用！
    '''

    #发送普通短信，普通短信需要审核
    #api_result_xml=sms.sendSms( "手机号码","PYTHON调用美圣短信接口，成功通知！")


    #获得状态报告
    #api_result_xml=sms.queryReport();


    #获得上行短信
    #api_result_xml=sms.queryMo();



    #获取短信帐号余额
    api_result_xml=sms.getAmount();


    #以下是对接口返回的xml结果的解析
    root = ElementTree.fromstring(api_result_xml)  
    status=root.find("mt/status")#获取返回值中的状态，为0代表成功，参数文档：http://www.jsmsxx.com/api/http_doc
    print(status);


