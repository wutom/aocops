require File.dirname(__FILE__) + '/ecs'

module Aliyun
  # Query instance status information
  class DescribeInstance
    parameters = {
      Action: 'DescribeInstances',
      RegionId: 'cn-beijing',
      PageSize: 50
    }
    ecs = ECS.new
    all_params = ecs.merge_parameters(parameters)
    sign_params = ecs.string_sign(all_params)
    ali_response = ecs.http_get(sign_params)
    if ali_response.nil?
      print 'False'
      exit 1
    elsif ecs.redis_set('aliyun_host_info', ali_response).nil?
      print 'False'
      exit 1
    else
      print 'True'
      exit 0
    end
  end
end
