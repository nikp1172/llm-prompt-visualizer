import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Description': ['This is a long description that should wrap', 'Short description', 'Another long description that should wrap']}
df = pd.DataFrame(data)

# define the column definitions for the grid
column_defs = [{'field': 'Name', 'headerName': 'Name', 'sortable': True},
               {'field': 'Description', 'headerName': 'Description', 'sortable': True,
                'cellStyle': {'white-space': 'normal'}}]

# display the grid
grid_result = AgGrid(df, column_defs=column_defs, height=200, width='100%')