# then making the project on the Global Supermarket Dataset then Analysics the Data And Visualizations the data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import mysql.connector
# import the csv file from the sql
Conn =mysql.connector.connect(
    host ="localhost",
    user="root",
    password="Gurvinder@SQL2026",
    database="global_superstore"
)
query ={
# -- THEN CHECK THE COUNT OF THE DATASET
"Total_Count":"""SELECT COUNT(*) FROM DATACOLUMNS;""",
"Fully_Data" : """SELECT * FROM DATACOLUMNS;""",
# -- Check Columns
"Columns":"""desc DATACOLUMNS;""",
"Total_Sales":"""select round(Sum(Sales),2) as Total_Sales from DATACOLUMNS ;""",
"Monthly_Sales":"""Select month(Ship_Date) as Month,sum(Sales) As Monthly_Sales from DATACOLUMNS group by Month(Ship_Date) order by Month(Ship_Date) asc ;""",
"Yearly_Sales":"""Select year(Ship_Date) AS Year,sum(Sales) As Yearly_Trend from DATACOLUMNS group by year(Ship_Date) order by year(Ship_Date) asc;""",
"Sales_Growth_rate":"""Select year(Ship_Date) AS Year,sum(Sales) as Sales_Trends ,sum(Sales) - lag(sum(Sales)) OVER(ORDER BY YEAR(SHIP_DATE)) AS SALES_GROWTH FROM DATACOLUMNS group by Year(Ship_Date);""",
"Sales_Growth_rate_Monthly":"""Select Month(Ship_Date) AS Month,sum(Sales) as Sales_Trends ,sum(Sales) - lag(sum(Sales)) OVER(ORDER BY Month(SHIP_DATE)) AS Monthly_Sales_GROWTH FROM DATACOLUMNS group by Month(Ship_Date);""",
"Catagorical_Sales":"""Select Category,sum(Sales) AS Categorical_Sales from DATACOLUMNS group by Category;""",
"Subcatagorical_Sales":"""Select Sub_Category as Sub_Category,sum(Sales) AS Sub_Categorical_Sales from DATACOLUMNS group by Sub_Category;""",
"region_Wish_Sales": """Select Region,sum(Sales) AS Region_Sales from DATACOLUMNS group by Region;""",
"Yearly_Sales_Growth":"""SELECT YEAR(Ship_Date) AS Year,SUM(Sales) AS Sales_Trends,ROUND(((SUM(Sales) -LAG(SUM(Sales)) OVER(ORDER BY YEAR(Ship_Date)))/LAG(SUM(Sales)) OVER(ORDER BY YEAR(Ship_Date))) * 100,2) AS SALES_GROWTH_RATE FROM DATACOLUMNS GROUP BY YEAR(Ship_Date) ORDER BY Year;""",
"Monthly_Sales_Growth":"""SELECT MONTH(Ship_Date) AS Month,SUM(Sales) AS Monthly_Sales_Trends,ROUND((SUM(Sales) -LAG(SUM(Sales)) OVER(ORDER BY MONTH(Ship_Date))),2) AS Monthly_Growth FROM DATACOLUMNS GROUP BY MONTH(Ship_Date) ORDER BY Month;""",
# Then analyze the data of the Product Analysics
"Total_Profit":"""Select ROUND(sum(Profit),2) as Total_Profit from DATACOLUMNS;""",
"PROFIT_MARGIN":"""SELECT SUM(Profit) As Profit,sum(Sales) as Sales, round((sum(Profit) / sum(Sales))*100,2) As Profit_Margin from DATACOLUMNS;""",
"Monthly_Profit":"""SELECT Month(Ship_Date) AS Month,Sum(Profit) AS Monthly_Profit from DATACOLUMNS group by Month(Ship_Date) order by Month(Ship_Date) asc;""",
"Yearly_Profit":"""Select Year(Ship_Date) as Year,SUM(Profit) as Yearly_Profit from DATACOLUMNS group by Year(Ship_Date) order by Year(Ship_Date) asc;""",
"Product_Profit":"""Select Product_Name as Product,Sum(Profit) as Product_Profit from DATACOLUMNS group by Product_Name order by Product_Name;""",
"Catagorical_Wish_Profit":"""SELECT Category,sum(profit) AS Categorical_Profit from DATACOLUMNS group by Category;""",
"Subcatagory_Wish_Profit":"""SELECT Sub_Category,sum(profit) AS SubCategorical_Profit from DATACOLUMNS group by Sub_Category;""",
"State_Profit":"""Select State as State,sum(Profit) as State_Profit from DATACOLUMNS group by State order by State asc;""",
"City_Profit":"""Select City as City,sum(Profit) as City_Profit from DATACOLUMNS group by City order by City asc;""",
"Country_Profit":"""Select Country as Country,sum(Profit) as Profit from DATACOLUMNS group by Country order by Country asc;""",
"Region_Wish_Profit":"""SELECT Region,sum(profit) AS Region_Profit from DATACOLUMNS group by Region;""",
"Loss_Making_Product": """SELECT Product_Name,sum(Profit) AS Product_Profit from DATACOLUMNS group by Product_Name having sum(Profit) <0 order by Product_Profit asc LIMIT 10;""",
# then analysics the data of customer  data
"Top_Customer":"""Select  Customer_ID,SUM(Sales) AS Top_Customer from DATACOLUMNS group by Customer_ID having sum(Sales)>20000 order by Top_Customer desc limit 5;""",
"Repeat_Customer":"""Select Customer_Name,Category,Sub_Category,Product_Name,count(Sales) AS Repeat_Customer from DATACOLUMNS group by Customer_Name,Category,Sub_Category,Product_Name having count(Sales) >1 order by Repeat_Customer asc limit 20;""",
"Customer_Contribution":"""Select Customer_Name as Customer,Sum(Sales) AS Sales ,round(SUM(Sales) * 100 /(Select SUM(Sales) from DATACOLUMNS),2) AS Sales_Contributions from DATACOLUMNS group by Customer_Name order by Sales_Contributions desc limit 10;""",
"High_Saling_CustomerCount":"""Select count(Customer_ID) as Top_Sales_Customer_Count,sum(Sales) as High_Sales from DATACOLUMNS group by Customer_ID having sum(sales)>30000;""",
"Low_Saling_CustomerCount":"""Select count(Customer_ID) as Worst_Sales_Customer_Count,sum(Sales) as High_Sales from DATACOLUMNS group by Customer_ID having sum(sales)<100;""",
"Top_State":"""Select State ,Count(distinct Customer_ID) as Customer_Count from DATACOLUMNS group by State order by State desc limit 10;""",
# THEN ANALYSICS THE DATA OF THE ORDER
"Total_Order":"""SELECT COUNT(DISTINCT Order_ID) AS Total_Orders FROM DATACOLUMNS;""",
"Monthly_Order":"""SELECT month(Order_Date) AS MONTH ,COUNT(distinct Order_ID) AS Order_Count from DATACOLUMNS GROUP BY MONTH order by MONTH;""",
"Yearly_Order_Count":"""SELECT YEAR(Order_Date) as Year,count(distinct Order_ID) AS Order_Count from DATACOLUMNS group by Year;""",
"ShipMode_Order":"""SELECT Ship_Mode,COUNT(distinct ORDER_ID) AS TOTAL_ORDER FROM DATACOLUMNS GROUP BY Ship_Mode ; """,
"Product_Order":"""Select Product_Name as Product, count(Distinct Order_ID) as Product_Order FROM DATACOLUMNS group by Product_Name order by Product_Name asc;""",
"Category_Order":"""Select Category ,Count(Distinct Order_ID) as Category_Order From DATACOLUMNS group BY Category order by Category asc;""",
"SubCategory_Order":"""Select Sub_Category ,count(Distinct Order_ID) as SubCategory_Order from DATACOLUMNS group by Sub_Category order by Sub_Category asc;""",
"Region_Wish_Order":"""SELECT REGION ,COUNT(DISTINCT ORDER_ID) AS REGION_WISH_ORDER FROM DATACOLUMNS GROUP BY REGION;""",
"Country_Order":"""SELECT COUNTRY,COUNT(DISTINCT ORDER_ID) AS COUNTRY_Order FROM DATACOLUMNS GROUP BY COUNTRY;""",
"City_Order":"""Select City,count(distinct Order_Id) as City_Order FROM DATACOLUMNS GROUP BY CITY ORDER BY CITY ASC;""",
"State_Order":"""SELECT STATE,COUNT(DISTINCT ORDER_ID) AS STATE_ORDERCOUNT FROM DATACOLUMNS GROUP BY STATE;""",
"Segment_Order":"""SELECT SEGMENT ,COUNT(DISTINCT ORDER_ID) AS SEGMENT_ORDER FROM DATACOLUMNS GROUP BY SEGMENT;""",
"Daily_Order_trends":"""SELECT ORDER_DATE,COUNT(distinct ORDER_DATE) AS DAILY_SALES_TRENDS FROM DATACOLUMNS  WHERE ORDER_DATE IS NOT NULL GROUP BY ORDER_DATE  ORDER BY ORDER_DATE; """,
# then Analysics the Product Analyic DATA
"Top_Selling_Product":"""Select  Product_Name ,sum(Sales) as Product_Sales from DATACOLUMNS group by Product_Name order by Product_Name limit 10;""",
"least_selling_Product":"""Select Product_Name,max(Sales) AS Recently_Salling_Product from DATACOLUMNS group by Product_Name;""",
"High_Profit_Product":"""Select Product_Name ,sum(Profit) AS High_Profit_Product from DATACOLUMNS group by Product_Name limit 1;""",
"Low_Profit_Product":"""Select Product_Name,sum(Profit) AS Low_Profit_Product from DATACOLUMNS group by Product_Name limit 1;""",
"SHIP_DATA":"""Select Ship_Mode, SUM(SALES) as SHIP_MODE_PERFORMANCE FROM DATACOLUMNS GROUP BY Ship_Mode;""",
"DELEVERY_TIME":"""SELECT ROUND(AVG(DATEDIFF(Ship_Date,Order_Date)),2) AS Average_Delievery_Day from DATACOLUMNS;""",
# -- Shipping cost Impact MEANS PRODUCT TO CUSTOMER DELEVERY PRODUCT
"Shipping_Cost":"""SELECT ROUND(AVG(Shipping_Cost),2) AS SHIPPING_COST_IMPACT FROM DATACOLUMNS;""",
# DISCOUNT ANALYSICS THE DATA 
"DISCOUNT_VS_SALES":"""SELECT Discount AS DISCOUNT,SUM(Sales) AS SALES_DESTRIBUTION_PROFIT FROM DATACOLUMNS group by Discount;""",
"Max_Discouunt_Max_Sales":"""SELECT Discount AS DISCOUNT,MAX(Sales) AS MAX_SALES_DESTRIBUTION_DISCOUNT FROM DATACOLUMNS group by Discount;""",
"Discount_Minimum_Sales":"""SELECT Discount AS DISCOUNT,MIN(Sales) AS MIN_SALES_DESTRIBUTION_DISCOUNT FROM DATACOLUMNS group by Discount;""",
"Discount_VS_Profit":"""SELECT Discount AS DISCOUNT,SUM(Profit) AS SALE_DESTRIBUTION_PROFIT FROM DATACOLUMNS group by Discount;""",
"Discount_Having_Max_Profit":"""SELECT Discount AS DISCOUNT,MAX(Profit) AS MAX_SALE_DESTRIBUTION_PROFIT FROM DATACOLUMNS group by Discount;""",
"Discount_Having_Min_Profit":"""SELECT Discount AS DISCOUNT,MIN(Profit) AS MIN_SALE_DESTRIBUTION_PROFIT FROM DATACOLUMNS group by Discount;""",
"High_Discount_Having_Min_Profit":"""SELECT Discount AS DISCOUNT,MIN(Profit) AS HIGH_DISCOUNT_LOSS FROM DATACOLUMNS group by Discount ORDER BY HIGH_DISCOUNT_LOSS LIMIT 1;""",
#-GEOGRAPHICAL ANALYSICS DATA
"Country_Sales":"""SELECT COUNTRY,ROUND(SUM(SALES),2) AS Country_Wise_Sales_Distributios,round(SUM(PROFIT),2)AS COUNTRY_WISH_PERFORMACE_PROFIT FROM DATACOLUMNS group by COUNTRY;""",
"Better_Performance_Country":"""SELECT COUNTRY,ROUND(SUM(SALES),2) AS Max_SALES_PERFORMANCE_SALES,round(SUM(PROFIT),2) AS Max_COUNTRY_WISH_PERFORMACE_PROFIT FROM DATACOLUMNS group by COUNTRY,SALES order by Max_COUNTRY_WISH_PERFORMACE_PROFIT desc limit 1 ;""",
"Worse_Performance_Country":"""SELECT COUNTRY,ROUND(SUM(SALES),2) AS Min_SALES_PERFORMANCE_SALES,round(SUM(PROFIT),2) AS Min_COUNTRY_WISH_PERFORMACE_PROFIT FROM DATACOLUMNS group by COUNTRY,SALES order by Min_COUNTRY_WISH_PERFORMACE_PROFIT asc limit 1 ;""",
"State_Wise_Performance":"""SELECT State,ROUND(SUM(SALES),2) AS STATE_PERFORMANCE_SALES,round(SUM(PROFIT),2) AS STATE_WISH_PERFORMACE_PROFIT FROM DATACOLUMNS group by State;""",
"Better_Performance_State":"""SELECT STATE,ROUND(SUM(SALES),2) AS MAX_STATE_PERFORMANCE_SALES,round(SUM(PROFIT),2) AS MAX_STATE_WISH_PERFORMACE_PROFIT FROM DATACOLUMNS group by STATE order by MAX_STATE_WISH_PERFORMACE_PROFIT desc limit 1 ;""",
"State_Sales&Profit":"""SELECT STATE,ROUND(SUM(SALES),2) AS MIN_STATE_PERFORMANCE_SALES,round(SUM(PROFIT),2) AS MIN_STATE_WISH_PERFORMACE_PROFIT FROM DATACOLUMNS group by STATE order by MIN_STATE_WISH_PERFORMACE_PROFIT asc limit 1 ;""",
"City_Sales&Profit":"""SELECT City,ROUND(SUM(SALES),2) AS City_PERFORMANCE_SALES,round(SUM(PROFIT),2) AS CITY_WISH_PERFORMACE_PROFIT FROM DATACOLUMNS group by City;""",
"Max_Sale&Profit_City":"""SELECT City,ROUND(SUM(SALES),2) AS MAX_City_PERFORMANCE_SALES,round(SUM(PROFIT),2) AS MAX_City_WISH_PERFORMACE_PROFIT FROM DATACOLUMNS group by City order by MAX_City_WISH_PERFORMACE_PROFIT desc limit 1 ;""",
"Min_Sale&Profit_City":"""SELECT City,ROUND(SUM(SALES),2) AS MIN_City_PERFORMANCE_SALES,round(SUM(PROFIT),2) AS MIN_City_WISH_PERFORMACE_PROFIT FROM DATACOLUMNS group by City order by MIN_City_WISH_PERFORMACE_PROFIT asc limit 1 ;""",
# "-- THEN ANAYICS THE SALES&PROFIT OF THE REGIONS
"Maximum_Sales_Region":"""select Region as Region, round(sum(Sales),2) as Maximum_Region_Sales from DATACOLUMNS group by Region order by sum(Sales) desc limit 1;""",
"Minimum_Sales_Region":"""select Region as Region, round(sum(Sales),2) as Minimum_Region_Sales from DATACOLUMNS group by Region order by sum(Sales) asc limit 1;""",
"Region_Sales&Profit":"""SELECT Region,ROUND(SUM(SALES),2) AS Region_Perfomance_Sales ,round(SUM(PROFIT),2) AS Region_Wish_Performance_Profits FROM DATACOLUMNS group by Region;""",
"Max_Sale&Profit_Region":"""SELECT Region,ROUND(SUM(SALES),2)  AS Max_Region_Perfomance_Sales,round(SUM(PROFIT),2) AS Max_Region_Perfomance_Profit FROM DATACOLUMNS group by Region order by Max_Region_Perfomance_Profit desc limit 1 ;""",
"Min_Sale&Profit_Region":"""SELECT Region,ROUND(SUM(SALES),2)  AS Min_Region_Perfomance_Sales,round(SUM(PROFIT),2) AS Min_Region_Perfomance_Profit FROM DATACOLUMNS group by Region order by Min_Region_Perfomance_Profit desc limit 1 ;""",
}
result ={}
for name, q in query.items():
    try:
        result[name] = pd.read_sql(q, Conn)
        print(f"✅ {name}")
    except Exception as e:
        print(f"\n❌ ERROR IN QUERY: {name}")
        print("SQL:")
        print(q)
        print("\nERROR:")
        print(e)
        break
