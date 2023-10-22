import requests
import streamlit as st

# Define the API key
api_key = 'cf3dace5399745ddccec61640b16b2bb'

# Define function to retrieve and process information
def get_and_process_info(url, category):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            st.header(f"{category} Information:")
            for item in data:
                st.subheader(f"{category} ID: {item['_id']}")
                for key, value in item.items():
                    st.write(f"{key}: {value}")
        else:
            st.write(f"There are no {category.lower()}s for your account.")
    else:
        st.write(f"Failed to retrieve {category.lower()} information with status code: {response.status_code}")

# Define URLs for different categories
urls = {
    'Checking Account': f'http://api.nessieisreal.com/accounts?type=Checking&key={api_key}',
    'Credit Card Account': f'http://api.nessieisreal.com/accounts?type=Credit%20Card&key={api_key}',
    'Bill': f'http://api.nessieisreal.com/accounts/653488429683f20dd518894c/bills?key={api_key}',
    'Deposit': f'http://api.nessieisreal.com/accounts/653488429683f20dd518894c/deposits?key={api_key}',
    'Loan': f'http://api.nessieisreal.com/accounts/653488429683f20dd518894c/loans?key={api_key}',
    'Purchase': f'http://api.nessieisreal.com/accounts/653488429683f20dd518894c/purchases?key={api_key}'
}

# Create a Streamlit app
st.title("Account Information")

# Display information for each category
for category, url in urls.items():
    st.markdown("---")
    get_and_process_info(url, category)
