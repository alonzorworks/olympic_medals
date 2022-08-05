import pandas as pd 
import streamlit as st 
import plotly.express as px
import plotly.graph_objects as go

from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title = "Olympics",
    page_icon = "🥇"
)

# NOTE Allow pictures to be put into the document. 
def load_lottieurl(url):
    """If the lottie file does not display the image return nothing. This will prevent errors when trying to display the Lottie Files.
    Requires importing packages streamlit_lottie and requests"""
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()


def lottie_credit(credit):
    return st.markdown(f"<p style='text-align: center; color: gray;'>{credit}</p>", unsafe_allow_html=True)




st.title("Olympic Games Summer 1976-2008 🥇🥈🥉")

winner = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_o86x2brk.json")
st_lottie(winner, height = 570)
lottie_credit("Olympic games 2021_Winner Girl Animation Abdul Latif LottieFiles")

st.subheader("Introduction and Rudimentary Analysis 🏅 ")
st.write("The Olympics Games is the biggest sports event in terms of scope. (It's only formidable rival is the World Cup). Elite athletes represent their countries from around the world in virtually every sport and discipline imagineable.")
st.write("This data comes from Divyansh Agrawal. He is a Data Analyst at PwC. He does not disclose any source for the data. The dataset provides medals won from 1976 - 2008. Note that the dataset only includes medals won during the summer Olympic Games.")

st.subheader("Variables Explained 🏀🥅⚽⚾🧢🎾🏊🏿‍♀️")
olympics = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_iamb7tjt.json")
st_lottie(olympics, height = 300)
lottie_credit("Olympics Loader - Jay Baculch LottieFiles")

st.write("The variables in the dataset are mostly self explanatory, but some of the terms are quite precise and nuanced. Below the dataset is explained in Agrawal's own words:")

col1, col2 = st.columns(2)

torch = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_uzzrjmto.json")

with col1:
    st.write("""
City - City in which the Olympic Games were held. \n
Year - Year in which the Olympic Games were held \n 
Sport - Sport Category (eg. Aquatics, Atheletics etc.) \n
Discipline - The discipline within the sport (eg. Diving, Swimming etc.) \n
Event - Event Name within the particular discipline (eg. 3m springboard, 10m platform etc.) \n
Athlete - Winner Name in that event \n
Gender - Gender \n
Country - Country to which the winning athlete belongs to \n
Country_Code 3 character country code \n
Country - Country to which the winning athlete belongs to \n
Event_gender - Genders which participated in the event (Male, Female or Common Event)
""")

with col2:
    st_lottie(torch)
    lottie_credit("Olympics - Sports Torch By LottieFiles on LottieFiles")

st.subheader("What is The Most Athletic Country? 👟🎽")
usa = load_lottieurl("https://assets2.lottiefiles.com/datafiles/PUa5p5WJhRg94F59AaaQytNjTG4IttKa0UT9bms7/us.json")
st_lottie(usa, height = 400)
lottie_credit("US Flag - Nattu Adnan LottieFiles")


st.write("""This question was not a hard one to answer. This is because the United States of America won the plurality of every medal type from 1976-2008.
This is likely due to a variety of factors. For one the United States loves sports, it is an essential component of the American identity, similar to how sports was an essential part of Greek and Roman culture. This is why someone who is a great athlete all around is called all American.
Many school children dedicate their lives in hopes to become a professional athletes, and very few matriculate to those esteemed ranks. 

In addition to this America is by far the most diverse country in the world. Genetic variation can be ascribed as one of the reasons for the US athletic dominance.
In addition to this the United States is one of the largest countries in the world, which makes the competition for Olympic slots more fierce in the US than smaller countries.
The US is also one of the richest countries in the world. They have access to some of the best doctors, trainers, nutritionists, and other professionals that can give US athletes the edge they need to beat the best in the world. \n

US culture may also play a small role in the country's athletic dominance. The US praises the feats of individuals arguable moreso than the collective even when the media's "hero" acts in a large team.
Think of Neil Armstrong in the Apollo mission. The thousands of people that helped in project and even if his own crew seldom receive comparably deep commemoration. This combined with a country with a reputation of pride, nationalism, and patrotinism culminates in a unquenchable desire for medals as well as glory.

""")



df = pd.read_csv("olympic_summer_cleaned.csv")
# df.dropna(inplace = True)


# df.Year = df.Year.astype(int)



df

st.header("Data Section 🎯👩🏿‍💻🚴🏿‍♂️🏐")

col3, col4 = st.columns(2)


spin = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_qgdcqwbg.json")
st_lottie(spin, height = 300)
lottie_credit("Basketball - Vladislav Sholohov")
# Bar Chart of the Nations that won medals 
df_country = df
#df_country = df_country["Medal"].groupby(by = "Country").count().sum()