# Access 
Total_Count=result["Total_Count"]
Fully_Data =result["Fully_Data"]
Columns =result["Columns"]
# Sales data
Total_Sales =result["Total_Sales"]
Monthly_Sales =result["Monthly_Sales"]
Yearly_Sales =result["Yearly_Sales"]
Sales_Growth_rate =result["Sales_Growth_rate"]
Catagorical_Sales=result["Catagorical_Sales"]
Subcatagorical_Sales =result["Subcatagorical_Sales"]
region_Wish_Sales=result["region_Wish_Sales"]
Yearly_Sales_Growth =result["Yearly_Sales_Growth"]
Monthly_Sales_Growth =result["Monthly_Sales_Growth"]
# PROFIT DATA
Total_Profit =result["Total_Profit"]
Profit_Margin =result["PROFIT_MARGIN"]
Monthly_Profit=result["Monthly_Profit"]
Yearly_Profit =result["Yearly_Profit"]
Product_Profit =result["Product_Profit"]
Catagorical_Wishes_Profit =result["Catagorical_Wish_Profit"]
Subcatagory_Wish_Profit =result["Subcatagory_Wish_Profit"]
State_Profit =result["State_Profit"]
City_Profit =result["City_Profit"]
Country_Profit =result["Country_Profit"]
Region_Wish_Profit =result["Region_Wish_Profit"]
Loss_Making_Product =result["Loss_Making_Product"]
# Customer_Data
Top_Customer =result["Top_Customer"]
Repeat_Customer =result["Repeat_Customer"]
Customer_Contribution =result["Customer_Contribution"]
High_Saling_CustomerCount =result["High_Saling_CustomerCount"]
Low_Saling_CustomerCount=result["Low_Saling_CustomerCount"]
Top_State=result["Top_State"]
# ORDER_DATA
Total_Order =result["Total_Order"]
Monthly_Order =result["Monthly_Order"]
Yearly_Order_Count =result["Yearly_Order_Count"]
ShipMode_Order =result["ShipMode_Order"]
Region_Wish_Order =result["Region_Wish_Order"]
Country_Order =result["Country_Order"]
State_Order =result["State_Order"]
Segment_Order =result["Segment_Order"]
Product_Order =result["Product_Order"]
City_Order =result["City_Order"]
SubCategory_Order =result["SubCategory_Order"]
Category_Order =result["Category_Order"]
Daily_Order_trends =result["Daily_Order_trends"]
# Product Data Analysics
Top_Selling_Product =result["Top_Selling_Product"]
least_selling_Product =result["least_selling_Product"]
High_Profit_Product =result["High_Profit_Product"]
Low_Profit_Product  =result["Low_Profit_Product"]
Ship_Info =result["SHIP_DATA"]
Delievery_Time =result["DELEVERY_TIME"]
Shipping_Cost =result["Shipping_Cost"]
# Discount data Analysics 
Discount_VS_Sales =result["DISCOUNT_VS_SALES"]
Max_Discouunt_Max_Sales=result["Max_Discouunt_Max_Sales"]
Discount_Minimum_Sales =result["Discount_Minimum_Sales"]
Discount_VS_Profit =result["Discount_VS_Profit"]
Discount_Having_Max_Profit =result["Discount_Having_Max_Profit"]
Discount_Having_Min_Profit =result["Discount_Having_Min_Profit"]
High_Discount_Having_Min_Profit =result["High_Discount_Having_Min_Profit"]
#-GEOGRAPHICAL ANALYSICS DATA
Country_Sales =result["Country_Sales"]
Better_Performance_Country =result["Better_Performance_Country"]
Worse_Performance_Country =result["Worse_Performance_Country"]
State_Wise_Performance =result["State_Wise_Performance"]
Better_Performance_State =result["Better_Performance_State"]
State_Sales_Profit = result["State_Sales&Profit"]
City_Sales_Profit =result["City_Sales&Profit"]
Max_Sale_Profit_City =result["Max_Sale&Profit_City"]
Min_Sale_Profit_City =result["Min_Sale&Profit_City"]
# REGION ANALYSICS DATA
Maximum_Sales_Region =result["Maximum_Sales_Region"]
Minimum_Sales_Region =result["Minimum_Sales_Region"]
Region_Sales_Profit =result["Region_Sales&Profit"]
Max_Sale_Profit_Region =result["Max_Sale&Profit_Region"]
Min_Sale_Profit_Region =result["Min_Sale&Profit_Region"]
# then store the all data in to the DF
df=pd.read_sql("SELECT * FROM DATACOLUMNS",Conn)
# then Visualization the data
import streamlit as st
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)
st.subheader("A Data-Driven View of Global Sales Performance and Profitability")
st.markdown("""
<style>

/* ================= SIDEBAR FIX ================= */
section[data-testid="stSidebar"]{
    padding-top: 0rem !important;
    margin-top: 0px !important;
    position: fixed;
    top: 0;
    left: 0;
    height: 100vh;
    overflow-y: auto;
}

/* Sidebar inner spacing */
section[data-testid="stSidebar"] > div{
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
}

/* Sidebar title size */
[data-testid="stSidebar"] h2{
    font-size: 32px !important;
}

/* Sidebar text size */
[data-testid="stSidebar"] p{
    font-size: 18px !important;
}

/* Sidebar button styling */
.stButton > button{
    font-size: 18px !important;
    font-weight: bold !important;
}

/* ================= MAIN PAGE SPACING FIX ================= */
.block-container{
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}

</style>
""", unsafe_allow_html=True)
# then create the sidebar Subplots name columns
st.sidebar.markdown("""
<h3 style='text-align:center;'>🛒 Global SuperStore</h3>
<p style='text-align:center;'>Business Analytics Dashboard</p>
""", unsafe_allow_html=True)
st.sidebar.divider()
if "page" not in st.session_state:
    st.session_state.page = "Overview"
