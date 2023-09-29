## Generate the dengue_1 dataset

### Generating the dataset through Terra

<a href='https://app.terra.bio/#workspaces/veme-training/VEME%202023%20Pathogen%20Dashboards'> VEME 2023 Dashboards halfway Module - Terra Workspace </a>

1. Browse to the "ANALYSES" menu.
2. Open the "Dashboard data cleaning.ipynb" code 
3. Follow the steps on the code and run everything to generate the dengue_1.csv dataset at the end
4. Click on the generated dataset link at the end to download it.

## VEME halfday module tutorial steps for customizing the dashboard:
1. Download the pathogen dataset you've generated using the Jupyter Notebook in the Terra workspace. In this case it is the "dengue_1.csv" file.

2. Browse to the DENV1_dashboard_veme_2023 -> app -> data folder, and create a new folder called "dengue".

3. Copy the dataset file that you've download from Terra (dengue_1.csv) from the "Downloads" folder and paste it inside the "dengue" folder you've just created.

4. Edit the python codes inside the DENV1_dashboard_veme_2023 -> app folder in order to customize the dashboard. To edit the codes you can use any code editor or IDE. If you don't have any of them you could download and install one of these suggestions: Pycharm, VScode)

5. Locate the "pathogen_1.py" file, inside the "pages" folder, and change the dataset location string (line 21). Write the full location to the "dengue_1.csv" dataset you have downloaded.  

6. If you wish, You can also change the dashboard's title on the "header.py" file (line 7), located inside the "pages" folder.

7. And also you could change the menu title on the "pathogen_1.py" file (line 29).

8. In the "dicts.py" file, fill the "dengue_categories" list with the names of the different types of category within the "category_2" dataset column (unique category_2 values).


## How to setup and run the app:
1. Make sure you have Docker installed. For more information access: https://docs.docker.com/engine/install/
2. Open the terminal (comand line) inside the folder where the dockerfile is located in (DENV1_dashboard_veme_2023)
3. Build the image: `docker build -t genomic-dashboard .`
4. Run the Docker container: `docker run -p 8511:8511 --name genomic-dashboard -d genomic-dashboard .` 
5. You can view your Dashboard in your browser URL: http://0.0.0.0:8511

## Data

### Using metadata
Create your metadata based on [data/template_metadata.csv](data/template_metadata.csv) and save as `./data/<pathogen>/metadata.csv`
For example, if you are working with Dengue, save your metadata on data/dengue/metadata.csv