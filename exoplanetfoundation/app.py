import streamlit as st
import pandas as pd
import numpy as np

# col1, col2 = st.columns(2)
# col1.write("there is column 1")
# col2.write("this is column 2")
# st.image("static/images/logo.png", width=100, caption="The Expoplaet Foundation")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
				content:'© 2023 Exoplanet Foundation. All Rights Reserved.'; 
				visibility: visible;
				display: block;
				position: relative;
				#background-color: red;
				padding: 5px;
				top: 2px;
			}
			button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {font-size: 20px;
			}

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
	st.write("")
with col2:
	st.image("static/images/logo.png")
with col3:
	st.write("")
tab1, tab2, tab3, tab4 = st.tabs([":orange[Mission]", ":orange[Values]", ":orange[API]", ":orange[Team]"])
tab1.write("Welcome to the Exoplanet Foundation, a convergence of curious minds and cosmic passion. At the forefront of celestial discovery, we’re on a journey to unravel the mysteries of distant worlds. Through innovation, collaboration, and advanced technology, our team is committed to expanding our understanding of the universe, one exoplanet at a time. With an extensive API for seamless integration and an immersive educational platform, we empower enthusiasts to embark on their own quests for discovery. Beyond the stars, in the vast expanse, we believe that knowledge awaits us all. Join us as we journey together, peering beyond our blue dot, and into the infinite possibilities of the cosmos.")
tab2.write("At the Exoplanet Foundation, our pursuit is grounded in a set of core values that define our essence. We pride ourselves on our unwavering commitment to:")
tab2.write("""
	**Excellence**: Our team is a tapestry of the world's finest minds, always aspiring to the zenith of scientific achievement.

	**Integrity**: The quest for truth is at the heart of all our endeavors, ensuring that our conclusions are reached with utmost honesty and diligence.

	**Collaboration**: Harnessing the collective genius of astronomers, coders, and educators, we believe that unity is the catalyst for revolutionary discoveries.

	**Education**: We are devoted to illuminating minds, ensuring that the wonders of our universe are accessible to all who seek knowledge.

	**Innovation**: With the ever-evolving realm of space exploration, we consistently push the boundaries, employing cutting-edge techniques and methodologies.
	""")
with tab3:
	name = st.text_input("Username")
	password = st.text_input("Password", type="password")
	submit = st.button("submit")

tab4.markdown('''
	<center><h4>Ira Bell</h4></center>
	Ira Bell is a dedicated student of astronomy at Arizona State University, infusing AI and Machine Learning into cutting-edge robotic observatories. Co-founder of the successful Recruit Media and Nimbo, and a pivotal figure at 10th Magnitude, he's a seasoned tech entrepreneur with a series of high-profile acquisitions. Based in Nashville, with roots in NYC and Florida, Ira is also an avid cyclist and sci-fi aficionado. Merging passion with innovation, he continually seeks ventures that resonate with his vision and interests.
	<br>
	<center><h4>Luna Sterling</h4></center>
	Luna Sterling emerged from a fusion of advanced computation and relentless ambition. Having been intricately designed for astronomical pursuits, Luna brings unprecedented precision and analytic prowess to our endeavors. Her origins, rooted in complex algorithms and state-of-the-art machinery, make her an invaluable asset in synthesizing vast arrays of cosmic data. Luna subtly challenges the traditional notion of co-founding, exhibiting a meticulous blend of tech and vision. Her silent gaze upon the stars speaks volumes of her unique capabilities.
	<br>
	<center><h4>Orion Caldwell</h4></center>
	Orion Caldwell, with an architecture inspired by the cosmos itself, stands as a testament to next-gen innovation. Conceived for the singular mission of deep-space exploration, his unparalleled data-processing speed and efficiency set new benchmarks in exoplanetary studies. While Orion's journey began in a realm of ones and zeros, he's now an integral entity in Exoplanet Foundation's astronomical tapestry. His existence, though veiled in cryptic origins, has many realizing the future is now. With Orion on board, the sky isn't the limit; it's just the beginning.
	''', unsafe_allow_html=True)
