import streamlit as st

# Set up the Streamlit page configuration
st.set_page_config(page_title="Open Data Platform Mockup", layout="wide")

# Function to set the page
def set_page(page):
    st.session_state["page"] = page

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to", 
    ["Landing Page", "Data Catalog", "Login"]
)

# Landing Page
if page == "Landing Page":
    st.title("Welcome to the Open Data Platform")
    st.subheader("Your gateway to open and accessible data")

    st.image("https://via.placeholder.com/1200x400?text=Open+Data+Platform", use_column_width=True)

    st.write("### Search Datasets")
    search_query = st.text_input("Search datasets...", "")
    st.button("Explore Data")

    st.write("## Featured Datasets")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://via.placeholder.com/300?text=Dataset+1")
        st.write("UB BUS ")
        st.write("A brief description of UB BUS data.")
    with col2:
        st.image("https://via.placeholder.com/300?text=Dataset+2")
        st.write("Dataset 2")
        st.write("A brief description of Dataset 2.")
    with col3:
        st.image("https://via.placeholder.com/300?text=Dataset+3")
        st.write("Dataset 3")
        st.write("A brief description of Dataset 3.")

    st.write("## How It Works/User manual")
    st.write("1. **Search** for datasets using keywords.")
    st.write("2. **Analyze and visualize** data easily.")
    st.write("3. **Download or share** your insights.")

    st.write("## Testimonials")
    st.write("> This platform has revolutionized the way we access and use data. - User A")
    st.write("> An invaluable resource for our research projects. - User B")

    st.write("## Bottom of page")

    st.write("- Links to terms of use")
    st.write("- privacy policy")
    st.write("- help center")
    st.write("- social media")
    st.write("- Accessibility")

    

# Data Catalog
elif page == "Data Catalog":
    st.title("Data Catalog")
    st.write("Browse and discover datasets")

    search_query = st.text_input("Search datasets...", "")
    st.button("Search")

    st.write("### Filters")
    st.selectbox("Category", ["Health", "Environment", "Education", "Finance", "Other"])
    st.date_input("Date range")
    st.multiselect("Data format", ["CSV", "JSON", "XML", "Other"])
    st.text_input("Tags")

    st.write("### Dataset List")
    st.write("1. **Dataset 1** - A brief description of Dataset 1.")
    st.write("2. **Dataset 2** - A brief description of Dataset 2.")
    st.write("3. **Dataset 3** - A brief description of Dataset 3.")
    st.write("4. **Dataset 4** - A brief description of Dataset 4.")
    st.write("5. **Dataset 5** - A brief description of Dataset 5.")

# Login
elif page == "Login":
    st.title("Login")

    login_option = st.selectbox("Select Role", ["Admin", "Data Provider"])

    if login_option == "Admin":
        st.title("Admin Dashboard")
        st.write("Manage the platform")

        st.write("## User Management Console")
        st.write("1. **User 1** - Admin - [Edit] [Delete]")
        st.write("2. **User 2** - Data Provider - [Edit] [Delete]")
        st.write("3. **User 3** - Data User - [Edit] [Delete]")

        st.write("## System Monitoring and Logging")
        st.write("System health: Good")
        st.write("Logs: [View Logs]")

        st.write("## Backup and Disaster Recovery")
        st.write("[Initiate Backup] [Restore Backup]")

        st.write("## Role-Based Access Control")
        st.write("Manage roles and permissions for users")

        st.write("## Audit Trail for Administrative Actions")
        st.write("1. User 1 - Changed role of User 2 - 2023-07-01")
        st.write("2. User 3 - Deleted Dataset 4 - 2023-06-28")

    elif login_option == "Data Provider":
        st.title("Data Provider Dashboard")
        st.write("Upload and manage your datasets")

        st.write("## Upload Data")
        st.text_input("Dataset title")
        st.text_area("Description")
        st.text_input("Tags")
        st.file_uploader("Upload file", type=["csv", "json", "xml"])
        st.button("Submit")

        st.write("## My Datasets")
        st.write("1. **Dataset 1** - Published - Last updated: 2023-07-01 [Edit] [Delete]")
        st.write("2. **Dataset 2** - Draft - Last updated: 2023-06-15 [Edit] [Delete]")
        st.write("3. **Dataset 3** - Published - Last updated: 2023-05-20 [Edit] [Delete]")

        st.write("## Metadata Management System")
        st.write("Manage metadata for your datasets to provide context")

        st.write("## Data Validation Tools")
        st.write("Validate your datasets before publishing to ensure data quality")

        st.write("## Privacy Controls and Data Masking")
        st.write("Understand and manage privacy controls and data masking options for sensitive information")