if st.sidebar.button("💰 Sales Analysis"):
    st.session_state.page="💰 Sales Analysis"
if st.sidebar.button("📈 Profit Analysis"):
    st.session_state.page="📈 Profit Analysis"
if st.sidebar.button("📋 Order Analysis"):
    st.session_state.page="📋 Order Analysis"
if st.sidebar.button("📦 Product Analysis"):
    st.session_state.page="📦 Product Analysis"
if st.sidebar.button("👥 Customer Analysis"):
    st.session_state.page="👥 Customer Analysis"
if st.sidebar.button("🌎 Geographical Analysis"):
    st.session_state.page="🌎 Geographical Analysis"

page = st.session_state.page
# side bar show the tool using
with st.sidebar.container(border=True):
    st.markdown("### 🛠️ Tools Used")
    with st.sidebar.container(border=True):
        st.write("🐍 Python")
        st.write("🗄️ MySQL")
        st.write("📊 Plotly")
        st.write("🌐 Streamlit")
# then analysics the data for the visualizations 
print(df.info())
Total_Saless =round(df["Sales"].sum(),2)
print("Total Sales :",Total_Saless)
Total_Order_Count =df["Order_ID"].nunique()
print("Total Order Count :",Total_Order_Count)
Total_Profits =round(df["Profit"].sum(),2)
print("Total Profit :",Total_Profits)
Total_Quantity =df["Quantity"].sum()
print("Total Quantity",Total_Quantity)
# Sales Growth Check 
# monthly data Change
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
Sales_Growth = df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum().reset_index()
Profit_Growth =df.groupby(df["Order_Date"].dt.to_period("M"))["Profit"].sum().reset_index()
# then growth calcuate
Sales_Growth["Sales_Growth%"] =Sales_Growth["Sales"].pct_change() *100
Profit_Growth["Profit_Growth%"] =Profit_Growth["Profit"].pct_change() *100
latest_sales_growth = Sales_Growth["Sales_Growth%"].iloc[-1]
latest_profit_growth = Profit_Growth["Profit_Growth%"].iloc[-1]

# then Visualization the plot 
if page == "💰 Sales Analysis":
    col1,col2 =st.columns([0.02,0.03])
    with col1:
        with st.container(border=True):
            st.markdown("""#### 🌍 Global Marketing Dataset Overview""")
            st.write("The Global Marketing dataset is a business analytics dataset that represents real-world sales, customers, products, shipping, and profit performance across different regions and markets.")

    with col2:
        with st.container(border=True):
            st.markdown(""" ### Tools Used""")
            st.write("🗄️ SQL,🐍 Python,📊 Plotly,🤖Scikit-learn,🌐Streamlit ")
        
# then making the metic of the KPI Dashboard
    m1,m2,m3,m4 =st.columns(4)
    with m1:
        with st.container(border=True):
            st.metric("💰 Total Sales",f"₹ {Total_Saless}",f"{latest_sales_growth}%")
    with m2:
        with st.container(border=True):
            st.metric("📦 Total_Quantity",f"{Total_Quantity}")
    with m3:
        with st.container(border=True):
            st.metric("🧾 Total Order ",f"{Total_Order_Count}")
    with m4:
        with st.container(border=True):
            st.metric("📈 Total Profit",f"{Total_Profits}",f"{latest_profit_growth}")
# then Visualzation the data
    p1,p2,p3,p4 =st.columns([1,1,1,1])    
    p5,p6,p7,p8 =st.columns([1,1,1,1])

    with p1:
        with st.container(border=True):
            Monthly_Sales = Monthly_Sales.dropna(subset=["Month"])
            fig1 = px.pie(Monthly_Sales,names="Month",values="Monthly_Sales",title="📊 Monthly Sales Distribution",hole=0.5)
            fig1.update_traces(textfont_size=14,pull=[0.05 if v == Monthly_Sales["Monthly_Sales"].max() else 0 for v in Monthly_Sales["Monthly_Sales"]],marker=dict(line=dict(color="#ffffff", width=2)))
            fig1.update_layout(height=400,title_font_size=22,title_x=0.5,showlegend=True,legend_title="Months")
            fig1.update_traces(textinfo="label+percent+value")
            st.plotly_chart(fig1, use_container_width=True)
        # Yearly Sales
    with p2:
        with st.container(border=True):
            fig2 =px.line(Yearly_Sales,x="Year",y="Yearly_Trend",text=Yearly_Sales["Yearly_Trend"].round(2),title="Yearly Sales Distributions",markers=True,color_discrete_sequence=["orange"])
            fig2.update_layout(height=400)
            fig2.update_traces(textfont_size=15,textposition="top center")
            fig2.update_layout(xaxis_title="Year",yaxis_title="Sales",hovermode="x unified")
            st.plotly_chart(fig2,use_container_width=True)
    with p3:
        print(Sales_Growth_rate.columns)
        with st.container(border=True):
            fig3 =px.line(Sales_Growth_rate,x="Year",y=["Sales_Trends","SALES_GROWTH"],text="Sales_Trends",markers=True,title="Sales Growth Distributions(%)",color_discrete_sequence=["blue"])
            fig3.update_layout(xaxis_title="Year",yaxis_title="Sales Growth",height=400,hovermode="x unified")
            fig3.update_traces(textfont_size=15)
            st.plotly_chart(fig3,use_container_width=True)
    with p4:
        print(Catagorical_Sales.columns)
        with st.container(border=True):
            fig4 =px.bar(Catagorical_Sales,x="Categorical_Sales",y="Category",text="Categorical_Sales",orientation="h",color_discrete_sequence=["green"],title="Category Sales Distributions")
            fig4.update_layout(height=400,hovermode="x unified")
            fig4.update_traces(textfont_size=15)
            fig4.update_layout(xaxis_title="Category",yaxis_title="Sales")
            st.plotly_chart(fig4,use_container_width=True)
    with p5:
        print(Subcatagorical_Sales.columns)
        with st.container(border=True):
            Subcatagorical_Sales["Sub_color"] =Subcatagorical_Sales["Sub_Categorical_Sales"].apply(lambda x:"Growths" if x>0 else "Less_Growths")
            fig5 =px.bar(Subcatagorical_Sales,x="Sub_Category",y="Sub_Categorical_Sales",color="Sub_color",text="Sub_Categorical_Sales",title="SubCategory Sales Distributions",color_discrete_map={"Growths":"red","Less_Growths":"red"})
            fig5.update_traces(textfont_size=15)
            fig5.update_layout(height=400,xaxis_title="Subcategory",yaxis_title="Sales")
            st.plotly_chart(fig5,use_container_width=True)
    with p6:
        print(region_Wish_Sales.columns)
        with st.container(border=True):
            fig6 =px.bar(region_Wish_Sales,x="Region",y="Region_Sales",text="Region_Sales",color_discrete_sequence=["purple"],title="Region Sales Distributions")
            fig6.update_layout(height=400,hovermode="x unified")
            fig6.update_traces(textfont_size=15)
            st.plotly_chart(fig6,use_container_width=True)
    with p7:
        print(Yearly_Sales_Growth.columns)
        with st.container(border=True):
            Yearly_Sales_Growth["Colors"] =Yearly_Sales_Growth["SALES_GROWTH_RATE"].apply(lambda x:"Growth" if x>0 else "Decline")
            fig7 =px.bar(Yearly_Sales_Growth,x="Year",y="SALES_GROWTH_RATE",color="Colors",text="SALES_GROWTH_RATE",title="Yearly Growth Distributions",color_discrete_map={"Growth":"green","Decline":"red"})
            fig7.update_layout(height=400,hovermode="x unified")
            fig7.update_traces(textfont_size=15)
            st.plotly_chart(fig7,use_container_width=True)
    with p8:  
        print(Monthly_Sales_Growth.columns)
        with st.container(border=True):
            Monthly_Sales_Growth["Color"] =Monthly_Sales_Growth["Monthly_Growth"].apply(lambda x:"Growth" if x >=0 else "Decline")
            fig8=px.bar(Monthly_Sales_Growth,x="Month",y="Monthly_Growth",color="Color",text="Monthly_Growth",title="Monthly Sales Growth Rate (%)",color_discrete_map={"Growth":"green","Decline":"red"})
            fig8.update_traces(texttemplate="%{text:.2f}%",textposition="outside")
            fig8.update_layout(title_x=0.5,xaxis_title="Year",yaxis_title="Growth Rate (%)",hovermode="x unified",showlegend=False)
            st.plotly_chart(fig8,use_container_width=True)
    # then analysics the data for the making the matrics
    # Total Customer 
    Total_Customer =df["Customer_ID"].nunique()
    print("Total Customer :",Total_Customer)
        # Avg Order
        # 
    Order =df.groupby("Order_ID")["Sales"].sum()
    Avg_Order =Order.mean()
    Max_Order =Order.max()
    Min_Order =Order.min()
    print("Avg Order Sale",Avg_Order)
        # Total Country
    Total_Country=df["Country"].nunique()
    print("Total Country Count",Total_Country)
        # high saling Product
    Product =df.groupby("Product_Name")["Sales"].sum()
    High_Saling_Product =str(Product.idxmax())
    print("High Saling Product",High_Saling_Product)
        # high saling Category
    Category =df.groupby("Category")["Sales"].sum()
    High_Saling_Category =str(Category.idxmax())
    print("High Saling Category",High_Saling_Category)
        # high saling Subcategory
    Subcategory =df.groupby("Sub_Category")["Sales"].sum()
    High_Saling_Subcategory =str(Subcategory.idxmax())
    print("High Saling SubCategory",High_Saling_Subcategory)
        # top Region
    Region =df.groupby("Region")["Sales"].sum()
    Top_Region =str(Region.idxmax())
    print("Top Region",Top_Region)
    #Profit Margin
    Profit_Margin = (df["Profit"].sum() /df["Sales"].sum()) * 100
    print("Profit Margin",Profit_Margin)
    # then making the Matrix of the data
    md1,md2,md3,md4,md5,md6,md7,md8 =st.columns(8)
    with md1:
        with st.container(border=True):
            st.metric("👤 Customer",Total_Customer)
    with md2:
        with st.container(border=True):
            st.metric("📊 Avg Order Value",Avg_Order)
    with md3:
        with st.container(border=True):
            st.metric("🌎 Total Country",Total_Country)
    with md4:
        with st.container(border=True):
            st.metric("🔥 Top Selling Product",High_Saling_Product)
    with md5:
        with st.container(border=True):
            st.metric("🏆 Top Category",High_Saling_Category)
    with md6:
        with st.container(border=True):
            st.metric("📦 Top Sub-Category",High_Saling_Subcategory)
    with md7:
        with st.container(border=True):
            st.metric("🌍 Top Region",Top_Region)
    with md8:
        with st.container(border=True):
            st.metric("📈 Profit Margin",Profit_Margin)

