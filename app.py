<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>منصة تعلم البرمجة | مسارات كاملة</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        body {
            background: linear-gradient(135deg, #f5f7fa 0%, #e9eef3 100%);
            padding: 20px;
            min-height: 100vh;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            margin-bottom: 10px;
            color: #2c3e50;
            font-size: 1.8rem;
        }
        .sub {
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 30px;
        }
        /* البطاقات */
        .tracks-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        .card {
            background: white;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.05);
            transition: transform 0.2s;
            cursor: pointer;
            border: 1px solid #ddd;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 30px rgba(0,0,0,0.1);
        }
        .card h2 {
            font-size: 1.5rem;
            margin-bottom: 10px;
        }
        .card p {
            color: #555;
            margin-bottom: 15px;
        }
        .btn-start {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 30px;
            cursor: pointer;
            font-size: 0.9rem;
            width: 100%;
            font-weight: bold;
        }
        /* صفحة المسار */
        .back-btn {
            background: none;
            border: none;
            font-size: 1rem;
            color: #3498db;
            cursor: pointer;
            margin-bottom: 20px;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }
        .track-header {
            background: white;
            border-radius: 20px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 5px 10px rgba(0,0,0,0.05);
        }
        .track-desc {
            background: #f0f7ff;
            padding: 15px;
            border-radius: 15px;
            margin: 15px 0;
            line-height: 1.6;
        }
        .step-card {
            background: white;
            border-radius: 18px;
            padding: 18px;
            margin-bottom: 20px;
            box-shadow: 0 3px 8px rgba(0,0,0,0.05);
            border-right: 5px solid #3498db;
        }
        .step-title {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 8px;
        }
        .step-desc {
            color: #555;
            margin-bottom: 15px;
            font-size: 0.9rem;
        }
        .sources {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 15px;
        }
        .btn-source {
            display: inline-block;
            background: #2c3e50;
            color: white;
            padding: 8px 16px;
            border-radius: 40px;
            text-decoration: none;
            font-size: 0.8rem;
            transition: 0.2s;
        }
        .btn-source.arabic {
            background: #27ae60;
        }
        .btn-source.english {
            background: #2980b9;
        }
        .check-label {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-top: 10px;
            cursor: pointer;
            font-size: 0.9rem;
        }
        .progress-bar {
            background: #ecf0f1;
            border-radius: 20px;
            height: 12px;
            margin: 20px 0;
            overflow: hidden;
        }
        .progress-fill {
            background: #27ae60;
            width: 0%;
            height: 100%;
            transition: width 0.3s;
        }
        .reset-btn {
            background: #e67e22;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 30px;
            cursor: pointer;
            margin-top: 10px;
            font-size: 0.8rem;
        }
        footer {
            text-align: center;
            margin-top: 40px;
            color: #7f8c8d;
            font-size: 0.8rem;
        }
        .hidden {
            display: none;
        }
        button, .btn-start, .reset-btn {
            touch-action: manipulation;
        }
    </style>
</head>
<body>
<div class="container" id="app"></div>

