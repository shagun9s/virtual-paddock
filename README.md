# Virtual Paddock 🏎️

An interactive F1 car builder where users configure a virtual race car and receive real-time performance telemetry, powered by a fully serverless AWS backend.

**[Live Demo →](https://d3hpqacv5c25zl.cloudfront.net)**

## What it does

Users select a team livery and configure six components — Power Unit, Tyre Compound, Aerodynamics, Suspension, Brake System, and Fuel Load — and the app calculates seven performance metrics in real time: Power, Cornering, Top Speed, Braking, Reliability, Balance, and Fuel Efficiency, along with an Overall Rating and telemetry readouts.

## Architecture

User → CloudFront → S3 (index.html)
↓
API Gateway (POST /calculate)
↓
AWS Lambda (Python)
↓
DynamoDB (F1Parts table)

| Service | Purpose |
|---|---|
| Amazon S3 | Static frontend hosting |
| Amazon CloudFront | Global CDN + HTTPS |
| Amazon API Gateway | Public HTTP API endpoint |
| AWS Lambda | Serverless performance calculation engine |
| Amazon DynamoDB | Parts catalogue storage |
| AWS IAM | Least-privilege Lambda execution role |

## Tech stack

- **Frontend**: HTML, CSS, JavaScript (single-file, no framework)
- **Backend**: Python 3.12 on AWS Lambda
- **Database**: DynamoDB (On-Demand billing)
- **Hosting**: S3 + CloudFront

## Cost

Entire stack runs within AWS Free Tier. Estimated monthly cost for demo usage: **$0**

## Project structure

virtual-paddock/
├── index.html          # Frontend — all HTML, CSS, JS
└── lambda_function.py  # AWS Lambda function (Python)

## AWS Solutions Architect learning goals covered

- Serverless compute (Lambda)
- API design and CORS configuration (API Gateway)
- NoSQL data modelling (DynamoDB)
- Static hosting and CDN patterns (S3 + CloudFront)
- IAM least-privilege access control
