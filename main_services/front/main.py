import streamlit as st
import requests
import os
from itertools import compress


###### st.session_state['new_users'] = []
### shariki ebanie

BACKHOST = os.environ.get("BACKEND_SERVICE_SERVICE_HOST")

def postdude(user:str, song:str):
    user = user.replace(' ', '%20')
    song = song.replace(' ', '%20')
    post_string = f"http://{BACKHOST}:8080/register?input={user}%20---%20{song}"
    requests.post(post_string)

def onClickFunction():
    st.session_state.infer = True

def get_user_ids():
    return requests.get(
        url=f"http://{BACKHOST}:8080/all_users?input=gigalul"
        ).text\
            .strip('[""]')\
            .split('","')

def get_recs(option):
    result = requests.get(url=f"http://{BACKHOST}:8080/predictions?user_id={option}&n=5")\
        .text.split('","')
    return result

def main():

    if 'sidebar_state' not in st.session_state:
        st.session_state.sidebar_state = 'expanded'

    st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state)

    if st.session_state.sidebar_state != 'expanded':
        st.balloons()

    if 'infer' not in st.session_state:
        st.session_state.click = False


    userids = get_user_ids()

    

    ### SIDEBAR
    sdb = st.sidebar
    sdb.write('If you cant find your username, please register here!')
    new_u_username = sdb.text_input('input your name here', key='newuid')
    new_u_song = sdb.text_input('please, provide us your favourite song!', key='newusong')
    new_u_author = sdb.text_input('please, name the author of the song', key='newauthor')
    if_commit = sdb.button("Press this button when you are sure that the format is proper to register yourself!")

    if st.session_state.sidebar_state != 'expanded':
        sdb.write(f"Thast.write(song)nk you, {new_u_username}! You have already registered!")

    if if_commit:
        if len(new_u_username) > 0 and len(new_u_song) > 0 and len(new_u_author):
            sdb.write(f"done! Thank you, {new_u_username}!")
            st.session_state.sidebar_state = 'collapsed' if st.session_state.sidebar_state == 'expanded' else 'expanded'
            st.experimental_rerun()
            st.balloons()
        else:
            sdb.write('wrong format')
    
    ### MAIN PAGE

    ### TITLES
    st.header('Welcome to our music recomender system!')
    st.write('Please, register in the sidebar, if you have not registered yet')

    ### USER ID DROPBOX
    option = st.selectbox('Enter your user id',
                          userids)
    ### BODY
    cont1 = st.container()

    ### GET INFER MAGIC BUTTON 
    inferBut = cont1.button('get me some recs', on_click = onClickFunction)
    try:
        if st.session_state['infer']:
            cont2 = st.container()
            cont2.col1, cont2.col2 = st.columns(2)
            checks = []
            songs = []
            for _ in get_recs(option):
                checks.append(cont2.col1.checkbox(_.strip('["').strip('"]').replace('__', ' -- ')))
                songs.append(_)
            cont2.col2.write("Which of them do u like? Checkmark the ones you like and submit the result so we could take your feedback into account further!")
                
            ### PART 3
            cont3 = st.container()


            ### SUBMIT BUTTON
            ifcl = cont3.button("Submit your reactions so we can improve our service!")
            if ifcl:
                for song in list(compress(songs, checks)):
                    postdude(user=option, song=song)

    except:
        cont1.write('Hi!')




if __name__ == "__main__":
    main()