import io
import urllib.parse
import streamlit as st
from docx import Document
from pptx import Presentation

# ==========================================
# 1. PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="Competitive Exam Prep & Goal Hub",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .exam-card {
        background-color: #1E222D;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #2E3440;
        margin-bottom: 20px;
    }
    .yt-btn {
        display: inline-block;
        background-color: #FF0000;
        color: white !important;
        padding: 10px 18px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .yt-btn:hover { background-color: #CC0000; text-decoration: none; }
    .download-btn {
        display: inline-block;
        background-color: #2563EB;
        color: white !important;
        padding: 8px 16px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 600;
        font-size: 14px;
        margin-top: 8px;
    }
    .download-btn:hover { background-color: #1D4ED8; text-decoration: none; }
    .official-btn {
        display: inline-block;
        background-color: #10B981;
        color: white !important;
        padding: 10px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .official-btn:hover { background-color: #059669; text-decoration: none; }
    .roadmap-step {
        border-left: 4px solid #22C55E;
        padding-left: 15px;
        margin-bottom: 15px;
    }
    .share-btn-wa {
        display: inline-block;
        background-color: #25D366;
        color: white !important;
        padding: 10px 16px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-right: 10px;
    }
    .share-btn-email {
        display: inline-block;
        background-color: #EA4335;
        color: white !important;
        padding: 10px 16px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# 2. HELPER FUNCTIONS FOR DOCX & PPTX GENERATION
# ==========================================
def create_docx_plan(exam_name, daily_hours, prep_months, plan_text):
    doc = Document()
    doc.add_heading(f"Study Goal Plan: {exam_name}", level=0)
    doc.add_paragraph(f"Target Exam: {exam_name}")
    doc.add_paragraph(f"Preparation Timeline: {prep_months} Months")
    doc.add_paragraph(f"Daily Allocated Time: {daily_hours} Hours")
    doc.add_heading("Detailed Strategy & Timetable", level=1)
    
    for line in plan_text.split('\n'):
        if line.strip():
            doc.add_paragraph(line.strip())
            
    bio = io.BytesIO()
    doc.save(bio)
    bio.seek(0)
    return bio

def create_pptx_plan(exam_name, daily_hours, prep_months, plan_text):
    prs = Presentation()
    
    # Title Slide
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = f"Study Goal Plan\n{exam_name}"
    subtitle.text = f"Timeline: {prep_months} Months | Daily Study: {daily_hours} Hours"
    
    # Plan Details Slide
    bullet_slide_layout = prs.slide_layouts[1]
    slide2 = prs.slides.add_slide(bullet_slide_layout)
    shapes = slide2.shapes
    title_shape = shapes.title
    body_shape = shapes.placeholders[1]
    title_shape.text = "Personalized Schedule & Strategy"
    
    tf = body_shape.text_frame
    tf.word_wrap = True
    
    lines = [l.strip() for l in plan_text.split('\n') if l.strip()]
    for i, line in enumerate(lines[:10]):  # Fit core bullet points onto the slide
        p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
        p.text = line
        p.level = 0
        
    bio = io.BytesIO()
    prs.save(bio)
    bio.seek(0)
    return bio


# ==========================================
# 3. EXAMS DATA (EXPANDED SSC COLLECTION)
# ==========================================
EXAMS_DATA = {
    "SSC CGL": {
        "full_name": "SSC Combined Graduate Level",
        "icon": "🏛️",
        "category": "SSC Group B & C",
        "description": "Premier exam for Inspector, Assistant Section Officer, and Tax Assistant posts.",
        "official_pyq_portal": "https://ssc.gov.in/",
        "roadmap": [
            "**Phase 1: Concepts & Core Math (Months 1-3):** Cover Advance & Arithmetic Maths, English Grammar rules, and Reasoning topics.",
            "**Phase 2: Speed Building & PYQs (Months 4-5):** Solve 5,000+ Previous Year Questions (PYQs) with speed tricks.",
            "**Phase 3: Tier-1 & Tier-2 Mock Drills (Month 6):** Daily sectional tests, full mocks, and typing practice."
        ],
        "top_teachers": [
            {
                "subject": "Quantitative Aptitude",
                "teacher": "Gagan Pratap Sir / Aditya Ranjan Sir",
                "channel": "Gagan Pratap Maths / Rankers Gurukul",
                "video_title": "SSC CGL Complete Maths Marathon",
                "youtube_link": "https://www.youtube.com/results?search_query=ssc+cgl+maths+gagan+pratap+marathon"
            },
            {
                "subject": "English Language",
                "teacher": "Nimisha Bansal / Rani Ma'am",
                "channel": "Nimisha Bansal / English With Rani Ma'am",
                "video_title": "120 Rules of Grammar Complete Marathon",
                "youtube_link": "https://www.youtube.com/results?search_query=120+rules+of+grammar+nimisha+bansal"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "SSC CGL Tier-1 All Shift Question Papers", "link": "https://ssc.gov.in/", "format": "PDF Archive"},
            {"year": "2023", "title": "SSC CGL Tier-2 (Mains) Official Question Paper", "link": "https://ssc.gov.in/", "format": "PDF Archive"}
        ],
        "quiz": [
            {
                "question": "Which article of the Indian Constitution empowers the President to declare a National Emergency?",
                "options": ["Article 352", "Article 356", "Article 360", "Article 370"],
                "answer": "Article 352",
                "explanation": "Article 352 deals with National Emergency."
            }
        ]
    },
    "SSC CHSL": {
        "full_name": "SSC Combined Higher Secondary Level",
        "icon": "📜",
        "category": "SSC 10+2 Level",
        "description": "Recruitment exam for Lower Division Clerk (LDC), JSA, and Data Entry Operators (DEO).",
        "official_pyq_portal": "https://ssc.gov.in/",
        "roadmap": [
            "**Phase 1: Syllabus Overview (Months 1-2):** Master Class 10th level Quantitative Aptitude, Basic English, and Logical Reasoning.",
            "**Phase 2: PYQ Drill & Speed Practice (Months 3-4):** Solve CHSL papers from the last 5 years.",
            "**Phase 3: Mocks & Typing Speed (Month 5):** Conduct full-length tests and daily typing practice."
        ],
        "top_teachers": [
            {
                "subject": "Reasoning Ability",
                "teacher": "Vikramjeet Sir",
                "channel": "Rankers Gurukul",
                "video_title": "SSC CHSL Reasoning Complete Playlist",
                "youtube_link": "https://www.youtube.com/results?search_query=ssc+chsl+reasoning+vikramjeet+sir"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "SSC CHSL Tier-1 Papers", "link": "https://ssc.gov.in/", "format": "PDF"}
        ],
        "quiz": [
            {
                "question": "What is the capital of Dadra and Nagar Haveli and Daman and Diu?",
                "options": ["Daman", "Silvassa", "Kavaratti", "Port Blair"],
                "answer": "Daman",
                "explanation": "Daman was declared the capital of the merged UT in 2020."
            }
        ]
    },
    "SSC GD": {
        "full_name": "SSC General Duty Constable",
        "icon": "🪖",
        "category": "SSC Defense & Paramilitary",
        "description": "Entrance for Constables in BSF, CISF, CRPF, SSB, ITBP, AR, and SSF.",
        "official_pyq_portal": "https://ssc.gov.in/",
        "roadmap": [
            "**Phase 1: Basics of Elementary Maths & Hindi/English (Months 1-2):** Practice basic arithmetic and grammar fundamentals.",
            "**Phase 2: GK/GS & Reasoning Drills (Months 3-4):** Focus on Static GK, Current Affairs, and Non-Verbal Reasoning.",
            "**Phase 3: Practice Tests & Physical Prep (Month 5):** Take online CBT speed mocks alongside morning physical training."
        ],
        "top_teachers": [
            {
                "subject": "General Studies & Hindi",
                "teacher": "Naveen Sir / Ankit Bhati Sir",
                "channel": "Rojgar with Ankit",
                "video_title": "SSC GD Complete Hindi & GS Practice",
                "youtube_link": "https://www.youtube.com/results?search_query=ssc+gd+rojgar+with+ankit"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "SSC GD Constable Official Shifts Paper", "link": "https://ssc.gov.in/", "format": "PDF"}
        ],
        "quiz": [
            {
                "question": "Which dance form originates from the state of Assam?",
                "options": ["Bihu", "Kathak", "Garba", "Ghoomar"],
                "answer": "Bihu",
                "explanation": "Bihu is the folk dance of Assam associated with the Bihu festival."
            }
        ]
    },
    "SSC JE": {
        "full_name": "SSC Junior Engineer (Civil, Electrical, Mechanical)",
        "icon": "🏗️",
        "category": "SSC Technical Engineering",
        "description": "Recruitment exam for Junior Engineers in CPWD, CWP&PRS, MES, and Central Water Commission.",
        "official_pyq_portal": "https://ssc.gov.in/",
        "roadmap": [
            "**Phase 1: Technical Engineering Fundamentals (Months 1-4):** Strengthen core concepts in Civil, Electrical, or Mechanical engineering.",
            "**Phase 2: Non-Tech Preparation (Months 5-6):** Prepare General Intelligence, Reasoning, and General Awareness.",
            "**Phase 3: Paper 1 CBT & Paper 2 Subjective Practice (Months 7-8):** Practice past 10-year JE papers and mock tests."
        ],
        "top_teachers": [
            {
                "subject": "Technical Engineering Subjects",
                "teacher": "Engineers Academy / Adda247 Technical",
                "channel": "Engineers Academy",
                "video_title": "SSC JE Complete Technical Revision",
                "youtube_link": "https://www.youtube.com/results?search_query=ssc+je+technical+revision"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "SSC JE Paper-1 (CBT) Official Question Paper", "link": "https://ssc.gov.in/", "format": "PDF"}
        ],
        "quiz": [
            {
                "question": "What is the SI unit of pressure?",
                "options": ["Pascal", "Joule", "Newton", "Watt"],
                "answer": "Pascal",
                "explanation": "Pascal (Pa) equals one newton per square meter."
            }
        ]
    },
    "SSC MTS": {
        "full_name": "SSC Multi-Tasking Staff & Havaldar",
        "icon": "📑",
        "category": "SSC 10th Level",
        "description": "Selection for non-technical General Central Service Group 'C' Posts.",
        "official_pyq_portal": "https://ssc.gov.in/",
        "roadmap": [
            "**Phase 1: Core Numerical Ability & Reasoning (Session 1) (Months 1-2):** Master fundamental math and logical reasoning.",
            "**Phase 2: English & General Awareness (Session 2) (Months 3-4):** Focus heavily on General Knowledge and English vocabulary, which determine selection.",
            "**Phase 3: Mock Tests & Revision (Month 5):** Take Session 1 & 2 full-length online computer-based tests."
        ],
        "top_teachers": [
            {
                "subject": "General Awareness & English",
                "teacher": "MTS Special Educators",
                "channel": "SSC Adda247 / Testbook",
                "video_title": "SSC MTS General Knowledge & English Revision",
                "youtube_link": "https://www.youtube.com/results?search_query=ssc+mts+gk+english+preparation"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "SSC MTS All Shift Question Papers", "link": "https://ssc.gov.in/", "format": "PDF Archive"}
        ],
        "quiz": [
            {
                "question": "Who was the first Governor-General of Independent India?",
                "options": ["Lord Mountbatten", "C. Rajagopalachari", "Dr. Rajendra Prasad", "Jawaharlal Nehru"],
                "answer": "Lord Mountbatten",
                "explanation": "Lord Mountbatten was the last Viceroy and first Governor-General of independent India."
            }
        ]
    },
    "UPSC CSE": {
        "full_name": "UPSC Civil Services Examination",
        "icon": "⚖️",
        "category": "Civil Services",
        "description": "Preparation roadmap for IAS, IPS, IFS, and Central Services.",
        "official_pyq_portal": "https://www.upsc.gov.in/examinations/previous-question-papers",
        "roadmap": [
            "**Phase 1: NCERT Foundations (Months 1-3):** Read Class 6-12 NCERTs for History, Geography, Polity, and Economy.",
            "**Phase 2: Standard Books & Optional Subject (Months 4-8):** Study Laxmikanth (Polity) and Spectrum.",
            "**Phase 3: Answer Writing & Mocks (Months 9-12):** Daily GS answer writing practice and Prelims mocks."
        ],
        "top_teachers": [
            {
                "subject": "Indian Polity",
                "teacher": "Dr. Vikas Divyakirti",
                "channel": "Drishti IAS",
                "video_title": "Indian Polity Complete Concept Series",
                "youtube_link": "https://www.youtube.com/results?search_query=upsc+polity+drishti+ias"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "UPSC CSE Prelims General Studies (Paper-I & CSAT)", "link": "https://www.upsc.gov.in/", "format": "Official PDF"}
        ],
        "quiz": [
            {
                "question": "Which Schedule of the Indian Constitution contains the anti-defection law?",
                "options": ["8th Schedule", "9th Schedule", "10th Schedule", "11th Schedule"],
                "answer": "10th Schedule",
                "explanation": "The 10th Schedule was added by the 52nd Amendment Act in 1985."
            }
        ]
    },
    "NEET UG": {
        "full_name": "National Eligibility cum Entrance Test",
        "icon": "🩺",
        "category": "Medical Entrance",
        "description": "Targeted learning path for MBBS/BDS entrance aspirants.",
        "official_pyq_portal": "https://neet.nta.nic.in/document-category/archive/",
        "roadmap": [
            "**Phase 1: NCERT Mastery (Months 1-6):** Line-by-line reading of Class 11 & 12 NCERT Biology, Chemistry, and Physics.",
            "**Phase 2: Problem Solving (Months 7-9):** Practice Physics numericals daily.",
            "**Phase 3: Mock Testing (Months 10-12):** Solve 15-year PYQs and speed tests."
        ],
        "top_teachers": [
            {
                "subject": "Biology",
                "teacher": "Dr. Anand Mani",
                "channel": "Dr. Anand Mani",
                "video_title": "Complete NCERT Biology One-Shot",
                "youtube_link": "https://www.youtube.com/results?search_query=neet+biology+one+shot"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "NEET UG Official Question Paper", "link": "https://neet.nta.nic.in/", "format": "Official NTA PDF"}
        ],
        "quiz": [
            {
                "question": "Which organelle is known as the powerhouse of the cell?",
                "options": ["Ribosome", "Mitochondria", "Golgi Apparatus", "Lysosome"],
                "answer": "Mitochondria",
                "explanation": "Mitochondria produce ATP."
            }
        ]
    },
    "JEE Main & Advanced": {
        "full_name": "Joint Entrance Examination",
        "icon": "📐",
        "category": "Engineering Entrance",
        "description": "Preparation pathway for IITs, NITs, and top engineering institutions.",
        "official_pyq_portal": "https://nta.ac.in/Downloads",
        "roadmap": [
            "**Phase 1: Conceptual Clarity (Months 1-6):** Master Mechanics, Organic Chemistry, and Calculus.",
            "**Phase 2: Advanced Problem Solving (Months 7-10):** Solve HC Verma and MS Chouhan.",
            "**Phase 3: CBT Mocks (Months 11-12):** Practice computer-based mock tests."
        ],
        "top_teachers": [
            {
                "subject": "Mathematics",
                "teacher": "NV Sir",
                "channel": "Unacademy Atoms",
                "video_title": "BounceBack Series - Complete JEE Maths",
                "youtube_link": "https://www.youtube.com/results?search_query=bounceback+maths+nv+sir"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "JEE Main Session 1 & Session 2 Papers", "link": "https://nta.ac.in/Downloads", "format": "Official NTA PDF"}
        ],
        "quiz": [
            {
                "question": "What is the derivative of sin(x^2) with respect to x?",
                "options": ["2x * cos(x^2)", "cos(x^2)", "-2x * cos(x^2)", "2 * sin(x)"],
                "answer": "2x * cos(x^2)",
                "explanation": "Chain rule application."
            }
        ]
    }
}


# ==========================================
# 4. SIDEBAR - EXAM SLIDER SELECTOR
# ==========================================
st.sidebar.title("🎓 Navigation & Selection")
st.sidebar.markdown("### 🎛️ Select Your Targeted Exam")

exam_list = list(EXAMS_DATA.keys())

# Sidebar select slider featuring all SSC exams
selected_exam_name = st.sidebar.select_slider(
    "Slide to select exam:",
    options=exam_list,
    value=exam_list[0],
    format_func=lambda exam: f"{EXAMS_DATA[exam]['icon']} {exam}"
)

exam_info = EXAMS_DATA[selected_exam_name]

st.sidebar.markdown("---")
st.sidebar.info(f"**Selected:** {exam_info['full_name']}\n\n**Category:** {exam_info['category']}")


# ==========================================
# 5. MAIN CONTENT & TABS NAVIGATION
# ==========================================
st.title("🎓 All-in-One Competitive Exam Prep Hub")
st.header(f"{exam_info['icon']} {selected_exam_name}")
st.write(f"**Full Title:** {exam_info['full_name']}")
st.write(f"**Category:** {exam_info['category']}")
st.info(exam_info['description'])

tab_roadmap, tab_content, tab_pyqs, tab_quiz, tab_custom = st.tabs([
    "🗺️ Preparation Roadmap", 
    "📺 Free Lectures", 
    "📄 PYQ Downloads", 
    "📝 MCQ Practice Quiz",
    "🤖 Custom Goal Planner"
])

# TAB 1: ROADMAP
with tab_roadmap:
    st.subheader(f"📌 Step-by-Step Preparation Strategy - {selected_exam_name}")
    for step in exam_info["roadmap"]:
        st.markdown(f"<div class='roadmap-step'>{step}</div>", unsafe_allow_html=True)

# TAB 2: TEACHERS
with tab_content:
    st.subheader(f"📺 Top Free Content & Video Links - {selected_exam_name}")
    cols = st.columns(2)
    for idx, item in enumerate(exam_info["top_teachers"]):
        col = cols[idx % 2]
        with col:
            st.markdown(f"#### 📖 {item['subject']}")
            st.write(f"👨‍🏫 **Educator:** {item['teacher']}")
            st.write(f"📢 **Channel:** {item['channel']}")
            st.markdown(
                f'<a href="{item["youtube_link"]}" target="_blank" class="yt-btn">▶️ Watch Live on YouTube</a>',
                unsafe_allow_html=True
            )
            st.write("")

# TAB 3: PYQs
with tab_pyqs:
    st.subheader(f"📄 PYQ Download Papers - {selected_exam_name}")
    st.markdown(
        f'<a href="{exam_info["official_pyq_portal"]}" target="_blank" class="official-btn">🌐 Open Official Portal</a>',
        unsafe_allow_html=True
    )
    for pyq in exam_info["pyqs"]:
        st.markdown(f"### 🗓️ {pyq['year']} - {pyq['title']}")
        st.markdown(f'<a href="{pyq["link"]}" target="_blank" class="download-btn">📥 Access Paper</a>', unsafe_allow_html=True)
        st.markdown("---")

# TAB 4: QUIZ
with tab_quiz:
    st.subheader(f"📝 Practice Quiz - {selected_exam_name}")
    quiz_questions = exam_info.get("quiz", [])
    if quiz_questions:
        with st.form(key=f"quiz_form_{selected_exam_name}"):
            user_answers = {}
            for q_idx, q_data in enumerate(quiz_questions):
                st.markdown(f"#### Q{q_idx + 1}: {q_data['question']}")
                user_answers[q_idx] = st.radio(
                    f"Select answer for Q{q_idx + 1}:",
                    options=q_data["options"],
                    key=f"q_{selected_exam_name}_{q_idx}",
                    index=None
                )
            submit_quiz = st.form_submit_button("🏆 Submit & View Score")

        if submit_quiz:
            score = sum([1 for i, q in enumerate(quiz_questions) if user_answers.get(i) == q["answer"]])
            st.success(f"🎯 Your Score: {score} / {len(quiz_questions)}")

# TAB 5: AI CUSTOM GOAL PLANNER & EXPORTS
with tab_custom:
    st.subheader(f"🤖 Generate & Export Customized Goal Plan for {selected_exam_name}")
    
    col_a, col_b = st.columns(2)
    daily_hours = col_a.slider("Daily study capacity (Hours):", 2, 14, 6)
    prep_months = col_b.slider("Months remaining for exam:", 1, 24, 6)
    api_key = st.text_input("🔑 Groq API Key (Optional)", type="password")

    if st.button("🚀 Generate Goal Plan"):
        if not api_key:
            plan_content = f"""Target Exam: {selected_exam_name} ({exam_info['full_name']})
Timeline: {prep_months} Months Out | Daily Schedule: {daily_hours} Hours

• Slot 1 ({int(daily_hours * 0.4)} hrs): Core Subject / Primary Technical / Advance Concepts.
• Slot 2 ({int(daily_hours * 0.3)} hrs): Secondary Subject & PYQ Practice Drills.
• Slot 3 ({int(daily_hours * 0.2)} hrs): Speed Mock Tests & Error Analysis.
• Slot 4 ({round(daily_hours * 0.1, 1)} hrs): Daily General Awareness / Current Affairs & Formula Review."""
        else:
            try:
                from groq import Groq
                client = Groq(api_key=api_key)
                prompt = f"Create a structured daily study plan for {selected_exam_name} ({exam_info['full_name']}) with {daily_hours} hours available daily and {prep_months} months remaining."
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}]
                )
                plan_content = response.choices[0].message.content
            except Exception as e:
                st.error(f"Error calling Groq API: {str(e)}")
                plan_content = "Default Goal Plan Generated."

        st.session_state['generated_plan'] = plan_content
        st.session_state['plan_exam'] = selected_exam_name
        st.session_state['plan_hours'] = daily_hours
        st.session_state['plan_months'] = prep_months

    # Display generated plan and export/share tools if present
    if 'generated_plan' in st.session_state:
        st.markdown("---")
        st.markdown("### 📋 Generated Study Plan")
        st.text_area("Your Custom Plan", st.session_state['generated_plan'], height=200)

        st.markdown("### 📥 Download Plan File")
        col_doc, col_ppt = st.columns(2)

        # Generate Word Document
        docx_file = create_docx_plan(
            st.session_state['plan_exam'],
            st.session_state['plan_hours'],
            st.session_state['plan_months'],
            st.session_state['generated_plan']
        )
        col_doc.download_button(
            label="📄 Download Word Doc (.docx)",
            data=docx_file,
            file_name=f"{st.session_state['plan_exam']}_Goal_Plan.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True
        )

        # Generate PowerPoint Presentation
        pptx_file = create_pptx_plan(
            st.session_state['plan_exam'],
            st.session_state['plan_hours'],
            st.session_state['plan_months'],
            st.session_state['generated_plan']
        )
        col_ppt.download_button(
            label="📊 Download PowerPoint (.pptx)",
            data=pptx_file,
            file_name=f"{st.session_state['plan_exam']}_Goal_Plan.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            use_container_width=True
        )

        st.markdown("### 📲 Share Goal Plan")
        
        # Prepare URL encoded messages
        share_text = f"My Study Goal Plan for {st.session_state['plan_exam']}:\n\n{st.session_state['generated_plan']}"
        encoded_text = urllib.parse.quote(share_text)
        
        whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_text}"
        email_url = f"mailto:?subject={urllib.parse.quote('My Study Goal Plan')}&body={encoded_text}"

        col_wa, col_em = st.columns(2)
        col_wa.markdown(
            f'<a href="{whatsapp_url}" target="_blank" class="share-btn-wa">💬 Share via WhatsApp</a>',
            unsafe_allow_html=True
        )
        col_em.markdown(
            f'<a href="{email_url}" target="_blank" class="share-btn-email">✉️ Share via Email</a>',
            unsafe_allow_html=True
        )
