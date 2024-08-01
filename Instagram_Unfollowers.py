"""
Streamlit integration webapp for instagram-unfollowers
"""
import streamlit as st
import json
import main
st.title('Instagram Unfollowers')

if 'helpbool' not in st.session_state:
    st.session_state['helpbool'] = False

readme_link = 'https://github.com/hemmatio/instagram-unfollowers/tree/main?tab=readme-ov-file#downloading-your-data'

def toggle_help():
    st.session_state['helpbool'] = not st.session_state['helpbool']


if st.button('Help'):
    toggle_help()

if st.session_state['helpbool']:
        st.write('You must download your following and followers_1.json files from Instagram in JSON format. '
                 f'Visit [the GitHub readme]({readme_link}) for a step-by-step guide.')


# File paths
st.markdown('### Upload Files')
following = st.file_uploader('**Upload your following.json file**', type=['json'], label_visibility='visible')
followers = st.file_uploader('**Upload your followers_1.json file**', type=['json'], label_visibility='visible')

dataready = [False, False]
computed = False

if following:
    followingdata = json.load(following)
    dataready[0] = True

if followers:
    followerdata = json.load(followers)
    dataready[1] = True

# Button to run the comparison
if all(dataready):
    if st.button('Check unfollowers', help ='Make sure to upload your files first.'):
        set1, set2 = main.create_sets(followingdata, followerdata)
        if type(set1) == str:
            st.write(set1)
            computed = False
        else:
            unfollowers = main.difference(set1, set2)
            computed = True

if computed:
    st.markdown('### Unfollowers :snake::')
    count = 0
    for index, unfollower in enumerate(unfollowers):
        st.text(f"{index + 1}: {unfollower}")
        count = index + 1
    st.write(f"##### {count} accounts don't follow you back! :sob::broken_heart:")
