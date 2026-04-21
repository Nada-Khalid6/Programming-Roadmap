منصة تعلم البرمجة - مسارات متسلسلة مع مصادر يوتيوب وشيكليست
يمكن تشغيلها بأمر: streamlit run app.py

import streamlit as st
import json
import os

# ==================== إعداد الصفحة ====================
st.set_page_config(
    page_title="منصة تعلم البرمجة",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="auto"
)

# ==================== تحميل وحفظ البيانات ====================
DATA_FILE = "data.json"
PROGRESS_FILE = "progress.json"

def load_data():
    """تحميل بيانات التخصصات والخريطة من ملف JSON"""
    default_data = {
        "tracks": [
            {
                "id": 1,
                "name": "أساسيات البرمجة",
                "description": "رحلة ممتعة للمبتدئين لفهم أساسيات البرمجة باستخدام Python.",
                "icon": "🐍"
            },
            {
                "id": 2,
                "name": "تطوير مواقع الويب",
                "description": "من الصفر لبناء موقع متكامل باستخدام HTML، CSS، و JavaScript.",
                "icon": "🌐"
            }
        ],
        "roadmaps": {
            "1": [
                {
                    "title": "مقدمة في البرمجة ومفاهيم أساسية",
                    "playlist_url": "https://www.youtube.com/playlist?list=PLMYF6NkLrdNvVZ0yQ5yQ5yQ5yQ5yQ5yQ5",
                    "description": "كورس شامل بالعربية يشرح المفاهيم من الصفر بأسلوب مبسط جداً.",
                    "completed": False
                },
                {
                    "title": "تعلم لغة Python من الصفر",
                    "playlist_url": "https://www.youtube.com/playlist?list=PLMYF6NkLrdNvVZ0yQ5yQ5yQ5yQ5yQ5yQ5",
                    "description": "أفضل كورس Python على اليوتيوب بالعربي، مناسب جداً للمبتدئين.",
                    "completed": False
                },
                {
                    "title": "الخوارزميات المنطقية وحل المشكلات",
                    "playlist_url": "https://www.youtube.com/playlist?list=PLMYF6NkLrdNvVZ0yQ5yQ5yQ5yQ5yQ5yQ5",
                    "description": "تعلم كيفية التفكير المنطقي وحل المشكلات البرمجية خطوة بخطوة.",
                    "completed": False
                }
            ],
            "2": [
                {
                    "title": "أساسيات HTML و CSS",
                    "playlist_url": "https://www.youtube.com/playlist?list=PLMYF6NkLrdNvVZ0yQ5yQ5yQ5yQ5yQ5yQ5",
                    "description": "كورس متكامل لبناء واجهات المواقع من الصفر باستخدام HTML و CSS.",
                    "completed": False
                },
                {
                    "title": "JavaScript للمبتدئين",
                    "playlist_url": "https://www.youtube.com/playlist?list=PLMYF6NkLrdNvVZ0yQ5yQ5yQ5yQ5yQ5yQ5",
                    "description": "شرح JavaScript بطريقة مبسطة مع أمثلة عملية وتطبيقات حقيقية.",
                    "completed": False
                },
                {
                    "title": "بناء موقع كامل (مشروع عملي)",
                    "playlist_url": "https://www.youtube.com/playlist?list=PLMYF6NkLrdNvVZ0yQ5yQ5yQ5yQ5yQ5yQ5",
                    "description": "تطبيق عملي: بناء موقع متكامل باستخدام HTML و CSS و JavaScript.",
                    "completed": False
                }
            ]
        }
    }
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_data, f, ensure_ascii=False, indent=4)
        return default_data

def load_progress():
    """تحميل تقدم الطالب (علامات الصح)"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_progress(progress):
    """حفظ تقدم الطالب"""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False, indent=4)

# ==================== واجهة التخصصات (البطاقات) ====================
def show_tracks():
    st.markdown("## 🎯 اختر تخصصك")
    st.markdown("---")
    
    data = load_data()
    tracks = data['tracks']
    
    cols = st.columns(3)
    for idx, track in enumerate(tracks):
        with cols[idx % 3]:
            with st.container(border=True):
                st.markdown(f"## {track['icon']} {track['name']}")
                st.markdown(f"_{track['description']}_")
                st.markdown("---")
                if st.button(f"ابدأ الرحلة 🚀", key=f"btn_{track['id']}", use_container_width=True):
                    st.session_state.selected_track = track['id']
                    st.rerun()

# ==================== واجهة الخريطة المتسلسلة ====================
def show_roadmap(track_id):
    data = load_data()
    progress = load_progress()
    
    track_name = "التخصص"
    for t in data['tracks']:
        if t['id'] == track_id:
            track_name = t['name']
            break
    
    roadmap = data['roadmaps'].get(str(track_id), [])
    
    col_back, col_title = st.columns([1, 5])
    with col_back:
        if st.button("🔙 العودة", use_container_width=True):
            del st.session_state.selected_track
            st.rerun()
    with col_title:
        st.markdown(f"## 🗺️ خريطة التعلم: {track_name}")
    
    st.markdown("---")
    
    for idx, step in enumerate(roadmap):
        with st.container(border=True):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(f"### 📍 المرحلة {idx+1}: {step['title']}")
                st.caption(f"📝 {step['description']}")
                st.link_button("🎥 ابدأ الآن (افتح قائمة التشغيل)", step['playlist_url'], use_container_width=False)
            
            with col2:
                completed = progress.get(str(track_id), {}).get(str(idx), False)
                new_completed = st.checkbox("✅ تم الإنجاز", value=completed, key=f"chk_{track_id}_{idx}")
                
                if new_completed != completed:
                    if str(track_id) not in progress:
                        progress[str(track_id)] = {}
                    progress[str(track_id)][str(idx)] = new_completed
                    save_progress(progress)
                    st.rerun()
    
    if roadmap:
        completed_count = sum(1 for i in range(len(roadmap)) 
                              if progress.get(str(track_id), {}).get(str(i), False))
        total_count = len(roadmap)
        percent = int(completed_count / total_count * 100)
        st.markdown("---")
        st.markdown(f"### 📊 تقدمك في المسار: {completed_count} من {total_count} مرحلة مكتملة ({percent}%)")
        st.progress(percent / 100)

# ==================== التشغيل الرئيسي ====================
def main():
    if 'selected_track' not in st.session_state:
        st.session_state.selected_track = None
    
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/learning.png", width=80)
        st.markdown("## 📘 منصة التعلم")
        st.markdown("منصة تجمع **مسارات تعلم البرمجة** مع أفضل قوائم تشغيل يوتيوب.")
        st.markdown("---")
        st.markdown("### ✨ المميزات")
        st.markdown("- ✅ مسارات متسلسلة")
        st.markdown("- 📺 قوائم تشغيل منسقة")
        st.markdown("- ☑️ شيكليست للتقدم")
        st.markdown("---")
        st.caption("نسخة 1.0 | Made with ❤️")
    
    if st.session_state.selected_track is None:
        show_tracks()
    else:
        show_roadmap(st.session_state.selected_track)

if __name__ == "__main__":
    main()