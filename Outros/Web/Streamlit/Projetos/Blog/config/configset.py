import streamlit as st

def set_config():
    """Configurações Gerais do Blog"""

    st.set_page_config(
        page_title = "Blog",
        page_icon = "🗒️",
        layout = "wide"
    )

def set_style():
    """Estilos do Blog"""

    st.markdown("""
<style>
    header.st-emotion-cache-1pru02b.e16b601d7 {
        color: white;
        font-size: 1em;
        font-weight: bolder;
    }

    h3#voce-pode-comecar-aqui {
        text-align: center;
    }

</style>
    """, unsafe_allow_html = True)


def main():
    set_config()
    set_style()


main()
