FROM centos:7

USER root

RUN yum groupinstall "Development Tools" -y
RUN yum install ruby ruby-devel -y
RUN gem install bundler --no-ri --no-rdoc
RUN gem install fpm --no-ri --no-rdoc
RUN gem install pleaserun --no-ri --no-rdoc

FROM docker.elastic.co/logstash/logstash:5.6.1
RUN bin/ruby -rzip -e \
  'puts Dir.glob(["**/*/logstash-input-tcp-*.jar", "**/*/log4j-core*.jar"]).each \
  {|zip| puts zip; Zip::File.open(zip, create: true) \
  {|zipfile| zipfile.remove("org/apache/logging/log4j/core/lookup/JndiLookup.class") }\
  }'