# then analysics the Data
Total_Loss =abs(df[df["Profit"]<0]["Profit"].sum())
print("Total Loss",Total_Loss)
# profit margin
Profit_Margin = (df["Profit"].sum() /df["Sales"].sum()) * 100
print("Profit Margin",Profit_Margin)
print(latest_profit_growth.round(2))
# Monthly_Profit
print(Monthly_Profit.columns)
print(Yearly_Profit.columns)
print(Catagorical_Wishes_Profit.columns)
print(Product_Profit.columns)
print(Subcatagory_Wish_Profit.columns)
print(Country_Profit.columns)
print(City_Profit.columns)
print(State_Profit.columns)
print(Region_Wish_Profit.columns)
print(Country_Profit.columns.tolist())
print(Country_Profit.head())
# Category
Category_Profit =df.groupby("Category")["Profit"].sum()
Max_Category=Category_Profit.idxmax()
print(Max_Category)
# SubCategory
Sub_Category_Profit =df.groupby("Sub_Category")["Profit"].sum()
Max_SCategory=Category_Profit.idxmax()
print(Max_SCategory)
# Region 
Region_Profit =df.groupby("Region")["Profit"].sum()
Max_Region=Region_Profit.idxmax()
print(Max_Region)
# Country
Country_Profit_M =df.groupby("Country")["Profit"].sum()
Max_Country=Country_Profit_M.idxmax()
print(Max_Country)
# city
City_Profit =df.groupby("City")["Profit"].sum()
Max_City=City_Profit.idxmax()
print(Max_City)
# State
State_Profit =df.groupby("State")["Profit"].sum()
Max_State=State_Profit.idxmax()
print(Max_State)
# then anaysics the data like metrics data 
# then Visualization the Profit Data
if page =="📈 Profit Analysis":
    st.title("📈 Profit Analysis Subplot")
    st.markdown("## 📌 Profit Dashboard")
    # making the matric like 
    m1,m2,m3,m4,m5=st.columns(5)
    with m1:
        with st.container(border=True):
            st.metric("💰 Total Profit",Total_Profits)
    with m2:
        with st.container(border=True):
            st.metric("🧾 Total Sales",Total_Saless)
    with m3:
        with st.container(border=True):
            st.metric("📈 Profit Margin",Profit_Margin)
    with m4:
        with st.container(border=True):
            st.metric("📊 Profit Growth",latest_profit_growth)
    with m5:
        with st.container(border=True):
            st.metric("📉 Total Loss",Total_Loss)
    st.title("📊 Profit Analytics Dashboard")
    pv1,pv2,pv3,pv4=st.columns(4)
    pv5,pv6,pv7,pv8=st.columns(4)
    # Month Profit Distributions
    with pv1:
        with st.container(border=True):
            Monthly_Profit = Monthly_Profit.dropna(subset=["Month"])
            Monthly_Profit["Monthly_Profit"] =pd.to_numeric(Monthly_Profit["Monthly_Profit"],errors="coerce").round(2)
            # Monthly_Profit["Monthly_Profit"] =Monthly_Profit["Monthly_Profit"]/10000
            fig1 =px.bar(Monthly_Profit,x="Month",y="Monthly_Profit",text="Monthly_Profit",title="Monthly Profit Distributions",color_discrete_sequence=["grey"])
            fig1.update_layout(xaxis_title="Month",yaxis_title="Monthly_Profit",height=400)
            fig1.update_traces(textfont_size =20)
            st.plotly_chart(fig1,use_container_width=True)
    # Yearly Profit Distributions
    with pv2:
        with st.container(border=True):
            Yearly_Profit["Yearly_Profit"] =pd.to_numeric(Yearly_Profit["Yearly_Profit"],errors="coerce").round(2)
            Yearly_Profit["Yearly_Profit"] =Yearly_Profit["Yearly_Profit"]/1000          
            fig2 =px.line(Yearly_Profit,x="Year",y="Yearly_Profit",text="Yearly_Profit",markers=True,title="Yearly Profit Distributions",color_discrete_sequence=["blue"])
            fig2.update_layout(height=400,xaxis_title="Year",yaxis_title="Yearly_Profit",hovermode="x unified")
            fig2.update_traces(textfont_size=20)
            st.plotly_chart(fig2,use_container_width=True)
    # Category Profit
    with pv3:
        with st.container(border=True):
            Catagorical_Wishes_Profit =Catagorical_Wishes_Profit.dropna(subset =["Category"])
            Catagorical_Wishes_Profit["Categorical_Profit"] =Catagorical_Wishes_Profit["Categorical_Profit"]/1000
            fig3 =px.pie(Catagorical_Wishes_Profit,names="Category",values="Categorical_Profit",color="Categorical_Profit",title="Category Profit Distributions",hole=0.5)
            fig3.update_layout(height=400,xaxis_title="Category",yaxis_title="Categorical_Profit")
            fig3.update_traces(textinfo="label+percent+value")
            fig3.update_traces(textfont_size=20)
            st.plotly_chart(fig3,use_container_width=True)
    # Subcategory Profit 
    with pv4:
        with st.container(border=True):
            Subcatagory_Wish_Profit["SubCategorical_Profit"] =Subcatagory_Wish_Profit["SubCategorical_Profit"] /100
            Subcatagory_Wish_Profit["Subc_Color"] =Subcatagory_Wish_Profit["SubCategorical_Profit"].apply(lambda x:"Growth" if x>0 else "Less")
            fig4 =px.bar(Subcatagory_Wish_Profit,x="Sub_Category",y="SubCategorical_Profit",color="Subc_Color",text="SubCategorical_Profit",title="Subcategory Profit Distributions",color_discrete_map={"Growth":"green","Less":"red"})
            fig4.update_layout(height=400,xaxis_title="Sub_Category",yaxis_title="Categorical_Profit")
            fig4.update_traces(textfont_size=20)
            st.plotly_chart(fig4,use_container_width=True)
    # Product Distributions profit 
    with pv5:
        with st.container(border=True):
            Top_Prduct =Product_Profit.nlargest(10,"Product_Profit")
            Top_Prduct["Product_color"] =Top_Prduct["Product_Profit"].apply(lambda x:"Growth" if x>0 else "Losser")
            fig5 =px.bar(Top_Prduct,x="Product",y="Product_Profit",text="Product_Profit",color="Product_color",title="Products Profit Distributions",color_discrete_map={"Growth":"Orange","Losser":"red"})
            fig5.update_layout(height=400,xaxis_title="Product",yaxis_title="Product_Profit")
            fig5.update_traces(textfont_size=20)
            st.plotly_chart(fig5,use_container_width=True)
    # Country Profit using the line plot
    with pv6:
        with st.container(border=True):
            Country_Profit.columns =["Country","Profit"]
            fig6=px.bar(Country_Profit,x="Country",y="Profit",text="Profit",title="Country Profit Distributions",color_discrete_sequence=["brown"])
            fig6.update_layout(height=400,xaxis_title="Country",yaxis_title="Profit")
            fig6.update_traces(textfont_size=20)
            st.plotly_chart(fig6,use_container_width=True)
    # state Profit Distributions
    with pv7:
        with st.container(border=True):
            State_Profit =df.groupby("State")["Profit"].sum().reset_index(name="State_Profit")
            State_Profit["State_color"] =State_Profit["State_Profit"].apply(lambda x:"Good" if x>0 else "Bad")
            fig7 =px.bar(State_Profit,x="State",y="State_Profit",text="State_Profit",color="State_color",title="State Profit Distributions",color_discrete_map={"Good":"green","Bad":"red"})
            fig7.update_layout(xaxis_title="State",yaxis_title="State_Profit",height=400)
            fig7.update_traces(textfont_size=20)
            st.plotly_chart(fig7,use_container_width=True)
    
    # region distribution the profit
    with pv8:
        with st.container(border=True):
            Region_Wish_Profit["region_color"] =Region_Wish_Profit["Region_Profit"].apply(lambda x:"Growth" if x>0 else "Lossing")
            fig8 =px.bar(Region_Wish_Profit,x="Region",y="Region_Profit",orientation="h",color="region_color",text="Region_Profit",title="Region Profit Distributions",color_discrete_map={"Growth":"green","Lossing":"red"})
            fig8.update_layout(xaxis_title="Region",yaxis_title="Region_Profit",height=400)
            fig8.update_traces(textfont_size=20)
            st.plotly_chart(fig8,use_container_width=True)
    # then making the metrics of the anaysics the Profit Distribution Data
    # Monthlyhigh Profit,yearly high profit ,catory high profit,suubcategory high profit ,region ,country,state,city,product
    # then analysics the data 
    mp1,mp2,mp3,mp4,mp5,mp6,mp7,mp8 =st.columns(8)
    # Monthly Profit
    with mp1:
        with st.container(border=True):
            st.metric("Monthly Profit",f"{Monthly_Profit["Monthly_Profit"].iloc[-1]:,.2f}")
    # Yearly Profit
    with mp2:
        with st.container(border=True):
            st.metric("Yearly Profit",f"{Yearly_Profit["Yearly_Profit"].iloc[-1]:,.2f}")
    # Category High Profit
    with mp3:
        with st.container(border=True):
            st.metric("📈 Highest Profit Category",Max_Category)
    # SubCategory High Profit
    with mp4:
        with st.container(border=True):
            st.metric("🏆 Top Profit-Generating Subcategory",Max_SCategory)
    # Region High Profit
    with mp5:
        with st.container(border=True):
            st.metric("🌍 Top Profit-Generating Region",Max_Region)
    # Country Profit
    with mp6:
        with st.container(border=True):
            st.metric("🌎 Top Profit-Generating Country",Max_Country)
    # City
    with mp7:
        with st.container(border=True):
            st.metric("🏙️ Top Profit-Generating City",Max_City)
    # state
    with mp8:
        with st.container(border=True):
            st.metric("🏛️ Top Profit-Generating State",Max_State)
