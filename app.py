import streamlit as st
import json
from datetime import datetime
import os

# إعدادات الصفحة
st.set_page_config(
    page_title="Programming_Platform",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS للتأكد من أن الـ Sidebar في المكان الصحيح
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        position: fixed !important;
        left: 0 !important;
        top: 0 !important;
        height: 100vh !important;
    }
    
    [data-testid="stSidebarContent"] {
        padding-top: 1rem;
    }
    
    .main {
        margin-left: 21rem;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
    }
    
    .nav-button {
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ======================= البيانات المدمجة =======================
tracks = {
    1: {
        "name": "🐍 أساسيات البرمجة (Python)",
        "description": "رحلة متكاملة لتعلم البرمجة من الصفر باستخدام Python",
        "long_desc": "هذا المسار مخصص للمبتدئين تماماً. ستتعلم أساسيات البرمجة مثل المتغيرات، الجمل الشرطية، الحلقات، الدوال، والقوائس.",
        "difficulty": "مبتدئ",
        "duration": "4 أسابيع",
        "steps": [
            {
                "title": "مقدمة في البرمجة والخوارزميات",
                "desc": "فهم ما هي البرمجة والخوارزميات",
                "ar": "https://youtube.com/playlist?list=PLRtfJqT1hc33qtw3SV7SItJF1oV_jwEfu&si=UZnpTtJB6EYPqk2P",
                "en": "https://youtube.com/playlist?list=PLRtfJqT1hc33qtw3SV7SItJF1oV_jwEfu&si=UZnpTtJB6EYPqk2P",
                "duration": "1 ساعة"
            },
            {
                "title": "تعلم Python - الأساسيات",
                "desc": "المتغيرات، الجمل الشرطية، الحلقات، الدوال",
                "ar": "https://youtube.com/playlist?list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs&si=N9mVhLEDTOpHZrse",
                "en": "https://youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&si=6ADmspRx51bm_t0a",
                "duration": "4 ساعات"
            },
            {
                "title": "مشروع عملي: آلة حاسبة",
                "desc": "تطبيق عملي لكل ما تعلمته",
                "ar": "https://youtu.be/y_LGngsl0-E?si=TwBfMi6WnLDiSrPK",
                "en": "https://youtu.be/y_LGngsl0-E?si=TwBfMi6WnLDiSrPK",
                "duration": "1 ساعة"
            }
        ]
    },
    2: {
        "name": "🌐 تطوير واجهات الويب",
        "description": "من الصفر إلى الاحتراف في HTML, CSS, JavaScript و React",
        "long_desc": "في هذا المسار ستتعلم بناء واجهات مواقع الويب الحديثة. نبدأ بـ HTML و CSS ثم JavaScript ثم React.",
        "difficulty": "مبتدئ - متوسط",
        "duration": "6 أسابيع",
        "steps": [
            {
                "title": "HTML و CSS - الأساسيات",
                "desc": "بناء هيكل وتنسيق الصفحات",
                "ar": "https://www.youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/playlist?list=PL4cUxeGkcC9ivBf_eKCPIAYXWzLlPAm6G",
                "duration": "5 ساعات"
            },
            {
                "title": "JavaScript للمبتدئين",
                "desc": "التعامل مع DOM والأحداث",
                "ar": "https://www.youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/playlist?list=PL4cUxeGkcC9haRX4IsKjI31V6pSvyUvxl",
                "duration": "7 ساعات"
            },
            {
                "title": "React.js - تطبيقات متقدمة",
                "desc": "مكونات، حالة، خصائص",
                "ar": "https://www.youtube.com/playlist?list=PLDoPjvoNmBAyXeV5jC5Z8yMPuHO9eFXL7",
                "en": "https://www.youtube.com/playlist?list=PL4cUxeGkcC9PI5PtvJ_je6S6EQG9GEsW9",
                "duration": "10 ساعات"
            }
        ]
    },
    3: {
        "name": "🗄️ قواعد البيانات (SQL)",
        "description": "فهم قواعد البيانات العلائقية ولغة SQL",
        "long_desc": "تعلم كيفية تصميم وإدارة قواعد البيانات باستخدام SQL.",
        "difficulty": "متوسط",
        "duration": "5 أسابيع",
        "steps": [
            {
                "title": "مقدمة في قواعد البيانات",
                "desc": "أنواع قواعد البيانات ومفاهيم أساسية",
                "ar": "https://youtube.com/playlist?list=PLUgzfC8Ca25u_fqLoYcAl2CVbDNfLWqVx&si=-WWM6O6Q9KwaZF2b",
                "en": "https://youtube.com/playlist?list=PLUgzfC8Ca25sfrLPvLQg1YOU1RhUcfwsR&si=1gCBbdA0IDl7c9wA",
                "duration": "4 ساعات"
            },
            {
                "title": "SQL الأساسي",
                "desc": "SELECT, WHERE, ORDER BY, GROUP BY",
                "ar": "https://youtube.com/playlist?list=PLxbVBWjVdAEj8TmOUKPG0avUmLqSoQOpf&si=_3fvbUi1CN6NLB1D",
                "en": "https://youtu.be/SSKVgrwhzus?si=EHjR53e32khrqEL9",
                "duration": "6 ساعات"
            },
            {
                "title": "Join والعلاقات",
                "desc": "INNER JOIN, LEFT JOIN, RIGHT JOIN",
                "ar": "https://youtu.be/bu6BqIkyPUk?si=ZxXbxYEqIEJ0xEXD",
                "en": "https://youtu.be/DjfVI_mNYwA?si=K8rZPI5FQHDUb9UO",
                "duration": "5 ساعات"
            }
        ]
    },
    4: {
        "name": "🔐 الأمن السيبراني (Cyber Security)",
        "description": "تعلم أساسيات الأمان السيبراني والحماية من التهديدات",
        "long_desc": "في هذا المسار ستتعلم أساسيات الأمان السيبراني، أنواع الهجمات، أدوات الحماية، واختبار الاختراق. مسار شامل لحماية الأنظمة والبيانات.",
        "difficulty": "متوسط - متقدم",
        "duration": "8 أسابيع",
        "steps": [
            {
                "title": "مقدمة في الأمان السيبراني",
                "desc": "المفاهيم الأساسية والتهديدات الشائعة",
                "ar": "https://www.youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU",
                "duration": "5 ساعات"
            },
            {
                "title": "التشفير وحماية البيانات",
                "desc": "أنواع التشفير والمفاتيح والبروتوكولات الآمنة",
                "ar": "https://www.youtube.com/playlist?list=PLDoPjvoNmBAyXeV5jC5Z8yMPuHO9eFXL7",
                "en": "https://www.youtube.com/playlist?list=PL4cUxeGkcC9PI5PtvJ_je6S6EQG9GEsW9",
                "duration": "6 ساعات"
            },
            {
                "title": "اختبار الاختراق (Penetration Testing)",
                "desc": "أدوات واستراتيجيات اختبار الأمان",
                "ar": "https://www.youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/playlist?list=PL08urSpVeNqjRQH2yVW-suQ318hJIUaDJ",
                "duration": "7 ساعات"
            },
            {
                "title": "مشروع عملي: حماية شبكة",
                "desc": "تطبيق عملي لحماية بيئة شبكة",
                "ar": "https://www.youtube.com/watch?v=KXY_J7CZ7Ow",
                "en": "https://www.youtube.com/watch?v=8ext9G7xspg",
                "duration": "ساعتان"
            }
        ]
    },
    5: {
        "name": "📊 تحليل البيانات (Data Analysis)",
        "description": "استخراج الرؤى من البيانات باستخدام Python و Pandas",
        "long_desc": "تعلم كيفية جمع وتنظيف وتحليل البيانات باستخدام أدوات مثل Pandas و NumPy و Matplotlib. سترتقي بمهاراتك في التعامل مع البيانات الضخمة.",
        "difficulty": "متوسط",
        "duration": "7 أسابيع",
        "steps": [
            {
                "title": "مقدمة في تحليل البيانات",
                "desc": "مفاهيم أساسية وأهمية البيانات",
                "ar": "https://www.youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU",
                "duration": "3 ساعات"
            },
            {
                "title": "Python مع Pandas و NumPy",
                "desc": "مكتبات معالجة البيانات الأساسية",
                "ar": "https://www.youtube.com/playlist?list=PLDoPjvoNmBAyXeV5jC5Z8yMPuHO9eFXL7",
                "en": "https://www.youtube.com/playlist?list=PL4cUxeGkcC9PI5PtvJ_je6S6EQG9GEsW9",
                "duration": "8 ساعات"
            },
            {
                "title": "تصور البيانات (Data Visualization)",
                "desc": "Matplotlib, Seaborn و Plotly",
                "ar": "https://www.youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/playlist?list=PL08urSpVeNqjRQH2yVW-suQ318hJIUaDJ",
                "duration": "6 ساعات"
            },
            {
                "title": "الإحصائيات والتنبؤ",
                "desc": "تحليل إحصائي وبناء نماذج توقعية",
                "ar": "https://www.youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF",
                "en": "https://www.youtube.com/playlist?list=PL9SnRnlzoyIENV8Tphe0b3qMLKfjlezQC",
                "duration": "7 ساعات"
            }
        ]
    },
    6: {
        "name": "📱 Huawei Courses",
        "description": "دورات متخصصة من شركة هواوي - Networking, DataCom, Security",
        "long_desc": "دورات تدريبية معتمدة من شركة هواوي في مختلف المجالات التقنية. تعلم من خبراء هواوي وحصل على شهادات معترف بها عالمياً.",
        "difficulty": "متوسط - متقدم",
        "duration": "10 أسابيع",
        "steps": [
            {
                "title": "كورس 1 - Networking",
                "desc": "أساسيات الشبكات مع هواوي - المفاهيم الأساسية وبنية الشبكات",
                "ar": "https://youtu.be/sRv5ZASs2eU?si=Jsb7V8VVripht_tD",
                "en": "https://youtu.be/sRv5ZASs2eU?si=Jsb7V8VVripht_tD",
                "duration": "6 ساعات"
            },
            {
                "title": "كورس 1 - DataCom",
                "desc": "مقدمة في اتصالات البيانات والشبكات الرقمية",
                "ar": "https://youtu.be/onDhv_QzfWI?si=E5PMG00BeLTVyT3_",
                "en": "https://youtu.be/onDhv_QzfWI?si=E5PMG00BeLTVyT3_",
                "duration": "5 ساعات"
            },
            {
                "title": "كورس 2 - DataCom",
                "desc": "بروتوكولات الشبكة وطبقات OSI",
                "ar": "https://youtu.be/N_hEeQ0xfNg?si=AfqPJ4Zd-VOQJitU",
                "en": "https://youtu.be/N_hEeQ0xfNg?si=AfqPJ4Zd-VOQJitU",
                "duration": "6 ساعات"
            },
            {
                "title": "كورس 3 - DataCom",
                "desc": "التوجيه والتبديل في شبكات البيانات",
                "ar": "https://youtu.be/mkRM-EbuoGw?si=PmR4QOoKZIdsP28m",
                "en": "https://youtu.be/mkRM-EbuoGw?si=PmR4QOoKZIdsP28m",
                "duration": "6 ساعات"
            },
            {
                "title": "كورس 4 - DataCom",
                "desc": "إدارة الشبكات ومراقبة الأداء",
                "ar": "https://youtu.be/aIMavZAJ-9w?si=AuB81fBp3eVv5t0l",
                "en": "https://youtu.be/aIMavZAJ-9w?si=AuB81fBp3eVv5t0l",
                "duration": "5 ساعات"
            },
            {
                "title": "كورس 5 - DataCom",
                "desc": "الشبكات اللاسلكية وتقنيات Wi-Fi",
                "ar": "https://youtu.be/aIMavZAJ-9w?si=Mfd75eKI9i-9OPu-",
                "en": "https://youtu.be/aIMavZAJ-9w?si=Mfd75eKI9i-9OPu-",
                "duration": "6 ساعات"
            },
            {
                "title": "كورس 6 - DataCom",
                "desc": "الشبكات السحابية وتقنيات SDN",
                "ar": "https://youtu.be/s4VCJDlkpgQ?si=2NB7d4dvp81v-8gM",
                "en": "https://youtu.be/s4VCJDlkpgQ?si=2NB7d4dvp81v-8gM",
                "duration": "7 ساعات"
            },
            {
                "title": "كورس 1 - Security",
                "desc": "أساسيات الأمن في شبكات هواوي والتهديدات الشائعة",
                "ar": "https://youtu.be/1V0iYsS8LUw?si=ezfktKffwXwqdXO6",
                "en": "https://youtu.be/1V0iYsS8LUw?si=ezfktKffwXwqdXO6",
                "duration": "6 ساعات"
            },
            {
                "title": "كورس 2 - Security",
                "desc": "تطبيق سياسات الأمان وحماية الشبكات باستخدام تقنيات هواوي",
                "ar": "https://youtu.be/4UcFVSHtcFc?si=Wf8P8eOk9rm3g_lG",
                "en": "https://youtu.be/4UcFVSHtcFc?si=Wf8P8eOk9rm3g_lG",
                "duration": "7 ساعات"
            }
        ]
    },
    7: {
        "name": "🌐 Cisco Courses",
        "description": "دورات معتمدة من شركة سيسكو",
        "long_desc": "برنامج تدريبي متكامل من سيسكو لتعلم تقنيات الشبكات والأمن. احصل على شهادات CCNA و CCNP المعترف بها عالمياً.",
        "difficulty": "متوسط - متقدم",
        "duration": "12 أسبوع",
        "steps": [
            {
                "title": "مقدمة في شبكات سيسكو",
                "desc": "أساسيات تقنيات سيسكو والشبكات",
                "ar": "https://youtu.be/97u8e0G4RJY?si=vYYtB7U3iU-Fi9Fq",
                "en": "https://youtu.be/97u8e0G4RJY?si=vYYtB7U3iU-Fi9Fq",
                "duration": "5 ساعات"
            },
            {
                "title": "CCNA - أساسيات الشهادة",
                "desc": "تحضير شامل لشهادة CCNA",
                "ar": "https://youtu.be/TrQljnE49-o?si=VIkh5d6Vi1Irjwax",
                "en": "https://youtu.be/4u3LVXDOkyw?si=wkzWOKJgMNjopXk_",
                "duration": "10 ساعات"
            },
            {
                "title": "Routing و Switching",
                "desc": "تعلم التوجيه والتبديل في سيسكو",
                "ar": "https://youtu.be/eGxl085nN-s?si=cr31qr84DhlcY49c",
                "en": "https://youtu.be/7dXBN8a-X2U?si=KywiEH-HAAcs9z2M",
                "duration": "9 ساعات"
            },
            {
                "title": "أمان الشبكات",
                "desc": "تطبيق أفضل الممارسات الأمنية في سيسكو",
                "ar": "https://youtu.be/4KtcomKXO-Q?si=16EEXfeSWWafWjUu",
                "en": "https://youtu.be/4KtcomKXO-Q?si=16EEXfeSWWafWjUu",
                "duration": "8 ساعات"
            }
        ]
    }
}

# ======================= إدارة الجلسة والبيانات =======================
if "progress" not in st.session_state:
    st.session_state.progress = {}

if "user_name" not in st.session_state:
    st.session_state.user_name = None

if "completed_tracks" not in st.session_state:
    st.session_state.completed_tracks = []

if "page" not in st.session_state:
    st.session_state.page = "home"

def mark_completed(track_id, step_idx, value):
    if track_id not in st.session_state.progress:
        st.session_state.progress[track_id] = {}
    st.session_state.progress[track_id][step_idx] = value

def reset_track(track_id):
    if track_id in st.session_state.progress:
        del st.session_state.progress[track_id]

def get_progress_percentage(track_id):
    track = tracks[track_id]
    total = len(track["steps"])
    completed = sum(1 for i in range(total) if st.session_state.progress.get(track_id, {}).get(i, False))
    return int(completed / total * 100) if total else 0

def embed_youtube_video(video_url):
    """تحويل رابط يوتيوب إلى iframe قابل للتضمين"""
    if "playlist?list=" in video_url:
        playlist_id = video_url.split("list=")[1].split("&")[0]
        return f'<iframe width="100%" height="380" src="https://www.youtube.com/embed/videoseries?list={playlist_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    elif "watch?v=" in video_url:
        video_id = video_url.split("watch?v=")[1].split("&")[0]
        return f'<iframe width="100%" height="380" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    elif "youtu.be/" in video_url:
        video_id = video_url.split("youtu.be/")[1].split("?")[0]
        return f'<iframe width="100%" height="380" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    else:
        return None

# ======================= الشريط الجانبي =======================
with st.sidebar:
    st.markdown("## 💻 منصة التعلم")
    st.markdown("---")
    
    # معلومات المستخدم
    if st.session_state.user_name:
        st.success(f"مرحباً بك: **{st.session_state.user_name}** 👋")
    else:
        user_input = st.text_input("أدخل اسمك:")
        if user_input:
            st.session_state.user_name = user_input
            st.rerun()
    
    st.markdown("---")
    
    # القائمة الجانبية
    st.markdown("### 📌 القائمة")
    
    if st.button("🏠 الرئيسية", use_container_width=True, key="nav_home"):
        st.session_state.page = "home"
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📚 المسارات")
    
    for tid, track in tracks.items():
        progress = get_progress_percentage(tid)
        track_name = track["name"]
        if st.button(f"{track_name}\n({progress}%)", use_container_width=True, key=f"nav_{tid}"):
            st.session_state.page = f"track_{tid}"
            st.rerun()
    
    st.markdown("---")
    
    # الإحصائيات
    st.markdown("### 📊 إحصائياتك")
    
    total_progress = 0
    completed_count = 0
    for tid in tracks.keys():
        progress = get_progress_percentage(tid)
        total_progress += progress
        if progress == 100:
            completed_count += 1
    
    avg_progress = int(total_progress / len(tracks)) if tracks else 0
    st.metric("التقدم الإجمالي", f"{avg_progress}%")
    st.metric("المسارات المكتملة", f"{completed_count}/{len(tracks)}")
    
    st.markdown("---")
    st.markdown("### 📞 تواصل معنا")
    st.link_button("📧 راسلنا على الإيميل", "mailto:nadaany1@gmail.com", use_container_width=True)
    
    st.markdown("---")
    st.caption("Keep Going💯🚀")

# ======================= المحتوى الرئيسي =======================

if st.session_state.page == "home":
    st.title("🚀 منصة مسارات تعلم البرمجة")
    st.markdown("---")
    st.markdown("""
    ### 🎯 أهلاً وسهلاً بك!
    
    هذه المنصة توفر لك مسارات تعليمية شاملة في مختلف المجالات البرمجية والتقنية. 
    اختر المسار الذي يناسبك من القائمة الجانبية وابدأ رحلة التعلم الآن!
    
    ✨ **المميزات:**
    - ✅ مسارات متكاملة من المستوى المبتدئ إلى المتقدم
    - 🌍 محتوى عربي وإنجليزي
    - 📊 تتبع التقدم والإحصائيات
    - 🏆 شهادات عند إكمال كل مسار
    - 💼 مشاريع عملية واقعية
    
    ---
    
    ### 📍 ابدأ رحلتك الآن
    
    اضغط على أحد المسارات من القائمة الجانبية واختر ما يناسبك! 🚀
    """)

else:
    if st.session_state.page.startswith("track_"):
        tid = int(st.session_state.page.split("_")[1])
        track = tracks[tid]
        
        col_back, col_title, col_reset = st.columns([1, 3, 1])
        
        with col_back:
            if st.button("🔙 العودة للرئيسية", use_container_width=True):
                st.session_state.page = "home"
                st.rerun()
        
        with col_title:
            st.header(f"{track['name']}")
        
        with col_reset:
            if st.button("🔄 إعادة تعيين", use_container_width=True):
                reset_track(tid)
                st.rerun()
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info(f"📊 المستوى: {track['difficulty']}")
        with col2:
            st.info(f"⏱️ المدة: {track['duration']}")
        with col3:
            progress = get_progress_percentage(tid)
            st.info(f"✅ التقدم: {progress}%")
        
        with st.expander("📌 تعريف المسار", expanded=True):
            st.write(track["long_desc"])
        
        st.markdown("---")
        st.subheader("📚 خطوات التعلم (بالترتيب)")
        
        completed_count = 0
        for i, step in enumerate(track["steps"]):
            with st.container(border=True):
                col_num, col_title, col_duration = st.columns([1, 3, 2])
                with col_num:
                    st.markdown(f"### المرحلة {i+1}")
                with col_title:
                    st.markdown(f"### {step['title']}")
                with col_duration:
                    st.caption(f"⏱️ {step['duration']}")
                
                st.write(f"📝 **{step['desc']}**")
                
                tab1, tab2, tab3 = st.tabs(["🇸🇦 مصدر عربي", "🇬🇧 مصدر إنجليزي", "📊 إحصائيات"])
                
                with tab1:
                    col_btn, col_preview = st.columns([1, 2])
                    with col_btn:
                        st.link_button("▶️ ابدأ الآن", step["ar"], use_container_width=True)
                    with col_preview:
                        if st.checkbox("👁️ معاينة الفيديو", key=f"preview_ar_{tid}_{i}"):
                            embed_code = embed_youtube_video(step["ar"])
                            if embed_code:
                                st.components.v1.html(embed_code, height=400)
                            else:
                                st.warning("لا يمكن معاينة هذا الفيديو")
                
                with tab2:
                    col_btn, col_preview = st.columns([1, 2])
                    with col_btn:
                        st.link_button("▶️ Start Now", step["en"], use_container_width=True)
                    with col_preview:
                        if st.checkbox("👁️ Video Preview", key=f"preview_en_{tid}_{i}"):
                            embed_code = embed_youtube_video(step["en"])
                            if embed_code:
                                st.components.v1.html(embed_code, height=400)
                            else:
                                st.warning("Cannot preview this video")
                
                with tab3:
                    st.markdown(f"""
                    - **العنوان:** {step['title']}
                    - **المدة المتوقعة:** {step['duration']}
                    - **نوع المحتوى:** فيديو تعليمي
                    - **المستوى:** {'مبتدئ' if i == 0 else 'متوسط' if i == 1 else 'متقدم'}
                    """)
                
                is_checked = st.session_state.progress.get(tid, {}).get(i, False)
                checked = st.checkbox("✅ تم إكمال هذه المرحلة", value=is_checked, key=f"chk_{tid}_{i}", label_visibility="visible")
                
                if checked != is_checked:
                    mark_completed(tid, i, checked)
                    st.rerun()
                
                if checked:
                    completed_count += 1
                    st.success("🎉 مرحلة مكتملة!")
        
        st.markdown("---")
        total = len(track["steps"])
        percent = int(completed_count / total * 100) if total else 0
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### 📊 تقدمك: {completed_count} من {total} مرحلة مكتملة")
            st.progress(percent / 100)
        with col2:
            st.metric("نسبة الإنجاز", f"{percent}%")
        
        if completed_count == total and total > 0:
            st.balloons()
            st.success(f"🎉 **تهانينا!** لقد أكملت مسار **{track['name']}** بالكامل!")
            
            with st.container(border=True):
                st.markdown(f"""
                ### 🏆 شهادة إنجاز
                
                تم منح هذه الشهادة إلى: **{st.session_state.user_name if st.session_state.user_name else 'الطالب المجتهد'}**
                
                لإكماله مسار: **{track['name']}**
                
                التاريخ: **{datetime.now().strftime('%Y-%m-%d')}**
                
                _جميع الحقوق محفوظة لمنصة التعلم 2026_
                """)
                
                if st.button("🖨️ طباعة الشهادة"):
                    st.balloons()
                    st.info("تم نسخ الشهادة! يمكنك طباعتها من المتصفح (Ctrl+P)")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888;">
    <p>⚡ProgrammingRoadmap🕸⚡</p>
    <p>✨By:𝑪𝒚𝒃𝒆𝒓 𝑴𝒊𝒏𝒅𝒔✨</p>
</div>
""", unsafe_allow_html=True)