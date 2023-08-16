##### Palette colors #####
main_lineages_color_scheme = {}
##### Dictionary to convert names of variants #####
variant_names = {}

# Variant cutoffs
variant_cutoffs = {}

concerned_variants = {}

###### Dictionary to standardize duplicated countries ####
standardize_country_names = {'Republic of Burundi': 'Burundi', 'Republic of Cameroon': 'Cameroon',
                             'Republic of Chad': 'Chad', 'Republic of Equatorial Guinea': 'Equatorial Guinea',
                             'Gabonese Republic': 'Gabon',
                             'Democratic Republic of São Tomé and Principe': 'São Tomé and Principe',
                             'Union of the Comoros': 'Comoros', 'Republic of Djibouti': 'Djibouti',
                             'State of Eritrea': 'Eritrea', 'Federal Democratic Republic of Ethiopia': 'Ethiopia',
                             'Republic of Kenya': 'Kenya', 'Republic of Madagascar': 'Madagascar',
                             'Republic of Mauritius': 'Mauritius', 'Republic of Rwanda': 'Rwanda',
                             'Republic of Seychelles': 'Seychelles', 'Federal Republic of Somalia': 'Somalia',
                             'Republic of Sudan': 'Sudan', 'Republic of South Sudan': 'South Sudan',
                             'United Republic of Tanzania': 'Tanzania', 'Republic of Uganda': 'Uganda',
                             'Peoples Republic of Algeria': 'Algeria', 'Arab Republic of Egypt': 'Egypt',
                             'State of Libya': 'Libya', 'Islamic Republic of Mauritania': 'Mauritania',
                             'Kingdom of Morocco': 'Morocco', 'Republic of Tunisia': 'Tunisia',
                             'Republic of Angola': 'Angola', 'Republic of Botswana': 'Botswana',
                             'Kingdom of eSwatini': 'eSwatini', 'Swaziland': 'eSwatini',
                             'Kingdom of Lesotho': 'Lesotho',
                             'Republic of Malawi': 'Malawi', 'Republic of Mozambique': 'Mozambique',
                             'Republic of Namibia': 'Namibia', 'Republic of South Africa': 'South Africa',
                             'Republic of Zambia': 'Zambia', 'Republic of Zimbabwe': 'Zimbabwe',
                             'Republic of Benin': 'Benin', 'Cape Verde': 'Cabo Verde',
                             'Republic of Cabo Verde': 'Cabo Verde',
                             'Republic of Côte d\'Ivoire': 'Cote d\'Ivoire', 'Ivory Coast': 'Cote d\'Ivoire',
                             'Republic of Gambia': 'Gambia',
                             'Republic of Ghana': 'Ghana', 'Republic of Guinea': 'Guinea',
                             'Republic of Guinea-Bissau': 'Guinea-Bissau', 'Republic of Liberia': 'Liberia',
                             'Republic of Mali': 'Mali',
                             'Republic of Niger': 'Niger', 'Federal Republic of Nigeria': 'Nigeria',
                             'Republic of Senegal': 'Senegal',
                             'Republic of Sierra Leone': 'Sierra Leone', 'Togolese': 'Togo',
                             'Togolese Republic': 'Togo', 'La Reunion': 'Reunion',
                             'DR Congo': 'Democratic Republic of the Congo', 'Congo': 'Republic of the Congo'}

###### Dictionary to select countries per region ####
countries_regions = {'Central Africa': {'Burundi', 'Cameroon', 'Central African Republic', 'Chad',
                                        'Republic of the Congo', 'Democratic Republic of the Congo',
                                        'Equatorial Guinea', 'Gabon', 'São Tomé and Principe'},
                     'Eastern Africa': {'Comoros', 'Djibouti', 'Eritrea', 'Ethiopia', 'Kenya', 'Madagascar',
                                        'Mauritius', 'Rwanda', 'Seychelles', 'Somalia', 'Sudan', 'South Sudan',
                                        'Tanzania',
                                        'Uganda'},
                     'Northern Africa': {'Algeria', 'Egypt', 'Libya', 'Mauritania', 'Morocco', 'Sahrawi', 'Tunisia'},
                     'Southern Africa': {'Angola', 'Botswana', 'eSwatini', 'Lesotho', 'Malawi', 'Mozambique', 'Namibia',
                                         'South Africa', 'Zambia', 'Zimbabwe'},
                     'Western Africa': {'Benin', 'Burkina Faso', 'Cabo Verde', 'Côte d\'Ivoire', 'Gambia', 'Ghana',
                                        'Guinea', 'Guinea-Bissau', 'Liberia', 'Mali', 'Niger', 'Nigeria', 'Senegal',
                                        'Sierra Leone', 'Togo'},
                     'Dependencies in Africa': {'Reunion', 'Western Sahara', 'Mayotte', 'Saint Helena'}}

missing_country_codes = {'Guinea-Bissau': 'GNB', 'Mauritius': 'MUS', 'Republic of the Congo': 'COG', 'Reunion': 'REU',
                         'Seychelles': 'SYC', 'Mayotte': 'MYT', 'Cabo Verde': 'CPV', "Cote d'Ivoire": 'CIV',
                         'Eswatini': 'SWZ', 'Tanzania': 'TZA', 'South Sudan': 'SSD'}

#https://plotly.com/python/builtin-colorscales/#discrete-color-sequences
vocs_color_pallet = {'Unassigned': 'Greys', 'DENV-1': 'YlOrBr', 'DENV-2': 'Oranges', 'DENV-3': 'algae', 'DENV-4': 'RdPu'}


##### CLIMADE dicts ########
dengue_variants = {"Unassigned", "DENV-1", "DENV-2", "DENV-3", "DENV-4"}

dengue_variants_genotypes = {"Genotype I", "Genotype II", "Genotype III", "Genotype IV", "Genotype V", "Genotype VI"}

chikv_lineages = {"East-Central-South-African", "West African", "Asian Urban", "Indian Ocean", "Asian and Caribbean",
                  "Unassigned"}

zika_lineages = {"African", "Asian"}