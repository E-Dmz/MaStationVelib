PACKAGE_NAME=velibapi
FILENAME=fast

run_locally:
	python -m ${PACKAGE_NAME}.${FILENAME}

run_api:
	uvicorn velibapi.fast:app --reload  # load web server with code autoreload