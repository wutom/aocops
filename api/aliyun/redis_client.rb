require 'redis'

module Aliyun
  # reids client
  module RedisClient
    REDIS_HOST = 'redis://192.168.1.210:7100'.freeze

    def redis_set(key, value)
      redis = Redis.new(url: REDIS_HOST)
      redis.set(key, value)
    rescue Redis::BaseError => e
      puts e.inspect
      return nil
    end

    def redis_get(key)
      redis = Redis.new(url: REDIS_HOST)
      redis.get(key)
    rescue Redis::BaseError => e
      puts e.inspect
      return nil
    end

    def redis_del(key)
      redis = Redis.new(url: REDIS_HOST)
      redis.del(key)
    rescue Redis::BaseError => e
      puts e.inspect
      return nil
    end
  end
end
