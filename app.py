"""Streamlit UI for the AI Content Repurposing Assistant."""
import os
import streamlit as st
from content_engine import generate_content_pack, demo_content_pack, quality_report

st.set_page_config(page_title="AI Content Repurposing Assistant", page_icon="🎬", layout="wide")
st.title("🎬 AI Content Repurposing Assistant")
st.write("Turn a story or transcript into editable hooks, video scripts, captions and CTAs.")
st.caption("Built as a small workflow prototype for content teams. Human review is required.")

with st.sidebar:
    st.header("Content brief")
    platform = st.selectbox("Platform", ["Instagram Reels", "YouTube Shorts", "Both"])
    language = st.selectbox("Language", ["English", "Hindi", "Hinglish"])
    tone = st.selectbox("Tone", ["Suspenseful", "Emotional", "Inspirational", "Conversational"])
    duration = st.selectbox("Video duration", [15, 30, 45, 60], index=1)
    audience = st.text_input("Audience", "Young adults interested in stories")
    use_demo = st.checkbox("Demo mode (no API key)", value=not bool(os.getenv("GEMINI_API_KEY")))
    st.info("Demo mode uses a fixed illustrative example, not AI generation.")

sample = """A college student named Maya discovers a handwritten note inside an old library book.
The note warns that the library clock will stop at midnight. She stays behind to investigate.
At 11:59 PM, she hears footsteps from the locked archive room. The story ends before
she opens the door."""
source = st.text_area("Paste a story, episode summary or transcript", value=sample, height=190)
if st.button("Generate content pack", type="primary"):
    if len(source.strip()) < 50:
        st.error("Please provide at least 50 characters of source material.")
    else:
        brief = dict(platform=platform, language=language, tone=tone, duration=duration, audience=audience)
        try:
            with st.spinner("Preparing content..."):
                pack = demo_content_pack(source, brief) if use_demo else generate_content_pack(source, brief)
            st.session_state["pack"] = pack
            st.session_state["source"] = source
        except Exception as e:
            st.error(f"Could not generate: {e}")
if "pack" in st.session_state:
    pack = st.session_state["pack"]
    st.subheader("Content pack")
    st.write("**Summary:**", pack.get("summary", ""))
    st.markdown("### Five hooks")
    for i, hook in enumerate(pack.get("hooks", []), 1):
        st.write(f"{i}. {hook}")
    st.markdown("### Three short-video scripts")
    for i, script in enumerate(pack.get("scripts", []), 1):
        with st.expander(f"Script {i}", expanded=i==1):
            st.write("**Visual:**", script.get("visual", ""))
            st.write("**Voiceover:**", script.get("voiceover", ""))
            st.write("**On-screen text:**", script.get("on_screen_text", ""))
    st.markdown("### Captions")
    for cap in pack.get("captions", []):
        st.write("•", cap)
    st.markdown("### Calls to action")
    for cta in pack.get("ctas", []):
        st.write("•", cta)
    st.markdown("### Quality check")
    report = quality_report(pack, st.session_state["source"])
    st.json(report)
    st.warning("Automatic checks do not prove factual accuracy. An editor must verify every claim against the source.")
    st.download_button("Download content pack (JSON)", data=__import__("json").dumps(pack, ensure_ascii=False, indent=2),
                       file_name="content_pack.json", mime="application/json")
