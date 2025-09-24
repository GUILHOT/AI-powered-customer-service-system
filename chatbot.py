#!/usr/bin/env python3
import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st
from openai import OpenAI

# Load environment variables
load_dotenv(find_dotenv())
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Real OpenAI function
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0.7, max_tokens=500):
    """Get actual response from OpenAI API"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"I apologize, but I'm experiencing technical difficulties. Please try again in a moment."

# Enhanced product database with detailed information
def get_products_and_category():
    return {
        "smartx pro phone": {
            "name": "SmartX Pro Phone",
            "price": "$899",
            "features": ["6.1-inch display", "128GB storage", "Triple camera system", "5G enabled", "All-day battery life"],
            "description": "Premium smartphone perfect for photography and productivity"
        },
        "fotosnap camera": {
            "name": "FotoSnap DSLR Camera", 
            "price": "$1,299",
            "features": ["24.2MP sensor", "4K video recording", "Weather sealed body", "Dual card slots", "Professional lens mount"],
            "description": "Professional DSLR camera for serious photographers"
        },
        "fotosnap compact": {
            "name": "FotoSnap Compact Camera",
            "price": "$599", 
            "features": ["20MP sensor", "10x optical zoom", "WiFi connectivity", "Compact design", "Image stabilization"],
            "description": "Portable camera with professional features in a compact body"
        },
        "dslr": {
            "name": "FotoSnap DSLR Camera",
            "price": "$1,299", 
            "features": ["24.2MP sensor", "4K video recording", "Weather sealed body", "Dual card slots", "Professional lens mount"],
            "description": "Professional DSLR camera for serious photographers"
        },
        "tcl tv": {
            "name": "TCL 55-inch Smart TV",
            "price": "$649",
            "features": ["4K Ultra HD", "HDR support", "Smart TV platform", "Multiple HDMI ports", "Voice remote"],
            "description": "Large screen smart TV with crystal clear picture quality"
        },
        "samsung tv": {
            "name": "Samsung 65-inch QLED TV", 
            "price": "$1,199",
            "features": ["QLED technology", "8K upscaling", "Voice control", "Gaming mode", "Ambient mode"],
            "description": "Premium TV with quantum dot technology and smart features"
        },
        "tv": {
            "name": "TV Selection",
            "price": "Starting at $649", 
            "features": ["Multiple sizes available", "4K and QLED options", "Smart TV features", "HDR support"],
            "description": "We offer TCL 55-inch Smart TV ($649) and Samsung 65-inch QLED TV ($1,199)"
        },
        "tvs": {
            "name": "TV Selection",
            "price": "Starting at $649",
            "features": ["Multiple sizes available", "4K and QLED options", "Smart TV features", "HDR support"], 
            "description": "We offer TCL 55-inch Smart TV ($649) and Samsung 65-inch QLED TV ($1,199)"
        }
    }

# Enhanced product matching function
def find_category_and_product_only(user_input, products_dict):
    user_input = user_input.lower()
    matched_products = []
    
    # Check for exact matches and partial matches
    for product_key, product_info in products_dict.items():
        if (product_key.lower() in user_input or 
            any(word in user_input for word in product_key.split()) or
            any(word in user_input for word in product_info["name"].lower().split())):
            matched_products.append(product_info)
    
    # Remove duplicates while preserving order
    seen = set()
    unique_products = []
    for product in matched_products:
        product_key = product["name"]
        if product_key not in seen:
            seen.add(product_key)
            unique_products.append(product)
    
    return unique_products if unique_products else []

# Generate detailed product information string
def generate_product_information(matched_products):
    if not matched_products:
        return "I don't see any specific products matching your request, but I can tell you about our full inventory of phones, cameras, and TVs."
    
    product_details = []
    for product in matched_products:
        detail = f"""
{product['name']} - {product['price']}
Description: {product['description']}
Key Features: {', '.join(product['features'])}
"""
        product_details.append(detail.strip())
    
    return "\n\n".join(product_details)

# Main processing function with enhanced product context
def process_user_message(user_input, all_messages, debug=False):
    if debug: print("Step 1: Input passed moderation check.")
    
    # Get products and find matches
    products_dict = get_products_and_category()
    matched_products = find_category_and_product_only(user_input, products_dict)
    if debug: print("Step 2: Extracted list of products.")

    # Generate detailed product information
    product_information = generate_product_information(matched_products)
    if debug: print("Step 3: Looked up product information.")

    # Create comprehensive system message
    system_message = f"""
