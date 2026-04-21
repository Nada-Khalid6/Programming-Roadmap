import streamlit as st

# إعداد الصفحة - بدون أي CSS إضافي
st.set_page_config(
    page_title="منصة تعلم البرمجة",
    page_icon="💻",
    layout="wide"
)

# ======================= البيانات المدمجة =======================
tracks = {
    1: {
        "name": "🐍 أساسيات البرمجة (Python)",
        "description": "رحلة متكاملة لتعلم البرمجة من الصفر باستخدام Python",
        "long_desc": "هذا المسار مخصص للمبتدئين تماماً. ستتعلم أساسيات البرمجة مثل المتغيرات، الجمل الشرطية، الحلقات، الدوال، والقوائم.",
        "steps": [
            {
                "title": "مقدمة في البرمجة والخوارزميات",
                "desc": "فهم ما هي البرمجة والخوارزميات",
                "ar": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/watch?v=nLRL_NcnK-4"
            },
            {
                "title": "تعلم Python - الأساسيات",
                "desc": "المتغيرات، الجمل الشرطية، الحلقات، الدوال",
                "ar": "https://youtube.com/playlist?list=PLMYF6NkLrdNvVZ0yQ5yQ5yQ5yQ5yQ5yQ5",
                "en": "https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU"
            },
            {
                "title": "مشروع عملي: آلة حاسبة",
                "desc": "تطبيق عملي لكل ما تعلمته",
                "ar": "https://www.youtube.com/watch?v=9kzl9nwX7k8",
                "en": "https://www.youtube.com/watch?v=8ext9G7xspg"
            }
        ]
    },
    2: {
        "name": "🌐 تطوير واجهات الويب",
        "description": "من الصفر إلى الاحتراف في HTML, CSS, JavaScript و React",
        "long_desc": "في هذا المسار ستتعلم بناء واجهات مواقع الويب الحديثة. نبدأ بـ HTML و CSS ثم JavaScript ثم React.",
        "steps": [
            {
                "title": "HTML و CSS - الأساسيات",
                "desc": "بناء هيكل وتنسيق الصفحات",
                "ar": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/watch?v=G3e-cpL7ofc"
            },
            {
                "title": "JavaScript للمبتدئين",
                "desc": "التعامل مع DOM والأحداث",
                "ar": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/watch?v=PkZNo7MFNFg"
            },
            {
                "title": "React.js - تطبيقات متقدمة",
                "desc": "مكونات، حالة، خصائص",
                "ar": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/watch?v=w7ejDZ8SWv8"
            }
        ]
    },
    3: {
        "name": "🗄️ قواعد البيانات (SQL)",
        "description": "فهم قواعد البيانات العلائقية ولغة SQL",
        "long_desc": "تعلم كيفية تصميم وإدارة قواعد البيانات باستخدام SQL.",
        "steps": [
            {
                "title": "مقدمة في قواعد البيانات",
                "desc": "أنواع قواعد البيانات ومفاهيم أساسية",
                "ar": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/watch?v=HXV3zeQKqGY"
            },
            {
                "title": "SQL الأساسي",
                "desc": "SELECT, WHERE, ORDER BY, GROUP BY",
                "ar": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/watch?v=7S_tz1z_5bA"
            },
            {
                "title": "Join والعلاقات",
                "desc": "INNER JOIN, LEFT JOIN",
                "ar": "https://youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/watch?v=9yeOJ0ZMUYw"
            }
        ]
    }
}

# حفظ التقدم (في الجلسة فقط، لإعادة التشغيل ستضيع - مناسب للتجربة)
if "progress" not in st.session_state:
    st.session_state.progress = {}

def mark_completed(track_id, step_idx, value):
    if track_id not in st.session_state.progress:
        st.session_state.progress[track_id] = {}
    st.session_state.progress[track_id][step_idx] = value

def reset_track(track_id):
    if track_id in st.session_state.progress:
        del st.session_state.progress[track_id]

# ======================= واجهة المستخدم =======================
st.title("🚀 منصة مسارات تعلم البرمجة")
st.markdown("اختر تخصصك وابدأ رحلة التعلم خطوة بخطوة")

# الشريط الجانبي - سيظهر على اليسار تلقائياً
with st.sidebar:
    st.header("💻 منصة التعلم")
    st.markdown("مسارات برمجية متكاملة مع مصادر عربية وإنجليزية")
    st.markdown("---")
    st.markdown("**المميزات**")
    st.markdown("- مسارات متسلسلة")
    st.markdown("- مصادر عربية وإنجليزية")
    st.markdown("- شيكليست للتقدم")
    st.markdown("- إعادة تعيين التقدم")
    st.markdown("---")
    st.caption("By: Nada Khalid ✨♥")

# الصفحة الرئيسية أو عرض المسار المختار
if "selected_track" not in st.session_state:
    # عرض البطاقات
    cols = st.columns(3)
    for idx, (tid, track) in enumerate(tracks.items()):
        with cols[idx % 3]:
            with st.container(border=True):
                st.subheader(track["name"])
                st.write(track["description"])
                if st.button(f"📖 عرض المسار", key=f"btn_{tid}"):
                    st.session_state.selected_track = tid
                    st.rerun()
else:
    tid = st.session_state.selected_track
    track = tracks[tid]
    
    # زر العودة
    if st.button("🔙 العودة إلى التخصصات"):
        del st.session_state.selected_track
        st.rerun()
    
    st.header(f"🗺️ {track['name']}")
    with st.expander("📌 تعريف المسار", expanded=True):
        st.write(track["long_desc"])
    
    # إعادة تعيين التقدم
    if st.button("🔄 إعادة تعيين التقدم لهذا المسار"):
        reset_track(tid)
        st.rerun()
    
    st.markdown("---")
    st.subheader("📚 خطوات التعلم (بالترتيب)")
    
    # عرض المراحل
    completed_count = 0
    for i, step in enumerate(track["steps"]):
        with st.container(border=True):
            st.markdown(f"**المرحلة {i+1}: {step['title']}**")
            st.write(f"📝 {step['desc']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.link_button("🇸🇴 مصدر عربي - ابدأ الآن", step["ar"], use_container_width=True)
            with col2:
                st.link_button("🇬🇧 مصدر إنجليزي - Start Now", step["en"], use_container_width=True)
            
            # شيكليست
            is_checked = st.session_state.progress.get(tid, {}).get(i, False)
            checked = st.checkbox("✅ تم إكمال هذه المرحلة", value=is_checked, key=f"chk_{tid}_{i}")
            if checked != is_checked:
                mark_completed(tid, i, checked)
                st.rerun()
            if checked:
                completed_count += 1
    
    total = len(track["steps"])
    percent = int(completed_count / total * 100) if total else 0
    st.markdown("---")
    st.markdown(f"### 📊 تقدمك: {completed_count} من {total} مرحلة مكتملة ({percent}%)")
    st.progress(percent / 100)
    if completed_count == total and total > 0:
        st.balloons()
        st.success("🎉 تهانينا! لقد أكملت هذا المسار بالكامل.")