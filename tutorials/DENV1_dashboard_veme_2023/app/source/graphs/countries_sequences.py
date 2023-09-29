import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import timedelta, datetime

from utils.dicts import main_categories_1_color_scheme


def countries_with_sequences_chart(df_count, column):
    c = column
    df_country_categories = df_count.copy()

    df_country_categories['date_initial'] = pd.to_datetime(df_country_categories['date']) - timedelta(days=14)
    df_country_categories['date_initial'] = df_country_categories['date_initial'].dt.strftime('%d/%m')

    df_country_categories['date_final'] = pd.to_datetime(df_country_categories['date']).dt.strftime('%d/%m/%Y')

    ##### Processing df to show prevalent categories
    # Total genomes column
    df_country_categories['total_genomes'] = df_country_categories.groupby(['country', 'date'])['Count']\
        .transform('sum')

    # counting genomes per category_2
    df_country_categories['categories'] = df_country_categories[['country', 'category_2', 'date',
                                                           'Count']].groupby(['country', 'date'])['category_2']\
        .transform(lambda x: ', '.join(x))

    df_country_categories['counts_per_variant'] = df_country_categories[
        ['country', 'category_2', 'date', 'categories', 'Count']].groupby(
        ['country', 'date', 'categories'])['Count'].transform(lambda x: ', '.join(x.astype(str)))

    genomes_per_category = []
    for index, row in df_country_categories.iterrows():
        label = ', '.join(' : '.join(x) for x in zip(row['categories'].split(','), row['counts_per_variant'].split(',')))
        genomes_per_category.append(label)

    df_country_categories['genomes_per_category'] = genomes_per_category

    df_country_categories = df_country_categories.drop_duplicates(subset=["country", "date", "genomes_per_category"])

    # Determining prevalent category per date and country
    prevalent_category = []
    for index, row in df_country_categories.iterrows():
        a = row['genomes_per_category']
        genomes_per_variant_dict = dict((x.strip(), int(y.strip()))
                                        for x, y in (element.split(' : ')
                                                     for element in a.split(', ')))
        prevalent_category.append(max(genomes_per_variant_dict, key=genomes_per_variant_dict.get))

    df_country_categories['prevalent_category'] = prevalent_category

    df_country_categories.drop(['category_2', 'categories', 'Count', 'counts_per_variant', ], axis=1, inplace=True)

    with st.container():
        c.subheader("Sequence data available per country")

        country_lineages = px.strip(df_country_categories.sort_values('total_genomes', ascending=False),
                                    x="date", y='country',
                                    color="prevalent_category",
                                    custom_data=['country','date', 'prevalent_category', 'total_genomes',
                                                 'genomes_per_category', 'date_initial', 'date_final'],
                                    color_discrete_map=main_categories_1_color_scheme,
                                    stripmode='group').update_traces(jitter=1)
        country_lineages.update_traces(marker=dict(size=13, line=dict(width=0.5, color='#E5ECF6')))
        country_lineages.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1,
            xanchor="right",
            x=1
        ), legend_title_text="Prevalent Categories")
        country_lineages.update_layout(title=dict(y=1), yaxis={'categoryorder': 'category descending'})
        country_lineages.update_yaxes(title="Country")
        country_lineages.update_xaxes(title="Date", range=[df_country_categories['date'].min(), datetime.today()])

        # creating standardize hover template
        custom_hovertemplate = '<b>Country: %{customdata[0]} <br>' + \
                                'Date: %{customdata[5]} to %{customdata[6]} <br>' +\
                                'Total of Genomes: %{customdata[3]} </b><br>' +\
                                'Prevalent Variant: %{customdata[2]} <br>' +\
                                'Genomes per variant: %{customdata[4]} <br>'

        country_lineages.update_traces(hovertemplate=custom_hovertemplate)

        for frame in country_lineages.frames:
            for data in frame.data:
                data.hovertemplate = custom_hovertemplate

        country_lineages.update_layout(hovermode="closest")

        c.plotly_chart(country_lineages, use_container_width=True)

def countries_with_sequences_chart_one_category(df_count, column, category_2, start_date, color):
    c = column
    df_country_categories = df_count[df_count['category_2'].isin(category_2)]

    df_country_categories['date_initial'] = pd.to_datetime(df_country_categories['date']) - timedelta(days=14)
    df_country_categories['date_initial'] = df_country_categories['date_initial'].dt.strftime('%Y-%m-%d')

    with st.container():
        country_lineages = px.strip(df_country_categories.sort_values(by='category_2', ascending=False), x="date",
                                      y="country", color="category_2", custom_data=['country','category_2', 'date', 'Count'],
                                      color_discrete_map=color)
        country_lineages.update_traces(marker=dict(size=13, line=dict(width=0.5, color='#E5ECF6')))
        country_lineages.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1,
            xanchor="right",
            x=1
        ), legend_title_text="Categories")
        country_lineages.update_layout(title=dict(y=1), yaxis={'categoryorder': 'category descending'})
        country_lineages.update_yaxes(title="Country")
        country_lineages.update_xaxes(title="Date", range=[start_date, datetime.today()])

        # creating standardize hover template
        custom_hovertemplate = '<b>Country: %{customdata[0]} </b><br><br>' + \
                               'Variant: %{customdata[1]} <br>Date: %{customdata[2]} <br>' + \
                               'Genomes: %{customdata[3]} <br>'

        country_lineages.update_traces(hovertemplate=custom_hovertemplate)

        for frame in country_lineages.frames:
            for data in frame.data:
                data.hovertemplate = custom_hovertemplate

        c.plotly_chart(country_lineages, use_container_width=True)