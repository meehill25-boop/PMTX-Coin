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
# 4. قاموس اللغات المحدث (شامل المراحل والأسعار الجديدة)
i18n = {
    "English": {
        "nav": ["Overview", "Roadmap", "Dashboard", "Presale & Referrals", "Staking", "P2P Market", "Contact Us"],
        "hero": "PMTX COIN: Future of Finance", "sub": "Staking, Burns, & Massive Growth.",
        "hero_desc": "Join our ecosystem. Deflationary burn & protocols ensuring growth.",
        "roadmap_title": "Project Roadmap",
        "presale_header": "💎 PMTX Presale Stages",
        "target_price": "Final Listing Target Price:",
        "rm": ["Phase 1: Launch", "Airdrop & Presale", "Phase 2: Deflation", "Token Burn", "Phase 3: Utility", "Staking & P2P"],
        "rm_footer": "PMTX is built for long-term growth.",
        "ref": "Presale & Referrals", "user_lbl": "Username:", "gen_btn": "Generate Link", "connect": "Connect Wallet",
        "bal": "Balance", "soon": "Coming Soon!", "inv_btn": "Calculate 2% Reward", "inv_text": "Enter Investment ($)",
        "p1": "0.00007 $", "p2": "0.0002 $", "p3": "0.0005 $",
        "promo": "Double your profits! Share your link.", "explain": "Earnings System: You will receive 2% of any investment."
    },
    "العربية": {
        "nav": ["نظرة عامة", "خارطة الطريق", "لوحة التحكم", "البيع المسبق والإحالات", "قريباً التخزين", "سوق البيع بين الأعضاء", "اتصل بنا"],
        "hero": "عملة PMTX: مستقبل التمويل", "sub": "تخزين، حرق، ونمو هائل.",
        "hero_desc": "انضم لنظامنا البيئي المتكامل. بروتوكولات الأمان تضمن نمو أصولك.",
        "roadmap_title": "خارطة الطريق",
        "presale_header": "💎 مراحل البيع المسبق لـ PMTX",
        "target_price": "سعر الإدراج النهائي المستهدف:",
        "rm": ["المرحلة 1: الانطلاق", "الإيردروب والبيع المسبق", "المرحلة 2: الانكماش", "حرق العملات", "المرحلة 3: المنفعة", "عائدات التخزين"],
        "rm_footer": "صممت PMTX للنمو طويل الأمد.",
        "ref": "البيع المسبق والإحالات", "user_lbl": "اسم المستخدم:", "gen_btn": "إنشاء الرابط", "connect": "ربط المحفظة",
        "bal": "الرصيد", "soon": "قريباً جداً!", "inv_btn": "حساب مكافأة 2%", "inv_text": "أدخل قيمة الاستثمار ($)",
        "p1": "0.00007 $", "p2": "0.0002 $", "p3": "0.0005 $",
        "promo": "ضاعف أرباحك اليوم! شارك رابط الإحالة الخاص بك.", "explain": "نظام الأرباح: ستحصل على 2% من قيمة أي استثمار."
    },
    "日本語": {
        "nav": ["概要", "ロードマップ", "ダッシュボード", "プレセール", "ステーキング", "P2P市場", "お問い合わせ"],
        "hero": "PMTX COIN: 金融の未来", "sub": "ステーキングと成長.",
        "hero_desc": "堅牢なエコシステムに参加しましょう.",
        "roadmap_title": "ロードマップ",
        "presale_header": "💎 PMTX プレセール段階",
        "target_price": "最終上場目標価格:",
        "rm": ["開始", "エアドロップとプレセール", "デフレ", "バーン", "ユーティリティ", "ステーキング"],
        "rm_footer": "長期的な成長を目指します.",
        "ref": "プレセールと紹介", "user_lbl": "ユーザー名:", "gen_btn": "リンク生成", "connect": "ウォレット接続",
        "bal": "残高", "soon": "まもなく公開", "inv_btn": "2%報酬を計算", "inv_text": "投資額 ($)",
        "p1": "0.00007 $", "p2": "0.0002 $", "p3": "0.0005 $",
        "promo": "利益を2倍に！リンクをシェアして報酬を獲得。", "explain": "投資額の 2% を獲得できます。"
    },
    "Français": {
        "nav": ["Aperçu", "Roadmap", "Tableau", "Prévente", "Staking", "Marché P2P", "Contact"],
        "hero": "PMTX COIN: Futur financier", "sub": "Staking et Croissance.",
        "hero_desc": "Rejoignez notre écosystème robuste.",
        "roadmap_title": "Feuille de route",
        "presale_header": "💎 Étapes de prévente PMTX",
        "target_price": "Prix cible final:",
        "rm": ["Lancement", "Airdrop et Prévente", "Déflation", "Burn", "Utilité", "Staking"],
        "rm_footer": "PMTX conçu pour la croissance.",
        "ref": "Prévente et Parrainage", "user_lbl": "Utilisateur:", "gen_btn": "Générer", "connect": "Connecter",
        "bal": "Solde", "soon": "Bientôt", "inv_btn": "Calculer 2% récompense", "inv_text": "Investissement ($)",
        "p1": "0.00007 $", "p2": "0.0002 $", "p3": "0.0005 $",
        "promo": "Doublez vos profits ! Partagez votre lien.", "explain": "Vous obtenez 2% de chaque investissement."
    },
    "Español": {
        "nav": ["Resumen", "Hoja de ruta", "Panel", "Preventa", "Staking", "Mercado P2P", "Contacto"],
        "hero": "PMTX COIN: Futuro financiero", "sub": "Staking y Crecimiento.",
        "hero_desc": "Únase a nuestro ecosistema robusto.",
        "roadmap_title": "Hoja de ruta",
        "presale_header": "💎 Etapas de preventa de PMTX",
        "target_price": "Precio objetivo final:",
        "rm": ["Lanzamiento", "Airdrop y Preventa", "Deflación", "Quema", "Utilidad", "Staking"],
        "rm_footer": "PMTX diseñado para crecer.",
        "ref": "Preventa y Referidos", "user_lbl": "Usuario:", "gen_btn": "Generar", "connect": "Conectar",
        "bal": "Saldo", "soon": "Pronto", "inv_btn": "Calcular 2% recompense", "inv_text": "Inversión ($)",
        "p1": "0.00007 $", "p2": "0.0002 $", "p3": "0.0005 $",
        "promo": "¡Duplica tus ganancias! Comparte tu enlace.", "explain": "Obtienes el 2% de cada inversión."
    },
    "Deutsch": {
        "nav": ["Überblick", "Roadmap", "Dashboard", "Vorverkauf", "Staking", "P2P-Markt", "Kontakt"],
        "hero": "PMTX COIN: Finanzzukunft", "sub": "Staking und Wachstum.",
        "hero_desc": "Werden Sie Teil unseres Ökosystems.",
        "roadmap_title": "Roadmap",
        "presale_header": "💎 PMTX Vorverkaufsphasen",
        "target_price": "Endgültiger Zielpreis:",
        "rm": ["Start", "Airdrop und Vorverkauf", "Deflation", "Burn", "Nutzen", "Staking"],
        "rm_footer": "PMTX auf Wachstum ausgelegt.",
        "ref": "Vorverkauf & Empfehlungen", "user_lbl": "Benutzername:", "gen_btn": "Erstellen", "connect": "Verbinden",
        "bal": "Guthaben", "soon": "Bald", "inv_btn": "2% Belohnung berechnen", "inv_text": "Investition ($)",
        "p1": "0.00007 $", "p2": "0.0002 $", "p3": "0.0005 $",
        "promo": "Verdoppeln Sie Ihre Gewinne! Teilen Sie Ihren Link.", "explain": "Sie erhalten 2% pro Investition."
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
# --- تنظيم الصفحات ---

# صفحة Overview
# --- تنظيم الصفحات (نسخة مصححة) ---

# 1. صفحة Overview
# 1. صفحة Overview (المحتوى المفقود)
# --- تنظيم الصفحات ---

# 1. صفحة Overview
if page == t["nav"][0]:
    st.subheader(f"💰 {t['bal']}")
    col_bal1, col_bal2 = st.columns(2)
    with col_bal1:
        st.metric("PMTX", f"{st.session_state.balance:,.0f}")
    with col_bal2:
        usd_value = (st.session_state.balance / 1000) * 500
        st.metric("USD Balance", f"${usd_value:,.0f}")
    st.write("---")
    # (رسالة الترحيب هنا...)
    st.success("🎉 Welcome! Wallet connected and Airdrop successfully claimed! Your current balance is 1,000 PMTX valued at 500$ 🚀")
    st.link_button("📄 View Token Smart Contract on PolygonScan", "https://polygonscan.com/token/0xc4af4aeebab3b717f771941ce7f1a3e4c765a53e#transactions", type="primary")

# 2. صفحة Roadmap (المفقودة)
elif page == t["nav"][1]:
    st.subheader(f"📍 {t['roadmap_title']}")
    
    # 1. الأسعار ومراحل البيع (كلها مترجمة)
    st.markdown(f"### {t['presale_header']}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Phase 1", t["p1"])
    col2.metric("Phase 2", t["p2"])
    col3.metric("Phase 3", t["p3"])
    
    # 2. السعر المستهدف
    st.markdown(f"**{t['target_price']}** 🚀 <span style='color: #FFD700; font-size: 24px;'>0.50 $</span>", unsafe_allow_html=True)
    
    st.divider()
    
    # 3. محتوى خارطة الطريق المترجم بالكامل
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"#### {t['rm'][0]}\n{t['rm'][1]}")
    c2.markdown(f"#### {t['rm'][2]}\n{t['rm'][3]}")
    c3.markdown(f"#### {t['rm'][4]}\n{t['rm'][5]}")
    
    st.divider()
    st.info(t["rm_footer"])

# 3. صفحة Dashboard
elif page == t["nav"][2]:
    st.subheader(f"📈 {t['nav'][2]}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total PMTX", f"{st.session_state.balance:,.0f}")
    col2.metric("Referrals", "0")
    col3.metric("Growth", "+15%")

# 4. صفحة Presale & Referrals
elif page == t["nav"][3]:
    st.subheader(f"🔗 {t['ref']}")
    # (كود الإحالات والحاسبة هنا...)
    st.info(f"🚀 {t['promo']}")
    st.warning(f"💡 {t['explain']}")
    inv = st.number_input(t["inv_text"], min_value=0.0, step=10.0)
    if st.button(t["inv_btn"]):
        commission = inv * 0.02
        st.session_state.balance += commission
        st.rerun()

# 5. الصفحات التي قيد الإنشاء (Staking & P2P)
elif page in [t["nav"][4], t["nav"][5]]:
    st.markdown(f'<div class="soon-box">{t["soon"]}</div>', unsafe_allow_html=True)

# 6. صفحة Contact Us
elif page == t["nav"][6]:
    st.subheader("✉️ اتصل بنا / Contact Us")
    with st.form("contact_form"):
        st.text_input("الاسم")
        st.text_area("رسالتك")
        st.form_submit_button("إرسال")

elif page in [t["nav"][4], t["nav"][5]]: # Coming Soon (الاستثمار و P2P)
    st.markdown(f'<div class="soon-box">{t["soon"]}</div>', unsafe_allow_html=True)
