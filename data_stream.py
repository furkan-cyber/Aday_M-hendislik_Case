import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io
import scipy
from scipy.stats.stats import pearsonr
import psycopg2


# Connection parameters, yours will be different
param_dic = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "2000"
}


def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn


def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()

    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df


conn = connect(param_dic)
column_names = ["flight_id","timee","xyz0","xyz1","xyz2","typee"]
# Execute the "SELECT *" query
ang_vel = postgresql_to_dataframe(conn, "select * from ang_vel", column_names)
print(ang_vel.head())


# Connect to the database
conn = connect(param_dic)
column_names = ["flight_id","timee","lat","lon","alt"]
# Execute the "SELECT *" query
gps= postgresql_to_dataframe(conn, "select * from gps", column_names)
print(gps.head())


# Connect to the database
conn = connect(param_dic)
column_names = ["flight_id","model_id","mission_id","flight_date","landing_date",
               "landing_success","flight_success","flight_county","flight_province",
               "flight_region","real_flight_time","mission_success"]
# Execute the "SELECT *" query
flight = postgresql_to_dataframe(conn, "select * from flight", column_names)
print(flight.head())

st.title("Titra Candidate Engineer Case")
st.subheader("Aeroplane analysis")
st.subheader("Fırst process start dataset")


dataset_name=st.sidebar.selectbox("Select Dataset",("Flight","Gps","Ang_Vel"))

if dataset_name=="Flight":
    st.subheader("Flight Data")
    st.write(flight.head())
    if st.button('FLight all analysis'):
        st.write('Okkaaay We start nowww')
        st.subheader("Dataset info")
        buffer = io.StringIO()
        flight.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
        st.subheader("Descriptice Statistics")
        st.write(flight.describe())


