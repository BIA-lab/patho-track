![genomic-dash-logo](https://github.com/BIA-lab/genomic-dash/assets/48869631/e1c6b505-8f16-4881-9744-1900b4d7ae83)

# genomic-dash

This repository is dedicated for the genomic dashboard template

# CLIMADE Africa dashboard
Repository contains code and files to interactive genomics Africa Dashboard

## How to install:
1. Make sure you have Docker installed. For more information access: https://docs.docker.com/engine/install/
2. Build the image: `sudo docker build -t climade-dashboard .`
3. Run the Docker container: `sudo docker run -p 8511:8511 climade-dashboard .` 
4. You can view your Dashboard in your browser URL: http://0.0.0.0:8511

## Data

### Using metadata
Create your metadata based on [data/template_metadata.csv](data/template_metadata.csv) and save as `./data/<pathogen>/metadata.csv`
For example, if you are working with Dengue, save your metadata on data/dengue/metadata.csv
