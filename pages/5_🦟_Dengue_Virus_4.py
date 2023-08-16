from config import *
from source.pages import sidebar_dengue_1 as sd
from source.pages.header import *
from source.graphs.africa_map import *
from source.graphs.variants_proportion import variants_bar_plot
from source.graphs.countries_sequences import countries_with_sequences_chart, countries_with_sequences_chart_one_variant
from source.pages.tables import variant_summary_table as vst


def main():
    st.set_page_config(
        page_title="Dengue Africa Dashboard",
        layout="wide",
        initial_sidebar_state="expanded",
        page_icon="img/cropped-ceri_branco-01-150x150.png"
    )

    st.markdown(css_changes, unsafe_allow_html=True)
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

    ## Getting the data
    df_africa = load_data('data/dengue/metadata-dengue-4.csv')

    ##### CHECK LAST UPDATE #####
    with open('last_update.txt', 'r') as f:
        last_update = f.readlines()[-1]
    # last_update = datetime.today().strftime("%Y-%m-%d")

    ## Add sidebar to the app
    st.sidebar.title("CLIMADE AFRICA - DENGUE")
    st.sidebar.subheader("Last update: %s" % last_update)

    # Sidebar filter data
    st.sidebar.markdown(" ")
    st.sidebar.header("Filter data ")

    ### Begin of filters

    # Filter data by countries
    countries_choice, display_countries = sd.get_countries_choice(df_africa)

    # Sidebar filter lineages
    lineages_choice = sd.get_lineages_choice(df_africa)

    # Sidebar filter period
    start_date, end_date = sd.get_dates_choice(df_africa)

    ### Auxiliar dataframes ###

    # Couting variants
    df_count = sd.build_df_count(df_africa)

    # Building percentage dataframe
    variants_percentage = sd.build_variant_percentage_df(df_count)

    ### Filter and reset buttons ###
    bt_col_1, bt_col_2 = st.sidebar.columns(2)
    if bt_col_1.button("Reset filters", key='button_reset_filters'):
        sd.reset_filters(df_africa)

    # # Button to call filtering function
    if bt_col_2.button("Filter data", key='button_filter'):
        df_africa = sd.filter_df_africa(countries_choice, lineages_choice, start_date, end_date, df_africa)
        variant_count = sd.build_variant_count_df(df_africa)
        df_count = sd.build_df_count(df_africa)
        variants_percentage = sd.build_variant_percentage_df(df_count)

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
        ('Total of genomes', 'Genomes by variant'
         # 'Variants proportion'
         ))
    if map_option == 'Total of genomes':
        colorpath_africa_map(df_count, column=c1, color_pallet="speed")
    elif map_option == 'Genomes by variant':
        # Multiselect to choose variants to show
        voc_selected = c1.selectbox("Choose VOC to show", dengue_variants_genotypes)
        df_count_map = sd.build_df_count(df_africa[df_africa['variant'] == voc_selected])
        colorpath_africa_map(df_count_map, column=c1, color_pallet=vocs_color_pallet.get(voc_selected))
    # elif map_option == 'Variants proportion':
    #     c1.write(variants_percentage.head())
    #     scatter_africa_map(variants_percentage, column=c1, map_count_column='Count')

    ############ Second column ###############
    ####### Circulating lineages CHART ###########
    variants_bar_plot(variants_percentage, c2)

    ####### COUNTRIES WHITH SEQUENCE CHART #########
    countries_with_sequences_chart(df_count, c2)

if __name__ == "__main__":
    main()