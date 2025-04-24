import streamlit as st
from transformers import AutoTokenizer
import random
from PIL import Image
import numpy as np



# Set page configuration
st.set_page_config(
    page_title="Tokenizer Playground",
    layout="centered"
)

st.markdown("""
    <style>
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the tokenizer
@st.cache_resource
def load_tokenizer():
    return AutoTokenizer.from_pretrained("bert-base-uncased")

tokenizer = load_tokenizer()

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def get_text_color(bg_hex):
    r = int(bg_hex[1:3], 16)
    g = int(bg_hex[3:5], 16)
    b = int(bg_hex[5:7], 16)
    luma = 0.299 * r + 0.587 * g + 0.114 * b
    return "black" if luma > 150 else "white"

def highlight_tokens(raw_text):
    if not raw_text.strip():
        return "", 0, 0

    encoded = tokenizer.encode_plus(raw_text, return_offsets_mapping=True, add_special_tokens=False)
    tokens = tokenizer.convert_ids_to_tokens(encoded["input_ids"])
    offsets = encoded["offset_mapping"]

    # Create a mapping of character indices to their token index and color
    char_to_token = {}
    colors = {}

    for idx, (start, end) in enumerate(offsets):
        token_color = random_color()
        colors[idx] = token_color
        for char_idx in range(start, end):
            if char_idx < len(raw_text):
                char_to_token[char_idx] = idx

    # Create HTML to highlight tokens
    html_parts = []
    for i, char in enumerate(raw_text):
        if i in char_to_token:
            token_idx = char_to_token[i]
            bg_color = colors[token_idx]
            text_color = get_text_color(bg_color)
            html_parts.append(f'<span style="background-color: {bg_color}; color: {text_color};">{char}</span>')
        else:
            html_parts.append(char)

    highlighted_html = ''.join(html_parts)
    return highlighted_html, len(tokens), len(raw_text)

# Header with icon and title

try:
    # Try to load the icon
    icon = Image.open("header.png")
    st.image(icon, use_container_width=True)
except FileNotFoundError:
    # Use a placeholder icon
    st.title("Tokenizer Playground")

st.caption("Using BERT Tokenizer (bert-base-uncased)")

# Input text area
text_input = st.text_area("Enter text:", height=150)

if st.button("Analyze"):
    if text_input:
        highlighted_text, token_count, char_count = highlight_tokens(text_input)

        # Display KPIs
        st.markdown("""
            <div style="display: flex; justify-content: center; gap: 40px; margin-top: 20px;">
                <div style="background-color: #000000; padding: 20px; border-radius: 10px; text-align: center; min-width: 120px; width: 200px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                    <h4 style="margin: 0; font-size: 16px;">TOKENS</h4>
                    <p style="margin: 2px 0 0; font-size: 34px; font-weight: bold;">{}</p>
                </div>
                <div style="background-color: #000000; padding: 20px; border-radius: 10px; text-align: center; min-width: 120px; width: 200px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                    <h4 style="margin: 0; font-size: 16px;">CHARACTERS</h4>
                    <p style="margin: 5px 0 0; font-size: 34px; font-weight: bold;">{}</p>
                </div>
            </div>
        """.format(token_count, char_count), unsafe_allow_html=True)

        # Display highlighted tokens
        st.markdown("### Result:")
        st.markdown(f'<div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px;">{highlighted_text}</div>', unsafe_allow_html=True)
    else:
        # st.warning("Please enter some text to analyze.")
        pass
