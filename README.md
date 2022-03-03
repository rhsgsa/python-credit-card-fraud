## README.md

Show AI/ML Demo

oc new-build --name=python-credit-card-fraud --binary --image-stream=python:latest or oc apply -f staging-build-config.yaml

oc apply -f staging-image.yaml

oc start-build python-credit-card-fraud --from-dir=. --follow -n staging

oc new-app ython-credit-card-fraud or oc apply -f staging-deployment.yaml

oc apply -f staging-service.yaml

oc apply -f staging-route.yaml