<script>
    // ======================= بيانات المنصة =======================
    const tracks = [
        {
            id: 1,
            name: "🐍 أساسيات البرمجة (Python)",
            shortDesc: "رحلة متكاملة لتعلم البرمجة من الصفر باستخدام Python",
            longDesc: "هذا المسار مخصص للمبتدئين تماماً. ستتعلم أساسيات البرمجة مثل المتغيرات، الجمل الشرطية، الحلقات، الدوال، والقوائم. اللغة المستخدمة هي Python لأنها الأسهل. بعد الانتهاء، ستكون قادراً على كتابة برامج بسيطة وحل مشكلات منطقية.",
            steps: [
                { title: "مقدمة في البرمجة والخوارزميات", desc: "فهم ما هي البرمجة، الخوارزميات، وكيف يعمل الكمبيوتر.", ar: "https://youtube.com/playlist?list=PL9YIYM2p5i5l3K6E7F8G9H0J1K2L3M4N5O", en: "https://youtube.com/playlist?list=PLhQjrBD2T381k8J6K7L9M0N1O2P3Q4R5S6T" },
                { title: "تعلم Python - الأساسيات", desc: "المتغيرات، أنواع البيانات، الجمل الشرطية، الحلقات، الدوال.", ar: "https://youtube.com/playlist?list=PLMYF6NkLrdNvVZ0yQ5yQ5yQ5yQ5yQ5yQ5", en: "https://youtube.com/playlist?list=PLXuTq7QK7l3sZ8Y9A0B1C2D3E4F5G6H7I8J" },
                { title: "مشروع عملي: تطبيق آلة حاسبة", desc: "تطبيق كل ما تعلمته في مشروع حقيقي.", ar: "https://youtube.com/playlist?list=PLA1B2C3D4E5F6G7H8I9J", en: "https://youtube.com/playlist?list=PLK1L2M3N4O5P6Q7R8S9T" }
            ]
        },
        {
            id: 2,
            name: "🌐 تطوير واجهات الويب (Frontend)",
            shortDesc: "من الصفر إلى الاحتراف في HTML، CSS، JavaScript و React",
            longDesc: "في هذا المسار ستتعلم بناء واجهات مواقع الويب الحديثة. نبدأ بـ HTML و CSS لإنشاء الهيكل والتصميم، ثم ننتقل إلى JavaScript لإضافة التفاعلية. أخيراً، نتعلم إطار عمل React لبناء تطبيقات متقدمة. مناسب لمن يعرف أساسيات البرمجة.",
            steps: [
                { title: "HTML5 و CSS3 - الأساسيات", desc: "بناء هيكل الصفحات وتنسيقها.", ar: "https://youtube.com/playlist?list=PLU7Z6L1Q5K9J8H7G6F5D4S3A2", en: "https://youtube.com/playlist?list=PL4cUxeGkcC9gB9fA8B7C6D5E4F3G2H1I0J" },
                { title: "JavaScript للمبتدئين", desc: "التعامل مع DOM، الأحداث، والوظائف الأساسية.", ar: "https://youtube.com/playlist?list=PL9YIYM2p5i5l3K6E7F8G9H0J1K2L3M4N5O", en: "https://youtube.com/playlist?list=PLillGF-RfqbYE6IkUi7n8F6Q8L7M9N0O1P" },
                { title: "React.js - بناء تطبيقات متقدمة", desc: "مكونات، حالة، خصائص، وتطبيق كامل.", ar: "https://youtube.com/playlist?list=PLA1B2C3D4E5F6G7H8I9J", en: "https://youtube.com/playlist?list=PLN3n1USn4xlmyw3ebBuZmknGKr6LhM2fB" }
            ]
        },
        {
            id: 3,
            name: "🗄️ قواعد البيانات (SQL)",
            shortDesc: "فهم قواعد البيانات العلائقية ولغة SQL من البداية",
            longDesc: "تعلم كيفية تصميم وإدارة قواعد البيانات باستخدام SQL. سنغطي إنشاء الجداول، الاستعلامات، الانضمامات، والفهارس. هذا المسار ضروري لأي مطور يريد بناء تطبيقات تعتمد على البيانات.",
            steps: [
                { title: "مقدمة في قواعد البيانات", desc: "ما هي قواعد البيانات؟ أنواعها، ومفاهيم أساسية.", ar: "https://youtube.com/playlist?list=PLXYZ1_2_3_4_5_6_7_8_9", en: "https://youtube.com/playlist?list=PLABC1_2_3_4_5_6_7_8_9" },
                { title: "SQL الأساسي - استعلامات وفلترة", desc: "SELECT, WHERE, ORDER BY, GROUP BY", ar: "https://youtube.com/playlist?list=PLDEF1_2_3_4_5_6_7_8_9", en: "https://youtube.com/playlist?list=PLGHI1_2_3_4_5_6_7_8_9" },
                { title: "Join وعلاقات بين الجداول", desc: "INNER JOIN, LEFT JOIN, تصميم قواعد بيانات.", ar: "https://youtube.com/playlist?list=PLJKL1_2_3_4_5_6_7_8_9", en: "https://youtube.com/playlist?list=PLMNO1_2_3_4_5_6_7_8_9" }
            ]
        }
    ];

    // تحميل التقدم من localStorage
    let progress = {};
    function loadProgress() {
        const saved = localStorage.getItem("learning_progress");
        if (saved) progress = JSON.parse(saved);
        else progress = {};
    }
    function saveProgress() {
        localStorage.setItem("learning_progress", JSON.stringify(progress));
    }
    function setStepCompleted(trackId, stepIndex, completed) {
        if (!progress[trackId]) progress[trackId] = {};
        progress[trackId][stepIndex] = completed;
        saveProgress();
        render(); // إعادة الرسم لتحديث النسبة
    }
    function resetTrackProgress(trackId) {
        if (progress[trackId]) delete progress[trackId];
        saveProgress();
        render();
    }

    // حالة العرض: 'tracks' أو معرف المسار
    let currentView = 'tracks';

    // دالة عرض الصفحة الرئيسية (البطاقات)
    function renderTracks() {
        let html = `<h1>🚀 منصة مسارات تعلم البرمجة</h1>
                    <div class="sub">اختر تخصصك وابدأ رحلة التعلم خطوة بخطوة</div>
                    <div class="tracks-grid">`;
        tracks.forEach(track => {
            html += `
                <div class="card" data-id="${track.id}">
                    <h2>${track.name}</h2>
                    <p>${track.shortDesc}</p>
                    <button class="btn-start" data-id="${track.id}">📖 عرض المسار</button>
                </div>
            `;
        });
        html += `</div><footer>📚 كل مسار يحتوي على خريطة متسلسلة + مصادر عربية وإنجليزية + شيكليست لحفظ التقدم</footer>`;
        document.getElementById("app").innerHTML = html;

        // ربط الأحداث
        document.querySelectorAll('.btn-start').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const id = parseInt(btn.getAttribute('data-id'));
                currentView = id;
                render();
            });
        });
    }

    // دالة عرض مسار محدد
    function renderTrack(trackId) {
        const track = tracks.find(t => t.id === trackId);
        if (!track) {
            currentView = 'tracks';
            render();
            return;
        }
        const trackProgress = progress[trackId] || {};
        let completedCount = 0;
        track.steps.forEach((_, idx) => {
            if (trackProgress[idx]) completedCount++;
        });
        const percent = track.steps.length ? (completedCount / track.steps.length) * 100 : 0;

        let html = `
            <button class="back-btn" id="backBtn">🔙 العودة إلى التخصصات</button>
            <div class="track-header">
                <h2>${track.name}</h2>
                <div class="track-desc">📖 ${track.longDesc}</div>
                <div class="progress-bar"><div class="progress-fill" style="width: ${percent}%;"></div></div>
                <div>📊 التقدم: ${completedCount} من ${track.steps.length} مرحلة (${Math.round(percent)}%)</div>
                <button class="reset-btn" id="resetTrackBtn">🔄 إعادة تعيين التقدم لهذا المسار</button>
            </div>
        `;

        track.steps.forEach((step, idx) => {
            const isChecked = trackProgress[idx] || false;
            html += `
                <div class="step-card">
                    <div class="step-title">${idx+1}. ${step.title}</div>
                    <div class="step-desc">📝 ${step.desc}</div>
                    <div class="sources">
                        <a href="${step.ar}" target="_blank" class="btn-source arabic">🇸🇴 مصدر عربي - ابدأ الآن</a>
                        <a href="${step.en}" target="_blank" class="btn-source english">🇬🇧 مصدر إنجليزي - Start Now</a>
                    </div>
                    <label class="check-label">
                        <input type="checkbox" class="step-check" data-step="${idx}" ${isChecked ? 'checked' : ''}>
                        ✅ تم إكمال هذه المرحلة
                    </label>
                </div>
            `;
        });

        if (percent === 100 && track.steps.length > 0) {
            html += `<div style="background: #d4edda; padding: 15px; border-radius: 20px; text-align: center; margin-top: 20px;">🎉 تهانينا! لقد أكملت هذا المسار بالكامل. 🎉</div>`;
        }

        document.getElementById("app").innerHTML = html;

        // ربط الأحداث
        document.getElementById("backBtn").addEventListener('click', () => {
            currentView = 'tracks';
            render();
        });
        document.getElementById("resetTrackBtn").addEventListener('click', () => {
            resetTrackProgress(trackId);
        });
        document.querySelectorAll('.step-check').forEach(chk => {
            chk.addEventListener('change', (e) => {
                const stepIndex = parseInt(chk.getAttribute('data-step'));
                setStepCompleted(trackId, stepIndex, chk.checked);
            });
        });
    }

    function render() {
        loadProgress();
        if (currentView === 'tracks') renderTracks();
        else renderTrack(currentView);
    }

    render();
</script>
</body>
</html>