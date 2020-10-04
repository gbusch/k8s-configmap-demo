FROM adoptopenjdk/maven-openjdk11 as development

WORKDIR /work
ADD hello-world/pom.xml /work/
RUN mvn dependency:resolve-plugins dependency:go-offline

ADD hello-world/src /work/src
RUN mvn -q package --quiet

FROM openjdk:11-jdk-slim as deployment
RUN apt-get update && apt-get install -y curl
WORKDIR /
COPY --from=development /work/target/*.jar app.jar

ENV stage=dev

ENTRYPOINT ["java","-jar","/app.jar", "--spring.config.location=classpath:/,file:/config/"]
HEALTHCHECK --interval=5s --timeout=5s --retries=5 CMD curl --fail http://localhost:8080/actuator/health || exit 1