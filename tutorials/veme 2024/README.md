# VEME 2024 Pathogen Dashboards Tutorial

## Generate the dengue_1 dataset:

- Download the VIPR Dengue dataset, clean and extract the GenBank Accession
- Use the file with the GenBank IDs to download the sequences from NCBI
- Run the sequences for classification on Genome Detective
- Merge the VIPR dataset produced with the report from Genome Detective
- Adjust the previous dataset to follow the PathoTrack template 

## Customize the dashboard:

1. Download the pathogen dataset you've generated in your machine. In this case it is the "dengue_1.csv" file.

2. Browse to the app -> data folder, and create a new folder called "dengue".

3. Copy the dataset file (dengue_1.csv) from the "Downloads" folder and paste it inside the "dengue" folder you've just created.

4. Edit the python codes inside the app folder in order to customize the dashboard. To edit the codes you can use any code editor or IDE. If you don't have any of them you could download and install one of these suggestions: Pycharm, VScode)

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
