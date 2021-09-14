import streamlit as st
import plotly_express as px
import pandas as pd

st.set_option('deprecation.showfileUploaderEncoding', False)
# Tiêu đề
st.title("Data visualization App")
# Thêm sidebar
st.sidebar.subheader("Settings")
maxUploadSize = 200
# Set up
uploaded_file=st.sidebar.file_uploader(label="Upload your CSV or Excel file.",
			type=['csv','xlsx'])

# Function load data
@st.cache
def load_data(nrows):
    df = pd.read_csv(uploaded_file, nrows=nrows,encoding= 'unicode_escape')
    lowercase = lambda x: str(x).lower()
    df.rename(lowercase, axis='columns', inplace=True)
    return df
# Load 10,000 rows of data into the dataframe.
if uploaded_file is not None:
	try:
		df = load_data(10000000000)
	except Exception as e:
		print(uploaded_file)
# Notify the reader that the data was successfully loaded.
global numeric_columns
kq=st.sidebar.checkbox("Show data")

if kq:
	try:
		st.write("Loading data .........")
		st.write(df)
		numeric_columns=df.columns.tolist()
	except Exception as e:
		print(e)
		st.write("Please upload file")

chart_select = st.sidebar.selectbox(
	label="Select the chart type",
	options = ['','Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
)

if chart_select == 'Scatterplots' :
	st.sidebar.subheader("'Scatterplot Settings'")
	try:
		x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
		y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
		plot = px.scatter(data_frame=df, x=x_values, y=y_values)
		kq1=st.sidebar.checkbox("Show Dashboard")
		if kq1:
			st.plotly_chart(plot) 
	except Exception as e:
		print(e)