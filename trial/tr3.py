import streamlit as st
import pandas as pd
import numpy as np
from data import get_data

# {
#     "model_name": "my_mod",
#     "prompt": "hello world promt",
#     "response": "this is a dummy response of any arbit lengthsdwecijweciewnicienocneceiwcden cefnicnief ",
#     "inference_time": 1.44,
#     "user_reaction": "Green"
# }, 
# df = pd.DataFrame(
#    np.random.randn(10, 5),
#    columns=('col %d' % i for i in range(5)))

st.dataframe(get_data())