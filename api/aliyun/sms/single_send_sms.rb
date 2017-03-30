require File.dirname(__FILE__) + '/sms'

module Aliyun
  # Send a text message
  class SingleSendSms
    phone_num, code = ARGV
    parameters = {
      Action: 'SingleSendSms',
      SignName: '爱接力科技',
      TemplateCode: 'SMS_59060043',
      ParamString: "{\"code\":\"#{code}\"}",
      RecNum: phone_num
    }
    sms = SMS.new
    all_params = sms.merge_parameters(parameters)
    sign_params = sms.string_sign(all_params)
    if sms.http_get(sign_params).nil?
      print 'False'
      exit 1
    else
      print 'True'
      exit 0
    end
  end
end
