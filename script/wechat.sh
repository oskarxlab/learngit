#!/bin/bash
#########################################################################
# File Name: wechat.sh
# Author: shaonbean
# Email: shaonbean@qq.com
# Created Time: Sun 24 Jul 2016 05:48:14 AM CST
#########################################################################
# Functions: send messages to wechat app
# set variables
CropID='wx3323878d0f7d465a'
Secret='eC3JO6rEsFXsqRsxAZcWBpDRWA0Df09jPHIobDZ19oGVJrkgY11qnPBj4Q0HShE5'
GURL="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=$CropID&corpsecret=$Secret"
#get acccess_token
Gtoken=$(/usr/bin/curl -s -G $GURL | awk -F\" '{print $4}')
PURL="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=$Gtoken"
#
function body() {
local int AppID=1                        #appid
local UserID="touser"                        #userid
local PartyID=2                             #partid
local Msg=$(echo "$@" | cut -d" " -f3-)   #zabbix comment
printf '{\n'
printf '\t"touser": "'"$UserID"\"",\n"
printf '\t"toparty": "'"$PartyID"\"",\n"
printf '\t"msgtype": "text",\n'
printf '\t"agentid": "'" $AppID "\"",\n"
printf '\t"text": {\n'
printf '\t\t"content": "'"$Msg"\""\n"
printf '\t},\n'
printf '\t"safe":"0"\n'
printf '}\n'
}
/usr/bin/curl --data-ascii "$(body $! $2 $3)" $PURL
