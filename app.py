import streamlit as st
from streamlit_folium import folium_static
import folium

st.write("Created by Attapon Pillai")
# center on Liberty Bell
m = folium.Map(location=[8.50076515112644, 98.63120555686038], zoom_start=12)

# add marker for Liberty Bell
tooltip1 = "วัดบางเหรียง"
tooltip2 = "องค์การบริหารส่วนตำบลบางเหรียง"
tooltip3 = "สถานีอนามัย"
tooltip4 = "โรงเรียนบ้านทับปุด"
tooltip5 = "น้ำตก"
tooltip6 = "สถานีตำรวจ"
folium.Marker([8.474505954251509, 98.600169116302], tooltip=tooltip1).add_to(m)
folium.Marker([8.474827386201078, 98.65077865428118], tooltip=tooltip2).add_to(m)
folium.Marker([8.456242050613291, 98.61251587579054], tooltip=tooltip3).add_to(m)
folium.Marker([8.469946800016434, 98.59057261751371],  tooltip=tooltip4).add_to(m)
folium.Marker([8.48779407016935, 98.58609466831747],  tooltip=tooltip5).add_to(m)
folium.Marker([8.509355339211703, 98.680222924119], tooltip=tooltip6).add_to(m)

# call to render Folium map in Streamlit
folium_static(m)

