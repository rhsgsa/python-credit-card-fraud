## README.md

Show AI/ML Demo
## Access Right
oc new-project staging

oc create serviceaccount pipeline

oc policy add-role-to-user admin system:serviceaccount:pipeline:pipeline -n staging

oc new-project sit

oc policy add-role-to-user admin system:serviceaccount:pipeline:pipeline -n sit

oc policy add-role-to-user system:image-puller system:serviceaccount:sit:default -n staging

## Staging build and deployment
oc new-build --name=python-credit-card-fraud --binary --image-stream=python:latest or oc apply -f staging-build-config.yaml

oc apply -f staging-image.yaml

oc start-build python-credit-card-fraud --from-dir=. --follow -n staging

oc new-app ython-credit-card-fraud or oc apply -f staging-deployment.yaml

oc apply -f staging-service.yaml

oc apply -f staging-route.yaml

## SIT deployment 
oc -n staging tag staging/python-credit-card-fraud:latest sit/python-credit-card-fraud:sit

oc -n $(params.currentenv) tag $(params.currentenv)/$(params.imagename):latest $(params.nextenv)/$(params.imagename):sit

oc apply -f sit-deployment.yaml

oc apply -f sit-service.yaml

oc apply -f sit-route.yaml