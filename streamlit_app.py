
import streamlit as st


def emoji_demoji(addFlag):
    zwj = '\u200d'
    out = sep = ''
    j = 0

    if addFlag == 'Emoji':
        emotic = out = ''
        emotic = st.text_input(label='Enter your simple Emojis to add',
                               placeholder='Enter your simple Emojis to add')
        for i in range(len(emotic)):
            out += zwj + emotic[i]
        if out:
            st.write('Joined emoji: ', out)
    else:
        emotic = out = ''
        emotic = st.text_input(label='Enter your complex Emojis to break',
                               placeholder='Enter your complex Emojis to break')
        for i in range(len(emotic)):
            if emotic[i] != zwj:
                if j == 0:
                    out = emotic[i]
                else:
                    out += sep + emotic[i]
                j += 1
        if out:
            st.write('Demystified emoji: ', out)


def pageSettings():
    st.set_page_config(page_title='Emoji-Demoji', page_icon=':sunglasses:', initial_sidebar_state='auto')
    addFlag = st.sidebar.radio(label='Select Emoji or Demoji', options=['Emoji', 'Demoji'])

    # hide hamburger menu and footer
    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden}
                    footer {visibility: hidden}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    emoji_demoji(addFlag)


if __name__ == '__main__':
    pageSettings()
