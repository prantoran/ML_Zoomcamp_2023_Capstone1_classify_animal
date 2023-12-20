# ML_Zoomcamp_2023_Capstone1_classify_animal

My capstone project ML Zoomcamp 2023 aimed to classify animals from pictures (because animals are cute! ❤️🐱🐕🐎).

## Dataset

The dataset is from Kaggle (https://www.kaggle.com/datasets/alessiocorrado99/animals10) which has total 26,179 images of 10 animals:
| Category      | Total pictures    |
|---------------|-------------------|
| 🐑 pecora / sheep         | 1820  |
| 🦋 farfalla / butterfly   | 2112  |
| 🐮 mucca / cow            | 1866  |
| 🐘 elefante / elephant    | 1446  |
| 🕷️ ragno / spider         | 4821  |
| 🐱 gatto / cat            | 1668  |
| 🐕 cane / dog             | 4863  |
| 🐥 gallina / chicken      | 3098  |
| 🐿️ scoiattolo / squirrel  | 1862  |
| 🐎 cavallo / horse        | 2623  |



## Creating script from notebook
```
jupyter nbconvert --to script notebook.ipynb
```

### Docker
#### Build
```
docker build -t animal-model .
```
#### Run
```
docker run -it --rm -p 8080:8080 animal-model:latest
```

### Creating λ function
#### Setup CLI
```bash
pip install awscli
aws configure
```
#### Create repository for docker image
```bash
aws ecr create-repository --repository-name animal-tflite-images
```
- Stdout:
```json
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:eu-west-1:xoxoxoxoxoxo:repository/animal-tflite-images",
        "registryId": "xoxoxoxoxoxo",
        "repositoryName": "animal-tflite-images",
        "repositoryUri": "xoxoxoxoxoxo.dkr.ecr.eu-west-1.amazonaws.com/animal-tflite-images",
        "createdAt": 1703053160.0,
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}
```
#### Log into ecr
```
aws ecr get-login --no-include-email | sed 's/[0-9a-zA-Z=]\{20,\}/PASSOWRD/g'
$(aws ecr get-login --no-include-email)
```

```bash
ACCOUNT=xoxoxoxoxoxo
REGION=eu-west-1
REGISTRY=animal-tflite-images
PREFIX=${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com/${REGISTRY}

TAG=animal-model-xception-v4-001
REMOTE_URI=${PREFIX}:${TAG}

echo $REMOTE_URI
    xoxoxoxoxoxo.dkr.ecr.us-west-1.amazonaws.com/animal-tflite-images:animal-model-xception-v4-001

docker tag animal-model:latest ${REMOTE_URI}
docker push ${REMOTE_URI}
```

#### Create Lambda function using the docker image uploaded into ECR
- Upate the maximum execution time to 30 seconds.

#### Setup public URI for the lambda function using API Gateway
- API GateWay -> Rest API -> Build -> Set a name (i.e. animal-classifcation) -> Create API
- Create resource -> Set Resource name to `predict` -> Create resource
- For `/predict`, Create method -> Method type POST
- Integration type is Lambda function 
- Set region and arn for Lambda function
- Test with request body:
```
{
    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS43GnsWMaclquIceMZNGL6uUVeeHmAkh3lphE5M3Wh8A&s"
}
```
- Deploy API with new stage and named it `test` to generate the public invoke url

Here is demo public URL for testing: https://7sd6z109se.execute-api.eu-west-1.amazonaws.com/test/predict
- The test.py script can be run for testing by setting the url of an image inside the script.