# then analysics the data of the Order Table 
print(Total_Order)
Order =df["Order_ID"].nunique()
print("Total" ,Order)
Order_Sum =df.groupby("Order_ID")["Sales"].sum()
Avg_Order =Order_Sum.mean()
print(Avg_Order)
Max_Order =Order_Sum.max()
print(Max_Order)
Min_Order =Order_Sum.min()
print(Min_Order)
# then analysics the data of the plot
print(Monthly_Order.columns)
print(Yearly_Order_Count.columns)
print(Category_Order.columns)
print(SubCategory_Order.columns)
print(Product_Order.columns)
print(Country_Order.columns)
print(State_Order.columns)
print(City_Order.columns)
print(Segment_Order.columns)
print(ShipMode_Order.columns)
print(Region_Wish_Order.columns)
# then anaysics the data for the matrics
Max_Month_Order=Monthly_Order["MONTH"].idxmax()
print(Max_Month_Order)
# Year Order
Max_Year_Order =round(Yearly_Order_Count["Year"].max())
print(Max_Year_Order)
# High order Category
Max_Category_order =Category_Order["Category"].max()
print(Max_Category_order)
# subcategpory
MaxSub_Category_order =SubCategory_Order["Sub_Category"].max()
print(MaxSub_Category_order)
# High order product
High_Order_product=Product_Order["Product"].max()
print(High_Order_product)
# country
High_Order_country=Country_Order["COUNTRY"].max()
print(High_Order_country)
#City
High_Order_City=City_Order["City"].max()
print(High_Order_City)
# state
High_Order_State=State_Order["STATE"].max()
print(High_Order_State)
# region
High_Order_Region=Region_Wish_Order["REGION"].max()
print(High_Order_Region)
# segment
High_Order_Segment=Segment_Order["SEGMENT"].max()
print(High_Order_Segment)
# ship mode
High_Order_Ship_mode=ShipMode_Order["Ship_Mode"].max()
print(High_Order_Ship_mode)
# then Visualization the "📋 Order Analysis"
if page=="📋 Order Analysis":
    st.title("📋 Order Analysis Subplot")
    st.markdown("## 📌 Order Dashboard")
    om1,om2,om3,om4,om5,om6 =st.columns(6)
    # total order
    with om1:
        with st.container(border=True):
            st.metric("📦 Total Order",Order)
    #Avg Order Amount
    with om2:
        with st.container(border=True):
            st.metric("🛒 Avg Order Amount",Avg_Order)
    # Max_Order Amount
    with om3:
        with st.container(border=True):
            st.metric("🚀 Maximum Order Amount",Max_Order)
    # Min Order Amount
    with om4:
        with st.container(border=True):
            st.metric("🔻 Minimum Order Amount",Min_Order)
    # Max Order Month
    with om5:
        with st.container(border=True):
            st.metric("📅 Maximum Order Month",Max_Month_Order)
    # Max Order Year
    with om6:
        with st.container(border=True):
            st.metric("🗓️ Maximum Order Year",Max_Year_Order)        
    # then Visulaization the Dashboard
    st.title("📊 Order Analytics Dashboard Visualization")
    po1,po2,po3,po4 =st.columns(4)
    po5,po6,po7,po8 =st.columns(4)
    po9,po10,po11,po12 =st.columns(4)

    # monhtly Order 
    with po1:
        with st.container(border=True):
            Monthly_Order["Order_Count"] =Monthly_Order["Order_Count"]/100
            fig1= px.bar(Monthly_Order,x="MONTH",y="Order_Count",title="Monthly Order Distributions",text ="Order_Count",color_discrete_sequence=["Brown"])
            fig1.update_traces(textfont_size=20)
            fig1.update_layout(xaxis_title="Month",yaxis_title="Order_Count",height=400)
            st.plotly_chart(fig1,use_container_width=True)
    # yearly Order
    with po2:
        with st.container(border=True):
            fig1 =px.line(Yearly_Order_Count,x="Year",y="Order_Count",markers=True,text="Order_Count",title="Yearly Order Distributions")
            fig1.update_layout(height=400,xaxis_title="Year",yaxis_title="Yearly Count",hovermode="x unified")
            fig1.update_traces(textfont_size=20)
            fig1.update_traces(marker=dict(size=10),textposition ="top center",textfont_size=20)
            fig1.update_traces(marker=dict(symbol="circle",size=15))
            st.plotly_chart(fig1,use_container_width=True)
    # Category Order
    with po3:
        with st.container(border=True):
            fig3 =px.pie(Category_Order,names="Category",values="Category_Order",title="Category Order Distributions",hole=0.5,color="Category_Order")
            fig3.update_layout(xaxis_title="Category",yaxis_title="Category Order",height=400)
            fig3.update_traces(textfont_size=20,textinfo="label+percent+value")
            st.plotly_chart(fig3,use_container_width=True)
    # subcategory order Distributions
    with po4:
        with st.container(border=True):
            SubCategory_Order["Suborder_color"] =SubCategory_Order["SubCategory_Order"].apply(lambda x:"Grow" if x>0 else "loss")
            fig4=px.bar(SubCategory_Order,x="Sub_Category",y="SubCategory_Order",text="SubCategory_Order",color="Suborder_color",color_discrete_map={"Grow":"green","loss":"red"})
            fig4.update_layout(xaxis_title="Sub_Category",yaxis_title="SubCategory_Order",height=400)
            fig4.update_traces(textfont_size=20,textposition="outside")
            st.plotly_chart(fig4,use_container_width=True)
    # product order Distribution
    with po5:
        with st.container(border=True):
            Top_Product_Order =Product_Order.nlargest(10,"Product_Order")
            Top_Product_Order["Productordercolor"] =Top_Product_Order["Product_Order"].apply(lambda x:"Grow" if x>0 else "Loss")
            fig5 =px.bar(Top_Product_Order,x="Product",y="Product_Order",color="Productordercolor",text="Product_Order",title="Product Order Distributions",color_discrete_map={"Grow":"Green","Loss":"red"})
            fig5.update_layout(xaxis_title="Product",yaxis_title="Product Order",height=400,showlegend=True)
            fig5.update_traces(textposition="outside",textfont_size=20)
            st.plotly_chart(fig5,use_container_width=True)
    # Country Order
    with  po6:
        with st.container(border=True):
            Top_Country_Order =Country_Order.nlargest(10,"COUNTRY_Order")
            Top_Country_Order["Countryorder_color"] =Top_Country_Order["COUNTRY_Order"].apply(lambda x:"Grow" if x>0 else "Loss")
            fig6 =px.bar(Top_Country_Order,x="COUNTRY",y="COUNTRY_Order",text="COUNTRY_Order",color="Countryorder_color",color_discrete_map={"Grow":"blue","Loss":"blue"},title="Order Distribution By Country")
            fig6.update_layout(xaxis_title="Country",yaxis_title="Country_Order",height=400,showlegend=True)
            fig6.update_traces(textfont_size=20,textposition="outside")
            st.plotly_chart(fig6,use_container_width=True)
    # state Order Distributions
    with po7:
        with st.container(border=True):
            Top_State_order=State_Order.nlargest(10,"STATE_ORDERCOUNT")
            Top_State_order["STATEorder_color"] =Top_State_order["STATE_ORDERCOUNT"].apply(lambda x:"Growing" if x>0 else "Lossing")
            fig7=px.bar(Top_State_order,x="STATE",y="STATE_ORDERCOUNT",text="STATE_ORDERCOUNT",color="STATEorder_color",title="Order Distribution by State",color_discrete_map={"Growing":"purple","Lossing":"purple"})
            fig7.update_layout(xaxis_title="State",yaxis_title="State Order_Count",height=400)
            fig7.update_traces(textfont_size=20,textposition="outside")
            st.plotly_chart(fig7,use_container_width=True)
    # City Distributing Order 
    with po8:
        with st.container(border=True):
            Top_city_order = City_Order.nlargest(10,"City_Order")
            Top_city_order["Cityorder_color"]  =Top_city_order["City_Order"].apply(lambda x:"Grows" if x>0 else "Losss")
            fig8 =px.bar(Top_city_order,x="City",y="City_Order",text="City_Order",title="Order Distribution by City",color="Cityorder_color",color_discrete_map={"Grows":"pink","Losss":"pink"})
            fig8.update_layout(xaxis_title="City",yaxis_title="City Order",height=400)
            fig8.update_traces(textfont_size=20,textposition="outside")
            st.plotly_chart(fig8,use_container_width=True)
    # Order Distribution by segemnt
    with po9:
        with st.container(border=True):
            fig9 =px.pie(Segment_Order,names="SEGMENT",values="SEGMENT_ORDER",title="Profit Distribution by Segment",hole=0.5,color="SEGMENT")
            fig9.update_layout(xaxis_title="Segment",yaxis_title="Segment Order",height=400)
            fig9.update_traces(textfont_size =20,textinfo="label+percent+value")
            st.plotly_chart(fig9,use_container_width=True)
    # Order Distribution by Ship_Mode 
    with po10:
        with st.container(border=True):
            fig10 =px.line(ShipMode_Order,x="Ship_Mode",y="TOTAL_ORDER",text="TOTAL_ORDER",markers=True,title="Order Distributoon by Ship Mode")
            fig10.update_layout(xaxis_title="Ship Mode",yaxis_title="Order",height=400,hovermode="x unified")
            fig10.update_traces(marker=dict(symbol="circle",size=15),textposition ="top center",textfont_size=20)
            fig10.update_traces(marker=dict(size=10))
            st.plotly_chart(fig10,use_container_width=True)
    # Order Distribution by Region
    with po11:
        with st.container(border=True):
            Top_Region =Region_Wish_Order.nlargest(10,"REGION_WISH_ORDER")
            fig11= px.bar(Top_Region,x="REGION",y="REGION_WISH_ORDER",text="REGION_WISH_ORDER",color_discrete_sequence=["Purple"],title="Order Distribution By Regions")
            fig11.update_layout(xaxis_title="Region",yaxis_title="Region_Order",height=400)
            fig11.update_traces(textposition="outside",textfont_size=20)
            st.plotly_chart(fig11,use_container_width=True)
    # then making the matric of the data
    om1,om2,om3,om4,om5,om6,om7,om8,om9 =st.columns(9)
    # Max Order Category
    with om1:
        with st.container(border=True):
            st.metric("🏷️ High Order Category",Max_Category_order)
    # max Order Subcategory
    with om2:
        with st.container(border=True):
            st.metric("📂 Max Order SubCategory",MaxSub_Category_order)
    # High Order Product
    with om3:
        with st.container(border=True):
            st.metric("📦 High Order Product",High_Order_product)
    # high Order Country
    with om4:
        with st.container(border=True):
            st.metric("🌍 High Order Country",High_Order_country)
    # high order state
    with om5:
        with st.container(border=True):
            st.metric("🗺️ High Order State",High_Order_State)
    # high order city 
    with om6:
        with st.container(border=True):
            st.metric("🏙️ High Order City",High_Order_City)
    # High Order Segment        
    with om7:
        with st.container(border=True):
            st.metric("👥 High Order Segment",High_Order_Segment)
    # high order Ship mode
    with om8:
        with st.container(border=True):
            st.metric("🚚 High Order Ship_Mode",High_Order_Ship_mode)
    # high order Region
    with om9:
        with st.container(border=True):
            st.metric("🌐 High Order Region",High_Order_Region)
