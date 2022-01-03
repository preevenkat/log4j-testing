FROM ruby:3.1.0

FROM docker.elastic.co/logstash/logstash:5.6.1
RUN bin/ruby -rzip -e \
  'puts Dir.glob(["**/*/logstash-input-tcp-*.jar", "**/*/log4j-core*.jar"]).each \
  {|zip| puts zip; Zip::File.open(zip, create: true) \
  {|zipfile| zipfile.remove("org/apache/logging/log4j/core/lookup/JndiLookup.class") }\
  }'
