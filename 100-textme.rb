#!/usr/bin/env ruby

# [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
