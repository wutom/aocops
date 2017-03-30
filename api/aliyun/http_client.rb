require 'rest-client'
require 'json'

module Aliyun
  # http request module
  module HttpClient
    # Initiate a request
    def http_get(parameters)
      response = RestClient.get("#{@url}?#{parameters}")
      if response.code == 200
        return response.body
      end
    rescue RestClient::ExceptionWithResponse => e
      puts JSON.parse(e.response.body)
      return nil
    end
  end
end
