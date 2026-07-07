import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="PMTX COIN", layout="centered")

# 2. كود التصميم (CSS)
st.markdown("""
    <style>
    .hero-box { background: linear-gradient(135deg, #1e3a8a, #7e22ce); padding: 30px; border-radius: 25px; color: white; text-align: center; margin-bottom: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.3); }
    .soon-box { border: 2px dashed #8b5cf6; padding: 40px; text-align: center; border-radius: 20px; color: #8b5cf6; font-size: 20px; font-weight: bold; }
    .stButton>button { background: linear-gradient(90deg, #db2777, #7c3aed); color: white; border: none; border-radius: 12px; font-weight: bold; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# 3. إدارة الحالة (قم بتحديث هذا الجزء)
if 'balance' not in st.session_state: st.session_state.balance = 1000.0
if 'username' not in st.session_state: st.session_state.username = "user"

# أضف هذه الأسطر الجديدة للتهيئة:
if 'wallet_connected' not in st.session_state: st.session_state.wallet_connected = False
if 'twitter_linked' not in st.session_state: st.session_state.twitter_linked = False
if 'pending_reward' not in st.session_state: st.session_state.pending_reward = 1000
if 'airdrop_claimed' not in st.session_state: st.session_state.airdrop_claimed = False

# 4. قاموس اللغات الشامل (مُحدث بالكامل)
i18n = {
    "English": {
        "nav": ["Overview", "Roadmap", "Dashboard", "Presale & Referrals", "Staking", "P2P Market", "Contact Us"],
        "hero": "PMTX COIN: Future of Finance", "sub": "Staking, Burns, & Massive Growth.",
        "hero_desc": "Join our ecosystem. Deflationary burn & protocols ensuring growth.",
        "roadmap_title": "Project Roadmap", "presale_header": "💎 PMTX Presale Stages",
        "target_price": "Final Listing Target Price:", "rm": ["Phase 1: Launch", "Airdrop & Presale", "Phase 2: Deflation", "Token Burn", "Phase 3: Utility", "Staking & P2P"],
        "rm_footer": "PMTX is built for long-term growth.", "ref": "Presale & Referrals", "user_lbl": "Username:", "gen_btn": "Generate Link",
        "connect": "Connect Wallet", "bal": "Balance", "soon": "Coming Soon!", "inv_btn": "Calculate 2% Reward", "inv_text": "Enter Investment ($)",
        "p1": "0.00005 $", "p2": "0.0001 $", "p3": "0.0003 $", "promo": "Double your profits!", "explain": "2% of investment reward.",
        "airdrop_title": "Airdrop Options", "opt1": "Complete Tasks (1,000 PMTX)", "task_desc": "Follow, Like, Retweet & Tag 3 friends.",
        "opt2": "Express Claim (500 PMTX)", "express_desc": "Get 500 PMTX instantly without social tasks.", "fee_desc": "Fee: 0.3$ (Developer Fee + Gas).",
        "wallet_info": "Ensure your wallet is on the Polygon Network.", "connect_pay": "Connect Wallet & Pay 0.3$ Fee", "already_claimed": "✅ Airdrop already claimed!",
        "go_to_twitter": "📢 Go to Twitter/X Post", "tweet_input": "Enter your tweet link:", "verify_btn": "Verify & Get 1,000 PMTX",
        "setup_required": "🔒 Complete Setup to Claim Airdrop", "connect_wallet": "🔗 Connect Wallet (Polygon)",
        "link_twitter": "🐦 Link Twitter Account", "wallet_success": "✅ Wallet Connected", "twitter_success": "✅ Twitter Account Linked",
        "pending_text": "Pending Reward", "pay_btn": "Pay 0.3$ & Claim",
        "roadmap_details": ["Q3 2026: Launch", "Q4 2026: Staking", "Q1 2027: Listing"],
        "why_pmtx": "Why PMTX? We bridge scarcity with decentralized efficiency. Through deflationary burns and staking, we don't just follow trends; we build a sustainable digital economy. Join us to prioritize your assets' growth."
    },
    "العربية": {
        "nav": ["نظرة عامة", "خارطة الطريق", "لوحة التحكم", "البيع المسبق والإحالات", "قريباً التخزين", "سوق البيع بين الأعضاء", "اتصل بنا"],
        "hero": "عملة PMTX: مستقبل التمويل", "sub": "تخزين، حرق، ونمو هائل.",
        "hero_desc": "انضم لنظامنا البيئي المتكامل. بروتوكولات الأمان تضمن نمو أصولك.",
        "roadmap_title": "خارطة الطريق", "presale_header": "💎 مراحل البيع المسبق",
        "target_price": "سعر الإدراج النهائي:", "rm": ["المرحلة 1: الانطلاق", "الإيردروب والبيع المسبق", "المرحلة 2: الانكماش", "حرق العملات", "المرحلة 3: المنفعة", "عائدات التخزين"],
        "rm_footer": "صممت PMTX للنمو طويل الأمد.", "ref": "البيع المسبق والإحالات", "user_lbl": "اسم المستخدم:", "gen_btn": "إنشاء الرابط",
        "connect": "ربط المحفظة", "bal": "الرصيد", "soon": "قريباً جداً!", "inv_btn": "حساب مكافأة 2%", "inv_text": "أدخل قيمة الاستثمار ($)",
        "p1": "0.00005 $", "p2": "0.0001 $", "p3": "0.0003 $", "promo": "ضاعف أرباحك اليوم!", "explain": "مكافأة 2% من الاستثمار.",
        "airdrop_title": "خيارات الإيردروب", "opt1": "إكمال المهام (1,000 PMTX)", "task_desc": "تابع، أعجب، أعد تغريد وتاغ لـ 3 أصدقاء.",
        "opt2": "الاستلام السريع (500 PMTX)", "express_desc": "احصل على 500 PMTX فوراً بدون مهام.", "fee_desc": "الرسوم: 0.3$ (رسوم مطور + شبكة).",
        "wallet_info": "تأكد من أن محفظتك على شبكة Polygon.", "connect_pay": "ربط المحفظة ودفع رسوم 0.3$", "already_claimed": "✅ تم استلام الإيردروب مسبقاً!",
        "go_to_twitter": "📢 انتقل إلى تغريدة تويتر/X", "tweet_input": "أدخل رابط التغريدة:", "verify_btn": "تحقق واستلم 1,000 PMTX",
        "setup_required": "🔒 أكمل الإعدادات للمطالبة بالإيردروب", "connect_wallet": "🔗 ربط المحفظة (Polygon)",
        "link_twitter": "🐦 ربط حساب تويتر", "wallet_success": "✅ تم ربط المحفظة", "twitter_success": "✅ تم ربط حساب تويتر",
        "pending_text": "الجائزة المعلقة", "pay_btn": "ادفع 0.3$ واستلم",
        "roadmap_details": ["الربع الثالث 2026: الإطلاق", "الربع الرابع 2026: التخزين", "الربع الأول 2027: الإدراج"],
        "why_pmtx": "لماذا PMTX؟ نحن ندمج الندرة مع كفاءة التمويل اللامركزي. من خلال آليات الحرق المبرمج وعوائد التخزين، نحن لا نتبع الترند، بل نبني اقتصاداً رقمياً مستداماً. انضم إلينا لتعزيز نمو أصولك."
    },
    "日本語": {
        "nav": ["概要", "ロードマップ", "ダッシュボード", "プレセール", "ステーキング", "P2P市場", "お問い合わせ"],
        "hero": "PMTX COIN: 金融の未来", "sub": "ステーキングと成長.", "hero_desc": "堅牢なエコシステム.",
        "roadmap_title": "ロードマップ", "presale_header": "💎 PMTX プレセール",
        "target_price": "最終上場目標:", "rm": ["開始", "エアドロップ", "デフレ", "バーン", "ユーティリティ", "ステーキング"],
        "rm_footer": "長期的な成長.", "ref": "プレセール", "user_lbl": "ユーザー名:", "gen_btn": "リンク生成",
        "connect": "ウォレット接続", "bal": "残高", "soon": "まもなく", "inv_btn": "2%報酬計算", "inv_text": "投資額 ($)",
        "p1": "0.00005 $", "p2": "0.0001 $", "p3": "0.0003 $", "promo": "利益を2倍に!", "explain": "投資額の2%.",
        "airdrop_title": "エアドロップオプション", "opt1": "タスク完了 (1,000 PMTX)", "task_desc": "フォロー、いいね、RT、3人タグ付け。",
        "opt2": "クイック請求 (500 PMTX)", "express_desc": "ソーシャルタスクなしで即時取得.", "fee_desc": "手数料: 0.3$ (開発費+ガス代).",
        "wallet_info": "Polygonネットワークを確認.", "connect_pay": "接続 & 0.3$支払い", "already_claimed": "✅ 受取済み!",
        "go_to_twitter": "📢 Twitter/X投稿へ移動", "tweet_input": "ツイートリンクを入力:", "verify_btn": "確認して1,000 PMTXを取得",
        "setup_required": "🔒 エアドロップ請求のための設定", "connect_wallet": "🔗 ウォレット接続 (Polygon)",
        "link_twitter": "🐦 Twitter連携", "wallet_success": "✅ 接続済み", "twitter_success": "✅ 連携済み",
        "pending_text": "保留中の報酬", "pay_btn": "0.3$払って取得",
        "roadmap_details": ["2026 Q3: 開始", "2026 Q4: ステーキング", "2027 Q1: 上場"],
        "why_pmtx": "PMTXを選ぶ理由：希少性と分散型効率の融合。デフレ燃焼メカニズムとステーキングにより、単なるトレンドではなく、持続可能なデジタル経済を構築します。資産の成長のために私たちに参加してください。"
    },
    "Français": {
        "nav": ["Aperçu", "Roadmap", "Tableau", "Prévente", "Staking", "Marché P2P", "Contact"],
        "hero": "PMTX COIN: Futur financier", "sub": "Staking et Croissance.", "hero_desc": "Rejoignez notre écosystème.",
        "roadmap_title": "Roadmap", "presale_header": "💎 Étapes de prévente",
        "target_price": "Prix cible final:", "rm": ["Lancement", "Airdrop", "Déflation", "Burn", "Utilité", "Staking"],
        "rm_footer": "Croissance long terme.", "ref": "Prévente et Parrainage", "user_lbl": "Utilisateur:", "gen_btn": "Générer",
        "connect": "Connecter", "bal": "Solde", "soon": "Bientôt", "inv_btn": "Calculer 2% récompense", "inv_text": "Investissement ($)",
        "p1": "0.00005 $", "p2": "0.0001 $", "p3": "0.0003 $", "promo": "Doublez vos profits!", "explain": "2% de récompense.",
        "airdrop_title": "Options d'Airdrop", "opt1": "Tâches (1,000 PMTX)", "task_desc": "Suivre, Aimer, RT et taguer 3 amis.",
        "opt2": "Réclamation Express (500 PMTX)", "express_desc": "Obtenez 500 PMTX instantanément.", "fee_desc": "Frais: 0.3$ (Dev + Gaz).",
        "wallet_info": "Assurez-vous d'être sur Polygon.", "connect_pay": "Connecter & Payer 0.3$", "already_claimed": "✅ Déjà réclamé !",
        "go_to_twitter": "📢 Aller au tweet Twitter/X", "tweet_input": "Entrez le lien du tweet :", "verify_btn": "Vérifier & Réclamer 1,000 PMTX",
        "setup_required": "🔒 Configuration pour l'Airdrop", "connect_wallet": "🔗 Connecter le portefeuille",
        "link_twitter": "🐦 Lier Twitter", "wallet_success": "✅ Portefeuille connecté", "twitter_success": "✅ Twitter lié",
        "pending_text": "Récompense en attente", "pay_btn": "Payer 0.3$ & Réclamer",
        "roadmap_details": ["T3 2026: Lancement", "T4 2026: Staking", "T1 2027: Cotation"],
        "why_pmtx": "Pourquoi PMTX ? Nous allions rareté et efficacité décentralisée. Grâce au mécanisme de burn et au staking, nous ne suivons pas seulement les tendances ; nous bâtissons une économie numérique durable. Rejoignez-nous pour la croissance de vos actifs."
    },
    "Español": {
        "nav": ["Resumen", "Hoja de ruta", "Panel", "Preventa", "Staking", "Mercado P2P", "Contacto"],
        "hero": "PMTX COIN: Futuro financiero", "sub": "Staking y Crecimiento.", "hero_desc": "Ecosistema robusto.",
        "roadmap_title": "Hoja de ruta", "presale_header": "💎 Etapas de preventa",
        "target_price": "Precio objetivo:", "rm": ["Lanzamiento", "Airdrop", "Deflación", "Quema", "Utilidad", "Staking"],
        "rm_footer": "Diseñado para crecer.", "ref": "Preventa y Referidos", "user_lbl": "Usuario:", "gen_btn": "Generar",
        "connect": "Conectar", "bal": "Saldo", "soon": "Pronto", "inv_btn": "Calcular 2% recompensa", "inv_text": "Inversión ($)",
        "p1": "0.00005 $", "p2": "0.0001 $", "p3": "0.0003 $", "promo": "¡Duplica tus ganancias!", "explain": "2% de recompensa.",
        "airdrop_title": "Opciones de Airdrop", "opt1": "Tareas (1,000 PMTX)", "task_desc": "Seguir, Like, RT y taguer 3 amigos.",
        "opt2": "Reclamo Express (500 PMTX)", "express_desc": "Obtén 500 PMTX al instante.", "fee_desc": "Tarifa: 0.3$ (Dev + Gas).",
        "wallet_info": "Asegúrate de estar en Polygon.", "connect_pay": "Conectar & Pagar 0.3$", "already_claimed": "✅ ¡Ya reclamado!",
        "go_to_twitter": "📢 Ir a la publicación de Twitter/X", "tweet_input": "Ingresa el enlace del tweet:", "verify_btn": "Verificar y Reclamar 1,000 PMTX",
        "setup_required": "🔒 Configuración para Airdrop", "connect_wallet": "🔗 Conectar billetera",
        "link_twitter": "🐦 Vincular Twitter", "wallet_success": "✅ Billetera conectada", "twitter_success": "✅ Twitter vinculado",
        "pending_text": "Recompensa pendiente", "pay_btn": "Pagar 0.3$ y Reclamar",
        "roadmap_details": ["T3 2026: Lanzamiento", "T4 2026: Staking", "T1 2027: Listado"],
        "why_pmtx": "¿Por qué PMTX? Unimos escasez con eficiencia descentralizada. A través de quemas deflacionarias y staking, no solo seguimos tendencias; construimos una economía digital sostenible. Únete para priorizar el crecimiento de tus activos."
    },
    "Deutsch": {
        "nav": ["Überblick", "Roadmap", "Dashboard", "Vorverkauf", "Staking", "P2P-Markt", "Kontakt"],
        "hero": "PMTX COIN: Finanzzukunft", "sub": "Staking und Wachstum.", "hero_desc": "Robustes Ökosystem.",
        "roadmap_title": "Roadmap", "presale_header": "💎 Vorverkaufsphasen",
        "target_price": "Zielpreis:", "rm": ["Start", "Airdrop", "Deflation", "Burn", "Nutzen", "Staking"],
        "rm_footer": "Auf Wachstum ausgelegt.", "ref": "Vorverkauf & Empfehlungen", "user_lbl": "Benutzername:", "gen_btn": "Erstellen",
        "connect": "Verbinden", "bal": "Guthaben", "soon": "Bald", "inv_btn": "2% Belohnung", "inv_text": "Investition ($)",
        "p1": "0.00005 $", "p2": "0.0001 $", "p3": "0.0003 $", "promo": "Verdoppeln Sie Ihre Gewinne!", "explain": "2% Belohnung.",
        "airdrop_title": "Airdrop-Optionen", "opt1": "Aufgaben (1,000 PMTX)", "task_desc": "Folgen, Like, RT & markiere 3 Freunde.",
        "opt2": "Express-Anspruch (500 PMTX)", "express_desc": "Erhalte 500 PMTX sofort.", "fee_desc": "Gebühr: 0.3$ (Dev + Gas).",
        "wallet_info": "Stelle sicher, dass du im Polygon-Netzwerk bist.", "connect_pay": "Verbinden & 0.3$ zahlen", "already_claimed": "✅ Beansprucht!",
        "go_to_twitter": "📢 Zum Twitter/X-Beitrag", "tweet_input": "Tweet-Link eingeben:", "verify_btn": "Verifizieren & 1,000 PMTX erhalten",
        "setup_required": "🔒 Airdrop-Einrichtung", "connect_wallet": "🔗 Wallet verbinden",
        "link_twitter": "🐦 Twitter verknüpfen", "wallet_success": "✅ Wallet verbunden", "twitter_success": "✅ Twitter verknüpft",
        "pending_text": "Ausstehende Belohnung", "pay_btn": "0.3$ zahlen & Anspruch",
        "roadmap_details": ["Q3 2026: Start", "Q4 2026: Staking", "Q1 2027: Listung"],
        "why_pmtx": "Warum PMTX? Wir verbinden Knappheit mit dezentraler Effizienz. Durch Deflations-Burns und Staking folgen wir nicht nur Trends, sondern bauen eine nachhaltige digitale Wirtschaft auf. Schließen Sie sich uns an."
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

# 1. ابحث عن صفحة الـ Overview في كودك
# 1. صفحة Overview
if page == t["nav"][0]:
    st.subheader(f"💰 {t['bal']}")
    col_bal1, col_bal2 = st.columns(2)
    with col_bal1:
        st.metric("PMTX", f"{st.session_state.balance:,.0f}")
    with col_bal2:
        usd_value = st.session_state.balance * 0.2
        st.metric("USD Value (Listing $0.2)", f"${usd_value:,.2f}")
    
    st.write("---")
    
    # --- كود بوابة الربط والجائزة المعلقة المدمج ---
    # قسم الإيردروب
    if not st.session_state.get('airdrop_claimed', False):
        st.warning(f"💎 {t.get('pending_text')}: **{st.session_state.pending_reward} PMTX**")
        st.markdown(f"### 🔒 {t.get('setup_required')}")
        
        # بوابة الربط (إجبارية)
        if not st.session_state.wallet_connected:
            if st.button(t.get('connect_wallet')):
                st.session_state.wallet_connected = True
                st.rerun()
        elif not st.session_state.twitter_linked:
            st.success(t.get('wallet_success'))
            if st.button(t.get('link_twitter')):
                st.session_state.twitter_linked = True
                st.rerun()
        else:
            st.success(t.get('twitter_success'))
            
            # خيارات المطالبة (لا تظهر إلا بعد الربط)
            st.markdown(f"### 🚀 {t.get('airdrop_title')}")
            
            # الخيار 1: المهام (1,000 PMTX)
            with st.expander(f"✅ {t.get('opt1')}"):
                st.write(t.get('task_desc'))
                st.link_button(t["go_to_twitter"], "https://x.com/PMTXCoin")
                tweet_link = st.text_input(t.get('tweet_input'))
                if st.button(t.get('verify_btn')):
                    if tweet_link and "twitter" in tweet_link:
                        st.session_state.balance += 1000
                        st.session_state.airdrop_claimed = True
                        st.rerun()
                    else: st.error("Invalid Link!")

            # الخيار 2: الاستلام السريع (500 PMTX)
            with st.expander(f"⚡ {t.get('express_btn')}"):
                st.write(t.get('express_desc'))
                st.write(f"**{t.get('fee_note')}**")
                if st.button(t.get('pay_btn')):
                    st.session_state.balance += 500
                    st.session_state.airdrop_claimed = True
                    st.success("Payment Received & PMTX Claimed!")
                    st.rerun()
    else:
        st.success(t.get('already_claimed'))
# 2. صفحة Roadmap
elif page == t["nav"][1]:
    st.subheader(f"📍 {t['roadmap_title']}")
    
    # نص تسويقي مقنع وجديد
    st.info(t["why_pmtx"])
    
    # 1. الأسعار ومراحل البيع
    st.markdown(f"### {t['presale_header']}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Phase 1", t["p1"])
    col2.metric("Phase 2", t["p2"])
    col3.metric("Phase 3", t["p3"])
    
    # 2. السعر المستهدف
    st.markdown(f"**{t['target_price']}** 🚀 <span style='color: #FFD700; font-size: 24px;'>0.50 $</span>", unsafe_allow_html=True)
    
    st.divider()
    
    # 3. خارطة الطريق
    st.markdown("### 🗓️ Project Timeline")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"#### {t['roadmap_details'][0]}")
    c2.markdown(f"#### {t['roadmap_details'][1]}")
    c3.markdown(f"#### {t['roadmap_details'][2]}")
    
    st.divider()
    st.info(t["rm_footer"])

# 3. صفحة Dashboard
elif page == t["nav"][2]:
    st.subheader(f"📈 {t['nav'][2]}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total PMTX", f"{st.session_state.balance:,.0f}")
    col2.metric("Referrals", "0")
    col3.metric("Growth", "+15%")

# 4. صفحة Presale & Referrals (تمت إضافة حقل اسم المستخدم وإنشاء الرابط)
elif page == t["nav"][3]:
    st.subheader(f"🔗 {t['ref']}")
   
    # قسم إنشاء رابط الإحالة
    st.info(f"🚀 {t['promo']}")
    user_input = st.text_input(t["user_lbl"], value=st.session_state.username)
   
    if st.button(t["gen_btn"]):
        st.session_state.username = user_input
        # يمكنك تغيير 'pmtx-coin-official2026.streamlit.app' برابط موقعك الحقيقي لاحقاً
        ref_link = f"https://pmtx-coin-official2026.streamlit.app/?ref={user_input}"
        st.success(f"🔗 Your Referral Link: {ref_link}")
        st.code(ref_link, language="text")
   
    st.divider()
   
    # قسم حاسبة الاستثمار
    st.warning(f"💡 {t['explain']}")
    inv = st.number_input(t["inv_text"], min_value=0.0, step=10.0)
    if st.button(t["inv_btn"]):
        commission = inv * 0.02
        st.session_state.balance += commission
        st.success(f"🎉 2% Commission Calculated: ${commission:,.2f} added to your balance!")
        st.rerun()

# 5. الصفحات التي قيد الإنشاء (Staking & P2P)
elif page in [t["nav"][4], t["nav"][5]]:
    st.markdown(f'<div class="soon-box">{t["soon"]}</div>', unsafe_allow_html=True)

# 6. صفحة Contact Us
elif page == t["nav"][6]:
    st.subheader("✉️ اتصل بنا / Contact Us")
    with st.form("contact_form"):
        # طلب مساعدة سابقة بخصوص اسم مستعار
        st.text_input("Name (You can use a pseudonym)")
        st.text_area("رسالتك / Message")
        st.form_submit_button("إرسال / Submit")
