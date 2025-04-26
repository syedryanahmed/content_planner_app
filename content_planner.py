import streamlit as st

st.set_page_config(page_title="Content Planner", layout="centered")

# Initialize session state for each platform
if "instagram" not in st.session_state:
    st.session_state.instagram = []
if "youtube" not in st.session_state:
    st.session_state.youtube = []
if "tiktok" not in st.session_state:
    st.session_state.tiktok = []

st.title("📱 Content Planner")

platform = st.selectbox("Choose Platform", ["Instagram Reels", "YouTube Shorts", "TikTok"])

st.subheader(f"📝 Add {platform} Content")

if platform == "YouTube Shorts":
    title = st.text_input("Title")
    description = st.text_area("Description")
    tags = st.text_input("Tags (comma-separated)")
    
    if st.button("Add to YouTube Shorts"):
        content = {
            "title": title,
            "description": description,
            "tags": tags
        }
        st.session_state.youtube.append(content)
        st.success("✅ Added to YouTube Shorts")
        
        # Show copy-paste section
        st.markdown("---")
        st.subheader("📋 Copy Content")
        st.code(f"Title: {title}\n\nDescription: {description}\n\nTags: {tags}")

else:  # Instagram Reels or TikTok
    title = st.text_input("Title")
    caption = st.text_area("Caption with Hashtags")
    
    if st.button(f"Add to {platform}"):
        content = {
            "title": title,
            "caption": caption
        }
        if platform == "Instagram Reels":
            st.session_state.instagram.append(content)
            st.success("✅ Added to Instagram Reels")
        else:
            st.session_state.tiktok.append(content)
            st.success("✅ Added to TikTok")
        
        # Show copy-paste section
        st.markdown("---")
        st.subheader("📋 Copy Content")
        st.code(f"Title: {title}\n\nCaption: {caption}")

st.markdown("---")
st.subheader("📋 Saved Content")

def display_items(label, items, key):
    st.markdown(f"### {label}")
    for i, item in enumerate(items):
        with st.expander(f"{i+1}. {item['title']}"):
            if key == "youtube":
                st.markdown(f"**Description:** {item['description']}")
                st.markdown(f"**Tags:** {item['tags']}")
                st.code(f"Title: {item['title']}\n\nDescription: {item['description']}\n\nTags: {item['tags']}")
            else:
                st.markdown(f"**Caption:** {item['caption']}")
                st.code(f"Title: {item['title']}\n\nCaption: {item['caption']}")
            
            if st.button("🗑️ Delete", key=f"delete_{key}_{i}"):
                items.pop(i)
                st.rerun()

if st.session_state.instagram:
    display_items("Instagram Reels", st.session_state.instagram, "instagram")

if st.session_state.youtube:
    display_items("YouTube Shorts", st.session_state.youtube, "youtube")

if st.session_state.tiktok:
    display_items("TikTok", st.session_state.tiktok, "tiktok")
