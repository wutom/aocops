require 'cgi'
require 'time'
require 'uuid'
require 'base64'
require 'openssl'

# Aliyun public module
module Aliyun
  ACCESS_SECRET = ''.freeze
  ACCESS_ID = ''.freeze

  # Signature parameters module
  module Signature
    # String encoding
    def percent_encode(value)
      CGI.escape(value.to_s).gsub('+', '%20').gsub('%7E', '~')
    end

    # Sort the parameters first and then use utf-8 to encode the parameters
    # and then calculate the HMAC value
    # and finally use the Base64 encoding rules on the HMAC value encoding
    def string_sign(hash)
      sort_parameters = hash.sort.to_h
      canonicalized_string = ''
      string_to_sign = "GET&#{percent_encode('/')}&"
      i = 0
      sort_parameters.each do |k, v|
        canonicalized_string.concat('&') if i > 0
        canonicalized_string.concat("#{percent_encode(k)}=#{percent_encode(v)}")
        i += 1
      end
      string_to_sign.concat(percent_encode(canonicalized_string))
      digest = OpenSSL::Digest.new('sha1')
      hmac = OpenSSL::HMAC.digest(digest, "#{ACCESS_SECRET}&", string_to_sign)
      signature = Base64.strict_encode64(hmac)
      canonicalized_string.concat("&Signature=#{percent_encode(signature)}")
    end

    # Get the full request parameter
    def merge_parameters(parameters)
      @public_parameters.merge!(parameters)
    end
  end
end
