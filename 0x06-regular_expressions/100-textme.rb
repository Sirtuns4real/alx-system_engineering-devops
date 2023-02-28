#!/usr/bin/env ruby
# script should output: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[from:(\w*).*to:(\+\d+).*flags:(\-\d:\d:\-\d:\d:\-\d)/).join(",")
