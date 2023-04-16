import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"command": "st.selectbox dehjcbdbjc ceiciejcn icneicnencnidecinednc cniedcniendci jhcjdcjdcjed cj edjc jed c nee", "rating": "wcjknwdjcndkjcnndcndcjknd kjc cnwecneijdcn cniencijedncnedi cniwdncijwdncinwdicnd cnijwndijcndwijcnijwdcn", "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.experimental_data_editor(df, num_rows="dynamic", use_container_width=0.9)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")