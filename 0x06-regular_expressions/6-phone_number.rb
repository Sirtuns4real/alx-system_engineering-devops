#!/usr/bin/env ruby
# , create a Ruby script that accepts one argument and pass it to a regular expression matching method

puts ARGV[0].scan(/^\d{1,4}\s?-?+\d{1,3}\s?-?\d{1,4}$/).join
