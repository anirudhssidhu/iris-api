# iris-api (clean start)

Project wiring:
- Project ID: vocal-marking-473407-c4
- GAR repo: iris-api (region asia-south1)
- Cluster: autopilot-cluster-1 (asia-south1)
- Namespace: iris-api
- Model: gs://mlops-course-vocal-marking-473407-c4-unique/my-models/iris-classifier-week-1/model.joblib

## Secrets to add in GitHub
GCP_PROJECT_ID=vocal-marking-473407-c4
GAR_LOCATION=asia-south1
GAR_REPO=iris-api
IMAGE_NAME=iris-api
GKE_CLUSTER=autopilot-cluster-1
GKE_LOCATION=asia-south1
K8S_NAMESPACE=iris-api
GCP_CREDENTIALS_JSON=<paste full JSON>

Then run Actions: Build & Push → Deploy to GKE.
