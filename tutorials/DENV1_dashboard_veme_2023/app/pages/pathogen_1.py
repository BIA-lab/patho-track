from config import *
from source.pages import sidebar_pathogen_1 as sd
from source.pages.header_pathogen_1 import *
from source.graphs.africa_map import *
from source.graphs.categories_proportion import categories_bar_plot
from source.graphs.countries_sequences import countries_with_sequences_chart, countries_with_sequences_chart_one_category


def main():
    st.set_page_config(
        page_title="Genomic Dashboard Template",
        layout="wide",
        initial_sidebar_state="expanded",
        page_icon="img/cropped-ceri_branco-01-150x150.png"
    )

    st.markdown(css_changes, unsafe_allow_html=True)
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

    ## Getting the data
    df_africa = load_data('data/dengue/dengue_1.csv') #TODO change the dataset here

    ##### CHECK LAST UPDATE #####
    with open('last_update.txt', 'r') as f:
        last_update = f.readlines()[-1]
    # last_update = datetime.today().strftime("%Y-%m-%d")

    ## Add sidebar to the app
    st.sidebar.title("GENOMIC DASH - PATHOGEN 1")
    st.sidebar.subheader("Last update: %s" % last_update)

    # Sidebar filter data
    st.sidebar.markdown(" ")
    st.sidebar.header("Filter data ")

    ### Begin of filters

    # Filter data by countries
    countries_choice, display_countries = sd.get_countries_choice(df_africa)

    # Sidebar filter lineages
    categories_choice = sd.get_categories_choice(df_africa)

    # Sidebar filter period
    start_date, end_date = sd.get_dates_choice(df_africa)

    ### Auxiliar dataframes ###

    # Couting variants
    df_count = sd.build_df_count(df_africa)

    # Building percentage dataframe
    categories_2_percentage = sd.build_category_2_percentage_df(df_count)

    ### Filter and reset buttons ###
    bt_col_1, bt_col_2 = st.sidebar.columns(2)
    if bt_col_1.button("Reset filters", key='button_reset_filters'):
        sd.reset_filters(df_africa)

    # # Button to call filtering function
    if bt_col_2.button("Filter data", key='button_filter'):
        df_africa = sd.filter_df_africa(countries_choice, categories_choice, start_date, end_date, df_africa)
        variant_count = sd.build_category_2_count_df(df_africa)
        df_count = sd.build_df_count(df_africa)
        categories_2_percentage = sd.build_category_2_percentage_df(df_count)

    # Metrics
    sd.show_metrics(df_africa)

    # End of sidebar
    st.sidebar.header("About")
    sd.about_section()
    # st.sidebar.header("Acknowledgment")
    # sd.acknowledgment_section(logo_path='img/gisaid_logo.png', link='https://www.gisaid.org/')

    # Add title and subtitle to the main interface of the app
    main_title(display_countries)

    ### Layout of main page
    c1, c2 = st.columns((1.5, 1.9))

    ############ First column ###############
    ############## MAP CHART ################
    c1.subheader("Genomes per country")
    map_option = c1.selectbox(
        'Metric',
        ('Total of genomes', 'Genomes by category 2'
         # 'Variants proportion'
         ))
    if map_option == 'Total of genomes':
        colorpath_africa_map(df_count, column=c1, color_pallet="speed")
    elif map_option == 'Genomes by Category 2':
        # Multiselect to choose variants to show
        voc_selected = c1.selectbox("Choose VOC to show", dengue_categories)
        df_count_map = sd.build_df_count(df_africa[df_africa['category_2'] == voc_selected])
        colorpath_africa_map(df_count_map, column=c1, color_pallet=vocs_color_pallet.get(voc_selected))
    # elif map_option == 'Variants proportion':
    #     c1.write(categories_2_percentage.head())
    #     scatter_africa_map(categories_2_percentage, column=c1, map_count_column='Count')

    ############ Second column ###############
    ####### Circulating lineages CHART ###########
    categories_bar_plot(categories_2_percentage, c2)

    ####### COUNTRIES WHITH SEQUENCE CHART #########
    countries_with_sequences_chart(df_count, c2)

if __name__ == "__main__":
    main()
