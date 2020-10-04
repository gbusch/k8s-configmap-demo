FROM adoptopenjdk/maven-openjdk11 as development

WORKDIR /work
ADD hello-world/pom.xml /work/
RUN mvn dependency:resolve-plugins dependency:go-offline

ADD hello-world/src /work/src
RUN mvn -q package --quiet

FROM openjdk:11-jdk-slim as deployment
WORKDIR /
COPY --from=development /work/target/*.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]