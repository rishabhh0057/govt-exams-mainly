import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="Competitive Exam Prep & Quiz Hub",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for UI Enhancement
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
    .yt-btn:hover {
        background-color: #CC0000;
        text-decoration: none;
    }
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
    .download-btn:hover {
        background-color: #1D4ED8;
        text-decoration: none;
    }
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
    .official-btn:hover {
        background-color: #059669;
        text-decoration: none;
    }
    .roadmap-step {
        border-left: 4px solid #22C55E;
        padding-left: 15px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# 2. CURATED EXAM DATA, ROADMAPS, PYQS & QUIZZES
# ==========================================
EXAMS_DATA = {
    "SSC CGL / CHSL": {
        "full_name": "Staff Selection Commission (CGL / CHSL)",
        "icon": "🏛️",
        "category": "Government Jobs",
        "description": "Comprehensive preparation for central government non-technical posts.",
        "official_pyq_portal": "https://ssc.gov.in/",
        "roadmap": [
            "**Phase 1: Syllabus & Fundamentals (Months 1-3):** Master Quantitative Aptitude, English Grammar, Reasoning, and General Awareness basics.",
            "**Phase 2: Practice & Speed (Months 4-5):** Solve 5,000+ Previous Year Questions (PYQs) with speed math tricks.",
            "**Phase 3: Mock Testing & Revisions (Month 6):** Attempt full-length daily mocks and analyze weak topics."
        ],
        "top_teachers": [
            {
                "subject": "Quantitative Aptitude (Maths)",
                "teacher": "Gagan Pratap Sir / Aditya Ranjan Sir",
                "channel": "Gagan Pratap Maths / Rankers Gurukul",
                "video_title": "SSC CGL Complete Maths Marathon",
                "youtube_link": "https://www.youtube.com/results?search_query=ssc+cgl+maths+gagan+pratap+marathon"
            },
            {
                "subject": "English Language",
                "teacher": "Nimisha Bansal Ma'am / Rani Ma'am",
                "channel": "Nimisha Bansal / English With Rani Ma'am",
                "video_title": "120 Rules of Grammar Complete Marathon",
                "youtube_link": "https://www.youtube.com/results?search_query=120+rules+of+grammar+nimisha+bansal"
            },
            {
                "subject": "Reasoning Ability",
                "teacher": "Vikramjeet Sir",
                "channel": "Rankers Gurukul",
                "video_title": "Reasoning Complete Syllabus Revision",
                "youtube_link": "https://www.youtube.com/results?search_query=ssc+reasoning+rankers+gurukul"
            },
            {
                "subject": "General Awareness & GS",
                "teacher": "Parcham Classes / Parmar SSC",
                "channel": "Parmar SSC",
                "video_title": "Complete Static GK & History Series",
                "youtube_link": "https://www.youtube.com/results?search_query=parmar+ssc+static+gk"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "SSC CGL Tier-1 All Shift Question Papers with Answer Key", "link": "https://ssc.gov.in/", "format": "PDF Archive"},
            {"year": "2023", "title": "SSC CGL Tier-2 (Mains) Question Paper with Solutions", "link": "https://ssc.gov.in/", "format": "PDF Archive"},
            {"year": "2023", "title": "SSC CHSL Tier-1 Previous Year Paper Sets", "link": "https://ssc.gov.in/", "format": "PDF Archive"},
            {"year": "2022", "title": "SSC CGL Tier-1 & Tier-2 Master Question Bank (All Shifts)", "link": "https://ssc.gov.in/", "format": "PDF Archive"}
        ],
        "quiz": [
            {
                "question": "Which article of the Indian Constitution empowers the President to declare a National Emergency?",
                "options": ["Article 352", "Article 356", "Article 360", "Article 370"],
                "answer": "Article 352",
                "explanation": "Article 352 deals with National Emergency, Article 356 with President's Rule, and Article 360 with Financial Emergency."
            },
            {
                "question": "If A can complete a work in 12 days and B in 24 days, in how many days can they complete it together?",
                "options": ["6 days", "8 days", "10 days", "12 days"],
                "answer": "8 days",
                "explanation": "Combined rate = 1/12 + 1/24 = 3/24 = 1/8. So together they take 8 days."
            },
            {
                "question": "Select the synonym of 'CANDID':",
                "options": ["Frank", "Secretive", "Deceitful", "Reserved"],
                "answer": "Frank",
                "explanation": "'Candid' means truthful and straightforward; 'Frank' is its exact synonym."
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
            "**Phase 2: Standard Books & Optional Subject (Months 4-8):** Study Laxmikanth (Polity), Spectrum (Modern History), and finalize optional subject preparation.",
            "**Phase 3: Answer Writing & Prelims Mocks (Months 9-12):** Daily GS answer writing practice, current affairs revision, and 30+ Prelims mocks."
        ],
        "top_teachers": [
            {
                "subject": "Indian Polity",
                "teacher": "M. Laxmikanth Lectures / Dr. Vikas Divyakirti",
                "channel": "Drishti IAS / Unacademy IAS",
                "video_title": "Indian Polity Complete Concept Series",
                "youtube_link": "https://www.youtube.com/results?search_query=upsc+polity+drishti+ias"
            },
            {
                "subject": "Economics",
                "teacher": "Mrunal Patel Sir",
                "channel": "Mrunal Patel",
                "video_title": "Mrunal PCB Economy Series",
                "youtube_link": "https://www.youtube.com/results?search_query=mrunal+patel+economy+lectures"
            },
            {
                "subject": "Modern Indian History",
                "teacher": "Pratik Nayak Sir / Ojha Sir",
                "channel": "Unacademy / Ray Avadh Ojha",
                "video_title": "Complete Modern History for UPSC",
                "youtube_link": "https://www.youtube.com/results?search_query=modern+history+upsc+lecture"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "UPSC CSE Prelims General Studies (Paper-I & CSAT Paper-II)", "link": "https://www.upsc.gov.in/examinations/previous-question-papers", "format": "Official PDF"},
            {"year": "2024", "title": "UPSC CSE Mains General Studies (GS 1, GS 2, GS 3, GS 4)", "link": "https://www.upsc.gov.in/examinations/previous-question-papers", "format": "Official PDF"},
            {"year": "2023", "title": "UPSC CSE Prelims GS-1 & CSAT Question Papers", "link": "https://www.upsc.gov.in/examinations/previous-question-papers", "format": "Official PDF"},
            {"year": "2022", "title": "UPSC CSE Mains Optional Subject Papers", "link": "https://www.upsc.gov.in/examinations/previous-question-papers", "format": "Official PDF"}
        ],
        "quiz": [
            {
                "question": "Which Schedule of the Indian Constitution contains the anti-defection law?",
                "options": ["8th Schedule", "9th Schedule", "10th Schedule", "11th Schedule"],
                "answer": "10th Schedule",
                "explanation": "The 10th Schedule was added by the 52nd Constitutional Amendment Act, 1985, to address defection."
            },
            {
                "question": "The term 'repo rate' refers to the rate at which:",
                "options": ["RBI borrows from commercial banks", "RBI lends money to commercial banks against government securities", "Banks lend to public", "Banks borrow from international market"],
                "answer": "RBI lends money to commercial banks against government securities",
                "explanation": "Repo rate is the key benchmark interest rate at which the Reserve Bank of India lends short-term money to commercial banks."
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
            "**Phase 2: Problem Solving (Months 7-9):** Practice 100+ Physics numericals and Chemistry reaction mechanisms daily.",
            "**Phase 3: Mock Testing (Months 10-12):** Solve 15-year PYQs and full 3-hour speed tests."
        ],
        "top_teachers": [
            {
                "subject": "Biology",
                "teacher": "Dr. Tarun Kumar / Dr. Anand Mani",
                "channel": "Physics Wallah / Dr. Anand Mani",
                "video_title": "Complete NCERT Biology One-Shot",
                "youtube_link": "https://www.youtube.com/results?search_query=neet+biology+one+shot+pw"
            },
            {
                "subject": "Physics",
                "teacher": "Alakh Pandey Sir / MR Sir",
                "channel": "Physics Wallah",
                "video_title": "NEET Physics Complete Mechanics & Electrodynamics",
                "youtube_link": "https://www.youtube.com/results?search_query=neet+physics+mr+sir+one+shot"
            },
            {
                "subject": "Chemistry",
                "teacher": "Pankaj Sir / Sudhanshu Sir",
                "channel": "Physics Wallah - Competition Wallah",
                "video_title": "Organic & Inorganic Chemistry One-Shot",
                "youtube_link": "https://www.youtube.com/results?search_query=neet+chemistry+pankaj+sir+one+shot"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "NEET UG Official Question Paper (All Codes E, F, G, H)", "link": "https://neet.nta.nic.in/", "format": "Official NTA PDF"},
            {"year": "2023", "title": "NEET UG Question Paper with Answer Keys & Hints", "link": "https://neet.nta.nic.in/document-category/archive/", "format": "Official NTA PDF"},
            {"year": "2022", "title": "NEET UG Complete Solved Question Paper", "link": "https://neet.nta.nic.in/document-category/archive/", "format": "Official NTA PDF"},
            {"year": "2021", "title": "NEET UG Re-Exam & Main Question Sets", "link": "https://neet.nta.nic.in/document-category/archive/", "format": "Official NTA PDF"}
        ],
        "quiz": [
            {
                "question": "Which organelle is known as the powerhouse of the cell?",
                "options": ["Ribosome", "Mitochondria", "Golgi Apparatus", "Lysosome"],
                "answer": "Mitochondria",
                "explanation": "Mitochondria produce cellular energy in the form of ATP via aerobic respiration."
            },
            {
                "question": "What is the pH of human blood under normal physiological conditions?",
                "options": ["6.5 - 6.8", "7.0 - 7.2", "7.35 - 7.45", "8.0 - 8.5"],
                "answer": "7.35 - 7.45",
                "explanation": "Human blood is slightly alkaline with a tightly regulated normal pH range of 7.35 to 7.45."
            },
            {
                "question": "Unit of electric current is:",
                "options": ["Volt", "Ampere", "Ohm", "Watt"],
                "answer": "Ampere",
                "explanation": "Ampere (A) is the SI unit of electric current."
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
            "**Phase 1: Conceptual Clarity (Months 1-6):** Master core principles of Mechanics, Organic Chemistry, and Calculus.",
            "**Phase 2: Advanced Problem Solving (Months 7-10):** Solve Irodov / HC Verma (Physics) and MS Chouhan (Chemistry) problems.",
            "**Phase 3: CBT Mocks & Strategy (Months 11-12):** Practice computer-based mock tests with time management focus."
        ],
        "top_teachers": [
            {
                "subject": "Mathematics",
                "teacher": "NV Sir / Arvind Kalia Sir",
                "channel": "Unacademy Atoms / Vedantu JEE",
                "video_title": "BounceBack Series - Complete JEE Maths",
                "youtube_link": "https://www.youtube.com/results?search_query=bounceback+maths+nv+sir"
            },
            {
                "subject": "Physics",
                "teacher": "Nitin Sachan Sir / Vinay Shur Sir",
                "channel": "INSP / Vedantu JEE",
                "video_title": "JEE Advanced Physics Problem Solving",
                "youtube_link": "https://www.youtube.com/results?search_query=jee+advanced+physics+one+shot"
            },
            {
                "subject": "Chemistry",
                "teacher": "Sachin Rana / Anupam Gupta",
                "channel": "Unacademy JEE",
                "video_title": "Organic Chemistry Complete Mechanism",
                "youtube_link": "https://www.youtube.com/results?search_query=jee+chemistry+one+shot+bounceback"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "JEE Main Session 1 & Session 2 (All Shifts NTA Papers)", "link": "https://nta.ac.in/Downloads", "format": "Official NTA PDF"},
            {"year": "2024", "title": "JEE Advanced Paper 1 & Paper 2 Question Papers", "link": "https://jeeadv.ac.in/", "format": "Official IIT PDF"},
            {"year": "2023", "title": "JEE Main January & April Session Shifts Solved Archive", "link": "https://nta.ac.in/Downloads", "format": "Official NTA PDF"},
            {"year": "2022", "title": "JEE Advanced Official Paper-1 and Paper-2 Solutions", "link": "https://jeeadv.ac.in/", "format": "Official IIT PDF"}
        ],
        "quiz": [
            {
                "question": "What is the derivative of sin(x^2) with respect to x?",
                "options": ["2x * cos(x^2)", "cos(x^2)", "-2x * cos(x^2)", "2 * sin(x)"],
                "answer": "2x * cos(x^2)",
                "explanation": "Applying the Chain Rule: d/dx[sin(x^2)] = cos(x^2) * d/dx[x^2] = 2x * cos(x^2)."
            },
            {
                "question": "Which element has the highest electronegativity on the Pauling scale?",
                "options": ["Oxygen", "Chlorine", "Fluorine", "Nitrogen"],
                "answer": "Fluorine",
                "explanation": "Fluorine is the most electronegative element with a value of 3.98 on the Pauling scale."
            },
            {
                "question": "The dimensional formula for Force is:",
                "options": ["[M L T^-1]", "[M L T^-2]", "[M L^2 T^-2]", "[M^2 L T^-2]"],
                "answer": "[M L T^-2]",
                "explanation": "Force = Mass * Acceleration = M * (L / T^2) = [M L T^-2]."
            }
        ]
    },
    "Banking (IBPS / SBI PO)": {
        "full_name": "IBPS PO / SBI PO / RRB Exams",
        "icon": "🏦",
        "category": "Banking & Insurance",
        "description": "Fast-paced preparation for Probationary Officer and Clerk positions.",
        "official_pyq_portal": "https://www.ibps.in/",
        "roadmap": [
            "**Phase 1: Speed Building (Months 1-2):** Master Vedic Maths, Syllogisms, and Reading Comprehension.",
            "**Phase 2: High-Level Puzzles & DI (Months 3-4):** Solve complex seating arrangements and Data Interpretation sets.",
            "**Phase 3: Mains & General Awareness (Months 5-6):** Focus on Banking Awareness, Current Affairs, and Mains sectional mocks."
        ],
        "top_teachers": [
            {
                "subject": "Quantitative Aptitude & DI",
                "teacher": "Arun Singh Rawat / Ashish Arora",
                "channel": "Bankers Way / Studified",
                "video_title": "Complete Data Interpretation & Speed Maths",
                "youtube_link": "https://www.youtube.com/results?search_query=banking+quant+ashish+arora"
            },
            {
                "subject": "Reasoning & Puzzles",
                "teacher": "Ankur Lamba / Puneet Kumar Sharma",
                "channel": "Bankers Way",
                "video_title": "100 Puzzles Series for Bank Exams",
                "youtube_link": "https://www.youtube.com/results?search_query=puneet+sir+reasoning+puzzles"
            },
            {
                "subject": "General & Banking Awareness",
                "teacher": "Ashish Gautam Sir",
                "channel": "Adda247",
                "video_title": "Daily Current Affairs & Banking Awareness",
                "youtube_link": "https://www.youtube.com/results?search_query=ashish+gautam+current+affairs+adda247"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "SBI PO Prelims Memory-Based Solved Paper", "link": "https://www.sbi.co.in/web/careers", "format": "PDF Memory Paper"},
            {"year": "2023", "title": "IBPS PO Mains Complete Memory-Based Paper", "link": "https://www.ibps.in/", "format": "PDF Memory Paper"},
            {"year": "2023", "title": "IBPS RRB PO & Clerk Officer Scale-1 Question Sets", "link": "https://www.ibps.in/", "format": "PDF Memory Paper"},
            {"year": "2022", "title": "SBI Clerk Mains Sectional PYQ Question Sets", "link": "https://www.sbi.co.in/web/careers", "format": "PDF Memory Paper"}
        ],
        "quiz": [
            {
                "question": "What does 'S' stand for in 'RTGS'?",
                "options": ["Settlement", "System", "Service", "Securities"],
                "answer": "Settlement",
                "explanation": "RTGS stands for Real Time Gross Settlement."
            }
        ]
    },
    "GATE (Engineering)": {
        "full_name": "Graduate Aptitude Test in Engineering",
        "icon": "⚙️",
        "category": "Post-Graduate / PSU",
        "description": "Preparation for M.Tech admissions and Public Sector Undertaking jobs.",
        "official_pyq_portal": "https://gate.iitk.ac.in/",
        "roadmap": [
            "**Phase 1: Core Subjects (Months 1-5):** Complete foundational technical subjects and Engineering Mathematics.",
            "**Phase 2: PYQ Solving (Months 6-8):** Practice 20-year GATE PYQs to understand formula application.",
            "**Phase 3: Test Series (Months 9-10):** Attempt subject-wise and full-length online test series."
        ],
        "top_teachers": [
            {
                "subject": "Engineering Mathematics & Aptitude",
                "teacher": "Umesh Dhande Sir / Shrenik Jain",
                "channel": "Gate Academy / Unacademy GATE",
                "video_title": "Engineering Maths Complete Revision",
                "youtube_link": "https://www.youtube.com/results?search_query=gate+engineering+mathematics+one+shot"
            },
            {
                "subject": "Core Engineering Branches",
                "teacher": "Ravindra Babu Ravula / Gate Academy Team",
                "channel": "RBR GATE / Gate Academy",
                "video_title": "Core Technical Subject Marathons",
                "youtube_link": "https://www.youtube.com/results?search_query=gate+pyq+marathon+lecture"
            }
        ],
        "pyqs": [
            {"year": "2024", "title": "GATE Official Question Papers & Master Keys (All Branches CS, EC, EE, ME, CE)", "link": "https://gate2024.iisc.ac.in/", "format": "Official IIT PDF"},
            {"year": "2023", "title": "GATE Official Question Paper and Answer Key Archive", "link": "https://gate.iitk.ac.in/", "format": "Official IIT PDF"},
            {"year": "2022", "title": "GATE Official Branch-Wise Master Papers", "link": "https://gate.iitkgp.ac.in/", "format": "Official IIT PDF"},
            {"year": "2021", "title": "GATE Official Solved Question Papers", "link": "https://gate.iitb.ac.in/", "format": "Official IIT PDF"}
        ],
        "quiz": [
            {
                "question": "What is the time complexity of searching an element in a balanced Binary Search Tree (BST)?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "answer": "O(log n)",
                "explanation": "In a balanced BST, the height is log(n), making search operations O(log n)."
            }
        ]
    }
}


# ==========================================
# 3. APP HEADER & SLIDER SELECTOR
# ==========================================
st.title("🎓 All-in-One Competitive Exam Prep Hub")
st.caption("Select your targeted exam below to unlock curated teacher content, structured roadmaps, PYQs download links, interactive quizzes, and instant YouTube learning links.")

st.markdown("### 🎛️ Select Your Targeted Exam")

exam_list = list(EXAMS_DATA.keys())

# Safe select slider implementation preventing type mismatch errors
selected_exam_name = st.select_slider(
    "Slide to browse exams:",
    options=exam_list,
    value=exam_list[0],
    format_func=lambda exam: f"{EXAMS_DATA[exam]['icon']} {exam}"
)

exam_info = EXAMS_DATA[selected_exam_name]

st.markdown("---")


# ==========================================
# 4. EXAM OVERVIEW & TABS NAVIGATION
# ==========================================
st.header(f"{exam_info['icon']} {selected_exam_name}")
st.write(f"**Full Title:** {exam_info['full_name']}")
st.write(f"**Category:** {exam_info['category']}")
st.info(exam_info['description'])

# Tabs for Structured Navigation
tab_roadmap, tab_content, tab_pyqs, tab_quiz, tab_custom = st.tabs([
    "🗺️ Complete Preparation Roadmap", 
    "📺 Best Free Teachers & Video Links", 
    "📄 PYQ Download Papers", 
    "📝 Practice MCQ Quiz",
    "🤖 AI Custom Study Planner"
])

# TAB 1: ROADMAP
with tab_roadmap:
    st.subheader("📌 Step-by-Step Preparation Strategy")
    for step in exam_info["roadmap"]:
        st.markdown(f"<div class='roadmap-step'>{step}</div>", unsafe_allow_html=True)

# TAB 2: TEACHERS & YOUTUBE LINKS
with tab_content:
    st.subheader("📺 Top Free Content & Video Links")
    st.caption("Click any button below to immediately open the best lecture series on YouTube in a new tab.")

    cols = st.columns(2)
    for idx, item in enumerate(exam_info["top_teachers"]):
        col = cols[idx % 2]
        with col:
            with st.container():
                st.markdown(f"#### 📖 {item['subject']}")
                st.write(f"👨‍🏫 **Recommended Educator:** {item['teacher']}")
                st.write(f"📢 **Channel:** {item['channel']}")
                st.write(f"🎥 **Series:** {item['video_title']}")
                
                # Direct YouTube Link Button
                st.markdown(
                    f'<a href="{item["youtube_link"]}" target="_blank" class="yt-btn">▶️ Watch Live on YouTube</a>',
                    unsafe_allow_html=True
                )
                st.write("")
                st.write("")

# TAB 3: PYQ DOWNLOAD PAPERS
with tab_pyqs:
    st.subheader(f"📄 Previous Year Question Papers (PYQs) - {selected_exam_name}")
    st.caption("Download official question papers, answer keys, and memory-based papers for practice.")

    # Official Download Portal Banner Button
    st.markdown(
        f'<a href="{exam_info["official_pyq_portal"]}" target="_blank" class="official-btn">🌐 Open Official {selected_exam_name} Download Portal</a>',
        unsafe_allow_html=True
    )
    st.write("")

    # Filter / Search within PYQs
    search_pyq = st.text_input("🔍 Search PYQ by Year or Title:", placeholder="e.g. 2024 or Prelims")

    pyq_list = exam_info["pyqs"]
    if search_pyq:
        pyq_list = [p for p in pyq_list if search_pyq.lower() in p["title"].lower() or search_pyq in p["year"]]

    if pyq_list:
        cols_pyq = st.columns(2)
        for idx, pyq in enumerate(pyq_list):
            col = cols_pyq[idx % 2]
            with col:
                st.markdown(f"### 🗓️ {pyq['year']} - {pyq['title']}")
                st.write(f"🏷️ **Format:** {pyq['format']}")
                st.markdown(
                    f'<a href="{pyq["link"]}" target="_blank" class="download-btn">📥 Download / Access Question Paper</a>',
                    unsafe_allow_html=True
                )
                st.markdown("---")
    else:
        st.warning("No question papers matched your search filter. Try searching for a different year.")

# TAB 4: INTERACTIVE MCQ QUIZ
with tab_quiz:
    st.subheader(f"📝 Interactive MCQ Practice Quiz - {selected_exam_name}")
    st.caption("Test your concepts with instant evaluation, feedback, and explanations.")

    quiz_questions = exam_info.get("quiz", [])

    if not quiz_questions:
        st.info("Additional practice questions for this exam are being added soon!")
    else:
        with st.form(key=f"quiz_form_{selected_exam_name}"):
            user_answers = {}
            for q_idx, q_data in enumerate(quiz_questions):
                st.markdown(f"#### Q{q_idx + 1}: {q_data['question']}")
                user_answers[q_idx] = st.radio(
                    f"Select your answer for Q{q_idx + 1}:",
                    options=q_data["options"],
                    key=f"q_{selected_exam_name}_{q_idx}",
                    index=None
                )
                st.markdown("---")

            submit_quiz = st.form_submit_button("🏆 Submit Quiz & View Score", use_container_width=True)

        if submit_quiz:
            score = 0
            total_questions = len(quiz_questions)

            st.markdown("### 📊 Quiz Results & Solution Breakdown")
            
            for q_idx, q_data in enumerate(quiz_questions):
                selected_ans = user_answers.get(q_idx)
                correct_ans = q_data["answer"]

                if selected_ans == correct_ans:
                    score += 1
                    st.success(f"✅ **Q{q_idx + 1}: Correct!** You selected '{selected_ans}'.")
                else:
                    st.error(f"❌ **Q{q_idx + 1}: Incorrect.** Your answer: '{selected_ans if selected_ans else 'Not Attempted'}'. Correct Answer: '{correct_ans}'.")
                
                st.info(f"💡 **Explanation:** {q_data['explanation']}")
                st.write("")

            score_percentage = (score / total_questions) * 100
            st.markdown("---")
            
            c1, c2 = st.columns(2)
            c1.metric("🎯 Total Score", f"{score} / {total_questions}")
            c2.metric("📈 Score Percentage", f"{score_percentage:.1f}%")

            if score_percentage == 100:
                st.balloons()
                st.success("🎉 Outstanding performance! Perfect score!")
            elif score_percentage >= 50:
                st.info("👍 Good effort! Review the detailed solutions to improve further.")
            else:
                st.warning("💪 Keep practicing! Go through the recommended YouTube lectures to strengthen core concepts.")

# TAB 5: AI CUSTOM STUDY PLANNER
with tab_custom:
    st.subheader("🤖 Generate a Personalized Daily Timetable")
    
    col_a, col_b = st.columns(2)
    daily_hours = col_a.slider("How many hours can you study daily?", 2, 14, 6)
    prep_months = col_b.slider("Months remaining for exam?", 1, 24, 6)
    api_key = st.text_input("🔑 Groq API Key (Optional for AI generation)", type="password", help="Leave blank for a smart built-in template.")

    if st.button("🚀 Generate Personalized Daily Plan"):
        if not api_key:
            st.success("✅ **Custom Timetable Generated:**")
            st.markdown(f"""
            **Target:** {selected_exam_name} ({prep_months} Months Out) | **Daily Hours:** {daily_hours} Hours
            
            - ⏰ **Slot 1 ({int(daily_hours * 0.4)} hrs):** Core Technical / Hardest Subject (Fresh mind session).
            - ⏰ **Slot 2 ({int(daily_hours * 0.3)} hrs):** Secondary Subject & Practice Problem Sets / PYQs.
            - ⏰ **Slot 3 ({int(daily_hours * 0.2)} hrs):** Daily Revision & Speed Tests / PYQs.
            - ⏰ **Slot 4 ({round(daily_hours * 0.1, 1)} hrs):** Current Affairs / Formulas Review before sleep.
            """)
        else:
            try:
                from groq import Groq
                client = Groq(api_key=api_key)
                prompt = f"Create a detailed daily study schedule for {selected_exam_name} with {daily_hours} hours available daily and {prep_months} months remaining. Focus on balance, mock tests, and PYQ practice."
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}]
                )
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error calling Groq API: {str(e)}")
