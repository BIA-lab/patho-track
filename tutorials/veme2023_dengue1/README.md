# VEME 2023 Pathogen Dashboards - DENV-1 Dashboard Tutorial

## Generate the dengue_1 dataset:

There are two ways to obtain the dataset to feed the Dengue Dashboard. Accessing the VEME Pathogen Workflow available on Terra and running the Jupyter Notebook with the data processing code in your own computer.

### Using Terra:

1. Open the <a href='https://app.terra.bio/#workspaces/veme-training/VEME%202023%20Pathogen%20Dashboards'> VEME 2023 Dashboards halfway Module - Terra Workspace </a> in your browser. Create an account on terra if necessary.
2. Browse to the "ANALYSES" menu.
3. Open the "Dashboard data cleaning.ipynb" code 
4. Follow the steps on the code and run everything to generate the dengue_1.csv dataset at the end
5. Click on the generated dataset link at the end to download it.

### Using Jupyter Notebook:

1. Browse to the tutorials -> veme2023_dengue1 folder in this repository.
2. Open the "dashboard_data_cleaning.ipynb" code using Jupyter Lab (or Google Colab as an alternative)
3. Follow all the steps on the code and run everything to generate the dengue_1.csv dataset at the end. Pay attention at the following parts:
    - Make sure to fill the variable "metadata_path" value with the path to the "VIPR_database.csv" file;
    - Make sure to fill the variable Entrez.email with your own email;
    - Make sure to fill the variable "output_file_path" value with the path you want to save the "dengue_1.csv" final result.

<br>
Obs: If you are using Google Colab, make sure to import the VIPR_databasae.csv file (located in the tutorials -> veme2023_dengue1 folder) to the Colab enviroment.

## Customize the dashboard:

1. Download the pathogen dataset you've generated using Terra, or make sure you have generated iy if you were using Jupyter Notebbok in your computer. In this case it is the "dengue_1.csv" file.

2. Browse to the DENV1_dashboard_veme_2023 -> app -> data folder, and create a new folder called "dengue".

3. Copy the dataset file that you've download from Terra (dengue_1.csv) from the "Downloads" folder and paste it inside the "dengue" folder you've just created.

4. Edit the python codes inside the DENV1_dashboard_veme_2023 -> app folder in order to customize the dashboard. To edit the codes you can use any code editor or IDE. If you don't have any of them you could download and install one of these suggestions: Pycharm, VScode)

5. Locate the "pathogen_1.py" file, inside the "pages" folder, and change the dataset location string (line 21). Write the full location to the "dengue_1.csv" dataset you have downloaded.  

6. If you wish, You can also change the dashboard's title on the "header.py" file (line 7), located inside the "pages" folder.

7. And also you could change the menu title on the "pathogen_1.py" file (line 29).

8. In the "dicts.py" file, fill the "dengue_categories" list with the names of the different types of category within the "category_2" dataset column (unique category_2 values).


## Running the Dashboard:

TO build the docker image, ooen the command line at the root folder of this repository and type:

```
docker build -t genomic-dashboard .
```

Running the container:

```
docker run -p 8511:8511 --name genomic-dashboard -d genomic-dashboard .
```
