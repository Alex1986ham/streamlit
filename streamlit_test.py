import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# My first app
Hello *world!*
""")

st.write("Hers is our first attempt at susing data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns(['a', 'b'], 'c'])
st.line_chart(chart_data)