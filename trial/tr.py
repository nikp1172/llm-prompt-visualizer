import streamlit as st
import requests
from data import get_data
from update import update_user_reaction

REACTIONS = ["Red", "Yellow", "Green"]

def main():
    st.title("API Data Viewer")
    # Add filtering options
    model_filter = st.text_input("Filter by Model Name")
    reaction_filter = st.selectbox("Filter by User Reaction", options=["All", "Red", "Yellow", "Green"])

    # Construct filter parameters
    params = {}
    if model_filter:
        params["model_name"] = model_filter
    if reaction_filter != "All":
        params["user_reaction"] = reaction_filter.lower()
    # Make a request to the API to retrieve the data
    
    data = get_data()

    # Display the data in a table with bigger rows
    st.write("## Data")
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write('<style>td{word-wrap: break-word;}</style>', unsafe_allow_html=True)
    st.write('<style>div.row-widget.stRadio > div > div{padding-right: 1rem;}</style>', unsafe_allow_html=True)
    st.write('<style>div.row-widget.stRadio > div > label{margin-right: 1rem;}</style>', unsafe_allow_html=True)
    st.write('<style>table th{font-size: 1.1rem;}</style>', unsafe_allow_html=True)
    st.write('<style>table td{font-size: 1.1rem;}</style>', unsafe_allow_html=True)

    st.write('<table style="width:100%"><tr><th>Model Name</th><th>Prompt</th><th>Response</th><th>Inference Time (s)</th><th>User Reaction</th></tr>', unsafe_allow_html=True)
    for i, row in enumerate(data):
        model_name = row["model_name"]
        prompt = row["prompt"]
        response = row["response"]
        inference_time = row["inference_time"]
        user_reaction = row.get("user_reaction", "Green")
        
        #user_reaction = st.selectbox(f"Select reaction: {i}", options=REACTIONS, index=REACTIONS.index(user_reaction))
        row = f'<tr><td>{model_name}</td><td>{prompt}</td><td>{response}</td><td>{inference_time:.2f}</td><td><div style="display: flex;"><span>{user_reaction}</span></div></td></tr>'
        # wrap the select box in a table cell element
        row = row.replace('</div></td>', f'</div></td><td>{user_reaction}</td>')
        st.write(row, unsafe_allow_html=True)
        # user_reaction = st.selectbox(f"Select reaction: {i}", options=REACTIONS, index=REACTIONS.index(user_reaction))
        # # Allow the user to update the user_reaction value and send the updated data back to the API
        # # if st.button(f"Update Reaction: {i}"):
        # #     updated_reaction = st.selectbox("Select reaction", options=REACTIONS, index=REACTIONS.index(user_reaction))
        # #     row["user_reaction"] = updated_reaction
        # #     #response = requests.put(API_URL, json=row)
        # #     if True:
        # #         st.success("Updated successfully!")
        # #     # else:
        #     #     st.error("Update failed.")
        # row = f'<tr><td>{model_name}</td><td>{prompt}</td><td>{response}</td><td>{inference_time:.2f}</td><td><div style="display: flex;"><span>{user_reaction}</span></div></td></tr>'
        # st.write(row, unsafe_allow_html=True)
        # #st.write(f'<tr><td>{model_name}</td><td>{prompt}</td><td>{response}</td><td>{inference_time:.2f}</td><td>{user_reaction}</td></tr>', unsafe_allow_html=True)
    st.write('</table>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()