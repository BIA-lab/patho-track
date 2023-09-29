import streamlit as st
import plotly.express as px
from utils.dicts import main_categories_1_color_scheme, concerned_categories
from datetime import datetime, timedelta
import pandas as pd
import plotly.graph_objs as go

#TODO consertar esse gráfico pra calcular porcentagem para todas as variantes

def categories_bar_plot(categories_percentage, column):
    c = column
    categories_percentage['date_initial'] = pd.to_datetime(categories_percentage['date']) - timedelta(days=14)
    categories_percentage['date_initial'] = categories_percentage['date_initial'].dt.strftime('%Y-%m-%d')
    categories_percentage['Count'] = categories_percentage['Count'].astype(int)

    # Reordering categories 2
    categories_percentage['category_2'] = categories_percentage['category_2'].astype('category')
    # categories_percentage['category_2'].cat.reorder_categories(variants_order, inplace=True)

    with st.container():
        c.subheader("Circulating pathogen categories")
        fig = px.bar(categories_percentage.sort_values(by='category_2'), x='date', y='Count',
                     color='category_2', color_discrete_map=main_categories_1_color_scheme,
                     barmode='stack',
                     custom_data=['category_2', 'Count', 'date_initial', 'date'],
                     labels={'category_2': 'Category', 'Count': 'Percentage', 'date': 'Date'})
        fig.update_yaxes(title="Proportion of Genomes")
        fig.update_xaxes(title="Date", range=[categories_percentage['date'].min(), datetime.today()])
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=0.9,
            xanchor="right",
            x=1
        ), legend_title_text="Lineages", height=450)
        fig.update_layout(title=dict(y=1))
        # fig.update_layout(xaxis={'overlaying': "free"})

        # creating standardize hover template
        custom_hovertemplate = '<b>Lineage: %{customdata[0]} </b><br><br>' + \
                               '%{customdata[1]}% of genomes <br>from %{customdata[2]}' + \
                               ' to %{customdata[3]}<br>'

        fig.update_traces(hovertemplate=custom_hovertemplate)

        for frame in fig.frames:
            for data in frame.data:
                data.hovertemplate = custom_hovertemplate

        c.plotly_chart(fig, use_container_width=True)
