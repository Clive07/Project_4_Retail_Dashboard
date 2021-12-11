#------------------------
#       imports
#------------------------
# dash
import dash
# dash bootstrap components
import dash_bootstrap_components as dbc
# dash core components, html
from dash import dcc, html
# input, output, state
from dash.dependencies import Input, Output, State
# plotly.express as ex
import plotly.express as ex
# pandas as pd
import pandas as pd
# petl as etl
import petl as etl

#------------------------
#       variables
#------------------------
# file path to the result files
results_path = 'data/refined/results/'

# READ CSV FILES

# product results via region
regional_products_df = pd.read_csv(f'{results_path}products_regional.csv')

# product results via county
county_products_df = pd.read_csv(f'{results_path}products_per_county.csv')

# prod category results via region
regional_prod_categories = pd.read_csv(f'{results_path}prod_categories_regional.csv')

# prod category results via county
county_prod_categories = pd.read_csv(f'{results_path}prod_categories_per_county.csv')

# performance results of region & best/worse counties
regional_performance = pd.read_csv(f'{results_path}regional_performance.csv')
counties_performance = pd.read_csv(f'{results_path}top10_bottom10_performed_counties.csv')

# hourly sales of best counties
hourly_sales_of_best_counties = pd.read_csv(f'{results_path}top10_counties_hourly_sales.csv')

# top 10 bottom 10 profitable branches file
profit_df = pd.read_csv(f'{results_path}top10_bottom10_profitable_counties.csv').sort_values('total_profits', ascending=False)

# best & worse profit branches
best_profiting_branches = profit_df.head(10)
worst_profiting_branches = profit_df.tail(10)

# creating bar charts for profit section
best_profit_figure = ex.bar(best_profiting_branches,
                            x='county',
                            y='total_profits',
                            color='county',
                            title='top 10 profitable branches')
worst_profit_figure = ex.bar(worst_profiting_branches,
                            x='county',
                            y='total_profits',
                            color='county',
                            title='worst 10 profitable branches')

#-----------------------
#           dash
#-----------------------


# INITIALISATION

app = dash.Dash(
    __name__,
    # connect to one of bootstrap themes otherwise it won't work
    # added meta_tags to try and be more mobile friendly 
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{
        'name':'viewport',
        'content':'width=device-width, initial-scale=1.0'
    }]
)
# server setup
server = app.server


# LAYOUT

