require File.dirname(__FILE__) + '/../aliyun'

module Aliyun
  # ECS interface initialize class
  class ECS
    include Signature
    include HttpClient
    include RedisClient

    def initialize
      @url = 'https://ecs.aliyuncs.com/'
      @public_parameters = {
        AccessKeyId: ACCESS_ID,
        Format: 'JSON',
        SignatureMethod: 'HMAC-SHA1',
        SignatureVersion: '1.0',
        SignatureNonce: UUID.new.generate,
        Timestamp: Time.now.utc.iso8601,
        Version: '2014-05-26'
      }
    end
  end
end
