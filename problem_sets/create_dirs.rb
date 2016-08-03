#!/usr/bin/env ruby

require 'fileutils'

if ARGV.empty?
  puts "Usage: ruby create_dirs.rb <ps#>"
  exit 1
end

ps_number = ARGV.first

langs = { cpp: 'cpp', octave: 'm', python: 'py', ruby: 'rb' }

langs.each do |lang, extension|
  problem_set = "ps#{ps_number}"
  ps_dir = "#{problem_set}/#{problem_set}_#{lang}"
  ps_file = "ps#{ps_number}.#{extension}"

  FileUtils::mkdir_p "#{ps_dir}/input"
  FileUtils::mkdir_p "#{ps_dir}/output"

  # copy templates
  if File.exist?("templates/#{lang}")
    Dir["templates/#{lang}/*"].each do |template|
      destination_file_name = File.basename(template)

      if destination_file_name == "main.#{extension}"
        destination_file_name = ps_file
      end

      File.open(File.join(ps_dir, destination_file_name), 'w+') do |dest|
        File.open(template) do |src|
          dest.puts src.read.gsub('<ps#>', problem_set)
        end
      end
    end
  end

  unless File.exist? File.join(ps_dir, ps_file)
    FileUtils.touch File.join(ps_dir, ps_file)
  end
end
