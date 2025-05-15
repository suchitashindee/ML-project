import streamlit as st
import pickle 
import time

# Load model
with open("rfmodel.pkl", "rb") as model_file:
    classifier = pickle.load(model_file)

# Prediction function
def perdicton_price(area_type_no, size, total_sqft, bath, balcony, price_per_sqft, location_no):
    try:
        prediction = classifier.predict([[area_type_no, size, total_sqft, bath, balcony, price_per_sqft, location_no]])
        return prediction[0]
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        return None

# Main Streamlit app
def main():
    st.title('House Price Prediction')
    st.subheader('kolhapur City')

    with st.sidebar:
        with st.spinner("Loading..."):
            time.sleep(2)
        st.success("Model Ready!")
        st.link_button("Contact Us", "https://www.linkedin.com/in/suchita-shinde-752487359/")
        st.link_button("Contribute", "https://github.com/aakashmohole/ML-Project")
        with st.expander("Developers info"):
            st.write("""
                1. [Bhumika Bumb]("https://www.linkedin.com/in/bhumika-bumb-b2720632b/")
                2. [Suchita Shinde]("https://www.linkedin.com/in/suchita-shinde-752487359/")
                3. [Apurva Kadam]("https://www.linkedin.com/in/apurva-kadam-2bb20532b/")
                4. [Siddhi Patil]("https://www.linkedin.com/in/siddhi-patil-11220432b/")
                5. [Sanika Ghodake]("https://www.linkedin.com/in/sanika-ghodake-80820432b/")
                6. [Apurva Bhosale]("https://www.linkedin.com/in/apurva-bhosale-4349b632a/")
            """)

    # Area type input
    area_type = st.selectbox('Select Area Type?', [
        'Super built-up  Area', 'Built-up  Area', 'Plot  Area', 'Carpet  Area'
    ])
    area_type_mapping = {
        'Super built-up  Area': 0,
        'Built-up  Area': 1,
        'Plot  Area': 2,
        'Carpet  Area': 3
    }
    area_type_no = area_type_mapping.get(area_type, 0)

    # User inputs as strings
    size_input = st.text_input('Enter BHK Size:', '')
    total_sqft_input = st.text_input('Enter Total Sqft Size:', '')
    bath_input = st.text_input('Enter Number of Bathrooms:', '')
    balcony_input = st.text_input('Enter Number of Balconies:', '')
    price_input = st.text_input('Enter Price per Sqft:', '')

    # Location input
    location = st.selectbox('Select Location Type?', [
        'Rajarampuri', 'Ruikar colony', 'Tarabai park', 'Nagala park',
        'Mangalwar peth', 'Ch.shivaji peth', 'Mahadwar road', 'R.K nagar',
        'NCC bhavan road', 'Uttareshwar peth', 'Other'
    ])
    location_mapping = {
        'Other': 0, 'Rajarampuri': 1, 'Ruikar colony': 2, 'Tarabai park': 3,
        'Nagala park': 4, 'Magalwar peth': 5, 'Ch.shivaji peth': 6,
        'Mahadwar road': 7, 'R.K nagar': 8, 'NCC bhavan road': 9,
        'Uttareshwar peth': 10
    }
    location_no = location_mapping.get(location, 0)

    # Prediction logic
    if st.button("Predict"):
        if not all([size_input, total_sqft_input, bath_input, balcony_input, price_input]):
            st.error("⚠️ Please fill in all fields.")
            return

        try:
            size = float(size_input)
            total_sqft = float(total_sqft_input)
            bath = int(bath_input)
            balcony = int(balcony_input)
            price_per_sqft = float(price_input)

            result = perdicton_price(area_type_no, size, total_sqft, bath, balcony, price_per_sqft, location_no)
            if result is not None:
                st.success(f'🏡 The predicted price is ₹{round(result, 2)} Lakh(s)')
        except ValueError:
            st.error("❌ Invalid input: please enter only numeric values.")

# Run the app
if __name__ == '__main__':
    main()
