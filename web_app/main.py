import streamlit as st
import requests
import pickle
import os
import json
import pandas as pd
PROJ_PATH = os.path.dirname(
    os.path.dirname(
        os.path.realpath(__file__)
    )
)

sess_reactions = set()

def main():
    with open(f"{PROJ_PATH}/app/data/userids.pkl", 'rb') as f:
        userids = pickle.load(f)

    st.header('Welcome to our music recomender system!')
    option = st.selectbox('Enter your user id',
                          userids)
    cont1 = st.container()
    getRecs = cont1.button('get me some recs')

    cont2 = st.container()
    cont2.col1, cont2.col2 = st.columns(2)
    checks = []
    songs = []
    for _ in requests.get(url="http://127.0.0.1:8054/predictions/",
                                       data=json.dumps({'user_id': option, 'n': 5})).text.split('","'):
        checks.append(cont2.col1.checkbox(_.strip('["').strip('"]').replace('__', ' -- ')))
        songs.append(_)
    cont2.col2.write("Which of them do u like? Checkmark the ones you like and submit the result so we could take your feedback into account further!")
    cont3 = st.container()
    ifcl = cont3.button("Submit your reactions so we can improve our service!")
    if ifcl:
        for i, b in enumerate(checks):
            if b:
                sess_reactions.add(option+'~'+songs[i])
        try:
            with open("web_app/stored_reactions.pkl", 'r+') as f:
                stored_reactions = pickle.load(f)
                stored_reactions.update(sess_reactions)
                pickle.dump(stored_reactions, f)
        except:
            with open("web_app/stored_reactions.pkl", 'wb') as f:
                pickle.dump(sess_reactions, f)

    sdb = st.sidebar
    sdb.write('If you cant find your username, please register here!')
    new_u_username = sdb.text_input('input your name here', key='newuid')
    new_u_song = sdb.text_input('please, provide us your favourite song!', key='newusong')
if __name__ == "__main__":
    main()