elif dataset_name == "Gps":
    st.subheader("Gps Data")
    st.write(gps.head())
    if st.button('GPS all analysis'):
        st.write('Okkaaay We start nowww')
        st.subheader("Dataset info")
        buffer = io.StringIO()
        gps.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.subheader("Descriptice Statistics")
        st.write(gps.describe())
        st.subheader("Scatter Latitute And Longtitude Relationship")
        sns.relplot(data=gps,x="lon",y="lat")
        st.pyplot()
        st.subheader("Scatter Latitute And Altitude Relationship")
        sns.relplot(data=gps, x="lat", y="alt")
        st.pyplot()
        st.subheader("Scatter Altitude And Longtitude Relationship")
        sns.relplot(data=gps, x="lon", y="alt")
        st.pyplot()
        st.subheader("Correlation matrix gps ")
        st.text("""
         CORRELATION MATRIX 
          IF CORRELATION COFFICIENT X> 0.8 STROGNLY POSITIVE CORRELATION
                                    X < 0.8 STRONGLY NEGATIVE CORRELATION
        """)
        matrix = gps.corr().round(2)
        mask = np.triu(np.ones_like(matrix, dtype=bool))
        sns.heatmap(matrix, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag', mask=mask)
        st.pyplot()
        st.subheader("We apply pearson test in order to take information an prove correration")
        st.write("calculation correlation coefficient and p-value between lontitıde and latitude")
        st.write(pearsonr(gps["lon"], gps["lat"]))
        st.write("p_value <0.01  that association is  high significance")
        st.write("calculation correlation coefficient and p-value between lontitıde and altitude")
        st.write(pearsonr(gps["lon"], gps["alt"]))
        st.write("p_value <0.01  that association is  high significance")
        st.write("calculation correlation coefficient and p-value between latitude and altitude")
        st.write(pearsonr(gps["lat"], gps["alt"]))
        st.write("p_value <0.01  that assocation is  high significance")
        st.subheader("Is there radical value in dataset?")
        st.write("GPS Radical Value latitude")
        sns.boxplot(data=gps, x="lat")
        st.write("1 radical value that not important for now")
        st.pyplot()
        st.write("GPS Radical Value lontitude")
        sns.boxplot(data=gps, x="lon")
        st.write("1 radical value that not important for now")
        st.pyplot()
        st.write("GPS Radical Value altitude")
        sns.boxplot(data=gps, x="alt")
        st.write("0 radical values.Data is cleaned")
        st.pyplot()
        st.subheader("Latitude Longitude Mapping")
        st.map(data=gps[["lon","lat"]],use_container_width=True,zoom=10)

elif dataset_name =="Ang_Vel":
    st.subheader("Angular Velocity Data")
    st.write(ang_vel.head())
    if st.button('Angular velocity all analysis'):
        st.write('Okkaaay We start nowww')
        st.subheader("Dataset info")
        buffer = io.StringIO()
        ang_vel.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.subheader("Descriptice Statistics")
        st.write(ang_vel.describe())
        st.subheader("Scatter X And Y Angular Velocity Relationship")
        sns.relplot(data=ang_vel, x="xyz0", y="xyz1")
        st.pyplot()
        st.subheader("Scatter X And Z Angular Velocity  Relationship")
        sns.relplot(data=ang_vel, x="xyz0", y="xyz2")
        st.pyplot()
        st.subheader("Scatter Y And Z Angular Velocity Relationship")
        sns.relplot(data=ang_vel, x="xyz1", y="xyz2")
        st.pyplot()
        st.subheader("Correlation matrix Angular_Velocity ")
        st.text("""
                 CORRELATION MATRIX 
                  IF CORRELATION COFFICIENT X> 0.8 STROGNLY POSITIVE CORRELATION
                                            X < 0.8 STRONGLY NEGATIVE CORRELATION
                """)
        matrix = ang_vel.corr().round(2)
        mask = np.triu(np.ones_like(matrix, dtype=bool))
        sns.heatmap(matrix, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag', mask=mask)
        st.pyplot()
        st.write("Radical Value X Axis Velocity")
        sns.boxplot(data=ang_vel, x="xyz0")
        st.write("Dirtyyyy dataa")
        st.pyplot()
        st.write("Radical Value Y Axis Velocity")
        sns.boxplot(data=ang_vel, x="xyz1")
        st.write("Dirtyyyyyy dataa")
        st.pyplot()
        st.write("Radical Value Z Axis Velocity")
        sns.boxplot(data=ang_vel, x="xyz2")
        st.write("Dirty Data")
        st.pyplot()
        st.subheader("Data Clean IQR Method")
        st.write("""
         In descriptive statistics,
         the interquartile range (IQR) is a measure of statistical dispersion,
         which is the spread of the data.
         [1] The IQR may also be called the midspread,
         middle 50%, fourth spread, or H‑spread.
         It is defined as the difference between the 75th and 25th percentiles of the data.
         [2][3][4] To calculate the IQR, the data set is divided into quartiles,
          or four rank-ordered even parts via linear interpolation.
          [1] These quartiles are denoted by Q1 (also called the lower quartile), Q2 (the median), and Q3 (also called the upper quartile). The lower quartile corresponds with the 25th percentile and the upper quartile corresponds with the 75th percentile, so IQR = Q3 −  Q1[1].
          The IQR is an example of a trimmed estimator,
          defined as the 25% trimmed range,
          which enhances the accuracy of dataset statistics by dropping lower contribution,
         outlying points.
         [5] It is also used as a robust measure of scale[5] It can be clearly visualized by the box on a Box plot.[1]
        """)
        for i in ["xyz0", "xyz1", "xyz2"]:
            q1 = ang_vel[i].quantile(0.25)
            q3 = ang_vel[i].quantile(0.75)
            ıqr = q3 - q1
            lower = q1 - (1.5 * ıqr)
            upper = q3 + (1.5 * ıqr)
            lower_radical = (ang_vel[i] < (lower))
            upper_radical = (ang_vel[i] > (upper))
            ang_vel[i][lower_radical] = lower
            ang_vel[i][upper_radical] = upper
        st.write("""
         DATA CLEANED.......
         CLEANED SIR""")
        st.write("Radical Value X Axis Velocity")
        sns.boxplot(data=ang_vel, x="xyz0")
        st.write("Clean dataa")
        st.pyplot()
        st.write("Radical Value Y Axis Velocity")
        sns.boxplot(data=ang_vel, x="xyz1")
        st.write("Clean dataa")
        st.pyplot()
        st.write("Radical Value Z Axis Velocity")
        sns.boxplot(data=ang_vel, x="xyz2")
        st.write("Clean Data")
        st.pyplot()
        x_range = ang_vel["xyz0"]  # ASSIGMENT
        y_range = ang_vel["xyz1"]  # ASSIGMENT
        anom1 = pd.concat([x_range, y_range], 1)  # AGGREGATE TWO COLUMNS
        st.write("max difference")
        st.write(anom1[abs(anom1["xyz0"] - anom1["xyz1"]) >= 0.8829890284687281].iloc[0])
        radical = anom1[abs(anom1["xyz0"] - anom1["xyz1"]) >= 0.8829890284687281*0.3]  # threshold max difference %30
        st.write("threshold value (Max difference *0.3) = ",str(0.8829890284687281*0.3))
        st.subheader("Anomaly Visualization")
        radical_index = list(radical.index)
        a = np.array(radical_index)  # flatten index
        a = a.flatten()
        plt.scatter(anom1["xyz0"], anom1["xyz1"])
        plt.scatter(radical["xyz0"], radical["xyz1"], color='r')
        plt.xlabel("x angle velocity")
        plt.ylabel("y angle velocity")
        st.pyplot()
        radical_t = ang_vel[["timee"]].filter(items=a, axis=0)
        st.subheader("Anomaly Time Value")
        st.write(radical_t )
        st.subheader("Anomaly Time Show")
        sns.scatterplot(x=ang_vel["timee"], y=radical_t["timee"])  # radical time show blue
        plt.xlabel("all time")
        plt.ylabel("anomaly time")
        st.pyplot()



else :
     st.write("Oh sorry man.Just 3 dataset ın my bag")


