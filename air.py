import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")


st.set_page_config(page_title= "Airbnb Data Visualization",
                   layout= "wide",
                   initial_sidebar_state= "expanded"
                   )

st.title("AIRBNB DATA ANALYSIS")
st.write("")

with st.sidebar:
    select= option_menu("Main Menu", ["Home", "Data Exploration", "About"],
                        icons=["house","search","exclamation with circle"])
                        

if select == "Home":
    
    st.header("About Airbnb")
    st.write("")
    st.image("image-airbnb.webp")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    st.write("")
    st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***''')
    
    st.header("Background of Airbnb")
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')

if select == "Data Exploration":

    tab1, tab2, tab3, tab4, tab5= st.tabs(["PRICE ANALYSIS",
                                           "AVAILABILITY ANALYSIS",
                                           "LOCATION BASED", 
                                           "GEOSPATIAL VISUALIZATION", 
                                           "TOP CHARTS"])
    def datafr():
        df= pd.read_csv("Airbnb.csv")
        return df

    data=datafr()   
    
    with tab1:
        st.title("PRICE DIFFERENCE")

        #contry based price analysis

        st.write("**PRICE BASED ON COUNTRY**")

        contry=st.selectbox("Select the Country",data["country"].unique())
        df1= data[data["country"]==contry]
        df1.reset_index(drop= True, inplace= True)

        Roomty=st.selectbox("Select the Room Type for the Country",df1["room_type"].unique())

        df2=df1[df1["room_type"]==Roomty]
        df2.reset_index(drop =True, inplace= True)

        df_bar=pd.DataFrame(df2.groupby("property_type")[["price","review_scores", "number_of_reviews"]].sum())
        df_bar.reset_index(inplace= True)

        fig_bar=px.bar(df_bar, x="property_type",y="price", title="PRICE BASED ON PROPERTY TYPES",
                    hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.GnBu_r,
                    width=600,height=500)

        st.plotly_chart(fig_bar)

        st.write("**PRICE BASED ON ROOM TYPE WITH MAX AND MIN NIGHTS**")

        roomty=st.selectbox("Select the Room Type ",data["room_type"].unique())

        df_room_type=data[data["room_type"]==roomty]
        df_room_type.reset_index(drop=True,inplace=True)

        df4=pd.DataFrame(df_room_type.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
        df4.reset_index(inplace=True)


        fig_bar_1=px.bar(df4,x="bed_type",y=["minimum_nights","maximum_nights"],barmode="group",
                        title="PRICE BASED ON MINMUM AND MAXIMUM NIGHTS",hover_data="price",
                        color_discrete_sequence=px.colors.sequential.Rainbow,width=600,height=600)

        st.plotly_chart(fig_bar_1)

        # cancellation based price
        st.write("**PRICE BASED ON PROPERTY TYPE WITH CANCELLATION POLICY**")

        Pro_type=st.selectbox("Select the Property Type ",data["property_type"].unique())
        df_property_type=data[data["property_type"]==Pro_type]
        df_property_type.reset_index(drop=True,inplace=True)

        df5=pd.DataFrame(df_property_type.groupby("cancellation_policy")[["price","number_of_reviews"]].sum())
        df5.reset_index(inplace=True)

        fig_pie_1=px.pie(df5,names="cancellation_policy",values="price",
                        title="PRICE ANALYSIS BASED ON CANCELLATION POLICY",
                        width=600,height=600,hole=0.4,hover_data="number_of_reviews",)

        st.plotly_chart(fig_pie_1)


    with tab2:

        st.title("AVAILABILITY ANALYSIS")
        col1,col2= st.columns(2)
        with col1:
                  
            country_a= st.selectbox("Select the Country for Availability Analysis",
                                    data["country"].unique())

            df1_a= data[data["country"] == country_a]
            df1_a.reset_index(drop= True, inplace= True)

            property_ty_a= st.selectbox("Select the Property Type",df1_a["property_type"].unique())
            
            df2_a= df1_a[df1_a["property_type"] == property_ty_a]
            df2_a.reset_index(drop= True, inplace= True)

            df_a_sunb_30= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], 
                                      values="availability_30",width=400,
                                      height=500,title="Availability_30",
                                      color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_a_sunb_30)
        
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            

            df_a_sunb_60= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], 
                                      values="availability_60",width=400,height=500,
                                      title="Availability_60",
                                      color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(df_a_sunb_60)

        col3,col4= st.columns(2)

        with col3:
            
            df_a_sunb_90= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], 
                                      values="availability_90",width=400,height=500,
                                      title="Availability_90",
                                      color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
            st.plotly_chart(df_a_sunb_90)

        with col4:

            df_a_sunb_365= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"],
                                        values="availability_365",width=400,height=500,
                                        title="Availability_365",
                                        color_discrete_sequence=px.colors.sequential.Greens_r)
            st.plotly_chart(df_a_sunb_365)
        
        roomtype_a= st.selectbox("Select the Room Type for Availability Analysis", 
                                 df2_a["room_type"].unique())

        df3_a= df2_a[df2_a["room_type"] == roomtype_a]

        df_mul_bar_a= pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30",
                                                                        "availability_60",
                                                                        "availability_90",
                                                                        "availability_365",
                                                                        "price"]].sum())
        df_mul_bar_a.reset_index(inplace= True)

        fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time', 
                                  y=['availability_30', 
                                     'availability_60', 
                                     'availability_90', 
                                     "availability_365"], 
                                     title='AVAILABILITY BASED ON HOST RESPONSE TIME',
                                     hover_data="price",barmode='group',
                                     color_discrete_sequence=px.colors.sequential.Rainbow_r,
                                     width=1000)

        st.plotly_chart(fig_df_mul_bar_a)

    with tab3:

        st.title("LOCATION ANALYSIS")

        country_l= st.selectbox("Select the Country for Location Analysis",
                                data["country"].unique())

        df1_l= data[data["country"] == country_l]
        df1_l.reset_index(drop= True, inplace= True)

        proper_ty_l= st.selectbox("Select the Property_type_l",df1_l["property_type"].unique())

        df2_l= df1_l[df1_l["property_type"] == proper_ty_l]
        df2_l.reset_index(drop= True, inplace= True)


        
       
        df_val_sel_gr= pd.DataFrame(df2_l.groupby("accommodates")
                                    [["cleaning_fee","bedrooms","beds","extra_people"]].sum())
        df_val_sel_gr.reset_index(inplace= True)

        fig_1= px.bar(df_val_sel_gr, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], 
                      title="ACCOMMODATES",
                    hover_data= "extra_people", barmode='group', 
                    color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_1)
        
        
        room_ty_l= st.selectbox("Select the Room Type for Location Analysis",
                                 df2_l["room_type"].unique())

        df_val_sel_rt= df2_l[df2_l["room_type"] == room_ty_l]

        fig_2= px.bar(df_val_sel_rt, x= ["street","host_location","host_neighbourhood"],
                      y="market", title="MARKET",
                     hover_data= ["name","host_name","market"], barmode='group',orientation='h',
                      color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_2)

        fig_3= px.bar(df_val_sel_rt, x="government_area", 
                      y= ["host_is_superhost","host_neighbourhood","cancellation_policy"],
                        title="GOVERNMENT_AREA",
                    hover_data= ["guests_included","location_type"], barmode='group', 
                    color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_3)

    with tab4:

        st.title("GEOSPATIAL VISUALIZATION")

        fig_4 = px.scatter_mapbox(data, lat='latitude', lon='longitude', color='price',
                                   size='accommodates',color_continuous_scale= "rainbow",
                                   hover_name='name',range_color=(0,49000), 
                                   mapbox_style="open-street-map",zoom=1)
        fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
        st.plotly_chart(fig_4)   
      

    with tab5:

        country_t= st.selectbox("Select the Country for top charts",data["country"].unique())

        df1_t= data[data["country"] == country_t]

        property_ty_t= st.selectbox("Select the Property_type Top charts",
                                    df1_t["property_type"].unique())

        df2_t= df1_t[df1_t["property_type"] == property_ty_t]
        df2_t.reset_index(drop= True, inplace= True)

        df2_t_sorted= df2_t.sort_values(by="price")
        df2_t_sorted.reset_index(drop= True, inplace= True)


        df_price= pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace= True)
        df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
        
        col1, col2= st.columns(2)

        with col1:
            
            fig_price= px.bar(df_price, x= "Total_price", y= "host_neighbourhood", orientation='h',
                            title= "PRICE BASED ON HOST_NEIGHBOURHOOD", width= 600, height= 800)
            st.plotly_chart(fig_price)

        with col2:

            fig_price_2= px.bar(df_price, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                                title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",width= 600, height= 800)
            st.plotly_chart(fig_price_2)

        col1, col2= st.columns(2)

        with col1:

            df_price_1= pd.DataFrame(df2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
            df_price_1.reset_index(inplace= True)
            df_price_1.columns= ["host_location", "Total_price", "Avarage_price"]
            
            fig_price_3= px.bar(df_price_1, x= "Total_price", y= "host_location", orientation='h',
                                width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_3)

        with col2:

            fig_price_4= px.bar(df_price_1, x= "Avarage_price", y= "host_location", orientation='h',
                                width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "AVERAGE PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_4)

        
        #Avg Availability in each Country
        country_df = data.groupby('country',as_index=False)['availability_365'].mean()
        country_df.availability_365 = country_df.availability_365.astype(int)
        fig = px.scatter_geo(data_frame=country_df,
                                    locations='country',
                                    color= 'availability_365', 
                                    hover_data=['availability_365'],
                                    locationmode='country names',
                                    size='availability_365',
                                    title= 'Avg Availability in each Country',
                                    color_continuous_scale='agsunset',
                                    width= 1000, height= 1000
                            )
        st.plotly_chart(fig)

        #Avg Price in each Country
        country_df1 = data.groupby('country',as_index=False)['price'].mean()
        fig1 = px.scatter_geo(data_frame=country_df1,
                                    locations='country',
                                    color= 'price', 
                                    hover_data=['price'],
                                    locationmode='country names',
                                    size='price',
                                    title= 'Avg Price in each Country',
                                    color_continuous_scale='agsunset',
                                    width= 1000, height= 1000
                            )
        st.plotly_chart(fig1)

        

if select == "About":

    st.header(":red[*Airbnb Data Visualization*] By Jacob Raj Mark")
    col1, col2 = st.columns(2, gap='medium')
    with col1:

        col1.markdown("## :red[Domain] : ")
        col1.markdown("## Travel Industry")
        col1.markdown("## Property Management")
        col1.markdown("## Tourism")
        col1.markdown("## :red[Technologies used] : ")
        col1.markdown("## Python") 
        col1.markdown("## Pandas")
        col1.markdown("## Plotly")
        col1.markdown("## Streamlit")
        col1.markdown("## MongoDB")
        
    with col2:
        col2.markdown("#   ")
        st.image("https://i.gifer.com/7lI8.gif")
        col2.markdown("#   ")
       
    st.markdown("## :red[Overview] : To analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends. ")

    st.image("airbnb 1.jpg")