# Retains the actual year withoout summing
df_country = df_country.groupby("Country").sum()



df_country = df_country.iloc[:, 1::]
#Split these up because it was not displaying as one lone
df_country = df_country.sort_values(by = ["Gold", "Silver", "Bronze"], ascending= False)

# Double brackets are used to show that it is a Dataframe and not a series.
df_country = df_country[["Gold", "Silver", "Bronze"]]


df_country.reset_index(inplace = True)
df_country


# total_medal_country = gp.Figure(data = [
#     go.Bar(name = "Gold", x = )
# ])

medals = df_country.columns[1::]

# This for loop creates a pie chart for each medal
# The values are too small so I won't use this visual.
# for i in medals:
#     fig = px.pie(df_country, values = f"{i}" , names = "Country" )
#     st.plotly_chart(fig)

medal_colors = ["gold", "silver", "brown"]
new_line = "\n"

medal_num = 0

for i in medals:
    message = f"Country Bar Chart for {i} Medals"
    import streamlit as st
    st.markdown(f"<p style='text-align: center; color: #FAFAD2;'>{message}</p>", unsafe_allow_html=True)
    df_country_temp = df_country.sort_values([f"{i}"], ascending = False)
    df_country_temp = df_country_temp[df_country_temp[f"{i}"] >= 1]
    fig  = px.bar(df_country_temp , x = "Country", y = f"{i}", title = f"Country Count of {i} Medals 1976-2008", text_auto =True, width = 1000, height = 700)
    fig.update_traces(marker_color = f"{medal_colors[medal_num]}")
    st.plotly_chart(fig)

    #Must use data that has not been filtered. So we pull up the df_country data frame.
    losers = df_country[df_country[f"{i}"] == 0].Country.values.tolist()
    #losers = df_country_temp[df_country_temp[f"{i}"] == 0].Country.values.tolist()


    
    st.write(f"Countries that did not win at least one {i} medal was omitted from the chart.")
    with st.expander(f"Click here to see list of countries who did not win a {i} medal, between 1976-2008"):
        for country in losers:
            st.write(country)

    medal_num += 1
    # This for loop creates a bar chart for the olympic games. 
    #The chart is at the gold, silver, and bronze levels.
    #It dynamically calculates which medal is being evaluated and sorts in descending order in respects to it. 
    # It gets rid of any country that did not win a particular medal. 
    # It labels the bar chart. 
    # It creates a list of countries that did not win a particular medal inside a collaspeable interface. 
    #

# Next Section Medal Wins over time by Country 
#NOTE 
# Start of Interactive Section 
# Need to groupby country and year. 

df_yearly = df

df_yearly = df_yearly.groupby(["Year", "Country"]).sum()

df_yearly.reset_index(inplace = True)

df_yearly



# Function for Creating A Chart Based off of The Medal of The Country 
def medal_line(medal):
    medal = medal.title()

    line = px.line(df_yearly, x = "Year", y = medal, color = "Country", title = f"{medal} Medals By Year in The Olympics", markers = True,  width = 1000, height = 700)
    return st.plotly_chart(line)


medal_line("gold")
medal_line("silver")
medal_line("bronze")

# Pie charts for men and women 
df_gender = df
df_gender = df_gender.groupby("Gender").count().reset_index()


df_gender

pie = px.pie(df_gender, values = "Event", names =  "Gender", color = "Gender", color_discrete_map = {"Men" : "#2561EC ","Women": "pink"},
title =  "Winners By Gender")
st.plotly_chart(pie)

# pie = px(df_gender, values = "" )



# Best Athletes by number of medals 
df_athlete = df 
df_athlete = df_athlete.groupby(["Year" , "Athlete"]).sum(["Bronze", "Silver", "Gold"])
df_athlete = df_athlete.reset_index()
df_athlete

df_athlete[df_athlete["Gold"] > 1]

tier_medals = ["Bronze", "Silver", "Gold"]

#People That more than one medal
st.subheader("People That Won More Than One Medal")
for i in tier_medals:
    i = i.title()

    line =  df_athlete[df_athlete[f"{i}"] > 1]
    fig  = px.bar(df_athlete[df_athlete[f"{i}"] > 1], x = "Year", y = i, color = "Athlete", text_auto =True, width = 1000, height = 700, title = f"Athletes Who Won More Than One {i} Medals")
    st.plotly_chart(fig)

cup = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_DTf87D.json")
st_lottie(cup, height = 500)
lottie_credit("Cup - Vasyl Kolodiychyk LottieFiles")


# ath_line = px.line(df_athlete, x = "Year", y = "")

# Map of hosting countries 
# Map of countries and the ammount of medals won

