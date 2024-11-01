# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(":cup_with_straw: customise your Smoothie :cup_with_straw:")
st.write(
    "Choose the fruits you want in your custom smoothies"
)
#import streamlit as st
from snowflake.snowpark.functions import col
cnx=st.connection("snowflake")
session=cnx.session()
#session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

name_on_order = st.text_input("Name on Smoothie:")
st.write("The name on your Smoothie will be:", name_on_order)
#import streamlit as st

ingredients_list = st.multiselect(
    "Choose upto 5 ingredients:",
   my_dataframe
)
if ingredients_list:
 st.write("You selected:", ingredients_list)
 st.text( ingredients_list)
 ingredients_string= ''
 for each_fruit in ingredients_list:
      ingredients_string += each_fruit + ' '
 #st.write(ingredients_string)
 
 my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """'  )"""
 
 #st.write(my_insert_stmt)
 if ingredients_string:
  time_to_insert= st.button('Submit Order')
  if time_to_insert:   
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered!', icon="✅")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)