Total_Product_Count=df["Product_Name"].nunique()
print("Total Sale",Total_Saless)
print("Total Profit",Total_Profits)
print("Total Quantity",Total_Quantity)
print("Total Product Order",Total_Order_Count)
# then analysics the data for the Product MATRIX
print(Top_Selling_Product)
print(least_selling_Product)
print(High_Profit_Product)
print(Low_Profit_Product)
print(Product_Profit)
print(Product_Order)
print(Delievery_Time.columns)
print(Shipping_Cost.columns)
# analysics the data for the visualizations
# product sales
Product_Sales =df.groupby("Product_Name")["Sales"].sum().reset_index(name="Product_Sales")
# product_Quantity
Product_Quantity =df.groupby("Product_Name")["Quantity"].sum().reset_index(name="Product_Quantity")
print(Product_Quantity)
# then visualization the data
if page=="📦 Product Analysis":
    st.title("📦 Product Analysis Subplot")
    st.markdown("## 📌 Product Dashboard")
    # total product,product sales , product profit, Total_Quantity,total product order count 
    pm1,pm2,pm3,pm4,pm5= st.columns(5)
    with pm1:
        with st.container(border=True):
            st.metric("🛍️ Total Product Count",Total_Product_Count)
    with pm2:
        with st.container(border=True):
            st.metric("💰 Total Profit",Total_Profits)
    with pm3:
        with st.container(border=True):
            st.metric("🧾 Total Sales",Total_Saless)
    with pm4:
        with st.container(border=True):
            st.metric("🔢 Total Quantity",Total_Quantity)
    with pm5:
        with st.container(border=True):
            st.metric("📦 Total Order",Order)
    # then visualization dashboard   
    st.title("📊 Product Analytics Dashboard Visualization")
    pd1,pd2,pd3,pd4=st.columns(4)
    # Product Sales
    with pd1:
        with st.container(border=True):
            Product_Sales_Top = Product_Sales.nlargest(15,"Product_Sales")
            Product_Sales_Top["Product_color"] =Product_Sales_Top["Product_Sales"].apply(lambda x: "Grows" if x>0 else "Losses")
            fig1 =px.bar(Product_Sales_Top,x="Product_Name",y="Product_Sales",text="Product_Sales",title="Product Distribution bY Sales",color="Product_color",color_discrete_map={"Grows":"Green","Losses":"red"})
            fig1.update_layout(xaxis_title="Product Name",yaxis_title="Sales",height=400)
            fig1.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig1.update_traces(textfont_size=20,textposition ="outside")
            st.plotly_chart(fig1,use_container_width=True)
    # Product profit
    with pd2:

        Product_Profit_Top= Product_Profit.nlargest(10,"Product_Profit")
        Product_Profit_Top["Product_Profit"] =Product_Profit_Top["Product_Profit"].round(2)
        with st.container(border=True):
            fig2 =px.line(Product_Profit_Top,x="Product",y="Product_Profit",markers=True,text="Product_Profit",title="Product Profit Distributions",color_discrete_sequence=["pink"])
            fig2.update_layout(xaxis_title="Product",yaxis_title="Product Profit",height=400,hovermode="x unified")
            fig2.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig2.update_traces(marker=dict(symbol="circle",size=15),textposition="top center",textfont_size=20)
            st.plotly_chart(fig2,use_container_width=True)
    # product Quantity
    with pd3:
        with st.container(border=True):
            # Category_Order
            # df = df.drop_duplicates(subset=["Product_Quantity"])
            Top_Product_Quantity =Product_Quantity.nlargest(10,"Product_Quantity")
            # Top_Product_Quantity["Color"] =Top_Product_Quantity["Product_Quantity"].apply(lambda x:"high" if x> Top_Product_Quantity["Product_Quantity"].mean() else "low")
            fig3 =px.bar(Top_Product_Quantity,x="Product_Name",y="Product_Quantity",text="Product_Quantity",title="Product Quantity Distributions",color_discrete_sequence=["grey"])
            fig3.update_layout(xaxis_title="Product",yaxis_title="Quantity",height=400)
            fig3.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig3.update_traces(textposition ="outside",textfont_size=20)
            st.plotly_chart(fig3,use_container_width=True)
    # product Order
    with pd4:
        with st.container(border=True):
            Top_Product_Order =Product_Order.nlargest(10,"Product_Order")
            fig4 =px.bar(Top_Product_Order,x="Product",y="Product_Order",text="Product_Order",title="Product Distribtuion by Order",color_discrete_sequence=["brown"])
            fig4.update_layout(xaxis_title="Product",yaxis_title="Product Order",height=400)
            fig4.update_traces(textposition="outside",textfont_size=20)
            fig4.update_xaxes(tickangle=90,tickfont=dict(size=8))
            st.plotly_chart(fig4,use_container_width=True)
# then Visulization the data of the Category
    # Category Sales
    cp1,cp2,cp3,cp4 =st.columns(4)
    # Category Sales
    with cp1:
        # Category Sales
        Catagorical_Saless =df.groupby("Category")["Sales"].sum().reset_index(name="Category_Sales")
        with st.container(border=True):
            fig1 =px.line(Catagorical_Saless,x="Category",y="Category_Sales",markers=True,text="Category_Sales",title="Category Sales Distributions",color_discrete_sequence=["purple"])
            fig1.update_layout(xaxis_title="Category",yaxis_title="Category_Sales",height=400,hovermode="x unified")
            fig1.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig1.update_traces(marker=dict(symbol="circle",size=15),textposition="top center",textfont_size=20)
            st.plotly_chart(fig1,use_container_width=True)
    # Category Profit
    with cp2:
        # Category Profit 
        Category_Profits =df.groupby("Category")["Profit"].sum().reset_index(name="Category_Profit")
        with st.container(border=True):
            fig2 =px.pie(Category_Profits,names="Category",values="Category_Profit",title="Category Profit Distributions",color="Category",hole=0.5)
            fig2.update_layout(xaxis_title="Category",yaxis_title="Category_Profit",height=400)
            fig2.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig2.update_traces(textinfo ="label+percent+value",textposition ="outside",textfont_size=20)
            st.plotly_chart(fig2,use_container_width=True)
    # Category Order
    with cp3:
        with st.container(border=True):
            Category_Orders=df.groupby("Category")["Order_ID"].nunique().reset_index(name="Order_Count")
            fig3 =px.bar(Category_Orders,x="Category",y="Order_Count",text="Order_Count",title="Category Distribution by Order",color_discrete_sequence=["pink"])
            fig3.update_layout(xaxis_title="Category",yaxis_title="Order_Count",height=400)
            fig3.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig3.update_traces(textposition="outside",textfont_size=20)
            st.plotly_chart(fig3,use_container_width=True)
    # Category Quantity
    with cp4:
        with st.container(border=True):
            # Quantity Category
            Category_Quantity =df.groupby("Category")["Quantity"].sum().reset_index(name="Category_Quantity")
            fig4 =px.line(Category_Quantity,x="Category",y="Category_Quantity",markers=True,text ="Category_Quantity",title="Category Quantity Distributions",color_discrete_sequence=["blue"])
            fig4.update_layout(xaxis_title="Category",yaxis_title="Quantity",height=400)
            fig4.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig4.update_traces(marker=dict(symbol="circle",size=10),textposition="top center",textfont_size=15)
            st.plotly_chart(fig4,use_container_width=True)
    # then visualization the data of the subcategory
    sbm1,sbm2,sbm3,smbm4 =st.columns(4)
    with sbm1:
        with st.container(border=True):
            # Sub Category Sales
            Sub_Category_Saless =df.groupby("Sub_Category")["Sales"].sum().reset_index(name="Sub_Category_Sales")
            fig1 =px.line(Sub_Category_Saless,x="Sub_Category",y="Sub_Category_Sales",markers=True,text="Sub_Category_Sales",title="SubCategory Sales Distributions",color_discrete_sequence=["purple"])
            fig1.update_layout(xaxis_title="Sub_Category",yaxis_title="Sales",height=400,hovermode="x unified")
            fig1.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig1.update_traces(marker=dict(symbol="circle",size=15),textposition="top center",textfont_size=15)
            st.plotly_chart(fig1,use_container_width=True)
    # sub category Profit
    with st.container(border=True):
        with sbm2:     
            Sub_Category_Profits =df.groupby("Sub_Category")["Profit"].sum().reset_index(name="Sub_Category_Profit")
            fig2 =px.bar(Sub_Category_Profits,x="Sub_Category",y="Sub_Category_Profit",text="Sub_Category_Profit",title="Subcategory Distribution by Profit",color_discrete_sequence=["blue"])
            fig2.update_layout(xaxis_title="Sub Category",yaxis_title="Profit",height=400)
            fig2.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig2.update_traces(textposition="outside",textfont_size=20)
            st.plotly_chart(fig2,use_container_width=True)
    # Sub Category order
    with sbm3:
        with st.container(border=True):
            Sub_Category_Orders=df.groupby("Sub_Category")["Order_ID"].nunique().reset_index(name="Sub_Category_Order_Count")
            fig3 =px.bar(Sub_Category_Orders,x="Sub_Category",y="Sub_Category_Order_Count",text="Sub_Category_Order_Count",title="Sub_Category Distribution by Order",color_discrete_sequence=["red"])
            fig3.update_layout(xaxis_title="Category",yaxis_title="Order_Count",height=400)
            fig3.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig3.update_traces(textposition="outside",textfont_size=20)
            st.plotly_chart(fig3,use_container_width=True)
    # Sub category Quantity
    with smbm4:
        with st.container(border=True):
            Sub_Category_Quantity =df.groupby("Sub_Category")["Quantity"].sum().reset_index(name="Sub_Category_Quantity")
            fig4 =px.bar(Sub_Category_Quantity,x="Sub_Category",y="Sub_Category_Quantity",text="Sub_Category_Quantity",title="Sub_Category Distribution by Order",color_discrete_sequence=["yellow"])
            fig4.update_layout(xaxis_title="Sub_Category",yaxis_title="Quantity",height=400)
            fig4.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig4.update_traces(textposition="outside",textfont_size=20)
            st.plotly_chart(fig4,use_container_width=True)
