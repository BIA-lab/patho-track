import streamlit as st
import pandas as pd


from utils.dicts import countries_regions, concerned_categories
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
def get_category_2(df_africa):
    return df_africa['category_2'].unique()


def get_categories_choice(df_africa):
    categories = get_category_2(df_africa)
    categories_selected = st.sidebar.multiselect("Select categories to show", categories,
                                               default=sorted(categories), key='multiselect_variants',
                                               on_change=warning_filter_data)
    return categories_selected

@st.cache_data
def get_dates(df_africa):
    # TODO: instead of dropna, check if there is information on colention date
    df_africa.dropna(subset=['date'], inplace=True)

    df_africa['date'] = pd.to_datetime(df_africa['date'], errors='coerce', format='%Y-%m-%d',
                                              yearfirst=True)

    df_africa['date'] = df_africa['date'].sort_values(ascending=False)
    df_africa['date'] = df_africa['date'].dt.strftime('%Y-%m-%d')
    # df_africa['date'] = df_africa['date'].dt.strftime('%b %d,%Y')
    return df_africa['date'].unique()


def get_dates_choice(df_africa):
    dates = get_dates(df_africa)
    start_date, end_date = st.sidebar.select_slider("Select a range of time to show",
                                                    options=sorted(dates),
                                                    value=(dates.min(),
                                                           dates.max()), key='select_slider_dates',
                                                    on_change=warning_filter_data)
    return start_date, end_date


@st.cache_data
def build_category_2_count_df(df_africa):
    # Building category_2 data frame
    category_2_count = pd.DataFrame(df_africa.category_2)
    category_2_count = category_2_count.groupby(['category_2']).size().reset_index(name='Count').sort_values(['Count'],
                                                                                                    ascending=True)
    return category_2_count


@st.cache_data
def build_df_count(df_africa):
    return df_africa.groupby(['country', 'category_2', 'date']).size().reset_index(name='Count')


@st.cache_data
def build_category_2_percentage_df(df_count):
    variants_percentage = df_count.groupby(['date', 'category_2']).agg({'Count': 'sum'})
    variants_percentage = variants_percentage.groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).sort_values(by='Count',
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
    if 'multiselect_category_2' in st.session_state.keys():
        del st.session_state['multiselect_category_2']
        st.session_state.multiselect_category_2 = concerned_categories

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
def filter_df_africa(countries_choice, categories_choice, start_date, end_date, df_africa):
    """
    Function to filter and return all dfs used in the visualizations
    :return:
    """
    # filter by country
    mask_countries = df_africa['country'].isin(countries_choice)
    df_africa = df_africa[mask_countries]

    # filter by category_2
    mask_categ_1 = df_africa['category_2'].isin(categories_choice)
    df_africa = df_africa[mask_categ_1]
    df_africa.category_2[df_africa.category_2.isna()] = 'NA'

    # filter by period
    df_africa = df_africa.loc[(df_africa['date'] >= start_date) & (df_africa['date'] <= end_date)]

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
