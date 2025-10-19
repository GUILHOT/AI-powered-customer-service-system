#!/usr/bin/env python3
import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st
from openai import OpenAI

# Load environment variables
load_dotenv(find_dotenv())
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ Missing OPENAI_API_KEY in .env file")
    st.stop()

client = OpenAI(api_key=api_key)

# === UTILS ===
def clean_response(text):
    """Remove markdown like *italic* and **bold**"""
    import re
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    return text.strip()

def moderate_content(text):
    """Check for inappropriate content using OpenAI Moderation API"""
    try:
        response = client.moderations.create(input=text)
        result = response.results[0]
        return result.flagged, result.categories
    except Exception:
        return False, {}

# === CORE LOGIC ===
def get_products_and_category():
    return {
        # Smartphones (6)
        "smartx pro phone": {
            "name": "SmartX Pro Phone",
            "price": "$899",
            "features": ["6.1-inch display", "128GB storage", "Triple camera system", "5G enabled", "All-day battery life"],
            "description": "Premium smartphone perfect for photography and productivity"
        },
        "pixelview ultra": {
            "name": "PixelView Ultra",
            "price": "$749",
            "features": ["6.7-inch OLED", "256GB storage", "AI-enhanced camera", "Fast charging", "Water resistant"],
            "description": "Flagship phone with AI-powered photography"
        },
        "ecophone lite": {
            "name": "EcoPhone Lite",
            "price": "$399",
            "features": ["5.8-inch display", "64GB storage", "Dual camera", "All-day battery", "Eco-friendly materials"],
            "description": "Affordable and sustainable smartphone"
        },
        "galaxy s24": {
            "name": "Samsung Galaxy S24",
            "price": "$799",
            "features": ["6.2-inch AMOLED", "128GB storage", "AI camera", "5G", "IP68 water resistance"],
            "description": "Latest flagship from Samsung with AI features"
        },
        "iphone 16": {
            "name": "iPhone 16",
            "price": "$999",
            "features": ["6.3-inch Super Retina XDR", "256GB storage", "A18 chip", "Cinematic mode", "MagSafe"],
            "description": "Apple's latest innovation for power users"
        },
        "oneplus 12": {
            "name": "OnePlus 12",
            "price": "$699",
            "features": ["6.8-inch Fluid AMOLED", "512GB storage", "Snapdragon 8 Gen 3", "Hasselblad camera", "100W fast charge"],
            "description": "Flagship killer with premium specs at a value price"
        },
        # Cameras (6)
        "fotosnap dslr": {
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
        "actioncam pro": {
            "name": "ActionCam Pro",
            "price": "$299",
            "features": ["4K video", "Waterproof up to 30m", "Image stabilization", "Voice control", "Long battery life"],
            "description": "Rugged action camera for adventures and sports"
        },
        "mirrorless pro": {
            "name": "Mirrorless Pro X",
            "price": "$1,499",
            "features": ["33MP sensor", "8K video", "In-body stabilization", "Touchscreen", "Pro lenses support"],
            "description": "Next-gen mirrorless for pros and enthusiasts"
        },
        "vlog cam": {
            "name": "Vlog Cam Mini",
            "price": "$499",
            "features": ["16MP sensor", "Flip screen", "Audio input", "Live streaming", "Lightweight"],
            "description": "Perfect for content creators and vloggers"
        },
        "drone cam": {
            "name": "SkyDrone 4K",
            "price": "$899",
            "features": ["4K aerial video", "GPS tracking", "Obstacle avoidance", "30min flight time", "App control"],
            "description": "Capture stunning aerial shots with ease"
        },
        # TVs (6)
        "tcl 55 tv": {
            "name": "TCL 55-inch Smart TV",
            "price": "$649",
            "features": ["4K Ultra HD", "HDR support", "Smart TV platform", "Multiple HDMI ports", "Voice remote"],
            "description": "Large screen smart TV with crystal clear picture quality"
        },
        "samsung qled": {
            "name": "Samsung 65-inch QLED TV",
            "price": "$1,199",
            "features": ["QLED technology", "8K upscaling", "Voice control", "Gaming mode", "Ambient mode"],
            "description": "Premium TV with quantum dot technology and smart features"
        },
        "budgetview 43": {
            "name": "BudgetView 43-inch HD TV",
            "price": "$299",
            "features": ["Full HD", "Built-in streaming apps", "Slim design", "Energy efficient", "Easy setup"],
            "description": "Affordable HD TV for small spaces"
        },
        "oled 55": {
            "name": "UltraOLED 55-inch",
            "price": "$899",
            "features": ["OLED panel", "True Black", "Dolby Vision", "Game Mode", "Thin bezel"],
            "description": "Immersive viewing experience with perfect contrast"
        },
        "gaming tv": {
            "name": "GameMaster 65-inch",
            "price": "$1,099",
            "features": ["120Hz refresh", "HDMI 2.1", "VRR", "Low input lag", "G-Sync compatible"],
            "description": "The ultimate gaming TV for competitive players"
        },
        "smart tv 75": {
            "name": "SmartHub 75-inch",
            "price": "$1,399",
            "features": ["75-inch 4K", "Voice assistant", "Multi-room audio", "USB-C input", "Wall-mount ready"],
            "description": "Big screen entertainment center for your living room"
        },
        # Watches (6)
        "watch pro": {
            "name": "Watch Pro Series",
            "price": "$399",
            "features": ["Always-on display", "ECG monitor", "Sleep tracking", "GPS", "5-day battery"],
            "description": "Advanced health and fitness tracker with premium design"
        },
        "sport watch": {
            "name": "SportFit Watch",
            "price": "$199",
            "features": ["Heart rate monitor", "Run tracking", "Water resistant", "Customizable faces", "7-day battery"],
            "description": "Perfect for athletes and active lifestyles"
        },
        "kids watch": {
            "name": "KidSafe Watch",
            "price": "$99",
            "features": ["GPS location", "Emergency call", "Parental controls", "Durable case", "10-day battery"],
            "description": "Safe and fun wearable for children"
        },
        "luxury watch": {
            "name": "EliteTime Luxury",
            "price": "$899",
            "features": ["Stainless steel", "Sapphire glass", "Wireless charging", "Premium leather strap", "Limited edition"],
            "description": "Luxury smartwatch that combines style and technology"
        },
        "fitness band": {
            "name": "FitBand Plus",
            "price": "$49",
            "features": ["Step counter", "Calorie tracker", "Sleep analysis", "Water resistant", "30-day battery"],
            "description": "Affordable fitness tracker for everyday use"
        },
        "smart band": {
            "name": "SmartBand X",
            "price": "$79",
            "features": ["Notifications", "Music control", "Activity reminders", "Color screen", "5-day battery"],
            "description": "Smart band with advanced features at an entry-level price"
        },
        # Tablets (6)
        "tablet pro": {
            "name": "Tablet Pro 12.9",
            "price": "$899",
            "features": ["12.9-inch display", "M2 chip", "Pencil support", "Face ID", "5G connectivity"],
            "description": "Professional-grade tablet for creatives and professionals"
        },
        "edu tablet": {
            "name": "EduTab 10.5",
            "price": "$349",
            "features": ["10.5-inch display", "Kids mode", "Parental controls", "Durable case", "10-hour battery"],
            "description": "Perfect for students and educational use"
        },
        "budget tablet": {
            "name": "BudgetPad 8",
            "price": "$149",
            "features": ["8-inch display", "Basic apps", "Lightweight", "Long battery", "Simple interface"],
            "description": "Affordable tablet for casual browsing and media"
        },
        "gaming tablet": {
            "name": "GamePad 11",
            "price": "$599",
            "features": ["11-inch high refresh", "Game controller support", "Stereo speakers", "Cooling fan", "Fast charging"],
            "description": "Powerful tablet designed for mobile gaming"
        },
        "creative tablet": {
            "name": "ArtPad 10",
            "price": "$499",
            "features": ["10-inch pen display", "Pressure sensitivity", "Drawing apps", "Color accuracy", "Lightweight"],
            "description": "Ideal for artists and designers on the go"
        },
        "business tablet": {
            "name": "BizPad 10.2",
            "price": "$549",
            "features": ["Office suite", "Security features", "Fingerprint login", "Corporate MDM", "Stylus included"],
            "description": "Secure and productive tablet for business users"
        },
        # Aliases
        "phone": {"name": "Phone Selection", "price": "From $399", "features": [], "description": "We offer EcoPhone Lite ($399), PixelView Ultra ($749), and SmartX Pro ($899)"},
        "camera": {"name": "Camera Selection", "price": "From $299", "features": [], "description": "We offer ActionCam Pro ($299), FotoSnap Compact ($599), and DSLR ($1,299)"},
        "tv": {"name": "TV Selection", "price": "From $299", "features": [], "description": "We offer BudgetView 43\" ($299), TCL 55\" ($649), and Samsung QLED ($1,199)"},
        "watch": {"name": "Watch Selection", "price": "From $49", "features": [], "description": "We offer FitBand Plus ($49), SportFit Watch ($199), and Watch Pro ($399)"},
        "tablet": {"name": "Tablet Selection", "price": "From $149", "features": [], "description": "We offer BudgetPad 8 ($149), EduTab 10.5 ($349), and Tablet Pro 12.9 ($899)"},
        "phones": {"name": "Phone Selection", "price": "From $399", "features": [], "description": "We offer EcoPhone Lite ($399), PixelView Ultra ($749), and SmartX Pro ($899)"},
        "cameras": {"name": "Camera Selection", "price": "From $299", "features": [], "description": "We offer ActionCam Pro ($299), FotoSnap Compact ($599), and DSLR ($1,299)"},
        "tvs": {"name": "TV Selection", "price": "From $299", "features": [], "description": "We offer BudgetView 43\" ($299), TCL 55\" ($649), and Samsung QLED ($1,199)"},
        "watches": {"name": "Watch Selection", "price": "From $49", "features": [], "description": "We offer FitBand Plus ($49), SportFit Watch ($199), and Watch Pro ($399)"},
        "tablets": {"name": "Tablet Selection", "price": "From $149", "features": [], "description": "We offer BudgetPad 8 ($149), EduTab 10.5 ($349), and Tablet Pro 12.9 ($899)"},
    }

def find_category_and_product_only(user_input, products_dict):
    user_input = user_input.lower()
    matched_products = []
    for key, info in products_dict.items():
        if (key in user_input or 
            any(word in user_input for word in key.split()) or
            any(word in user_input for word in info["name"].lower().split())):
            matched_products.append(info)
    seen = set()
    unique = []
    for p in matched_products:
        if p["name"] not in seen:
            seen.add(p["name"])
            unique.append(p)
    return unique

def generate_product_information(matched_products):
    if not matched_products:
        return "I don't see any specific products matching your request, but I can tell you about our full inventory of phones, cameras, TVs, watches, and tablets."
    return "\n\n".join([
        f"{p['name']} - {p['price']}\nDescription: {p['description']}\nKey Features: {', '.join(p['features'])}"
        for p in matched_products
    ])

def process_user_message(user_input, all_messages, debug=False):
    # STEP 1: Input Moderation
    input_flagged, _ = moderate_content(user_input)
    if input_flagged:
        return "I'm sorry, but I can't assist with that type of request. Please ask about our products in a respectful manner.", all_messages

    products = get_products_and_category()
    matched = find_category_and_product_only(user_input, products)
    product_info = generate_product_information(matched)

    system_msg = f"""
You are Sarah, a knowledgeable sales representative at TechStore Electronics.

SPECIFIC PRODUCTS WE HAVE IN STOCK:
{product_info}

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
    
    messages = [{'role': 'system', 'content': system_msg}]
    
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

# === STREAMLIT UI ===
st.set_page_config(
    page_title="TechStore Electronics - Customer Service", 
    page_icon="",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #fafafa;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
[data-testid="stSidebar"] {
    background-color: #1a1c24;
    border-right: 1px solid #333;
}
[data-testid="stSidebar"] * {
    color: #fafafa;
}
.main-header {
    text-align: center;
    color: #2E86AB;
    border-bottom: 2px solid #2E86AB;
    padding-bottom: 10px;
    margin-bottom: 20px;
    font-size: 28px;
    font-weight: bold;
}
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin-top: 20px;
}
.user-message {
    background-color: #1E90FF;
    color: white;
    padding: 14px 18px;
    border-radius: 16px;
    max-width: 70%;
    align-self: flex-start;
    text-align: left;
    word-wrap: break-word;
    font-weight: 500;
}
.bot-message {
    background-color: #32CD32;
    color: white;
    padding: 14px 18px;
    border-radius: 16px;
    max-width: 70%;
    align-self: flex-end;
    text-align: left;
    word-wrap: break-word;
    font-weight: 500;
}
.message-label {
    font-weight: bold;
    margin-bottom: 4px;
    display: block;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">TechStore Electronics - Customer Service</h1>', unsafe_allow_html=True)
st.markdown(" ")
st.markdown(" ")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input state management
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

# Sidebar
with st.sidebar:
    st.markdown("<h2 style='color:#2E86AB;'>TechStore Electronics</h2>", unsafe_allow_html=True)
    st.markdown("**AI-Powered Customer Service**")
    
    st.markdown("---")
    st.subheader("Need Help?")
    st.caption("Click any product below or ask questions like:")
    st.markdown("- \"What phones do you have?\"")
    st.markdown("- \"Which tablet is best for students?\"")
    
    st.markdown("---")
    st.subheader("Our Products")

    categories = {
        "Smartphones": [
            "SmartX Pro Phone", "PixelView Ultra", "EcoPhone Lite",
            "Samsung Galaxy S24", "iPhone 16", "OnePlus 12"
        ],
        "Cameras": [
            "FotoSnap DSLR Camera", "FotoSnap Compact Camera", "ActionCam Pro",
            "Mirrorless Pro X", "Vlog Cam Mini", "SkyDrone 4K"
        ],
        "Televisions": [
            "TCL 55-inch Smart TV", "Samsung 65-inch QLED TV", "BudgetView 43-inch HD TV",
            "UltraOLED 55-inch", "GameMaster 65-inch", "SmartHub 75-inch"
        ],
        "Watches": [
            "Watch Pro Series", "SportFit Watch", "KidSafe Watch",
            "EliteTime Luxury", "FitBand Plus", "SmartBand X"
        ],
        "Tablets": [
            "Tablet Pro 12.9", "EduTab 10.5", "BudgetPad 8",
            "GamePad 11", "ArtPad 10", "BizPad 10.2"
        ]
    }

    for category, product_list in categories.items():
        with st.expander(category):
            for product_name in product_list:
                if st.button(f"• {product_name}", key=f"ask_{product_name}", use_container_width=True):
                    st.session_state.suggested_input = f"Tell me about the {product_name}."
                    st.session_state.input_key += 1  # Force reset on next load
                    st.rerun()

    st.markdown("---")
    st.markdown("**🔗 [View Project on GitHub](https://github.com/GUILHOT/Build-an-End-to-End-System---Evaluation)**")

# Input field with dynamic key to force reset
with st.container():
    col1, col2 = st.columns([4, 1])
    with col1:
        initial_value = st.session_state.get("suggested_input", "")
        user_input = st.text_input(
            "Ask Sarah about our products:",
            value=initial_value,
            placeholder="Votre message",
            key=f"user_input_{st.session_state.input_key}",
            label_visibility="collapsed"
        )
    with col2:
        send_button = st.button("Send", type="primary", use_container_width=True)

# Process message
if send_button and user_input.strip():
    with st.spinner("Sarah is helping you..."):
        response, updated_messages = process_user_message(
            user_input, 
            st.session_state.messages, 
            debug=False
        )
    st.session_state.messages = updated_messages
    
    # Clear input by incrementing key → forces new widget
    if "suggested_input" in st.session_state:
        del st.session_state.suggested_input
    st.session_state.input_key += 1
    st.rerun()

# Display chat
if st.session_state.messages:
    st.markdown("### 💬 Conversation")
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f'<div class="chat-container"><div class="user-message"><span class="message-label">Vous:</span>{msg["content"]}</div></div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="chat-container"><div class="bot-message"><span class="message-label">Sarah:</span>{msg["content"]}</div></div>',
                unsafe_allow_html=True
            )
else:
    st.markdown("""
### 👋 Hello, I'm Sarah!
I'm your personal shopping assistant at TechStore.  
I’ll help you find the **right tech product** — whether you’re comparing phones, need a camera under $500, or want the best TV for gaming.  
Just ask me anything — I know every detail about our products, and I’m here to give you honest, clear advice.
""")

# Footer
st.markdown("---")
st.markdown("*TechStore Electronics - Your Technology Partner* © 2025")