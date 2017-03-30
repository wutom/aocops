require File.dirname(__FILE__) + '/../aliyun'

module Aliyun
  # SMS interface initialize class
  class SMS
    include Signature
    include HttpClient
    include RedisClient

    def initialize
      @url = 'https://sms.aliyuncs.com/'
      @public_parameters = {
        AccessKeyId: ACCESS_ID,
        Format: 'JSON',
        SignatureMethod: 'HMAC-SHA1',
        SignatureVersion: '1.0',
        SignatureNonce: UUID.new.generate,
        Timestamp: Time.now.utc.iso8601,
        Version: '2016-09-27'
      }
    end
  end
end
