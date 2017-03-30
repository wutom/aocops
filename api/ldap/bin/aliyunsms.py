# -*- coding:utf-8 -*-

import sys, os, string, subprocess as sp

#mobile = sys.argv[1]
#newpwd = sys.argv[2]

def SmsSend(mobile,newpwd):
    smssend="ruby /opt/aocdev/aocops/api/aliyun/sms/single_send_sms.rb %s %s" % (mobile, newpwd)
    sms=os.popen(smssend).read()
    return sms

if __name__ == '__main__':
	main()