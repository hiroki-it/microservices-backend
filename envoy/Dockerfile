# @see https://www.envoyproxy.io/docs/envoy/latest/start/docker#build-and-run-a-docker-image
FROM envoyproxy/envoy:v1.20.1
COPY ./envoy/envoy.yaml /etc/envoy/envoy.yaml
RUN chmod go+r /etc/envoy/envoy.yaml
