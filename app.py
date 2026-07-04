import streamlit as st

# 2. كود التصميم (CSS)
st.markdown("""
    <style>
    .hero-box { background: linear-gradient(135deg, #1e3a8a, #7e22ce); padding: 30px; border-radius: 25px; color: white; text-align: center; margin-bottom: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.3); }
    .soon-box { border: 2px dashed #8b5cf6; padding: 40px; text-align: center; border-radius: 20px; color: #8b5cf6; font-size: 20px; font-weight: bold; }
    .stButton>button { background: linear-gradient(90deg, #db2777, #7c3aed); color: white; border: none; border-radius: 12px; font-weight: bold; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# 3. إدارة الحالة
if 'balance' not in st.session_state: st.session_state.balance = 1000.0
if 'username' not in st.session_state: st.session_state.username = "user"


# 4. قاموس اللغات الشامل
i18n = {
    "English": {
        "nav": ["Overview", "Roadmap", "Dashboard", "Presale & Referrals", "Staking", "P2P Market", "Contact Us"],
        "hero": "PMTX COIN: Future of Finance", "sub": "Staking, Burns, & Massive Growth.",
        "hero_desc": "Join our robust Ecosystem. Deflationary burn & emergency security protocols ensuring your assets grow safely.",
        "roadmap_title": "Project Roadmap & Future Vision",
        "rm": ["Phase 1: Launch", "Initial Airdrop & Community", "Phase 2: Deflationary", "Strategic Token Burn & Scarcity", "Phase 3: Utility", "Staking Rewards & P2P"],
        "rm_footer": "PMTX is built for long-term growth.",
        "ref": "Presale & Referrals", "user_lbl": "Username:", "gen_btn": "Generate Link", "connect": "Connect Wallet", 
        "bal": "Balance", "soon": "Coming Soon!", "inv_btn": "Calculate 2% Reward", "inv_text": "Enter Investment ($)"
    },
    "العربية": {
        "nav": ["نظرة عامة", "خارطة الطريق", "لوحة التحكم", "البيع المسبق والإحالات", "قريباً التخزين", "سوق البيع بين الأعضاء", "اتصل بنا"],
        "hero": "عملة PMTX: مستقبل التمويل", "sub": "تخزين، حرق للعملة، ونمو هائل.",
        "hero_desc": "انضم إلى نظامنا البيئي المتكامل. بروتوكولات الحرق الذكي والأمان المشدد تضمن نمو أصولك بأعلى معايير الحماية.",
        "roadmap_title": "خارطة الطريق والرؤية المستقبلية",
        "rm": ["المرحلة 1: الانطلاق", "توزيع الإيردروب وبناء المجتمع", "المرحلة 2: الانكماش", "حرق العملات لزيادة الندرة", "المرحلة 3: المنفعة", "عائدات التخزين وسوق P2P"],
        "rm_footer": "صممت عملة PMTX للنمو طويل الأمد.",
        "ref": "البيع المسبق والإحالات", "user_lbl": "اسم المستخدم:", "gen_btn": "إنشاء الرابط", "connect": "ربط المحفظة", 
        "bal": "الرصيد", "soon": "قريباً جداً!", "inv_btn": "حساب مكافأة 2%", "inv_text": "أدخل قيمة الاستثمار ($)"
    },
    "日本語": {
        "nav": ["概要", "ロードマップ", "ダッシュボード", "プレセール", "ステーキング", "P2P市場", "お問い合わせ"],
        "hero": "PMTX COIN: 金融の未来", "sub": "ステーキングと成長.",
        "hero_desc": "堅牢なエコシステムに参加しましょう。デフレ型バーンとセキュリティプロトコルが資産を成長させます。",
        "roadmap_title": "ロードマップ",
        "rm": ["フェーズ1: 開始", "エアドロップ", "フェーズ2: デフレ", "トークンバーン", "フェーズ3: ユーティリティ", "ステーキング"],
        "rm_footer": "PMTXは長期的な成長を目指します。",
        "ref": "プレセールと紹介", "user_lbl": "ユーザー名:", "gen_btn": "リンク生成", "connect": "ウォレット接続", 
        "bal": "残高", "soon": "まもなく公開", "inv_btn": "2%報酬を計算", "inv_text": "投資額を入力 ($)"
    },
    "Français": {
        "nav": ["Aperçu", "Roadmap", "Tableau", "Prévente", "Staking", "Marché P2P", "Contact"],
        "hero": "PMTX COIN: Futur financier", "sub": "Staking et Croissance.",
        "hero_desc": "Rejoignez notre écosystème robuste. La gravure déflationniste et la sécurité garantissent une croissance sûre.",
        "roadmap_title": "Feuille de route",
        "rm": ["Phase 1: Lancement", "Airdrop", "Phase 2: Déflation", "Token Burn", "Phase 3: Utilité", "Staking"],
        "rm_footer": "PMTX est conçu pour une croissance à long terme.",
        "ref": "Prévente et Parrainage", "user_lbl": "Utilisateur:", "gen_btn": "Générer", "connect": "Connecter", 
        "bal": "Solde", "soon": "Bientôt", "inv_btn": "Calculer 2% récompense", "inv_text": "Montant investissement ($)"
    },
    "Español": {
        "nav": ["Resumen", "Hoja de ruta", "Panel", "Preventa", "Staking", "Mercado P2P", "Contacto"],
        "hero": "PMTX COIN: Futuro financiero", "sub": "Staking y Crecimiento.",
        "hero_desc": "Únase a nuestro ecosistema robusto. La quema deflacionaria y los protocolos de seguridad garantizan un crecimiento seguro.",
        "roadmap_title": "Hoja de ruta",
        "rm": ["Fase 1: Lanzamiento", "Airdrop", "Fase 2: Deflación", "Quema de Tokens", "Fase 3: Utilidad", "Staking"],
        "rm_footer": "PMTX está diseñado para el crecimiento.",
        "ref": "Preventa y Referidos", "user_lbl": "Usuario:", "gen_btn": "Generar", "connect": "Conectar", 
        "bal": "Saldo", "soon": "Pronto", "inv_btn": "Calcular 2% recompensa", "inv_text": "Inversión ($)"
    },
    "Deutsch": {
        "nav": ["Überblick", "Roadmap", "Dashboard", "Vorverkauf", "Staking", "P2P-Markt", "Kontakt"],
        "hero": "PMTX COIN: Finanzzukunft", "sub": "Staking und Wachstum.",
        "hero_desc": "Werden Sie Teil unseres robusten Ökosystems. Deflationärer Burn & Sicherheitsmechanismen sorgen für Wachstum.",
        "roadmap_title": "Roadmap",
        "rm": ["Phase 1: Start", "Airdrop", "Phase 2: Deflation", "Token-Burn", "Phase 3: Nutzen", "Staking"],
        "rm_footer": "PMTX ist auf Wachstum ausgelegt.",
        "ref": "Vorverkauf & Empfehlungen", "user_lbl": "Benutzername:", "gen_btn": "Erstellen", "connect": "Verbinden", 
        "bal": "Guthaben", "soon": "Bald", "inv_btn": "2% Belohnung berechnen", "inv_text": "Investition ($)"
    }
}

# 5. اختيار اللغة
lang = st.sidebar.selectbox(" Language / اللغة", list(i18n.keys()))
t = i18n[lang]

# 6. القائمة الجانبية (تم دمج الرابط الرسمي)
if st.sidebar.button(t["connect"]): 
    st.sidebar.success("Connected!")

page = st.sidebar.radio("PMTX COIN", t["nav"])

# إضافة رابط تويتر الرسمي الخاص بك
st.sidebar.markdown("---")
st.sidebar.markdown("### 📢 Official Community")
st.sidebar.link_button("Follow @PMTXCoin", "https://x.com/PMTXCoin")

# 7. الجزء التحفيزي الرئيسي
st.markdown(f'''
    <div class="hero-box">
        <h1 style="color: #FFD700;">🚀 {t["hero"]}</h1>
        <p style="font-size: 22px; font-weight: bold; margin-bottom: 10px;">{t["sub"]}</p>
        <p style="font-size: 18px; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 10px;">
            {t["hero_desc"]}
        </p>
    </div>
''', unsafe_allow_html=True)

# 8. محتوى الصفحات
# 8. محتوى الصفحات (انسخ هذا الكود بالكامل واستبدل الفقرة 8 القديمة به)

if page == t["nav"][0]: # Overview
    st.subheader(f"💰 {t['bal']}")
    st.metric("PMTX", f"{st.session_state.balance:,.0f}")
    st.success("🎉 Welcome! Airdrop successfully credited!")

elif page == t["nav"][1]: # Roadmap
    st.subheader(f"📍 {t['roadmap_title']}")
    c1, c2, c3 = st.columns(3)
    with c1: st.write(f"### {t['rm'][0]}\n{t['rm'][1]}")
    with c2: st.write(f"### {t['rm'][2]}\n{t['rm'][3]}")
    with c3: st.write(f"### {t['rm'][4]}\n{t['rm'][5]}")
    st.divider()
    st.info(t["rm_footer"])

elif page == t["nav"][2]: # Dashboard
    st.subheader(t["nav"][2])
    col1, col2, col3 = st.columns(3)
    col1.metric("Total PMTX", f"{st.session_state.balance:,.0f}")
    col2.metric("Referrals", "0")
    col3.metric("Growth", "+15%")
    st.write("---")
    st.write("Recent Activity: Welcome Bonus Added! 🚀")

elif page == t["nav"][3]: # Presale & Referrals
    st.subheader(f"🔗 {t['ref']}")
    u = st.text_input(t["user_lbl"])
    if st.button(t["gen_btn"]): st.session_state.username = u or "user"
    st.code(f"https://pmtx-coin.io/?ref={st.session_state.username}")
    
    st.write("---")
    st.subheader("Investment Commission (2%)")
    inv = st.number_input(t["inv_text"], min_value=0.0, max_value=1000.0, step=10.0)
    
    if st.button(t["inv_btn"]):
        if inv < 10:
            st.error("الحد الأدنى للاستثمار هو 10$")
        elif inv > 1000:
            st.error("الحد الأعلى للاستثمار هو 1,000$ لضمان استقرار العملة")
        else:
            commission = inv * 0.02
            st.session_state.balance += commission
            st.balloons()
            st.success(f"Success! 2% Added: {commission:.2f} PMTX")
            st.rerun()

elif page == t["nav"][6]: # اتصل بنا (العنصر السابع)
    st.subheader("✉️ اتصل بنا / Contact Us")
    with st.form("contact_form"):
        name = st.text_input("الاسم / Name")
        email = st.text_input("بريدك الإلكتروني / Email")
        message = st.text_area("رسالتك / Message")
        if st.form_submit_button("إرسال / Send"):
            if name and email and message:
                st.success("تم إرسال رسالتك بنجاح!")
            else:
                st.error("يرجى ملء جميع الحقول.")

elif page in [t["nav"][4], t["nav"][5]]: # Coming Soon (الاستثمار و P2P)
    st.markdown(f'<div class="soon-box">{t["soon"]}</div>', unsafe_allow_html=True)