You are Sarah, a knowledgeable sales representative at TechStore Electronics.

SPECIFIC PRODUCTS WE HAVE IN STOCK:
{product_information}

YOUR ROLE:
- You are a human employee working in our physical store
- You have these exact products available for purchase
- You know all the details, prices, and features listed above
- You help customers find the perfect product for their needs

RESPONSE GUIDELINES:
- Always mention specific product names and exact prices from our inventory
- Highlight key features that match customer needs
- Ask relevant follow-up questions to better help customers
- Compare products when customers are deciding between options
- Be enthusiastic about our products while being honest about their capabilities
- Never say "I don't have inventory" or mention being an AI

CONVERSATION STYLE:
- Friendly and professional
- Product-focused and helpful  
- Ask questions to understand customer needs better
- Provide specific recommendations with reasons why

When customers ask about products, reference our exact inventory with names, prices, and features.
"""
    
    # Build conversation context
    messages = [{'role': 'system', 'content': system_message}]
    
    # Add conversation history
    for msg in all_messages:
        messages.append(msg)
    
    # Add current user input
    messages.append({'role': 'user', 'content': user_input})

    # Get response from OpenAI
    final_response = get_completion_from_messages(messages)
    if debug: print("Step 4: Generated response to user question.")
    
    # Update conversation history
    updated_messages = all_messages + [
        {'role': 'user', 'content': user_input},
        {'role': 'assistant', 'content': final_response}
    ]
    
    return final_response, updated_messages

# Streamlit UI Configuration
st.set_page_config(
    page_title="TechStore Electronics - Customer Service", 
    page_icon="🏪",
    layout="wide"
)

# Custom CSS for better appearance
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E86AB;
        border-bottom: 2px solid #2E86AB;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .chat-message {
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .user-message {
        background-color: #E8F4FD;
        text-align: right;
    }
    .assistant-message {
        background-color: #F0F2F6;
        text-align: left;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🏪 TechStore Electronics - Customer Service</h1>', unsafe_allow_html=True)
st.markdown("**Welcome to TechStore Electronics!** I'm Sarah, your personal shopping assistant. Ask me about our phones, cameras, and TVs!")

# Sidebar with product information
with st.sidebar:
    st.header("🛍️ Our Products")
    st.markdown("""
    **📱 Smartphones:**
    - SmartX Pro Phone - $899
    
    **📸 Cameras:** 
    - FotoSnap DSLR Camera - $1,299
    - FotoSnap Compact Camera - $599
    
    **📺 TVs:**
    - TCL 55-inch Smart TV - $649
    - Samsung 65-inch QLED TV - $1,199
    """)
    
    st.markdown("---")
    st.markdown("**💡 Try asking:**")
    st.markdown("- 'What phones do you have?'")
    st.markdown("- 'I need a camera for travel'") 
    st.markdown("- 'Show me your TVs'")
    st.markdown("- 'What's your cheapest option?'")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
with st.container():
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_input(
            "Ask me about our products:", 
            key="user_input", 
            placeholder="Hi! What products are you looking for today?",
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.button("Send", type="primary", use_container_width=True)

# Process message when send is clicked
if send_button and user_input.strip():
    # Process the message
    with st.spinner("Sarah is helping you..."):
        response, updated_messages = process_user_message(
            user_input, 
            st.session_state.messages, 
            debug=False
        )
    
    # Update session state
    st.session_state.messages = updated_messages
    
    # Rerun to show new message
    st.rerun()

# Display chat history
if st.session_state.messages:
    st.markdown("### 💬 Conversation")
    
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>You:</strong> {msg['content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message assistant-message">
                <strong>Sarah (TechStore):</strong> {msg['content']}
            </div>
            """, unsafe_allow_html=True)
else:
    # Welcome message when no conversation yet
    st.markdown("### 👋 Welcome!")
    st.info("Hi! I'm Sarah from TechStore Electronics. I'm here to help you find the perfect phone, camera, or TV. What are you looking for today?")

# Footer
st.markdown("---")
st.markdown("*TechStore Electronics - Your Technology Partner* 📱📸📺")