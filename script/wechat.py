#!/usr/bin/python
#_*_coding:utf-8 _*_

 
import urllib,urllib2
import json
import sys
import simplejson

reload(sys)
sys.setdefaultencoding('utf-8')


def gettoken(corpid,corpsecret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    print  gettoken_url
    try:
        token_file = urllib2.urlopen(gettoken_url)
    except urllib2.HTTPError as e:
        print e.code
        print e.read().decode("utf8")
        sys.exit()
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token
 
 
 
def senddata(access_token,user,subject,content):
 
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    send_values = {
        "touser":"touser",    
        "toparty":"2",    
        "msgtype":"text",
        "agentid":"1", 
        "text":{
            "content":subject + '\n' + content
           },
        "safe":"0"
        }
#    send_data = json.dumps(send_values, ensure_ascii=False)
    send_data = simplejson.dumps(send_values, ensure_ascii=False).encode('utf-8')
    send_request = urllib2.Request(send_url, send_data)
    response = json.loads(urllib2.urlopen(send_request).read())
    print str(response)
 
 
if __name__ == '__main__':
    user = str(sys.argv[1])     #zabbix one content
    subject = str(sys.argv[2])  #zabbix two content
    content = str(sys.argv[3])  #zabbix three content

    corpid =  'wx3323878d0f7d465a'   #CorpID compaty corpid
    corpsecret = 'eC3JO6rEsFXsqRsxAZcWBpDRWA0Df09jPHIobDZ19oGVJrkgY11qnPBj4Q0HShE5'  #corpsecretSecret administrators keys
    accesstoken = gettoken(corpid,corpsecret)
    senddata(accesstoken,user,subject,content)
