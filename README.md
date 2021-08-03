# TextbookAnalysis

# Steps to setup Infra. [TO BE EDITED]

1. `docker build -t fastapi:latest .`
2. `docker run -p 5000:5000 fastapi:latest`
3. [Optional]
```
url “https://awscli.amazonaws.com/AWSCLIV2.pkg" -o “AWSCLIV2.pkg”
sudo installer -pkg AWSCLIV2.pkg -target /
```
4. `aws configure`

5. `aws ecr get-login-password  --region us-east-2 | docker login --username AWS --password-stdin 483011899007.dkr.ecr.us-east-2.amazonaws.com`

6. `docker tag api:latest 483011899007.dkr.ecr.us-east-2.amazonaws.com/textbookanalysis`

7. `docker push 483011899007.dkr.ecr.us-east-2.amazonaws.com/textbookanalysis`

8. `ssh -i ta.pem ec2-user@ec2-3-139-59-49.us-east-2.compute.amazonaws.com`

9. `aws ecr get-login --region us-east-2 --no-include-email`

10. `run the output from the previous implementation`

11. `docker pull 483011899007.dkr.ecr.us-east-2.amazonaws.com/textbookanalysis:latest`

12. `docker run -p 5000:5000 483011899007.dkr.ecr.us-east-2.amazonaws.com/textbookanalysis`

` docker run -v ~/.aws/:/root/.aws:ro -p 5000:5000 483011899007.dkr.ecr.us-east-2.amazonaws.com/textbookanalysis -e AWS_PROFILE=default`

13. aws ec2 create-vpc-endpoint --vpc-id vpc-a81371c3 --service-name com.amazonaws.us-east-2.dynamodb --route-table-ids rtb-11aa22bb