import streamlit as st
import os

# Set page config
st.set_page_config(page_title="Quote Manager", page_icon="💬")

# File operations
QUOTES_FILE = "quotes.txt"

# Initialize with default quotes if file doesn't exist
DEFAULT_QUOTES = [
    "Jaun Elia: Har ik baat pe kehte ho tum ki tu kya hai, tumhi kaho ki yeh andaaz-e-guftagu kya hai",
    "Ahmed Faraz: Mohabbat karne waale kam na honge, teri mehfil mein lekin hum na honge",
    "Parveen Shakir: Khushboo ki tarah tum mere paas raho, hawa ke jhonke mein kahin kho na jao",
    "Allama Iqbal: Khudi ko kar buland itna ke har taqdeer se pehle, khuda bande se khud pooche bata teri raza kya hai",
    "Mirza Ghalib: Ishq par zor nahin hai ye woh aatish Ghalib, jo lagaye na lage aur bujhaye na bane"
]

def initialize_quotes_file():
    """Create file with default quotes if it doesn't exist"""
    if not os.path.exists(QUOTES_FILE):
        with open(QUOTES_FILE, "w") as f:
            for quote in DEFAULT_QUOTES:
                f.write(quote + "\n")

def save_quote(name, quote):
    """Save quote to file"""
    with open(QUOTES_FILE, "a") as f:
        f.write(f"{name}: {quote}\n")

def get_all_quotes():
    """Read all quotes from file"""
    initialize_quotes_file()  # Ensure file exists
    with open(QUOTES_FILE, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def search_quotes(search_term):
    """Search quotes by name or content"""
    quotes = get_all_quotes()
    search_term = search_term.lower()
    return [q for q in quotes if search_term in q.lower()]

# Streamlit UI
st.title("💬 Quote Manager")
st.write("Manage your favorite quotes")

# Initialize session state
if 'quotes' not in st.session_state:
    st.session_state.quotes = get_all_quotes()

# Sidebar navigation
menu = st.sidebar.radio(
    "Menu",
    ["Add Quote", "View All Quotes", "Search Quotes", "Delete Quotes"]
)

if menu == "Add Quote":
    st.header("Add New Quote")
    with st.form("quote_form"):
        name = st.text_input("Author Name")
        quote = st.text_area("Quote Text")
        submitted = st.form_submit_button("Save Quote")
        
        if submitted:
            if name and quote:
                save_quote(name, quote)
                st.session_state.qu