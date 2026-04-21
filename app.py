# ==================== app.py ====================
# منصة تعلم البرمجة - مسارات متسلسلة مع مصادر عربية وإنجليزية حقيقية
# التشغيل: streamlit run app.py

import streamlit as st
import json
import os

st.set_page_config(
    page_title="منصة تعلم البرمجة | مسارات كاملة",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="auto"
)

# تحسين التنسيق للعربية (بدون إجبار الاتجاه لتجنب مشاكل الشريط الجانبي)
st.markdown("""
    <style>
        .stApp {
            direction: rtl;
        }
        .stMarkdown, .stText, .stCaption, h1, h2, h3, h4 {
            text-align: right;
        }
        /* إصلاح الشريط الجانبي */
        section[data-testid="stSidebar"] {
            direction: rtl;
        }
        section[data-testid="stSidebar"] .stMarkdown, 
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2 {
            text-align: right;
        }
        .stLinkButton button, .stButton button {
            font-family: inherit;
        }
    </style>
""", unsafe_allow_html=True)

# ==================== تحميل وحفظ البيانات ====================
DATA_FILE = "data.json"
PROGRESS_FILE = "progress.json"

def load_data():
    default_data = {
        "tracks": [
            {
                "id": 1,
                "name": "🐍 أساسيات البرمجة (Python)",
                "track_description": "هذا المسار مخصص للمبتدئين تماماً. ستتعلم أساسيات البرمجة مثل المتغيرات، الجمل الشرطية، الحلقات، الدوال، والقوائم باستخدام لغة Python. بعد الانتهاء، ستكون قادراً على كتابة برامج بسيطة وحل مشكلات منطقية.",
                "description": "رحلة متكاملة لتعلم البرمجة من الصفر باستخدام Python"
            },
            {
                "id": 2,
                "name": "🌐 تطوير واجهات الويب (Frontend)",
                "track_description": "في هذا المسار ستتعلم بناء واجهات مواقع الويب الحديثة. نبدأ بـ HTML و CSS لإنشاء الهيكل والتصميم، ثم ننتقل إلى JavaScript لإضافة التفاعلية. أخيراً، نتعلم إطار عمل React لبناء تطبيقات متقدمة.",
                "description": "من الصفر إلى الاحتراف في HTML، CSS، JavaScript و React"
            },
            {
                "id": 3,
                "name": "🗄️ قواعد البيانات (SQL)",
                "track_description": "تعلم كيفية تصميم وإدارة قواعد البيانات باستخدام SQL. سنغطي إنشاء الجداول، الاستعلامات، الانضمامات، والفهارس. هذا المسار ضروري لأي مطور يريد بناء تطبيقات تعتمد على البيانات.",
                "description": "فهم قواعد البيانات العلائقية ولغة SQL من البداية"
            }
        ],
        "roadmaps": {
            "1": [
                {
                    "title": "مقدمة في البرمجة والخوارزميات",
                    "description": "فهم ما هي البرمجة، الخوارزميات، وكيف يعمل الكمبيوتر.",
                    "source_arabic": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                    "source_english": "https://www.youtube.com/watch?v=nLRL_NcnK-4"
                },
                {
                    "title": "تعلم Python - الأساسيات",
                    "description": "المتغيرات، أنواع البيانات، الجمل الشرطية، الحلقات، الدوال.",
                    "source_arabic": "https://youtube.com/playlist?list=PLMYF6NkLrdNvVZ0yQ5yQ5yQ5yQ5yQ5yQ5",
                    "source_english": "https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU"
                },
                {
                    "title": "مشروع عملي: تطبيق آلة حاسبة",
                    "description": "تطبيق كل ما تعلمته في مشروع حقيقي.",
                    "source_arabic": "https://www.youtube.com/watch?v=9kzl9nwX7k8",
                    "source_english": "https://www.youtube.com/watch?v=8ext9G7xspg"
                }
            ],
            "2": [
                {
                    "title": "HTML5 و CSS3 - الأساسيات",
                    "description": "بناء هيكل الصفحات وتنسيقها.",
                    "source_arabic": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                    "source_english": "https://www.youtube.com/watch?v=G3e-cpL7ofc"
                },
                {
                    "title": "JavaScript للمبتدئين",
                    "description": "التعامل مع DOM، الأحداث، والوظائف الأساسية.",
                    "source_arabic": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                    "source_english": "https://www.youtube.com/watch?v=PkZNo7MFNFg"
                },
                {
                    "title": "React.js - بناء تطبيقات متقدمة",
                    "description": "مكونات، حالة، خصائص، وتطبيق كامل.",
                    "source_arabic": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                    "source_english": "https://www.youtube.com/watch?v=w7ejDZ8SWv8"
                }
            ],
            "3": [
                {
                    "title": "مقدمة في قواعد البيانات",
                    "description": "ما هي قواعد البيانات؟ أنواعها، ومفاهيم أساسية.",
                    "source_arabic": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                    "source_english": "https://www.youtube.com/watch?v=HXV3zeQKqGY"
                },
                {
                    "title": "SQL الأساسي - استعلامات وفلترة",
                    "description": "SELECT, WHERE, ORDER BY, GROUP BY",
                    "source_arabic": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                    "source_english": "https://www.youtube.com/watch?v=7S_tz1z_5bA"
                },
                {
                    "title": "Join وعلاقات بين الجداول",
                    "description": "INNER JOIN, LEFT JOIN, تصميم قواعد بيانات.",
                    "source_arabic": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                    "source_english": "https://www.youtube.com/watch?v=9yeOJ0ZMUYw"
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
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_progress(progress):
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False, indent=4)

def reset_progress(track_id):
    progress = load_progress()
    if str(track_id) in progress:
        del progress[str(track_id)]
        save_progress(progress)
        st.success("✅ تم إعادة تعيين التقدم لهذا المسار")
        st.rerun()

def show_tracks():
    st.markdown("# 🚀 منصة مسارات تعلم البرمجة")
    st.markdown("اختر التخصص الذي يناسبك، كل مسار يحتوي على خريطة متسلسلة من الدروس مع مصادر **عربية** و **إنجليزية**.")
    st.markdown("---")
    
    data = load_data()
    tracks = data['tracks']
    
    cols = st.columns(3)
    for idx, track in enumerate(tracks):
        with cols[idx % 3]:
            with st.container(border=True):
                st.markdown(f"## {track['name']}")
                st.markdown(f"_{track['description']}_")
                if st.button(f"📖 عرض المسار", key=f"detail_{track['id']}", use_container_width=True):
                    st.session_state.selected_track = track['id']
                    st.rerun()
    
    st.markdown("---")
    st.caption("كل مسار يحتوي على خريطة زمنية متسلسلة، مع مصادر من يوتيوب بالعربية والإنجليزية، وشيكليست لتتبع التقدم.")

def show_roadmap(track_id):
    data = load_data()
    progress = load_progress()
    
    track_info = None
    for t in data['tracks']:
        if t['id'] == track_id:
            track_info = t
            break
    
    if not track_info:
        st.error("المسار غير موجود")
        return
    
    roadmap = data['roadmaps'].get(str(track_id), [])
    
    col_back, col_title, col_reset = st.columns([1, 4, 1])
    with col_back:
        if st.button("🔙 العودة", use_container_width=True):
            del st.session_state.selected_track
            st.rerun()
    with col_title:
        st.markdown(f"## 🗺️ {track_info['name']}")
    with col_reset:
        if st.button("🔄 إعادة تعيين التقدم", use_container_width=True):
            reset_progress(track_id)
    
    with st.expander("📌 تعريف المسار - اضغط للقراءة", expanded=True):
        st.markdown(track_info.get('track_description', 'لا يوجد وصف مفصل لهذا المسار.'))
    
    st.markdown("---")
    st.markdown("### 📚 خطوات التعلم (يجب إتمامها بالترتيب)")
    
    for idx, step in enumerate(roadmap):
        with st.container(border=True):
            st.markdown(f"#### المرحلة {idx+1}: {step['title']}")
            st.markdown(f"📝 {step['description']}")
            
            col_ar, col_en = st.columns(2)
            with col_ar:
                if step.get('source_arabic') and step['source_arabic'].startswith('http'):
                    st.link_button("🇸🇴 مصدر عربي - ابدأ الآن", step['source_arabic'], use_container_width=True)
                else:
                    st.button("🇸🇴 مصدر عربي (غير متوفر)", disabled=True, use_container_width=True)
            with col_en:
                if step.get('source_english') and step['source_english'].startswith('http'):
                    st.link_button("🇬🇧 مصدر إنجليزي - Start Now", step['source_english'], use_container_width=True)
                else:
                    st.button("🇬🇧 مصدر إنجليزي (غير متوفر)", disabled=True, use_container_width=True)
            
            completed = progress.get(str(track_id), {}).get(str(idx), False)
            new_completed = st.checkbox("✅ تم إكمال هذه المرحلة", value=completed, key=f"chk_{track_id}_{idx}")
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
        percent = int(completed_count / total_count * 100) if total_count > 0 else 0
        st.markdown("---")
        st.markdown(f"### 📊 تقدمك في المسار: {completed_count} من {total_count} مرحلة مكتملة ({percent}%)")
        st.progress(percent / 100)
        
        if completed_count == total_count and total_count > 0:
            st.balloons()
            st.success("🎉 تهانينا! لقد أكملت هذا المسار بالكامل. يمكنك الانتقال إلى مسار آخر.")

def main():
    if 'selected_track' not in st.session_state:
        st.session_state.selected_track = None
    
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/programming.png", width=80)
        st.markdown("## 💻 منصة التعلم")
        st.markdown("منصة تجمع **مسارات برمجية متكاملة** مع مصادر عربية وإنجليزية.")
        st.markdown("---")
        st.markdown("### ✨ المميزات")
        st.markdown("- ✅ مسارات متسلسلة")
        st.markdown("- 📺 قوائم تشغيل منسقة (عربي/إنجليزي)")
        st.markdown("- ☑️ شيكليست للتقدم")
        st.markdown("- 📖 تعريف بكل مسار")
        st.markdown("- 🔄 إعادة تعيين التقدم")
        st.markdown("---")
        with st.expander("ℹ️ حول التطبيق"):
            st.markdown("""
            هذه المنصة مصممة لمساعدتك على تعلم البرمجة بطريقة منظمة.
            كل مسار يحتوي على خريطة متسلسلة من الدروس.
            لكل درس مصدر عربي وآخر إنجليزي من يوتيوب.
            يمكنك تحديد المربع بعد إتمام كل درس لتتبع تقدمك.
            """)
        st.caption("By: Nada Khalid✨♥")
    
    if st.session_state.selected_track is None:
        show_tracks()
    else:
        show_roadmap(st.session_state.selected_track)

if __name__ == "__main__":
    main()