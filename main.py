from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st

import pandas as pd
from data import get_data
from data import update_changes_in_df

st.set_page_config(page_title='Truefoundry Experiments')
st.title('LLM Experiments By Truefoundry')
df = pd.DataFrame(get_data())

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_columns("response", wrapText = True, autoHeight=True, width=600, resizable=False)
gb.configure_columns("prompt", wrapText = True, autoHeight=True, width=250)
gb.configure_columns("model_name", wrapText = True, autoHeight=True, width=150)
gb.configure_columns("inference_time", wrapText = True, autoHeight=True, width=150)
gb.configure_columns("user_reaction", wrapText = True, autoHeight=True, width=150, editable=True)
gb.configure_columns("run_id", hide=True)

grid_return = AgGrid(df, gridOptions=gb.build())
update_changes_in_df(df, grid_return['data'])
df = grid_return['data']