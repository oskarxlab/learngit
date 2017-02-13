#!/usr/bin/env python
#coding: utf-8
import time
import urllib,urllib2
import json
import sys
# baseurl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
# securl = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % access_token
class WeChatMSG(object):x
    def __init__(self,content):
        self.gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        self.gettoken_content = {
                            'corpid' : 'wx3323878d0f7d465a',
                            'corpsecret'eC3JO6rEsFXsqRsxAZcWBpDRWA0Df09jPHIobDZ19oGVJrkgY11qnPBj4Q0HShE5' ,
                            }
        self.main_content = {
                            "toparty":"2",
                            "agentid":"1",
                            "msgtype":"text",
                            "text":{
                            "content":content,
                                    }
                            }
   def get_access_token(self,string):
        token_result = json.loads(string.read(),ensure_ascii=False)
        access_token=  token_result['access_token']
        return access_token.encode('utf-8')
    def geturl(self,url,data):
        data = self.encodeurl(data)
        response = urllib2.urlopen('%s?%s' % (url,data))
        return response.read().encode('utf-8')

    def posturl(self,url,data,isjson = True):
        if isjson:
            data = json.dumps(data,ensure_ascii=False)
        response = urllib2.urlopen(url,data)
        return response.read().encode('utf-8')
    def encodeurl(self,dict):
        data = ''
        for k,v in dict.items():
            data += '%s=%s%s' % (k,v,'&')
        return data
if __name__ == '__main__':
    if len(sys.argv) == 4:
        touser,notuse,content = sys.argv[1:]
    else:
        print 'error segments, now exit'
        sys.exit()
    msgsender = WeChatMSG(content)
    access_token_response = msgsender.geturl(msgsender.gettoken_url, msgsender.gettoken_content)
    access_token =  json.loads(access_token_response)['access_token']
    sendmsg_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % access_token
    print msgsender.posturl(sendmsg_url,msgsender.main_content)
                                                                   

