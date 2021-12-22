FROM docker.elastic.co/beats/metricbeat:5.6.16
USER root
COPY --chown=root:metricbeat metricbeat.yml /usr/share/metricbeat/metricbeat.yml
RUN chmod 640 /usr/share/metricbeat/metricbeat.yml
CMD ["/usr/share/metricbeat/metricbeat","-e"]
