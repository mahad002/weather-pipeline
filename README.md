# Weather Pipeline

A data pipeline for weather data collection, processing, and prediction.

[![Jenkins Build Status](http://localhost:8080/buildStatus/icon?job=weather-pipeline)](http://localhost:8080/job/weather-pipeline/)
[![GitHub Actions](https://github.com/mahad002/weather-pipeline/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/mahad002/weather-pipeline/actions/workflows/ci-cd.yml)

## Project Structure

\`\`\`
weather-pipeline/
├── airflow/               # Airflow DAGs
├── data/                  # Data directory
│   ├── raw/              # Raw collected data
│   └── processed/        # Processed data
├── model/                # Model directory
├── scripts/              # Python scripts
└── ...
\`\`\`

## Setup

1. Create virtual environment:
   \`\`\`bash
   python -m venv airflow_venv
   source airflow_venv/bin/activate  # Linux/Mac
   # or
   .\\airflow_venv\\Scripts\\activate  # Windows
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Initialize DVC:
   \`\`\`bash
   dvc init
   \`\`\`

## CI/CD Setup

### GitHub Actions
The project uses GitHub Actions for CI/CD. The workflow is defined in `.github/workflows/ci-cd.yml` and runs on every push and pull request.

### Jenkins Setup
1. Install Jenkins:
   \`\`\`bash
   # For Ubuntu/Debian
   wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
   sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
   sudo apt-get update
   sudo apt-get install jenkins
   \`\`\`

2. Start Jenkins:
   \`\`\`bash
   sudo systemctl start jenkins
   sudo systemctl status jenkins  # Check status
   \`\`\`

3. Get initial admin password:
   \`\`\`bash
   sudo cat /var/lib/jenkins/secrets/initialAdminPassword
   \`\`\`

4. Access Jenkins at http://localhost:8080

5. Install required plugins:
   - Git
   - Pipeline
   - Docker Pipeline
   - Kubernetes CLI

6. Configure credentials:
   - Go to Jenkins > Credentials > System > Global credentials
   - Add DockerHub credentials (ID: dockerhub-credentials)
   - Add GitHub credentials (ID: github-credentials)

7. Create new pipeline:
   - Click "New Item"
   - Enter "weather-pipeline" as name
   - Select "Pipeline"
   - In Pipeline section, select "Pipeline script from SCM"
   - Select "Git" as SCM
   - Enter your repository URL
   - Set branch to */main
   - Script Path: Jenkinsfile

## Usage

1. Start Airflow:
   \`\`\`bash
   airflow standalone
   \`\`\`

2. Run the pipeline:
   \`\`\`bash
   dvc repro
   \`\`\`

## Development

- Use \`