app.layout = dbc.Container([
    # TITLE & INFO ROW
    dbc.Row([
        # column containing the title
        dbc.Col([
            html.H1(
                "Project 4 - Retail Store Dashboard",
                className='text-center text-primary'
            ),
        ],
        width=12
        ),
        # column containing brief info
        dbc.Col([
            html.H5(
                "From here you are able to access statistical data which has been acquired by the cleaning & analysing of raw data\
                \n which was collected by all of the branches this retail company has established since 2010",
                className='text-center mb-5'
            ),
            html.P(
                'just click on one of the coloured buttons below to get started!',
                className='text-center'
                )
        ],
        width=10
        )
    ],
    justify='center'
    ),

    
    # PRODUCT & PROD CATEGORY SECTION
    dbc.Row([
        # btn to hide and reveal row
        dbc.Button(
            '5 best & 5 worse products / product categories per region & county',
            id='products-collapse-btn',
            className='mb-3',
            color='warning',
            n_clicks=0,
        ),

        # collapsing view of graph
        dbc.Collapse([
            dbc.Row([
                # COL FOR DROPDOWNS & INFO
                dbc.Col([
                    # dropdown dictating if region or county based
                    dcc.Dropdown(
                        id='reg-or-county-dropdown-products',
                        options=[
                        {'label': 'Regional', 'value': 'region'},
                        {'label': 'County', 'value': 'county'}
                        ],
                        placeholder='please pick if per region or county'
                    ),
                    # dropdown dictating if product or prod category based
                    dcc.Dropdown(
                        id='products-or-categories-dropdown',
                        options=[
                        {'label': 'Products', 'value': 'products'},
                        {'label': 'Product Categories', 'value': 'prod-cat'}
                        ],
                        placeholder='please pick to see products or product categories'
                    ),
                    # dropdown dictating which region/county to view
                    dcc.Dropdown(
                        id='individual-dropdown',
                        multi=False,
                        options=[],
                        placeholder='please pick to see products or product categories',
                        className='mb-5'
                    ),
                    html.P(
                        children='',
                        id='first-section-results-info',
                        className='text-center'
                        )
                ],
                width=4
                ),

                dbc.Col([
                    dcc.Graph(id='product-fig', figure={})
                ],
                width=8,
                class_name='mb-5'
                )
            ],
            className='mb-5'
            )
        ],
        id='prod-row-collapse',
        is_open=False
        )
    ],
    justify='center'
    ),

    # PERFORMANCE SECTION
    dbc.Row([
        dbc.Button(
            'performance of regions AND the best, worst performed branches',
            'performance-collapse-btn',
            className='mb-3',
            color='success',
            n_clicks=0
        ),
        dbc.Collapse([
            dbc.Row([
                # dropdown checking if you wish for the region or the counties
                dcc.Dropdown(
                        id='reg-or-county-dropdown-performance',
                        options=[
                        {'label': 'Regional', 'value': 'region'},
                        {'label': 'County', 'value': 'county'}
                        ],
                        placeholder='please pick if per region or county'
                    ),
                    # graph to display performance of counties or regions
                    dcc.Graph(id='performance-fig', figure={}, className='mb-5')
            ],
            className='mb-5'
            )
        ],
        id='performance-row-collapse',
        is_open=False)
    ]),

    # TOP 10 COUNTIES HOURLY SALES SECTION
    dbc.Row([
        dbc.Button(
            'top 10 counties hourly sales',
            'hourly-collapse-btn',
            className='mb-3',
            color='primary',
            n_clicks=0
        ),
        dbc.Collapse([
            dbc.Row([
                # dropdown checking which county you wish to check
                dcc.Dropdown(
                        id='county-dropdown-hourly',
                        options=[
                        {'label': x, 'value': x}
                            for x in sorted(hourly_sales_of_best_counties['county'].unique())
                        ],
                        placeholder='please pick a county'
                    ),
                    # graph to display performance of counties or regions
                    dcc.Graph(id='hourly-fig', figure={}, className='mb-5')
            ],
            className='mb-5'
            )
        ],
        id='hourly-row-collapse',
        is_open=False)
    ]),

    # BEST AND WORST PROFITING BRANCHES SECTION
    dbc.Row([
        dbc.Button(
            'best & worst profiting counties',
            'profit-collapse-btn',
            className='mb-3',
            color='secondary',
            n_clicks=0
        ),
        dbc.Collapse([
            dbc.Row([
                dbc.Col([dcc.Graph(id='best-profit-graph', figure=best_profit_figure)]),
                dbc.Col([dcc.Graph(id='worst-profit-graph', figure=worst_profit_figure)])
            ])
        ],
        'profit-row-collapse',
        is_open=False
        )
    ])

],
fluid=True
)


#------------------
#       Callbacks
#------------------

# PRODUCT & PRODUCT CATEGORY SECTION

# toggle collapse call back for product/prod category section
@app.callback(
    Output("prod-row-collapse", "is_open"),
    [Input("products-collapse-btn", "n_clicks")],
    [State("prod-row-collapse", "is_open")],
)
# func attached to callback
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# callback to reveal list of cities or regions in the dropdown for prod / prod category section
@app.callback(
    Output('individual-dropdown', 'options'),

    Input('reg-or-county-dropdown-products', 'value')
)
# func attached to callback
def toggle_region_or_county(selection):
    if selection == 'region':
        return [
            {'label': x, 'value': x}
                for x in regional_products_df['region'].unique()
        ]
    elif selection =='county':
        return [
            {'label': x, 'value': x}
                for x in county_products_df['county'].unique()
        ]
    else:
        return []


