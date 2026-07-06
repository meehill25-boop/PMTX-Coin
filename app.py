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
if page == t["nav"][0]: # Overview
    st.subheader(f"💰 {t['bal']}")
   
    # 📊 Affichage des soldes côte à côte sur une seule ligne
    col_bal1, col_bal2 = st.columns(2)
    with col_bal1:
        st.metric("PMTX", f"{st.session_state.balance:,.0f}")
    with col_bal2:
        # Calcul dynamique du solde équivalent en dollar
        usd_value = (st.session_state.balance / 1000) * 500
        st.metric("USD Balance", f"${usd_value:,.0f}")
       
    st.write("---")
   
    # 🌐 Détection stricte de la langue basée sur la variable "lang" de votre ligne 2
    # Cela garantit que le texte ne restera pas bloqué en anglais
    if "ar" in lang.lower():
        success_msg = "🎉 **تهانينا! تم ربط المحفظة والمطالبة بالإيردروب بنجاح!** حصلت على **1,000 PMTX** بقيمة تقدر بـ **500$** في حسابك 🚀 لا تفوت الفرصة، المستقبل يبدأ الآن **وضاعف أرباحك عبر دعوة أصدقائك!**"
        btn_text = "📄 عرض عقد العملة الذكي على شبكة PolygonScan"
    elif "fr" in lang.lower():
        success_msg = "🎉 **Félicitations ! Portefeuille connecté et Airdrop réclamé avec succès !** Votre solde actuel est de **1 000 PMTX** valorisé à **500$** 🚀 Prenez part à l'avenir de la crypto et **doublez vos gains en partagez votre lien de parrainage !**"
        btn_text = "📄 Voir le Smart Contract sur PolygonScan"
    elif "es" in lang.lower():
        success_msg = "🎉 **¡Bienvenido! ¡Billetera conectada y Airdrop reclamado con éxito!** Tu saldo actual es de **1,000 PMTX** valorados en **500$** 🚀 ¡Forja el futuro de las criptomonedas y **duplica tus ganancias compartiendo tu enlace de referido!**"
        btn_text = "📄 Ver Smart Contract en PolygonScan"
    elif "zh" in lang.lower():
        success_msg = "🎉 **欢迎！钱包已成功连接，空投已成功领取！** 您当前的余额为 **1,000 PMTX**（价值 **500$**）🚀 塑造加密货币 include 的未来，**分享您的推荐链接使您的回报翻倍！**"
        btn_text = "📄 在 PolygonScan 上查看智能合约"
    elif "de" in lang.lower() or "ge" in lang.lower():
        success_msg = "🎉 **Willkommen! Wallet verbunden und Airdrop erfolgreich beansprucht!** Ihr aktuelles Guthaben beträgt **1.000 PMTX** im Wert von **500$** 🚀 Gestalten Sie die Zukunft der Krypto-Welt und **verdoppeln Sie Ihre Rendite, indem Sie Ihren Empfehlungslink teilen!**"
        btn_text = "📄 Token-Smart-Contract auf PolygonScan anzeigen"
    else: # Langue anglaise ou option par défaut pour vos 6 langues
        success_msg = "🎉 **Welcome! Wallet connected and Airdrop successfully claimed!** Your current balance is **1,000 PMTX** valued at **500$** 🚀 Shape the future of crypto and **double your returns by sharing your referral link!**"
        btn_text = "📄 View Token Smart Contract on PolygonScan"

    # 🌟 1. Affichage du texte de réussite de l'Airdrop (Placé AU-DESSUS du bouton)
    st.success(success_msg)
    st.write("") # Petit espace esthétique
   
    # 📄 2. Bouton officiel du Smart Contract (PolygonScan) placé juste en dessous
    contract_url = "https://polygonscan.com/token/0xc4af4aeebab3b717f771941ce7f1a3e4c765a53e#transactions"
    st.link_button(btn_text, contract_url, type="primary", use_container_width=True)
    st.write("---")




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
    st.code(f"https://pmtx-coin.io{st.session_state.username}")
   
    # --- كاشف اللغة الدقيق والنهائي للموقع عبر فحص الكلمات المفتاحية لموقعك ---
    btn_text = str(t["gen_btn"]).lower()
   
    if "إنشاء" in btn_text or "توليد" in btn_text or "رابط" in btn_text:
        current_lang = "ar"
    elif "générer" in btn_text or "generer" in btn_text:
        current_lang = "fr"
    elif "generar" in btn_text:
        current_lang = "es"
    elif "создать" in btn_text or "сгенерировать" in btn_text:
        current_lang = "ru"
    elif "生成" in btn_text:
        current_lang = "zh"
    else:
        current_lang = "en"

    # تخصيص نصوص الشرح والأرباح (2/100) حسب اللغة المكتشفة
    if current_lang == "ar":
        promo = "**ضاعف أرباحك اليوم!** شارك رابطك المخصص مع أصدقائك واكسب عوائد مستمرة فور تفعيل استثماراتهم."
        explain = "**كيف تحسب أرباحك؟** لكل شخص يسجل عبر رابطك ويقوم بالاستثمار، ستحصل على **2%** من قيمة استثماره (بمعدل **2 دولار لكل 100 دولار مستثمرة**)."
   
    elif current_lang == "fr":
        promo = "**Doublez vos profits aujourd'hui !** Partagez votre lien et gagnez des revenus continus."
        explain = "**Comment calculer vos profits ?** Pour chaque personne inscrite via votre lien qui investit, vous obtenez **2%** (**2 $ pour chaque 100 $ investis**)."
   
    elif current_lang == "es":
        promo = "**¡Duplica tus ganancias hoy!** Comparte tu enlace y obtén rendimientos continuos."
        explain = "**¿Cómo calcular tus ganancias?** Por cada persona que se registre e invierta, obtienes el **2%** (**$2 por cada $100 invertidos**)."
   
    elif current_lang == "ru":
        promo = "**Удвойте свою прибыль сегодня!** Поделитесь ссылкой и получайте постоянный доход."
        explain = "**Как рассчитать прибыль?** За каждого реферала, который инвестирует, вы получаете **2%** (**2 доллара за каждые 100 долларов инвестиций**)."
   
    elif current_lang == "zh":
        promo = "**今天就让您的利润翻倍！** 分享您的专属链接，赚取持续回报。"
        explain = "**如何計算您的利润？** 每个人通过您的链接注册并投资，您将获得 **2%** 的奖励（**每投资 100 美元可获得 2 美元**）。"
   
    else: # English
        promo = "**Double your profits today!** Share your custom link with friends and earn continuous returns."
        explain = "**How to calculate your profits?** For everyone who registers via your link and invests, you get **2%** of their investment (**$2 for every $100 invested**)."
       
    # عرض الأقسام المرئية مع الصاروخ والمصباح بشكل فوري
    st.info(f"🚀 {promo}")
    st.markdown(f"💡 {explain}")
   
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
