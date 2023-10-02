![genomic-dash-logo](https://github.com/BIA-lab/genomic-dash/assets/48869631/e1c6b505-8f16-4881-9744-1900b4d7ae83)

# Genomic-Dash Repository

This repository aims to serve as a base to future works about genomic dashboards

## Feeding the dashboard with metadata

Create your metadata based on the the structure of [data/template_metadata.csv](data/template_metadata.csv) and save as `./data/<pathogen>/metadata.csv`
For example, if you are working with Dengue, save your metadata on data/dengue/metadata.csv

## How to setup and run the dashboard:

1. Make sure you have Docker installed. For more information access: https://docs.docker.com/engine/install/
2. Open the terminal (comand line) inside the folder where the dockerfile is located.
3. Build the image: `docker build -t genomic-dashboard .`
4. Run the Docker container: `docker run -p 8511:8511 --name genomic-dashboard -d genomic-dashboard .` 
5. You can view your Dashboard in your browser URL: http://0.0.0.0:8511

## Tutorials

### VEME 2023 Pathogen Dashboards - DENV-1 Dashboard (Half day module)

In this workshop we show how to use VIPR database and Genome Detective to generate a DENV-1 dataset from Dengue in Africa, and how to build a dashboard with the Degue data using the Genomic Dash Framework

<br>
<b>Generate the dengue_1 dataset: </b>

There are two ways to obtain the dataset to feed the Dengue Dashboard. Accessing the VEME Pathogen Workflow available on Terra and running the Jupyter Notebook with the data processing code in your own computer.

<br>

Using Terra:

<br>

1. Open the <a href='https://app.terra.bio/#workspaces/veme-training/VEME%202023%20Pathogen%20Dashboards'> VEME 2023 Dashboards halfway Module - Terra Workspace </a> in your browser. Create an account on terra if necessary.
2. Browse to the "ANALYSES" menu.
3. Open the "Dashboard data cleaning.ipynb" code 
4. Follow the steps on the code and run everything to generate the dengue_1.csv dataset at the end
5. Click on the generated dataset link at the end to download it.

<br>

Using Jupyter Notebook:

<br>

1. Browse to the tutorials -> veme2023_dengue1 folder in this repository.
2. Open the "dashboard_data_cleaning.ipynb" code using Jupyter Lab (or Google Colab as an alternative)
3. Follow all the steps on the code and run everything to generate the dengue_1.csv dataset at the end. Pay attention at the following parts:


- Make sure to fill the variable "metadata_path" value with the path to the "VIPR_database.csv" file;
- Make sure to fill the variable Entrez.email with your own email;
- Make sure to fill the variable "output_file_path" value with the path you want to save the "dengue_1.csv" final result.

<br>
Obs: If you are using Google Colab, make sure to import the VIPR_databasae.csv file (located in the tutorials -> veme2023_dengue1 folder) to the Colab enviroment.

<br>
<br>
<b>Customize the dashboard: </b>

1. Download the pathogen dataset you've generated using the Jupyter Notebook or using Terra. In this case it is the "dengue_1.csv" file.

2. Browse to the DENV1_dashboard_veme_2023 -> app -> data folder, and create a new folder called "dengue".

3. Copy the dataset file that you've download from Terra (dengue_1.csv) from the "Downloads" folder and paste it inside the "dengue" folder you've just created.

4. Edit the python codes inside the DENV1_dashboard_veme_2023 -> app folder in order to customize the dashboard. To edit the codes you can use any code editor or IDE. If you don't have any of them you could download and install one of these suggestions: Pycharm, VScode)

5. Locate the "pathogen_1.py" file, inside the "pages" folder, and change the dataset location string (line 21). Write the full location to the "dengue_1.csv" dataset you have downloaded.  

6. If you wish, You can also change the dashboard's title on the "header.py" file (line 7), located inside the "pages" folder.

7. And also you could change the menu title on the "pathogen_1.py" file (line 29).

8. In the "dicts.py" file, fill the "dengue_categories" list with the names of the different types of category within the "category_2" dataset column (unique category_2 values).

<br>
<b>Build the Docker image: </b>

docker build -t genomic-dashboard .

<br>
<b>Run the Docker container: </b>
docker run -p 8511:8511 --name genomic-dashboard -d genomic-dashboard .

## Reference
<br>
For further informations about genomic dashboards please go to <a href="https://www.nature.com/articles/s41564-022-01276-9"> SARS-CoV-2 Africa dashboard for real-time COVID-19 information </a>

## Reach Us
<br>
If you have any question please contact us through the following e-mail address: 
joicy.xavier@ufvjm.edu.br or joicy@sun.ac.za
