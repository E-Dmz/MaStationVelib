PACKAGE_NAME=velibapi
FILENAME=fast

run_locally:
	python -m ${PACKAGE_NAME}.${FILENAME}

run_api:
	uvicorn velibapi.fast:app --reload  # load web server with code autoreload

# ----------------------------------
#          DOCKER
# ----------------------------------
MULTI_REGION=eu.gcr.io
REGION=europe-west1
PROJECT_ID=le-wagon-bootcamp-328014

DOCKER_IMAGE_NAME=velibapi
BUILD_NAME = ${MULTI_REGION}/${PROJECT_ID}/${DOCKER_IMAGE_NAME}

docker_build:
	docker build --tag=${BUILD_NAME} .

docker_run:
	docker run -e PORT=8080 -p 8080:8080 ${BUILD_NAME}

docker_push:
	docker push ${BUILD_NAME}

gcp_run_deploy:
	gcloud run deploy --image ${BUILD_NAME} \
                	  --platform managed \
                	  --region ${REGION} \
					  --min-instances=0 \
					  --cpu=4\
					  --memory=8Gi