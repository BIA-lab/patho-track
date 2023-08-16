import pandas as pd
import datetime
from datetime import date

## Lineage dictionary:
from utils.dicts import variant_names

def variant_summary_table(raw_data_path="data/all_data_processed.csv"):

    raw_data = pd.read_csv(raw_data_path)

    # convert to date columns
    raw_data['collection_date'] = pd.to_datetime(raw_data['collection_date'], format='%Y-%m-%d', yearfirst=True)
    raw_data['subm_date'] = pd.to_datetime(raw_data['subm_date'], format='%Y-%m-%d', yearfirst=True)

    raw_data.sort_values(by=['collection_date'])

    cuttoff_date = pd.to_datetime(date(2018, 1, 1))
    date_filter_mask = raw_data['collection_date'] > cuttoff_date

    raw_data = raw_data[date_filter_mask]

    all_variants = list(set(variant_names.values()))

    variant_data = raw_data[raw_data['variant'].isin(all_variants)]  ## ~ for opposite

    ##count samples from the last 30 days
    currDate = date.today() - datetime.timedelta(days=30)

    variant_data_agg = variant_data.groupby(
        'variant'
    ).agg(
        Lineage_sublineage=('lineage', list),
        FirstSequence=('collection_date', max),
        LastSequence=('collection_date', min),
        Totalconfirmed=('subm_date', "count"),
        SamplesPast30=('subm_date', lambda x: len([y for y in x if y > pd.to_datetime(currDate)])),
        DaysSince=('collection_date', lambda x: (pd.to_datetime(date.today()) - max(x)).days)

    )
    ### Format fields
    #variant_data_agg['Lineage_sublineage']  = variant_data_agg['Lineage_sublineage'].apply(lambda x: set(x)).str.join(',')
    variant_data_agg['Lineage_sublineage']  = variant_data_agg['Lineage_sublineage'].apply(lambda x: sorted(set(x)))
    variant_data_agg['Lineage_sublineage']  = variant_data_agg['Lineage_sublineage'].apply(lambda x: ", ".join(x))
    variant_data_agg['FirstSequence']  = variant_data_agg['FirstSequence'].apply(lambda x: x.date())
    variant_data_agg['LastSequence']  = variant_data_agg['LastSequence'].apply(lambda x: x.date())    
    
    return variant_data_agg