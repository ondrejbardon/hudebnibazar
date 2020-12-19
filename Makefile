.PHONY: help package deploy all

LAMBDA_FUNCTION_NAME := hudebnibazar
LAMBDA_FILE_NAME := main.py

clear:
	@rm -rf ./package ${LAMBDA_FUNCTION_NAME}.zip

package: clear
	@pip3 install -r requirements.txt --target ./package
	cd ./package; zip -r9 ../${LAMBDA_FUNCTION_NAME}.zip *
	zip -g ${LAMBDA_FUNCTION_NAME}.zip ${LAMBDA_FILE_NAME}

deploy: clear package
	@echo "Deploying to infra account / eu-west-1"
	AWS_CONFIG_FILE=~/.aws/personal_credentials aws --profile default --region eu-central-1 lambda update-function-code \
		--function-name ${LAMBDA_FUNCTION_NAME} \
		--zip-file fileb://${LAMBDA_FUNCTION_NAME}.zip \
		--publish

all: clear package deploy