#     # then making the Matrics of the data 
    cm1,cm2,cm3,cm4,cm5,cm6,cm7,cm8= st.columns(8)
    with cm1:
    # Top product 
        Sale_Product =df.groupby("Product_Name")["Sales"].sum()
        Top_Product_Sale = Sale_Product.idxmax()
        with st.container(border=True):
            st.metric("🏆Top Saling Product",Top_Product_Sale)
    # Least product  sale
    with cm2:
        Least_Product_Sale = Sale_Product.idxmin()
        with st.container(border=True):
            st.metric("📉Least Saling Product",Least_Product_Sale)
    #top Profit Product
    with cm3:
        Profit_Product =df.groupby("Product_Name")["Profit"].sum()
        Top_Profit_Product =Profit_Product.idxmax()
        with st.container(border=True):
            st.metric("💰 High Profit Product",Top_Profit_Product)
    # less Profit Product 
    with cm4:
        # less Profit Product 
        Less_Profit_Product =Profit_Product.idxmin()
        with st.container(border=True):
            st.metric("🔻Low Profit Product",Less_Profit_Product)
    # High Sales of the Product
    with cm5:
        Product_top_Sale =Sale_Product.max()
        with st.container(border=True):
            st.metric("🚀 Product Top Sales",Product_top_Sale)
    # low Sales of the Product
    with cm6:
        Product_top_Sale =Sale_Product.max()
        with st.container(border=True):
            st.metric("📦 Product Low Sales",Product_top_Sale)
    # High Saling Category
    with cm7:
        Category_Sale =df.groupby("Category")["Sales"].sum()
        Top_Saling_Category =Category_Sale.idxmax()
        st.metric("🥇 Top Category",Top_Saling_Category)
    # high Saling Subcategory
    with cm8:
            Sub_Category_Sales =df.groupby("Sub_Category")["Sales"].sum()
            Top_Subcategory_Sales =Sub_Category_Sales.idxmax()
            st.metric("⭐ Top SubCategory",Top_Subcategory_Sales)
# then analysics the data of the customer anaysics 
print(Top_Customer["Top_Customer"].sum())
print(Repeat_Customer["Repeat_Customer"].sum())
print(Customer_Contribution["Sales_Contributions"].mean())
print(High_Saling_CustomerCount["Top_Sales_Customer_Count"].count())
print(Low_Saling_CustomerCount["Worst_Sales_Customer_Count"].count())
# Customer_Segment
Customer_Segment =df.groupby("Segment")["Sales"].sum()
Top_Customer_Segement =Customer_Segment.idxmax()
print(Top_Customer_Segement)
# least segment
Least_Customer_Segement =Customer_Segment.idxmin()
print(Least_Customer_Segement)
# then Visualization the Subplot of the "👥 Customer Analysis"
if page =="👥 Customer Analysis":
    st.title("👥 Customer Analysis Subplot")
    st.markdown("## 📌 Customer Dashboard")
    # making the KPi of the 👥 Customer Analysis
    c1,c2,c3,c4,c5,c6,c7,cm9,cm10=st.columns(9)
    # total Customer
    with c1:
        with st.container(border=True):
            st.metric("Total Customer",df["Customer_ID"].nunique())
    # total order :
    with c2:
        with st.container(border=True):
            st.metric("📦 Total Order",Order)
    # Repeat customer count
    with c3:
        with st.container(border=True):
            st.metric("Top Customer Count",Top_Customer["Top_Customer"].sum())
       
    # top Customer Count
    with c4:
        with st.container(border=True):
            st.metric("Repeat Customer Count",Repeat_Customer["Repeat_Customer"].sum())
    # Customer_Contribution
    with c5:
        with st.container(border=True):
            st.metric("Customer_Contribution",Customer_Contribution["Sales_Contributions"].mean())
      # top segement
    with cm9:
        with st.container(border=True):
            st.metric("🥇Top_Customer_Segement",Top_Customer_Segement)
    # Top Least Segment
    with cm10:
        with st.container(border=True):
            st.metric("📉Least Customer Segment ",Least_Customer_Segement)
    # then analysics the Dashboard of the Customer 
    st.title("📊 Customer Analytics Dashboard Visualization")
    cv1,cv2,cv3,cv4= st.columns(4)
    # top customer sales
    with cv1:
        with st.container(border=True):
            Top_Customer =df.groupby("Customer_Name")["Sales"].sum().reset_index(name="Top_Customer_Sales")
            Top_Customer_Sales =Top_Customer.nlargest(10,"Top_Customer_Sales")
            fig1 =px.bar(Top_Customer_Sales,x="Customer_Name",y="Top_Customer_Sales",text="Top_Customer_Sales",title="Top Customer By Sales",color_discrete_sequence=["Brown"])
            fig1.update_layout(xaxis_title="Customer_Name",yaxis_title="Customer Sales",height=400)
            fig1.update_xaxes(tickangle=90,tickfont=dict(size=10))
            fig1.update_traces(textposition="outside",textfont_size=20)
            st.plotly_chart(fig1,use_container_width=True)
    # top customer by sales
    with cv2:
        with st.container(border=True):
            Top_Customer_Profit =df.groupby("Customer_Name")["Profit"].sum().reset_index(name="Top_Customer_Profit")
            Top_Customer_Profit =Top_Customer_Profit.nlargest(10,"Top_Customer_Profit")
            fig2 =px.bar(Top_Customer_Profit,x="Customer_Name",y="Top_Customer_Profit",text="Top_Customer_Profit",title="Top Customer By Profit",color_discrete_sequence=["Grey"])
            fig2.update_layout(xaxis_title="Customer Name",yaxis_title=" Customer Profit",height=400)
            fig2.update_xaxes(tickangle=90,tickfont=dict(size=10))
            fig2.update_traces(textposition="outside",textfont_size=20)
            st.plotly_chart(fig2,use_container_width=True)
    # Top customer by Order 
    with cv3:
        with st.container(border=True):
            Top_Customer_Order =df.groupby("Customer_Name")["Order_ID"].nunique().reset_index(name="Top_Customer_Order")
            Top_Customer_Order =Top_Customer_Order.nlargest(10,"Top_Customer_Order")
            fig3 =px.bar(Top_Customer_Order,x="Customer_Name",y="Top_Customer_Order",text="Top_Customer_Order",title="Top Customer By Order",color_discrete_sequence=["Blue"])
            fig3.update_layout(xaxis_title="Customer_Name",yaxis_title=" Customer Order",height=400)
            fig3.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig3.update_traces(textposition="outside",textfont_size=20)
            st.plotly_chart(fig3,use_container_width=True)
    # customer Segement Analysics
    with cv4:
        with st.container(border=True):
            Customer_Segment =df.groupby("Segment")["Sales"].sum().reset_index(name="Customer_Segment")
            fig4 =px.pie(Customer_Segment,names="Segment",values="Customer_Segment",title="Customer Segment Analysics",color="Segment",hole=0.5)
            fig4.update_layout(xaxis_title="Segment",yaxis_title="Sales",height=400)
            fig4.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig4.update_traces(textinfo ="label+percent+value",textposition ="outside",textfont_size=15)
            st.plotly_chart(fig4,use_container_width=True)
    # then Visualization the Plot 
    cv5,cv6,cv7,cv8 =st.columns(4)
    # CLV Customer Lifetime Values 
    with cv5:
        with st.container(border=True):
            CLV =(df.groupby("Customer_Name")["Sales"].sum().reset_index(name="Customer_lifetime_Values").sort_values(by="Customer_lifetime_Values",ascending=False))
            Top_CLV =CLV.nlargest(10,"Customer_lifetime_Values")
            fig5 =px.line(Top_CLV,x="Customer_Name",y="Customer_lifetime_Values",markers=True,text="Customer_lifetime_Values",title="Customer_lifetime_Values Distributions",color_discrete_sequence=["purple"])
            fig5.update_layout(xaxis_title="Customer_Name",yaxis_title="Customer_lifetime_Values",height=400,hovermode="x unified")
            fig5.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig5.update_traces(marker=dict(symbol="circle",size=15),textposition="top center",textfont_size=15)
            st.plotly_chart(fig5,use_container_width=True)
    # Repeat Customer
    with cv6:
        with st.container(border=True):
            Repeat_Customers =df.groupby("Customer_Name")["Order_ID"].nunique().reset_index(name ="Order_Count")
            Repeat_Customers =Repeat_Customers[Repeat_Customers["Order_Count"] >1]
            Top_Repeat_Customers=Repeat_Customers.nlargest(10,"Order_Count")
            fig6 =px.bar(Top_Repeat_Customers,x="Customer_Name",y="Order_Count",text="Order_Count",title="Top 10 Repeat Customer",color_discrete_sequence=["yellow"])
            fig6.update_layout(xaxis_title="Customer_Name",yaxis_title="Order_Count",height=400)
            fig6.update_xaxes(tickangle=90,tickfont=dict(size=8))
            fig6.update_traces(textposition="outside",textfont_size=15)
            st.plotly_chart(fig6,use_container_width=True)
    # Monthly Sales
    Monthly_Customer_Sales =(df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum().reset_index(name="Monthly_Sales"))
    Monthly_Customer_Sales["Order_Date"] =Monthly_Customer_Sales["Order_Date"].astype(str)        
    with cv7:
        with st.container(border=True):
            fig7 =px.line(Monthly_Customer_Sales,x="Order_Date",y="Monthly_Sales",markers=True,title="Customer Monthly Sales",color_discrete_sequence=["pink"])                
            fig7.update_layout(xaxis_title="Order_Date",yaxis_title="Monthly_Sales",height=400,hovermode="x unified")
            fig7.update_xaxes(tickangle=90,tickfont=dict(size=6))
            fig7.update_traces(marker=dict(symbol="circle",size=15),textposition="top center",textfont_size=15)
            st.plotly_chart(fig7,use_container_width=True)
    # TOP state Hving thr Maximum Customer
    State =df.groupby("State")["Customer_ID"].nunique().reset_index(name="Top_State")
    Top_State =State.nlargest(10,"Top_State")
    # Top state Visulaizations
    with cv8:
        with st.container(border=True):
            fig8 =px.bar(Top_State,x="State",y="Top_State",text="Top_State",title="Top State",color="State")
            fig8.update_layout(xaxis_title="State",yaxis_title="Customer_Count",height=400)
            fig8.update_xaxes(tickangle=90,tickfont=dict(size=8))
            st.plotly_chart(fig8,use_container_width=True)
        # then analysics the data for the kPI plots
    # Top profit Customer Count 
    Customer_Profit_count =df.groupby("Customer_Name")["Profit"].count()
    Top_Customer_countp =Customer_Profit_count.max()
    print(Top_Customer_countp)

    # Clv
    CLV =(df.groupby("Customer_Name")["Sales"].sum())
    High_Clv =CLV.max()
    print(High_Clv)
    low_Clv =CLV.min()
    print(low_Clv)
    # check those customer that are order place by repeat or count of the single order
    Repeat_Customers =df.groupby("Customer_Name")["Order_ID"].nunique().reset_index(name="Order_Count")
    Customers_repeat_order =Repeat_Customers[Repeat_Customers["Order_Count"] >2].shape[0]
    Customers_single_order =Repeat_Customers[Repeat_Customers["Order_Count"] ==1].shape[0]
    print(Customers_repeat_order)
    print(Customers_single_order)
    # top state by customer high customer and the low customer
    State =df.groupby("State")["Customer_ID"].nunique()
    Top_State =State.idxmax()
    least_State =State.idxmin()
    # city
    City =df.groupby("City")["Customer_ID"].nunique()
    Top_City =City.idxmax()
    least_City =City.idxmin()
    # then visualization the data of the in the form of the Matrix 
    cm11,cm12,cm13,cm14,cm15,cm16 ,cm17=st.columns(7)
    # Customer Profit count
    with cm11:
        with st.container(border=True):
            st.metric("🏆 Top Customers by Profit",Top_Customer_countp)
    # high CLV
    with cm12:
        with st.container(border=True):
            st.metric("👑 High Clv",High_Clv)
    # least CLV
    with cm13:
        with st.container(border=True):
            st.metric("🪙 Least CLV",low_Clv)
    # chekc the high state
    with cm14:
        with st.container(border=True):
            st.metric("Top State",Top_State)
    # check the Leas state
    with cm15:
        with st.container(border=True):
            st.metric("Least State",least_State)
    # top City
    with cm16:
        with st.container(border=True):
            st.metric("Top City",Top_City)
    # least city
    with cm17:
        with st.container(border=True):
            st.metric("Least City",least_City)
