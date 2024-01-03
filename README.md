# gcp-devops-demo
Repo to hold DevOps Demo with Python Flask built on GCP


## Environment Set up

* ensure you environment can push / pull into github
* I am using Google Cloud Shell so the set up is quite minimal

## App Set up

* See `/sample-app/`
* I asked my ChatGPT Software Engineer Persona for the code you see

## GCP Artifact Registry Setup

* You can follow the docs for Artifact Registry
* If you are using the native Google Cloud Shell Environment there are far fewer steps involved with auth and all that
* after docker build in the cli use:

```bash
docker tag SOURCE-IMAGE LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE:TAG

docker push LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE
```

## Preping for Cloud Run

There are many way to run your code in GCP.
Packaging it up in Docker is a smart way of making it portable. You could run it on a VM, in a K8s cluster, in App Engine, or Cloud Run.  For this example we will be sticking with Cloud Run as its the cheapest as there is no continual upkeep and you only get charged per invokation very similar to Cloud Functions.

I have another baby app that I built with ChatGPT that can be found here https://myapp-tj4p6ap2ta-uc.a.run.app/

After some poking around, and fixing a port start up assignment Issue. I got the app hosted, Here: https://sample-app-tj4p6ap2ta-uc.a.run.app/

## Setting up Build and Deployment Automation with Cloud Build

At this stage in the game I've been doing these steps pretty manually.  Which is perfectly fine for getting a skelleton up and running, but its gunna get pretty annoying to deal with here shortly.  As Google and the SRE Book put it, all this manual work is toil that needs to be reduced.

I want to show what I have to start with via the GCP docs.

```yaml
# Test Cloud Builder file

# From https://cloud.google.com/build/docs/configuring-builds/create-basic-configuration
steps:
  # Docker Build
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build',
            '-t',
            'us-central1-docker.pkg.dev/cloud-devops-viking-test-area/demo-sample-app/sample-app',
            '.']
  # Docker Push
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push',
            'us-central1-docker.pkg.dev/cloud-devops-viking-test-area/demo-sample-app/sample-app']
```

These steps handle the build of the container image and the pushing of that image into our Artifact Registry. At this stage we already have a Cloud Build Service Set up.  I just now need to tell Cloud Build about this, the details surrounding the desired entry point, the arguments and which container image.  Lastly I will need add a Tigger to fire based on changes in the source.