require 'fileutils'

if ARGV.empty?
  puts "Usage: ruby create_dirs.rb <#ps>"
  exit 1
end

ps_number = ARGV.first

langs = { cpp: 'cpp', octave: 'm', python: 'py', ruby: 'rb' }

langs.each do |lang, extension|
  project_name = "ps#{ps_number}"
  project_dir = "#{project_name}_#{lang}"
  FileUtils::mkdir_p "#{project_dir}/input"
  FileUtils::mkdir_p "#{project_dir}/output"

  # copy templates
  if File.exist?("templates/#{lang}")
    Dir["templates/#{lang}/*"].each do |file|
      File.open("#{project_dir}/#{File.basename(file)}", 'w+') do |dest|
        File.open(file) do |src|
          dest.puts src.read.gsub('<project_name>', project_name)
        end
      end
    end
  end

  project_file = "#{project_dir}/ps#{ps_number}.#{extension}"
  unless File.exist? project_file
    FileUtils.touch project_file
  end
end