# Country_Sales =result["Country_Sales"]
print(Better_Performance_Country.columns) 
print(Worse_Performance_Country.columns) 
print(State_Wise_Performance.columns) 
print(Better_Performance_State,Columns) 
print(State_Sales_Profit.columns) 
print(City_Sales_Profit.columns) 
print(Max_Sale_Profit_City.columns) 
print(Min_Sale_Profit_City.columns) 
# then Visulaization the Plot of the 
if page =="🌎 Geographical Analysis":
    st.title("🌎 Geographical Analysis Dashboard")
    st.markdown("## 📌 Geographical Dashboard")
    # total sales total profit total country  total state total city total order 
    gm1,gm2,gm3,gm4,gm5,gm6 =st.columns(6)
    # total sales 
    with gm1:
        with st.container(border=True):
            st.metric("🌍Total Country",df["Country"].nunique())
    # total State :
    with gm2:
        with st.container(border=True):
            st.metric("🏛️ Total State",df["State"].nunique())
    # total city
    with gm3:
        with st.container(border=True):
            st.metric("🏙️ Total State",df["State"].nunique()) 
    # total Profit
    with gm4:
        with st.container(border=True):
            st.metric("💰 Total Profit",Total_Profits)
    with gm5:
        with st.container(border=True):
            st.metric("🧾 Total Sales",Total_Saless)
    with gm6:
        with st.container(border=True):
            st.metric("🔢 Total Quantity",Total_Quantity)
    # then visualization the data 
    st.title("📊 Geographical Analytics Dashboard Visualization")
    g1,g2,g3,g4=st.columns(4)
    with g1:
    # country sales using choropleth plot
        with st.container(border=True):
            Country_Sales = df.groupby("Country")["Sales"].sum().reset_index()
            fig1 = px.choropleth(Country_Sales,locations="Country",locationmode="country names",color="Sales",title="🌍 Sales Distribution by Country")
            st.plotly_chart(fig1,use_container_width=True)
    # top 10 states by sales
    with g2:
        with st.container(border=True):
            State_Sales = (df.groupby("State")["Sales"].sum().reset_index().nlargest(10, "Sales"))
            fig2 = px.bar(State_Sales,x="State",y="Sales",text="Sales",title="🏛️ Top 10 States by Sales")
            fig2.update_layout(xaxis_title="State",yaxis_title="Sales",height=400)
            fig2.update_xaxes(tickangle=90,tickfont=dict(size=8))
            st.plotly_chart(fig2,use_container_width=True)
    # top 10 cites by sales 
    with g3:
        with st.container(border=True):
            City_Sales = (df.groupby("City")["Sales"].sum().reset_index().nlargest(10, "Sales"))
            fig3 = px.bar(City_Sales,x="City",y="Sales", text="Sales",title="🏙️ Top 10 Cities by Sales",color="City")
            fig3.update_layout(xaxis_title="City",yaxis_title="Sales",height=400)
            fig3.update_xaxes(tickangle=90,tickfont=dict(size=8))
            st.plotly_chart(fig3,use_container_width=True)
    # city wish Profit Analysics 
    with g4:
        with st.container(border=True):
            City_Profit = (df.groupby("City")["Profit"].sum().reset_index().nlargest(10, "Profit"))
            fig4= px.bar(City_Profit,x="City",y="Profit",text="Profit",title="💰 Top 10 Cities by Profit",color="Profit")
            fig4.update_layout(xaxis_title="City",yaxis_title="Profit",height=400)
            fig4.update_xaxes(tickangle=90,tickfont=dict(size=8))
            st.plotly_chart(fig4,use_container_width=True)
    # geo map
    g5,g6,g7,g8=st.columns(4)
    with g5:
        with st.container(border=True):
            State_Order = (df.groupby("State")["Order_ID"].nunique().reset_index(name="Orders"))
            fig5=px.bar(State_Order,x="State",y="Orders",text="Orders",title="Order Distribution by State")
            fig5.update_layout(xaxis_title="State",yaxis_title="Orders",height=400)
            fig5.update_xaxes(tickangle=90,tickfont=dict(size=8))
            st.plotly_chart(fig5,use_container_width=True)
    # then making the country Profit using the 
    with g6:
        with st.container(border=True):
            Country_Sales = df.groupby("Country")["Profit"].sum().reset_index()
            fig6 = px.choropleth(Country_Sales,locations="Country",locationmode="country names",color="Profit",title="🌍 Profit Distribution by Country")
            st.plotly_chart(fig6,use_container_width=True)
    # state customer 
    with g7:
        with st.container(border=True):
            State_Customer = (df.groupby("State")["Customer_ID"].nunique().reset_index(name="Customers"))
            fig7 =px.bar(State_Customer,x="State",y="Customers",text="Customers",title="State Distribution By Customers")
            fig7.update_layout(xaxis_title="State",yaxis_title="Customers",height=400)
            fig7.update_xaxes(tickangle=90,tickfont=dict(size=8))
            st.plotly_chart(fig7,use_container_width=True)
    # low state Profit
    with g8:
        with st.container(border=True):
            Low_State_Profit = (df.groupby("State")["Profit"].sum().sort_values().head(10).reset_index())
            fig8 =px.bar(Low_State_Profit,x="State",y="Profit",text="Profit",title="State Profit Distributions")
            fig8.update_layout(xaxis_title="State",yaxis_title="Profit",height=400)
            fig8.update_xaxes(tickangle=90,tickfont=dict(size=8))
            st.plotly_chart(fig8,use_container_width=True)
    # then makiing  the KPI matrix
    # Top Country by Sales
    Top_Country = (df.groupby("Country")["Sales"].sum().idxmax())
    # Top State by Sales
    Top_State = (df.groupby("State")["Sales"].sum().idxmax())
    # Top City by Sales
    Top_City = (df.groupby("City")["Sales"].sum().idxmax())
    # Top State Profit
    Top_State_Profit = (df.groupby("State")["Profit"].sum().idxmax())
    # Top City Profit
    Top_City_Profit = (df.groupby("City")["Profit"].sum().idxmax())
    # Total Orders
    Total_Orders = df["Order_ID"].nunique()
    # Total Customers
    Total_Customers = df["Customer_ID"].nunique()
    # Average Order Value
    AOV = round(df["Sales"].sum() /df["Order_ID"].nunique(),2)
    # then making the matric
    gm1,gm2,gm3,gm4,gm5,gm6,gm7,gm8 =st.columns(8)
    # top country
    with gm1:
        with st.container(border=True):
            st.metric("🌍Top Country",Top_Country)
    # top state
    with gm2:
        with st.container(border=True):
            st.metric("🗺️ Top State",Top_State)
    # top city
    with gm3:
        with st.container(border=True):
            st.metric("🏙️Top City",Top_City)
    # Top_State_Profit
    with gm4:
        with st.container(border=True):
            st.metric("💰Top_State_Profit",Top_State_Profit)
    # Top_City_Profit
    with gm5:
        with st.container(border=True):
            st.metric("💸Top_City_Profit",Top_City_Profit)
    # Total_Orders
    with gm6:
        with st.container(border=True):
            st.metric("📦Total_Orders",Total_Orders)
    # Total_Customers
    with gm7:
        with st.container(border=True):
            st.metric("👥 Total_Customers",Total_Customers)
    # AOV
    with gm8:
        with st.container(border=True):
            st.metric("📊AOV",AOV)
    