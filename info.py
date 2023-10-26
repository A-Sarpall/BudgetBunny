import requests
import streamlit as st

# Define the API key
api_key = '[Redacted]'

# Define function to retrieve and process information
def get_and_process_info(url, category):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            st.header(f"{category} Information:")
            for i, item in enumerate(data, start=1):
                st.subheader(f"{category} {i}: {item['_id']}")
                for key, value in item.items():
                    if(key == "_id"):
                        st.write(f"ID: {value}")
                    elif(key == "account_id"):
                        st.write(f"Account ID: {value}")
                    elif(key == "customer_id"):
                        st.write(f"Customer ID: {value}")
                    else:
                        st.write(f"{key.capitalize()}: {value}")
                        
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
