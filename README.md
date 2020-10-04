# Configure Java Spring Application with Configmap on Kubernetes

When bringing an application into production, we often want to go through several stages to ensure that the application runs smoothly and fulfills all requirements. Some properties of the application might change between the stages, for example the URLs of external services that we need to connect to. 

Spring Boot allows us to define such properties externally. In this proof-of-concept, we built an example system where:
* The application can be run and tested locally using docker-compose. Properties for the test-environment are given via a Docker volume mount.
* The application is tested with a feature-test (using python's behave). This test is fully automatized and included in a github-workflow pipeline which runs at every push.
* The application can be deployed to Kubernetes via helm. Application properties can be defined in the values.yaml for every stage and are mounted into the container as ConfigMaps.


### Prerequisite to run the POC on your machine
* Docker installed
* kubectl and helm installed
* connection to a Kubernetes cluster (any cloud, or best locally, either minikube or Docker for Desktop)
* Java and/or Python is not required locally, as we built everything within Docker containers.


## Step 1: Develop locally
The Java application can be started locally with `docker-compose up --build`.

Once it's built and the application is up, you can request a greeting with `curl "localhost:8080?name=<your name>"`.

The application can be configured via [application.properties](./hello-world/src/main/resources/application.properties) and [application-test.properties](./test/application-test.properties) (while the latter has precedence), a restart is required.

A feature-file can be found in the [feature](./feature/)-folder and the tests can be run with `test/start-test.sh`.


## Step 2: Deploy on Kubernetes

To deploy on Kubernetes, we first need to build the Docker image. This can be done with:
`docker build -f hello-world/Dockerfile -t hello-world:tag .`

In a production environment, we probably would like to automatize the build process in a pipeline. Certainly we would need to push the image to a repository which is reachable from the Kubernetes cluster. As we run Kubernetes locally, this is not necessary.

Configuration that is valid for all stages is set in the [hello/values.yaml](./deployment/hello/values.yaml). In our example, we would set the name of the image (hello-world) here.

Configuration that is stage-specific is set in the [qa/values.yaml](./deployment/hello/stages/qa/values.yaml) and [prod/values.yaml](deployment/hello/stages/prod/values.yaml). In our example, this is the tag, the configuration for the greeting (which gets more formal from stage to stage) and the port.

Once everything is set as desired, we can deploy the service:
* `cd deployment`
* `helm upgrade -f stages/qa/values.yaml hello-qa hello` or `helm upgrade -f stages/prod/values.yaml hello-prod hello`

In this example, the services listen on port 8081 for QA and 8082 for production. In a real case, we might consider to deploy them on different clusters. So we can request a greeting with `curl "localhost:8081?name=<your name>"`.

To upgrade the service, there are two ways:
* Upgrade the software: Make changes in the Java code, build a new image (with new tag) and change the tag in the values.yaml.
* Only change configuration in the values.yaml, for example the greeting that should be used.

After these changes, the new version is deployed with `helm upgrade -f stages/<stage>/values.yaml hello-<stage> hello`.

The delete the deployment, run `helm delete hello-<stage>`. To list all deployments: `helm ls`.