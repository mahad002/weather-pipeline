# Weather Pipeline

A data pipeline for weather data collection, processing, and prediction.

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

- Use \`pytest\` for testing
- Follow PEP 8 style guide
- Update requirements.txt when adding new dependencies

## Deployment

- Docker: \`docker build -t weather-pipeline .\`
- Kubernetes: \`kubectl apply -f kubernetes/\`
