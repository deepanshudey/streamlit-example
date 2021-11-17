import streamlit as st
import streamlit_app

def app(conn):
    st.title('APP1')
    st.write('Welcome to app1')

    # Perform query.
    # Uses st.cache to only rerun when the query changes or after 10 min.
    @st.cache(ttl=600)
    def run_query(query):
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()



    rows = run_query("SELECT * from project;")

    # Print results.
    for row in rows:
        st.write(f"{row[0]} has a :{row[1]}:")