# callback checking what the user has selected to be viewed in the product/prod category section
@app.callback(
    Output(component_id='product-fig', component_property='figure'),
    Output('first-section-results-info', 'children'),

    Input(component_id='reg-or-county-dropdown-products', component_property='value'),
    Input(component_id='products-or-categories-dropdown', component_property='value'),
    Input(component_id='individual-dropdown', component_property='value')
)
# func attached to callback
def define_product_graph(first_selection, second_selection, last_selection):
    # if the user has not yet selected a specific region or county
    if first_selection == None or second_selection == None or last_selection == None:
        return {}, 'Nothing has been selected yet..'
        # USER CHOSE PER REGION
        # if user has picked to see a specific region's products
    elif first_selection == 'region' and second_selection == 'products' and last_selection != None:
        # filter regional df based on the users selection
        filtered_df = regional_products_df[regional_products_df.region == last_selection]
        # create a pie chart showing the percentages 
        figure = ex.bar(filtered_df, 
                x='product',
                y='total_quantity_purchased',
                color='product',
                title=f"{last_selection}'s best 5 & worst 5 products overall",
                )

        return figure, f"Here we can see the 5 best products & the 5 worst. \n \
                        Hover over to see total amount sold. \n \
                        Click on key to the right to remove products"
    # if they chose regional prod categories
    elif first_selection == 'region' and second_selection == 'prod-cat' and last_selection != None:
        # filter regional prod_categories based
        filtered_df = regional_prod_categories[regional_prod_categories.region == last_selection]
        # create a pie chart showing the percentages
        figure = ex.bar(filtered_df, 
                x='product_category',
                y='total_quantity_purchased',
                color='product_category',
                title=f"{last_selection}'s product category sales overall",
                )

        return figure, f"Here we can see the spread of sales for each product category. \n \
                        Hover over to for further details \n \
                        Click on key to the right to remove one or more of the categories"
        
    # USER CHOSE PER COUNTY
    # if user picked to see products per county
    elif first_selection == 'county' and second_selection == 'products' and last_selection != None:
        # filter county df based on users selection
        filtered_df = county_products_df[county_products_df.county == last_selection]
        # create a pie chart showing the percentages
        figure = ex.bar(filtered_df, 
                x='product',
                y='total_quantity_purchased',
                color='product',
                title=f"{last_selection}'s best & worst products",
                )
            
        return figure, 'Here we can see the spread of sales for the top 5 and worst 5 products. \n \
                        Hover over for further details \n \
                        Click on key to the right to remove products'
    # if user has picked prod category per county 
    elif first_selection == 'county' and second_selection == 'prod-cat' and last_selection != None:
        # filter county df based on users selection
        filtered_df = county_prod_categories[county_prod_categories.county == last_selection]
        # create a pie chart showing the percentages
        figure = ex.bar(filtered_df, 
                x='product_category',
                y='total_quantity_purchased',
                color='product_category',
                title=f"{last_selection}'s product category sales overall",
                )
            
        return figure, 'Here we can see the spread of sales based on the product categories. \n \
                        Hover over for further details.. \n \
                        Click on key to the right to remove products'



# PERFORMANCE SECTION

# toggle collapse call back for best performance section
@app.callback(
    Output("performance-row-collapse", "is_open"),
    [Input("performance-collapse-btn", "n_clicks")],
    [State("performance-row-collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# callback for presenting performance results
@app.callback(
    Output('performance-fig', 'figure'),

    Input('reg-or-county-dropdown-performance', 'value')
)
def define_performance_graph(selection):
    if selection == None:
        return {}
    elif selection == 'region':
        figure = ex.bar(regional_performance,x='region',
                        y=['total_quantity_purchased','amount_in_gbp'],
                        title='Regional Performance',
                        color='region')

        return figure
    else:
        figure = ex.bar(counties_performance,'county',
                        ['total_quantity_purchased', 'amount_in_gbp'],
                        'county', title='the 10 best and 10 worst performed counties')

        return figure


# HOURLY SECTION

# toggle collapse call back for hourly section
@app.callback(
    Output("hourly-row-collapse", "is_open"),
    [Input("hourly-collapse-btn", "n_clicks")],
    [State("hourly-row-collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# callback for presenting hourly sales results
@app.callback(
    Output('hourly-fig','figure'),

    Input('county-dropdown-hourly','value')
)
def define_hourly_graph(selection):
    if selection == None:
        return {}
    else:
        filtered_df = hourly_sales_of_best_counties[hourly_sales_of_best_counties.county == selection]
        figure = ex.bar(filtered_df,'hour','total_quantity_purchased','hour',title=f'sales made per hour for {selection}')

        return figure


# PROFITTING SECTION

# toggle collapse call back for hourly section
@app.callback(
    Output("profit-row-collapse", "is_open"),
    [Input("profit-collapse-btn", "n_clicks")],
    [State("profit-row-collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# run server

if __name__ == '__main__':
    app.run_server(debug=True)
