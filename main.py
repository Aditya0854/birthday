import streamlit as st
import os
import random
import requests
import base64
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="wide")

# --- ASSETS & SETUP ---
def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=3)
        if r.status_code != 200: return None
        return r.json()
    except: return None

# Animations
lottie_welcome = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_pwohahvd.json")
lottie_celebrate = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_teqkxj.json")

# Tenor GIF Embed
CAKE_EMBED_HTML = """
<div class="tenor-gif-embed" data-postid="15376044898665823571" data-share-method="host" data-aspect-ratio="1" data-width="100%">
    <a href="https://tenor.com/view/happy-cute-fun-party-celebrate-gif-15376044898665823571">Happy Cute Sticker</a>
    from <a href="https://tenor.com/search/happy-stickers">Happy Stickers</a>
</div> 
<script type="text/javascript" async src="https://tenor.com/embed.js"></script>
"""

# Quotes
quotes = [
    "To the best brother ever! 🌟",
    "Thanks for being my personal bodyguard. 🛡️",
    "You're not old, you're just... vintage. 🍷",
    "Mom loves me more, but I love you anyway. 😜",
    "Happy Birthday to my partner in crime! 🚀",
    "Cheers to another year of being awesome! 🥂"
]

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Fredoka+One&family=Delius&display=swap');
    
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
    }
    .title-text {
        font-family: 'Pacifico', cursive;
        font-size: 8vw;
        color: white;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        margin: 0;
        line-height: 1.2;
    }
    .subtitle-text {
        font-family: 'Fredoka One', cursive;
        font-size: 2vw;
        color: #FFF;
        letter-spacing: 2px;
    }
    .stButton>button {
        font-family: 'Fredoka One', cursive;
        font-size: 24px;
        background-image: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
        color: #555;
        border: none;
        border-radius: 50px;
        padding: 15px 50px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
        animation: pulse 2s infinite;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        color: #333;
    }
    @keyframes pulse {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.7); }
        70% { transform: scale(1.05); box-shadow: 0 0 0 10px rgba(255, 255, 255, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0); }
    }
    
    /* Image Styling */
    div[data-testid="stImage"] img {
        border: 12px solid white;
        border-bottom: 30px solid white;
        border-radius: 5px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        transition: all 0.3s ease;
    }
    div[data-testid="stImage"] img:hover {
        transform: scale(1.05);
        z-index: 10;
    }

    /* Video Styling Container */
    .video-container {
        border: 12px solid white;
        border-bottom: 30px solid white;
        border-radius: 5px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        overflow: hidden;
        transition: all 0.3s ease;
    }
    .video-container:hover {
        transform: scale(1.05);
        z-index: 10;
    }

    .quote-note {
        font-family: 'Delius', cursive;
        font-size: 22px;
        background-color: #fff9c4;
        padding: 20px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
        border-radius: 2px;
        transform: rotate(2deg);
        color: #444;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HELPER: CONVERT VIDEO TO HTML ---
def get_video_html(file_path):
    """
    Reads a local video file and returns an HTML string 
    that autoplays it without controls.
    """
    with open(file_path, "rb") as f:
        video_bytes = f.read()
    video_b64 = base64.b64encode(video_bytes).decode()
    
    # HTML5 Video Tag with autoplay, muted, loop, and NO controls
    html = f"""
    <div class="video-container">
        <video width="100%" autoplay muted loop playsinline style="display: block;">
            <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    """
    return html

# --- SESSION STATE ---
if 'stage' not in st.session_state:
    st.session_state.stage = 1
if 'candles_blown' not in st.session_state:
    st.session_state.candles_blown = False

# ==========================================
# STAGE 1: INTRO
# ==========================================
if st.session_state.stage == 1:
    st.write("")
    st.write("")
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<p class="title-text">Happy Birthday!</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle-text">TO MY FAVORITE BROTHER</p>', unsafe_allow_html=True)
        
        if lottie_welcome:
            st_lottie(lottie_welcome, height=250, key="welcome")
        else:
            st.markdown("🎁")
        st.markdown('</div>', unsafe_allow_html=True)

        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
            if st.button("✨ TAP TO OPEN ✨", use_container_width=True):
                st.session_state.stage = 2
                st.rerun()

# ==========================================
# STAGE 2: MAKE A WISH
# ==========================================
elif st.session_state.stage == 2:
    st.markdown('<p class="title-text" style="font-size: 60px; text-align: center;">Make a Wish! 🕯️</p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        if not st.session_state.candles_blown:
            components.html(CAKE_EMBED_HTML, height=600)
            st.write("")
            b1, b2, b3 = st.columns([1, 1, 1])
            with b2:
                if st.button("🌬️ Blow Candles", use_container_width=True):
                    st.session_state.candles_blown = True
                    st.rerun()
        else:
            st.balloons()
            if lottie_celebrate:
                st_lottie(lottie_celebrate, height=400, key="party")
            st.markdown('<h3 style="font-family: Fredoka One; text-align:center; color:#555;">Yay! Wishes sent to the universe! ✨</h3>', unsafe_allow_html=True)
            st.write("")
            b1, b2, b3 = st.columns([1, 1, 1])
            with b2:
                if st.button("🎁 Unwrap Gift", use_container_width=True):
                    st.session_state.stage = 3
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# STAGE 3: MEMORY LANE (IMAGES + VIDEO)
# ==========================================
else:
    st.balloons()
    st.markdown('<p class="title-text" style="font-size: 60px; text-align: center;">Memory Lane 📸</p>', unsafe_allow_html=True)
    st.write("---")

    image_folder = "."
    supported_extensions = (
        '.png', '.jpg', '.jpeg', '.gif', 
        '.mp4', '.mov', '.avi', '.mkv', '.webm', '.wmv'
    )
    
    media_files = [f for f in os.listdir(image_folder) if f.lower().endswith(supported_extensions)]
    random.shuffle(media_files)

    if not media_files:
        st.error("⚠️ No media detected! Check the Troubleshooting section at the bottom.")
    else:
        cols = st.columns(3)
        mixed_items = [('media', f) for f in media_files]
        num_quotes = min(len(quotes), len(media_files) // 2 + 1)
        for i in range(num_quotes):
             mixed_items.insert(random.randint(0, len(mixed_items)), ('quote', quotes[i]))

        for i, item in enumerate(mixed_items):
            with cols[i % 3]:
                if item[0] == 'media':
                    file_path = os.path.join(image_folder, item[1])
                    
                    is_video = item[1].lower().endswith(('.mp4', '.mov', '.avi', '.mkv', '.webm', '.wmv'))
                    
                    if is_video:
                         # ✅ CUSTOM VIDEO PLAYER: AUTOPLAY, MUTED, NO CONTROLS
                         video_html = get_video_html(file_path)
                         st.markdown(video_html, unsafe_allow_html=True)
                    else:
                         img = Image.open(file_path)
                         st.image(img, use_container_width=True)
                    
                    st.write("") 
                    
                elif item[0] == 'quote':
                    st.markdown(f'<div class="quote-note">📌 {item[1]}</div><br>', unsafe_allow_html=True)

    st.write("---")
    st.markdown('<p style="text-align:center; font-family:Delius; color:#FFF; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);">Made with ❤️ by your sister.</p>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1,1,1])
    with c2:
        if st.button("🔄 Start Over"):
            st.session_state.stage = 1
            st.session_state.candles_blown = False
            st.rerun()

    # ==========================================
    # 🕵️‍♀️ TROUBLESHOOTING
    # ==========================================
    st.write("---")
    with st.expander("🔧 Troubleshooting: Files not showing up?"):
        st.write("Files detected in folder:")
        st.write(os.listdir("."))