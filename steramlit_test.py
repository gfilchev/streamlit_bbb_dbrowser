
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import numpy as np
import csv
from tabulate import tabulate
import urllib

# Database parameters intersnak
params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
				 "SERVER=tcp:212.39.68.184\MSSQLSERVER,49159;"
				 "DATABASE=AX2012R3_Intersnack_Live;"
				 "UID=bbb;"
				 "PWD=12@bbs21")

# Connection to DB intersnak
engine = sal.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params),encoding="utf8")



#STREAMLIT_AGGRID_URL = "https://github.com/PablocFonseca/streamlit-aggrid"
st.set_page_config(
	layout="wide", page_icon="🖱️", page_title="Интерснак ДБ"
)
#st.title("Интерснак ДБ")

def main():
	page = st.sidebar.selectbox("Ибзор на таблица", [
		"AXPBBBORDERS", 
		"AXPBBBORDERSLINE" , 
		"AXPBBBRECEIPT",
		"AXPBBBRECEIPTLINE",
		"DSBBBORDERS",
		"DSBBBORDERSLINE",
		"DSBBBRECEIPT",
		"DSBBBRECEIPTLINE",
		])

	if page == "AXPBBBORDERS":
		def aggrid_interactive_table(df: pd.DataFrame):
			sql_query = pd.read_sql_query('SELECT * FROM AXPBBBORDERS ORDER BY RECID DESC', engine)
			# Saving the data into dataframe
			df1 = pd.DataFrame(sql_query)
			options = GridOptionsBuilder.from_dataframe(
				df1, enableRowGroup=True, enableValue=True, enablePivot=True
			)

			options.configure_side_bar()

			options.configure_auto_height(autoHeight = False)
			options.configure_pagination(enabled=True, paginationAutoPageSize=True, paginationPageSize=20)


			options.configure_selection("single")#use_checkbox = True)
			selection = AgGrid(
				df1,
				enable_enterprise_modules=True,
				gridOptions=options.build(),
				theme="light",
				update_mode=GridUpdateMode.MODEL_CHANGED,
				allow_unsafe_jscode=True,
				height=620,
				width="100%"
			)

			return selection

		iris = pd.read_csv(
			"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
		)

		selection = aggrid_interactive_table(df=iris)

		if selection:
			st.write("You selected:")
			st.json(selection["selected_rows"])

	if page == "AXPBBBORDERSLINE":
		def aggrid_interactive_table(df: pd.DataFrame):
			sql_query = pd.read_sql_query('SELECT * FROM AXPBBBORDERSLINE ORDER BY RECID DESC', engine)
			# Saving the data into dataframe
			df1 = pd.DataFrame(sql_query)
			options = GridOptionsBuilder.from_dataframe(
				df1, enableRowGroup=True, enableValue=True, enablePivot=True
			)

			options.configure_side_bar()

			options.configure_auto_height(autoHeight = False)
			options.configure_pagination(enabled=True, paginationAutoPageSize=True, paginationPageSize=20)


			options.configure_selection("single")#use_checkbox = True)
			selection = AgGrid(
				df1,
				enable_enterprise_modules=True,
				gridOptions=options.build(),
				theme="light",
				update_mode=GridUpdateMode.MODEL_CHANGED,
				allow_unsafe_jscode=True,
				height=620,
				width="100%"
			)

			return selection

		iris = pd.read_csv(
			"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
		)

		selection = aggrid_interactive_table(df=iris)

		if selection:
			st.write("You selected:")
			st.json(selection["selected_rows"])

	if page == "AXPBBBRECEIPT":
		def aggrid_interactive_table(df: pd.DataFrame):
			sql_query = pd.read_sql_query('SELECT * FROM AXPBBBRECEIPT ORDER BY RECID DESC', engine)
			# Saving the data into dataframe
			df1 = pd.DataFrame(sql_query)
			options = GridOptionsBuilder.from_dataframe(
				df1, enableRowGroup=True, enableValue=True, enablePivot=True
			)

			options.configure_side_bar()

			options.configure_auto_height(autoHeight = False)
			options.configure_pagination(enabled=True, paginationAutoPageSize=True, paginationPageSize=20)


			options.configure_selection("single")#use_checkbox = True)
			selection = AgGrid(
				df1,
				enable_enterprise_modules=True,
				gridOptions=options.build(),
				theme="light",
				update_mode=GridUpdateMode.MODEL_CHANGED,
				allow_unsafe_jscode=True,
				height=620,
				width="100%"
			)

			return selection

		iris = pd.read_csv(
			"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
		)

		selection = aggrid_interactive_table(df=iris)

		if selection:
			st.write("You selected:")
			st.json(selection["selected_rows"])

	if page == "AXPBBBRECEIPTLINE":
		def aggrid_interactive_table(df: pd.DataFrame):
			sql_query = pd.read_sql_query('SELECT * FROM AXPBBBRECEIPTLINE ORDER BY RECID DESC', engine)
			# Saving the data into dataframe
			df1 = pd.DataFrame(sql_query)
			options = GridOptionsBuilder.from_dataframe(
				df1, enableRowGroup=True, enableValue=True, enablePivot=True
			)

			options.configure_side_bar()

			options.configure_auto_height(autoHeight = False)
			options.configure_pagination(enabled=True, paginationAutoPageSize=True, paginationPageSize=20)


			options.configure_selection("single")#use_checkbox = True)
			selection = AgGrid(
				df1,
				enable_enterprise_modules=True,
				gridOptions=options.build(),
				theme="light",
				update_mode=GridUpdateMode.MODEL_CHANGED,
				allow_unsafe_jscode=True,
				height=620,
				width="100%"
			)

			return selection

		iris = pd.read_csv(
			"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
		)

		selection = aggrid_interactive_table(df=iris)

		if selection:
			st.write("You selected:")
			st.json(selection["selected_rows"])

	if page == "DSBBBORDERS":
		def aggrid_interactive_table(df: pd.DataFrame):
			sql_query = pd.read_sql_query('SELECT * FROM DSBBBORDERS ORDER BY RECID DESC', engine)
			# Saving the data into dataframe
			df1 = pd.DataFrame(sql_query)
			options = GridOptionsBuilder.from_dataframe(
				df1, enableRowGroup=True, enableValue=True, enablePivot=True
			)

			options.configure_side_bar()

			options.configure_auto_height(autoHeight = False)
			options.configure_pagination(enabled=True, paginationAutoPageSize=True, paginationPageSize=20)


			options.configure_selection("single")#use_checkbox = True)
			selection = AgGrid(
				df1,
				enable_enterprise_modules=True,
				gridOptions=options.build(),
				theme="light",
				update_mode=GridUpdateMode.MODEL_CHANGED,
				allow_unsafe_jscode=True,
				height=620,
				width="100%"
			)

			return selection

		iris = pd.read_csv(
			"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
		)

		selection = aggrid_interactive_table(df=iris)

		if selection:
			st.write("You selected:")
			st.json(selection["selected_rows"])

	if page == "DSBBBORDERSLINE":
		def aggrid_interactive_table(df: pd.DataFrame):
			sql_query = pd.read_sql_query('SELECT * FROM DSBBBORDERSLINE ORDER BY RECID DESC', engine)
			# Saving the data into dataframe
			df1 = pd.DataFrame(sql_query)
			options = GridOptionsBuilder.from_dataframe(
				df1, enableRowGroup=True, enableValue=True, enablePivot=True
			)

			options.configure_side_bar()

			options.configure_auto_height(autoHeight = False)
			options.configure_pagination(enabled=True, paginationAutoPageSize=True, paginationPageSize=20)


			options.configure_selection("single")#use_checkbox = True)
			selection = AgGrid(
				df1,
				enable_enterprise_modules=True,
				gridOptions=options.build(),
				theme="light",
				update_mode=GridUpdateMode.MODEL_CHANGED,
				allow_unsafe_jscode=True,
				height=620,
				width="100%"
			)

			return selection

		iris = pd.read_csv(
			"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
		)

		selection = aggrid_interactive_table(df=iris)

		if selection:
			st.write("You selected:")
			st.json(selection["selected_rows"])

	if page == "DSBBBRECEIPT":
		def aggrid_interactive_table(df: pd.DataFrame):
			sql_query = pd.read_sql_query('SELECT * FROM DSBBBRECEIPT ORDER BY RECID DESC', engine)
			# Saving the data into dataframe
			df1 = pd.DataFrame(sql_query)
			options = GridOptionsBuilder.from_dataframe(
				df1, enableRowGroup=True, enableValue=True, enablePivot=True
			)

			options.configure_side_bar()

			options.configure_auto_height(autoHeight = False)
			options.configure_pagination(enabled=True, paginationAutoPageSize=True, paginationPageSize=20)


			options.configure_selection("single")#use_checkbox = True)
			selection = AgGrid(
				df1,
				enable_enterprise_modules=True,
				gridOptions=options.build(),
				theme="light",
				update_mode=GridUpdateMode.MODEL_CHANGED,
				allow_unsafe_jscode=True,
				height=620,
				width="100%"
			)

			return selection

		iris = pd.read_csv(
			"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
		)

		selection = aggrid_interactive_table(df=iris)

		if selection:
			st.write("You selected:")
			st.json(selection["selected_rows"])

	if page == "DSBBBRECEIPTLINE":
		def aggrid_interactive_table(df: pd.DataFrame):
			sql_query = pd.read_sql_query('SELECT * FROM DSBBBRECEIPTLINE ORDER BY RECID DESC', engine)
			# Saving the data into dataframe
			df1 = pd.DataFrame(sql_query)
			options = GridOptionsBuilder.from_dataframe(
				df1, enableRowGroup=True, enableValue=True, enablePivot=True
			)

			options.configure_side_bar()

			options.configure_auto_height(autoHeight = False)
			options.configure_pagination(enabled=True, paginationAutoPageSize=True, paginationPageSize=20)


			options.configure_selection("single")#use_checkbox = True)
			selection = AgGrid(
				df1,
				enable_enterprise_modules=True,
				gridOptions=options.build(),
				theme="light",
				update_mode=GridUpdateMode.MODEL_CHANGED,
				allow_unsafe_jscode=True,
				height=620,
				width="100%"
			)

			return selection

		iris = pd.read_csv(
			"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
		)

		selection = aggrid_interactive_table(df=iris)

		if selection:
			st.write("You selected:")
			st.json(selection["selected_rows"])

if __name__ == "__main__":
    main()
