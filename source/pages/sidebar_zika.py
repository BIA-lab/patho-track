import streamlit as st
import pandas as pd

from utils.dicts import countries_regions, concerned_variants
from utils.functions import get_img_with_href, warning_filter_data


@st.cache_data
def get_countries(df_africa):
    return df_africa['country'].unique()


def get_countries_choice(df_africa):
    # Filter by selected country
    countries = get_countries(df_africa)
    selection = st.sidebar.radio("Select Countries to show", ("Show all countries", "Select region",
                                                              "Select one or more countries"), key='radio_country',
                                 on_change=warning_filter_data)
    if selection == "Show all countries":
        countries_selected = countries
        display_countries = "all countries in Africa continent"
    elif selection == "Select region":
        aux_countries = []
        countries_selected = st.sidebar.multiselect('What region do you want to analyze?', countries_regions.keys(),
                                                    default='Southern Africa', key='multiselect_regions',
                                                    on_change=warning_filter_data)
        display_countries = " and ".join([", ".join(countries_selected[:-1]), countries_selected[-1]] if len(
            countries_selected) > 2 else countries_selected)
        for key in countries_selected:
            aux_countries.extend(countries_regions[key])
        countries_selected = aux_countries
    else:
        countries_selected = st.sidebar.multiselect('What countries do you want to analyze?', countries,
                                                    default='South Africa', key='multiselect_countries')
        display_countries = " and ".join([", ".join(countries_selected[:-1]), countries_selected[-1]] if len(
            countries_selected) > 2 else countries_selected)

    return countries_selected, display_countries


@st.cache_data
def get_variants(df_africa):
    return df_africa['variant'].unique()


def get_lineages_choice(df_africa):
    variants = get_variants(df_africa)
    lineages_selected = st.sidebar.multiselect("Select lineages to show", variants,
                                               default=sorted(variants), key='multiselect_variants',
                                               on_change=warning_filter_data)
    return lineages_selected


@st.cache_data
def get_dates(df_africa):
    # TODO: instead of dropna, check if there is information on colention date
    df_africa.dropna(subset=['date_2weeks'], inplace=True)

    df_africa['date_2weeks'] = pd.to_datetime(df_africa['date_2weeks'], errors='coerce', format='%Y-%m-%d',
                                              yearfirst=True)

    df_africa['date_2weeks'] = df_africa['date_2weeks'].sort_values(ascending=False)
    df_africa['date_2weeks'] = df_africa['date_2weeks'].dt.strftime('%Y-%m-%d')
    # df_africa['date_2weeks'] = df_africa['date_2weeks'].dt.strftime('%b %d,%Y')
    return df_africa['date_2weeks'].unique()


def get_dates_choice(df_africa):
    dates = get_dates(df_africa)
    start_date, end_date = st.sidebar.select_slider("Select a range of time to show",
                                                    options=sorted(dates),
                                                    value=(dates.min(),
                                                           dates.max()), key='select_slider_dates',
                                                    on_change=warning_filter_data)
    return start_date, end_date


@st.cache_data
def build_variant_count_df(df_africa):
    # Building variant data frame
    variant_count = pd.DataFrame(df_africa.variant)
    variant_count = variant_count.groupby(['variant']).size().reset_index(name='Count').sort_values(['Count'],
                                                                                                    ascending=True)
    return variant_count


@st.cache_data
def build_df_count(df_africa):
    return df_africa.groupby(['country', 'variant', 'date_2weeks']).size().reset_index(name='Count')


@st.cache_data
def build_variant_percentage_df(df_count):
    variants_percentage = df_count.groupby(['date_2weeks', 'variant']).agg({'Count': 'sum'})
    variants_percentage = variants_percentage.groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).sort_values(
        by='Count',
        ascending=False)
    variants_percentage = variants_percentage.reset_index()
    return variants_percentage


def reset_filters(df):
    # Countries filters
    if 'multiselect_regions' in st.session_state.keys():
        del st.session_state.multiselect_regions

    if 'multiselect_countries' in st.session_state.keys():
        del st.session_state.multiselect_countries

    del st.session_state['radio_country']
    st.session_state.radio_country = 'Show all countries'

    # Variants filter
    if 'multiselect_variant' in st.session_state.keys():
        del st.session_state['multiselect_variant']
        st.session_state.multiselect_variant = concerned_variants

    # Date selection
    all_dates = get_dates(df_africa=df)
    start_date = min(all_dates)
    end_date = max(all_dates)

    del st.session_state['select_slider_dates']
    st.session_state.select_slider_dates = [start_date, end_date]

    # caching.clear_memo_cache()
    # caching.clear_singleton_cache()
    st.experimental_rerun()


@st.cache_data
def filter_df_africa(countries_choice, lineages_choice, start_date, end_date, df_africa):
    """
    Function to filter and return all dfs used in the visualizations
    :return:
    """
    # filter by country
    mask_countries = df_africa['country'].isin(countries_choice)
    df_africa = df_africa[mask_countries]

    # filter by variant
    mask_lineages = df_africa['variant'].isin(lineages_choice)
    df_africa = df_africa[mask_lineages]
    df_africa.variant[df_africa.variant.isna()] = 'NA'

    # filter by period
    df_africa = df_africa.loc[(df_africa['date_2weeks'] >= start_date) & (df_africa['date_2weeks'] <= end_date)]

    return df_africa


def show_metrics(df_africa):
    sd_col1, sd_col2 = st.sidebar.columns(2)
    sequences = int(df_africa.shape[0])
    sd_col1.metric("Sequences selected", '{:,}'.format(sequences))
    sd_col2.metric("Countries selected", len(df_africa.country.unique()))


def about_section():
    st.sidebar.info("""
    Figures inspired by Wilkinson et al. Science 2021
    
    Contact email: joicy.xavier@ufvjm.edu.br / tulio@sun.ac.za
    
    [Cite us](https://www.nature.com/articles/s41564-022-01276-9)
    """)


def acknowledgment_section(logo_path, link):
    logo = get_img_with_href(logo_path, link)
    st.sidebar.markdown(logo, unsafe_allow_html=True)
