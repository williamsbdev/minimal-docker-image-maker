ARG BASE
ARG JAVA

FROM ubuntu:16.04 as ubuntu1604
RUN \
  apt-get update && \
  apt-get dist-upgrade -y && \
  apt-get install python -y

FROM centos:7 as centos7
RUN \
  yum update -y

FROM ${BASE} as oracle-java-8u162
COPY server-jre-8u162-linux-x64.tar.gz /tmp/
RUN \
  mkdir -p /data/java/ && \
  tar -zx -C /data/java/ --strip-components=1 -f /tmp/server-jre-8u162-linux-x64.tar.gz

FROM ${BASE} as distro-openjdk-java-8
RUN \
  bash -c "[[ -x /usr/bin/yum ]] && yum install java-1.8.0-openjdk-headless -y || exit 0" && \
  bash -c "[[ -x /usr/bin/apt-get ]] && apt-get install openjdk-8-jre-headless -y || exit 0"

FROM ${JAVA} as java

FROM java as minimal
ADD create_minimal_image.py /data/
WORKDIR /data
RUN \
 export JAVA_HOME=$(readlink -e /usr/bin/java | sed "s:bin/java::") && \
 export JAVA_HOME=${JAVA_HOME:-/data/java/jre} && \
 python create_minimal_image.py ${JAVA_HOME} && \
 mkdir /data/build-output/tmp/ 

FROM scratch as minimal-final
COPY --from=minimal /data/build-output /
WORKDIR /
ENTRYPOINT ["/jre/bin/java"]

FROM minimal-final as spring-boot-example
COPY examples/java-app/spring-boot-web-1.0.jar /app/spring-boot-web-1.0.jar
CMD ["-jar", "/app/spring-boot-web-1.0.jar"]
