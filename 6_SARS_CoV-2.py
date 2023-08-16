# Import project packages
from datetime import datetime

from config import *
from source.pages import sidebar_dengue_all_serotypes as sd
from source.pages.header import *
from source.graphs.africa_map import *
from source.graphs.variants_proportion import variants_bar_plot
from source.graphs.countries_sequences import countries_with_sequences_chart, countries_with_sequences_chart_one_variant
from source.pages.tables import variant_summary_table as vst

# Import Python Libraries
import pandas as pd
from PIL import Image


def main():
    st.set_page_config(
        page_title="cs Africa ",
        layout="wide",
        initial_sidebar_state="expanded",
        page_icon="img/cropped-ceri_branco-01-150x150.png"
    )

    st.markdown(css_changes, unsafe_allow_html=True)
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

    ## Getting the data
    df_africa = load_data('./data/all_data_processed.csv')

    ##### CHECK LAST UPDATE #####
    # with open('last_update.txt', 'r') as f:
    #     last_update = f.readlines()[-1]
    last_update = datetime.today().strftime("%Y-%m-%d")

    ## Add sidebar to the app
    st.sidebar.title("CLIMADE AFRICA")
    st.sidebar.subheader("Last update: %s" % last_update)

    # Sidebar filter data
    st.sidebar.markdown(" ")
    st.sidebar.header("Filter data ")

    ### Begin of filters

    # form = st.sidebar.form("Filters_form", clear_on_submit=True)

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
        voc_selected = c1.selectbox("Choose VOC to show", concerned_variants)
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

    ########### TABLE WEEKLY VARIANT SUMMARY #########
    st.header("Variant details")
    weekly_variants_df = vst()

    rename_weekly_columns = {'Lineage_sublineage': 'Lineage/sub-lineages', 'Total_Confirmed': 'Total sequences',
                          'SamplesPast30': 'Sampled and submitted last 30 days',
                          'FirstSequence': 'First sequence', 'DaysSince': 'Days since last sequence'}
    weekly_variants_df.rename(columns=rename_weekly_columns, inplace=True)
    with st.container():
        with st.expander("Africa weekly variant summary"):
            st.table(weekly_variants_df)

    c1_2, c2_2 = st.columns((1, 1))
    with c1_2.container():
        with c1_2.expander("Alpha variant"):
            alpha_img = Image.open("data/figures/alpha-stanford-3-1536x226.png")
            st.image(alpha_img, caption="SARS_CoV2 Alpha variant sequence")
            countries_with_sequences_chart_one_variant(df_count, st, variant=['Alpha'], start_date=start_date,
                                                       color=main_lineages_color_scheme)

    with c2_2.container():
        with c2_2.expander("Beta variant"):
            beta_img = Image.open("data/figures/Beta-stanford.png")
            st.image(beta_img, caption="SARS_CoV2 Beta variant sequence")
            countries_with_sequences_chart_one_variant(df_count, st, variant=['Beta'], start_date=start_date,
                                                       color=main_lineages_color_scheme)

    with c1_2.container():
        with c1_2.expander("Delta variant"):
            delta_img = Image.open("data/figures/Delta-stanford.png")
            st.image(delta_img, caption="SARS_CoV2 Delta variant sequence")
            countries_with_sequences_chart_one_variant(df_count, st, variant=['Delta'], start_date=start_date,
                                                       color=main_lineages_color_scheme)

    with c2_2.container():
        with c2_2.expander("Omicron variant"):
            omicron_img = Image.open("data/figures/omicron-stanford.png")
            st.image(omicron_img, caption="SARS_CoV2 Omicron variant sequence")
            omicron_lineages = ['Omicron (BA.1)', 'Omicron (BA.2)', 'Omicron (BA.4)', 'Omicron (BA.5)']
            df_country_omicron = df_count[df_count['variant'].isin(omicron_lineages)]
            countries_with_sequences_chart_one_variant(df_country_omicron, st, variant=omicron_lineages,
                                                       start_date=start_date, color=main_lineages_color_scheme)

if __name__ == "__main__":
    main()
