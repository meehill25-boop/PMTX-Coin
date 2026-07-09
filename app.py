import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="PMTX COIN", layout="centered")

# 2. كود التصميم (CSS الموحد)
st.markdown("""
    <style>
    .hero-box { 
        background: linear-gradient(135deg, #1e3a8a, #7e22ce); 
        padding: 40px; 
        border-radius: 25px; 
        color: white; 
        text-align: center; 
        margin-bottom: 30px; 
        box-shadow: 0 10px 30px rgba(126, 34, 206, 0.5);
    }
    .hero-box h1 { font-size: 3.5rem !important; color: #FFD700 !important; }
    
    .glowing-text {
        font-size: 2.2rem !important;
        font-weight: 900 !important;
        color: #FFFFFF !important;
        text-align: center;
        padding: 20px;
        background: rgba(0, 0, 0, 0.6);
        border-radius: 15px;
        border: 3px solid #FFD700;
        text-shadow: 0 0 10px #FFD700, 0 0 20px #7c3aed;
    }
    
    .stButton>button { 
        background: linear-gradient(90deg, #db2777, #f43f5e); 
        color: white; 
        border-radius: 50px; 
        padding: 15px 40px; 
        font-size: 1.2rem;
        font-weight: bold;
        border: none;
        transition: transform 0.2s;
    }
    .stButton>button:hover { transform: scale(1.05); }
    </style>
""", unsafe_allow_html=True)

# 3. إدارة الحالة (كما هي في ملفك)
if 'balance' not in st.session_state: st.session_state.balance = 1000.0
if 'username' not in st.session_state: st.session_state.username = "user"
if 'wallet_connected' not in st.session_state: st.session_state.wallet_connected = False
if 'twitter_linked' not in st.session_state: st.session_state.twitter_linked = False
if 'pending_reward' not in st.session_state: st.session_state.pending_reward = 1000
if 'airdrop_claimed' not in st.session_state: st.session_state.airdrop_claimed = False

# 4. (هنا ضع قاموس اللغات i18n الخاص بك كاملاً كما كان في ملفك الأصلي)
# يمكنك نسخه من ملفك السابق ولصقه هنا مباشرة بعد هذا السطر

# 5. (بقية الكود الخاص بك: اختيار اللغة، القائمة الجانبية، والتبويبات)
# يمكنك وضعها هنا مباشرة وسيعمل كل شيء كما كان وأفضل

# 4. قاموس اللغات الشامل (مُحدث بالكامل)
i18n = {
    "English": {
        "nav": ["Overview", "Roadmap", "Dashboard", "Presale & Referrals", "Staking", "P2P Market", "Contact Us"],
        "hero": "PMTX COIN: Future of Finance", "sub": "Staking, Burns, & Massive Growth.",
        "hero_desc": "Join our ecosystem. Deflationary burn & protocols ensuring growth.",
        "why_buy_now": "Stage 1 price is only $0.00005! Don't miss this early entry.",
        "marketing_pitch": "You're in Stage 1 ($0.00005). Price rises to $0.0001 then $0.0003. We target $0.20 - $0.50 at listing. With staking and burns, we aim for $1.00+! Get in now.",
        "roadmap_title": "Project Roadmap", "presale_header": "💎 PMTX Presale Stages",
        "target_price": "Final Listing Target Price:", "rm": ["Phase 1: Launch", "Airdrop & Presale", "Phase 2: Deflation", "Token Burn", "Phase 3: Utility", "Staking & P2P"],
        "rm_footer": "PMTX is built for long-term growth.", "ref": "Presale & Referrals", "user_lbl": "Username:", "gen_btn": "Generate Link",
        "connect": "Connect Wallet", "bal": "Balance", "soon": "Coming Soon!", "inv_btn": "Calculate 2% Reward", "inv_text": "Enter Investment ($)",
        "p1": "0.00005 $", "p2": "0.0001 $", "p3": "0.0003 $", "promo": "Double your profits!", "explain": "2% of investment reward.",
        "airdrop_title": "Airdrop Options", "opt1": "Complete Tasks (1,000 PMTX)", "task_desc": "Follow, Like, Retweet & Tag 3 friends.",
        "opt2": "Express Claim (500 PMTX)", "express_desc": "Get 500 PMTX instantly without social tasks.",
        "wallet_info": "Ensure your wallet is on the Polygon Network.", "connect_pay": "Connect Wallet", "already_claimed": "✅ Airdrop already claimed!",
        "go_to_twitter": "📢 Go to Twitter/X Post", "tweet_input": "Enter your tweet link:", "verify_btn": "Verify & Get 1,000 PMTX",
        "setup_required": "🔒 Complete Setup to Claim Airdrop", "connect_wallet": "🔗 Connect Wallet (Polygon)",
        "link_twitter": "🐦 Link Twitter Account", "wallet_success": "✅ Wallet Connected", "twitter_success": "✅ Twitter Account Linked",
        "pending_text": "Pending Reward", "pay_btn": "Claim Tokens",
        "roadmap_details": ["Q3 2026: Launch", "Q4 2026: Staking", "Q1 2027: Listing"],
        "why_pmtx": "Why PMTX? We bridge scarcity with decentralized efficiency. Join us to prioritize your assets' growth.",
        "buy_title": "🚀 Golden Opportunity: Stage 1!", "inv_label": "Investment ($)", "receive_text": "You get", "bonus_txt": "Bonus", "total_pay": "Total to pay", "pay_info": "Send MATIC/USDT (Polygon) to:", "supported_wallets": "Supported Wallets:", "open_wallet_btn": "Open Wallet App", "manual_check": "Please confirm transaction in your wallet.",
        "contract_btn": "View on PolygonScan", "contract_help": "Verify contract on PolygonScan",
        "payment_notice": "⚠️ Payment will be enabled soon!"
    },
    "العربية": {
        "nav": ["نظرة عامة", "خارطة الطريق", "لوحة التحكم", "البيع المسبق والإحالات", "قريباً التخزين", "سوق البيع بين الأعضاء", "اتصل بنا"],
        "hero": "عملة PMTX: مستقبل التمويل", "sub": "تخزين، حرق، ونمو هائل.",
        "hero_desc": "انضم لنظامنا البيئي المتكامل. بروتوكولات الأمان تضمن نمو أصولك.",
        "why_buy_now": "سعر المرحلة الأولى 0.00005$ فقط! لا تفوت فرصة الدخول قبل ارتفاع السعر.",
        "marketing_pitch": "أنت الآن في المرحلة الأولى (0.00005$). السعر سيتدرج إلى 0.0001$ ثم 0.0003$. هدفنا عند الإدراج بين 0.20$ و 0.50$. وبفضل الحرق والتخزين، نطمح للوصول إلى 1 دولار وأكثر! اغتنم الفرصة الآن.",
        "roadmap_title": "خارطة الطريق", "presale_header": "💎 مراحل البيع المسبق",
        "target_price": "سعر الإدراج النهائي:", "rm": ["المرحلة 1: الانطلاق", "الإيردروب والبيع المسبق", "المرحلة 2: الانكماش", "حرق العملات", "المرحلة 3: المنفعة", "عائدات التخزين"],
        "rm_footer": "صممت PMTX للنمو طويل الأمد.", "ref": "البيع المسبق والإحالات", "user_lbl": "اسم المستخدم:", "gen_btn": "إنشاء الرابط",
        "connect": "ربط المحفظة", "bal": "الرصيد", "soon": "قريباً جداً!", "inv_btn": "حساب مكافأة 2%", "inv_text": "أدخل قيمة الاستثمار ($)",
        "p1": "0.00005 $", "p2": "0.0001 $", "p3": "0.0003 $", "promo": "ضاعف أرباحك اليوم!", "explain": "مكافأة 2% من الاستثمار.",
        "airdrop_title": "خيارات الإيردروب", "opt1": "إكمال المهام (1,000 PMTX)", "task_desc": "تابع، أعجب، أعد تغريد وتاغ لـ 3 أصدقاء.",
        "opt2": "الاستلام السريع (500 PMTX)", "express_desc": "احصل على 500 PMTX فوراً بدون مهام.",
        "wallet_info": "تأكد من أن محفظتك على شبكة Polygon.", "connect_pay": "ربط المحفظة", "already_claimed": "✅ تم استلام الإيردروب مسبقاً!",
        "go_to_twitter": "📢 انتقل إلى تغريدة تويتر/X", "tweet_input": "أدخل رابط التغريدة:", "verify_btn": "تحقق واستلم 1,000 PMTX",
        "setup_required": "🔒 أكمل الإعدادات للمطالبة بالإيردروب", "connect_wallet": "🔗 ربط المحفظة (Polygon)",
        "link_twitter": "🐦 ربط حساب تويتر", "wallet_success": "✅ تم ربط المحفظة", "twitter_success": "✅ تم ربط حساب تويتر",
        "pending_text": "الجائزة المعلقة", "pay_btn": "استلم العملات",
        "roadmap_details": ["الربع الثالث 2026: الإطلاق", "الربع الرابع 2026: التخزين", "الربع الأول 2027: الإدراج"],
        "why_pmtx": "لماذا PMTX؟ نحن ندمج الندرة مع كفاءة التمويل اللامركزي. انضم إلينا لتعزيز نمو أصولك.",
        "buy_title": "🚀 الفرصة الذهبية: المرحلة الأولى!", "inv_label": "مبلغ الاستثمار ($)", "receive_text": "سوف تحصل على", "bonus_txt": "مكافأة", "total_pay": "إجمالي المبلغ", "pay_info": "أرسل MATIC/USDT (Polygon) إلى:", "supported_wallets": "المحافظ المدعومة:", "open_wallet_btn": "افتح تطبيق المحفظة", "manual_check": "يرجى تأكيد العملية في محفظتك.",
        "contract_btn": "عرض على PolygonScan", "contract_help": "تحقق من العقد على PolygonScan",
        "payment_notice": "⚠️ سيتم تفعيل الدفع قريباً!"
    },
    "日本語": {
        "nav": ["概要", "ロードマップ", "ダッシュボード", "プレセール", "ステーキング", "P2P市場", "お問い合わせ"],
        "hero": "PMTX COIN: 金融の未来", "sub": "ステーキングと成長.",
        "hero_desc": "堅牢なエコシステム.",
        "why_buy_now": "フェーズ1の価格はわずか0.00005ドル！この早期参入のチャンスをお見逃しなく。",
        "marketing_pitch": "現在フェーズ1（0.00005ドル）です。価格は0.0001ドル、0.0003ドルへと段階的に上昇します。上場目標は0.20〜0.50ドル。ステーキングとバーンにより、1ドル超えを目指します！今すぐ参加してください。",
        "roadmap_title": "ロードマップ", "presale_header": "💎 PMTX プレセール",
        "target_price": "最終上場目標:", "rm": ["開始", "エアドロップ", "デフレ", "バーン", "ユーティリティ", "ステーキング"],
        "rm_footer": "長期的な成長.", "ref": "プレセール", "user_lbl": "ユーザー名:", "gen_btn": "リンク生成",
        "connect": "ウォレット接続", "bal": "残高", "soon": "まもなく", "inv_btn": "2%報酬計算", "inv_text": "投資額 ($)",
        "p1": "0.00005 $", "p2": "0.0001 $", "p3": "0.0003 $", "promo": "利益を2倍に!", "explain": "投資額の2%.",
        "airdrop_title": "エアドロップオプション", "opt1": "タスク完了 (1,000 PMTX)", "task_desc": "フォロー、いいね、RT、3人タグ付け。",
        "opt2": "クイック請求 (500 PMTX)", "express_desc": "ソーシャルタスクなしで即時取得.",
        "wallet_info": "Polygonネットワークを確認.", "connect_pay": "接続", "already_claimed": "✅ 受取済み!",
        "go_to_twitter": "📢 Twitter/X投稿へ移動", "tweet_input": "ツイートリンクを入力:", "verify_btn": "確認して1,000 PMTXを取得",
        "setup_required": "🔒 エアドロップ請求のための設定", "connect_wallet": "🔗 ウォレット接続 (Polygon)",
        "link_twitter": "🐦 Twitter連携", "wallet_success": "✅ 接続済み", "twitter_success": "✅ 連携済み",
        "pending_text": "保留中の報酬", "pay_btn": "取得",
        "roadmap_details": ["2026 Q3: 開始", "2026 Q4: ステーキング", "2027 Q1: 上場"],
        "why_pmtx": "PMTXを選ぶ理由：希少性と分散型効率の融合。資産の成長のために私たちに参加してください。",
        "buy_title": "🚀 黄金のチャンス：フェーズ1！", "inv_label": "投資額 ($)", "receive_text": "受取額", "bonus_txt": "ボーナス", "total_pay": "支払い合計", "pay_info": "MATIC/USDT (Polygon) 送付先:", "supported_wallets": "対応ウォレット:", "open_wallet_btn": "ウォレットを開く", "manual_check": "ウォレットで確認してください。",
        "contract_btn": "PolygonScanで表示", "contract_help": "コントラクトを確認",
        "payment_notice": "⚠️ 支払いはまもなく有効になります！"
    },
    "Français": {
        "nav": ["Aperçu", "Roadmap", "Tableau", "Prévente", "Staking", "Marché P2P", "Contact"],
        "hero": "PMTX COIN: Futur financier", "sub": "Staking et Croissance.",
        "hero_desc": "Rejoignez notre écosystème.",
        "why_buy_now": "Le prix de la phase 1 est de seulement 0,00005 $ ! Ne manquez pas cette entrée.",
        "marketing_pitch": "Vous êtes en Phase 1 (0,00005 $). Les prix monteront à 0,0001 $ puis 0,0003 $. Nous visons 0,20 $ - 0,50 $ lors de la cotation. Avec le staking et le burn, nous visons 1 $ et plus ! Investissez maintenant.",
        "roadmap_title": "Roadmap", "presale_header": "💎 Étapes de prévente",
        "target_price": "Prix cible final:", "rm": ["Lancement", "Airdrop", "Déflation", "Burn", "Utilité", "Staking"],
        "rm_footer": "Croissance long terme.", "ref": "Prévente et Parrainage", "user_lbl": "Utilisateur:", "gen_btn": "Générer",
        "connect": "Connecter", "bal": "Solde", "soon": "Bientôt", "inv_btn": "Calculer 2% récompense", "inv_text": "Investissement ($)",
        "p1": "0.00005 $", "p2": "0.0001 $", "p3": "0.0003 $", "promo": "Doublez vos profits!", "explain": "2% de récompense.",
        "airdrop_title": "Options d'Airdrop", "opt1": "Tâches (1,000 PMTX)", "task_desc": "Suivre, Aimer, RT et taguer 3 amis.",
        "opt2": "Réclamation Express (500 PMTX)", "express_desc": "Obtenez 500 PMTX instantanément.",
        "wallet_info": "Assurez-vous d'être sur Polygon.", "connect_pay": "Connecter", "already_claimed": "✅ Déjà réclamé !",
        "go_to_twitter": "📢 Aller au tweet Twitter/X", "tweet_input": "Entrez le lien du tweet :", "verify_btn": "Vérifier & Réclamer 1,000 PMTX",
        "setup_required": "🔒 Configuration pour l'Airdrop", "connect_wallet": "🔗 Connecter le portefeuille",
        "link_twitter": "🐦 Lier Twitter", "wallet_success": "✅ Portefeuille connecté", "twitter_success": "✅ Twitter lié",
        "pending_text": "Récompense en attente", "pay_btn": "Réclamer",
        "roadmap_details": ["T3 2026: Lancement", "T4 2026: Staking", "T1 2027: Cotation"],
        "why_pmtx": "Pourquoi PMTX ? Nous allions rareté et efficacité décentralisée. Rejoignez-nous pour la croissance de vos actifs.",
        "buy_title": "🚀 Opportunité en Or : Phase 1 !", "inv_label": "Investissement ($)", "receive_text": "Vous recevez", "bonus_txt": "Bonus", "total_pay": "Total à payer", "pay_info": "Envoyer MATIC/USDT (Polygon) à:", "supported_wallets": "Wallets supportés:", "open_wallet_btn": "Ouvrir l'application", "manual_check": "Veuillez confirmer dans votre portefeuille.",
        "contract_btn": "Voir sur PolygonScan", "contract_help": "Vérifier le contrat",
        "payment_notice": "⚠️ Le paiement sera activé bientôt !"
    },
    "Español": {
        "nav": ["Resumen", "Hoja de ruta", "Panel", "Preventa", "Staking", "Mercado P2P", "Contacto"],
        "hero": "PMTX COIN: Futuro financiero", "sub": "Staking y Crecimiento.",
        "hero_desc": "Ecosistema robusto.",
        "why_buy_now": "¡El precio de la fase 1 es de solo 0.00005$! No pierdas esta oportunidad de entrada.",
        "marketing_pitch": "Estás en la Fase 1 (0.00005$). El precio subirá a 0.0001$ y luego a 0.0003$. Apuntamos a 0.20$ - 0.50$ al listarse. Con staking y quema de tokens, ¡buscamos llegar a 1$ o más! Invierte ahora.",
        "roadmap_title": "Hoja de ruta", "presale_header": "💎 Etapas de preventa",
        "target_price": "Precio objetivo:", "rm": ["Lanzamiento", "Airdrop", "Deflación", "Quema", "Utilidad", "Staking"],
        "rm_footer": "Diseñado para crecer.", "ref": "Preventa y Referidos", "user_lbl": "Usuario:", "gen_btn": "Generar",
        "connect": "Conectar", "bal": "Saldo", "soon": "Pronto", "inv_btn": "Calcular 2% recompensa", "inv_text": "Inversión ($)",
        "p1": "0.00005 $", "p2": "0.0001 $", "p3": "0.0003 $", "promo": "¡Duplica tus ganancias!", "explain": "2% de recompensa.",
        "airdrop_title": "Opciones de Airdrop", "opt1": "Tareas (1,000 PMTX)", "task_desc": "Seguir, Like, RT y taguer 3 amigos.",
        "opt2": "Reclamo Express (500 PMTX)", "express_desc": "Obtén 500 PMTX al instante.",
        "wallet_info": "Asegúrate de estar en Polygon.", "connect_pay": "Conectar", "already_claimed": "✅ ¡Ya reclamado!",
        "go_to_twitter": "📢 Ir a la publicación de Twitter/X", "tweet_input": "Ingresa el enlace del tweet:", "verify_btn": "Verificar y Reclamar 1,000 PMTX",
        "setup_required": "🔒 Configuración para Airdrop", "connect_wallet": "🔗 Conectar billetera",
        "link_twitter": "🐦 Vincular Twitter", "wallet_success": "✅ Billetera conectada", "twitter_success": "✅ Twitter vinculado",
        "pending_text": "Recompensa pendiente", "pay_btn": "Reclamar",
        "roadmap_details": ["T3 2026: Lanzamiento", "T4 2026: Staking", "T1 2027: Listado"],
        "why_pmtx": "¿Por qué PMTX? Unimos escasez con eficiencia descentralizada. Únete para priorizar el crecimiento de tus activos.",
        "buy_title": "🚀 ¡Oportunidad de Oro: Fase 1!", "inv_label": "Inversión ($)", "receive_text": "Recibes", "bonus_txt": "Bono", "total_pay": "Total a pagar", "pay_info": "Enviar MATIC/USDT (Polygon) a:", "supported_wallets": "Billeteras soportadas:", "open_wallet_btn": "Abrir billetera", "manual_check": "Por favor confirma en tu billetera.",
        "contract_btn": "Ver en PolygonScan", "contract_help": "Verificar contrato",
        "payment_notice": "⚠️ ¡El pago se activará pronto!"
    },
    "Deutsch": {
        "nav": ["Überblick", "Roadmap", "Dashboard", "Vorverkauf", "Staking", "P2P-Markt", "Kontakt"],
        "hero": "PMTX COIN: Finanzzukunft", "sub": "Staking und Wachstum.",
        "hero_desc": "Robustes Ökosystem.",
        "why_buy_now": "Der Preis der Phase 1 beträgt nur 0,00005 $! Verpassen Sie nicht diesen frühen Einstieg.",
        "marketing_pitch": "Sie befinden sich in Phase 1 (0,00005 $). Der Preis steigt auf 0,0001 $ und dann auf 0,0003 $. Wir streben 0,20 $ - 0,50 $ bei der Listung an. Durch Staking und Burn-Strategien zielen wir auf 1 $ und mehr ab! Jetzt einsteigen.",
        "roadmap_title": "Roadmap", "presale_header": "💎 Vorverkaufsphasen",
        "target_price": "Zielpreis:", "rm": ["Start", "Airdrop", "Deflation", "Burn", "Nutzen", "Staking"],
        "rm_footer": "Auf Wachstum ausgelegt.", "ref": "Vorverkauf & Empfehlungen", "user_lbl": "Benutzername:", "gen_btn": "Erstellen",
        "connect": "Verbinden", "bal": "Guthaben", "soon": "Bald", "inv_btn": "2% Belohnung", "inv_text": "Investition ($)",
        "p1": "0.00005 $", "p2": "0.0001 $", "p3": "0.0003 $", "promo": "Verdoppeln Sie Ihre Gewinne!", "explain": "2% Belohnung.",
        "airdrop_title": "Airdrop-Optionen", "opt1": "Aufgaben (1,000 PMTX)", "task_desc": "Folgen, Like, RT & markiere 3 Freunde.",
        "opt2": "Express-Anspruch (500 PMTX)", "express_desc": "Erhalte 500 PMTX sofort.",
        "wallet_info": "Stelle sicher, dass du im Polygon-Netzwerk bist.", "connect_pay": "Verbinden", "already_claimed": "✅ Beansprucht!",
        "go_to_twitter": "📢 Zum Twitter/X-Beitrag", "tweet_input": "Tweet-Link eingeben:", "verify_btn": "Verifizieren & 1,000 PMTX erhalten",
        "setup_required": "🔒 Airdrop-Einrichtung", "connect_wallet": "🔗 Wallet verbinden",
        "link_twitter": "🐦 Twitter verknüpfen", "wallet_success": "✅ Wallet verbunden", "twitter_success": "✅ Twitter verknüpft",
        "pending_text": "Ausstehende Belohnung", "pay_btn": "Anspruch",
        "roadmap_details": ["Q3 2026: Start", "Q4 2026: Staking", "Q1 2027: Listung"],
        "why_pmtx": "Warum PMTX? Wir verbinden Knappheit mit dezentraler Effizienz. Schließen Sie sich uns an.",
        "buy_title": "🚀 Goldene Chance: Phase 1!", "inv_label": "Investition ($)", "receive_text": "Du erhältst", "bonus_txt": "Bonus", "total_pay": "Gesamtbetrag", "pay_info": "Sende MATIC/USDT (Polygon) an:", "supported_wallets": "Unterstützte Wallets:", "open_wallet_btn": "Wallet öffnen", "manual_check": "Bitte bestätige in deiner Wallet.",
        "contract_btn": "Auf PolygonScan ansehen", "contract_help": "Kontrakt prüfen",
        "payment_notice": "⚠️ Die Zahlung wird in Kürze aktiviert!"
    }
}
# 5. اختيار اللغة
lang = st.sidebar.selectbox(" Language / اللغة", list(i18n.keys()))
t = i18n[lang]

# 6. القائمة الجانبية (بعد حذف زر الاتصال بالمحفظة مع الحفاظ على توافق اللغات)
# 1. إضافة زر العقد الذكي في الأعلى
st.sidebar.markdown("### 🛡️ Smart Contract")

polygonscan_url = "https://polygonscan.com/address/0xc4AF4aEeBab3B717f771941ce7F1A3E4C765a53E"

# التوافق التام مع اللغات الـ 6 باستخدام .get()
st.sidebar.link_button(
    t.get("contract_btn", "View on PolygonScan"), 
    polygonscan_url, 
    help=t.get("contract_help", "Verify contract on PolygonScan")
)

# 2. إضافة رابط تويتر الرسمي
st.sidebar.markdown("### 📢 Official Community")
st.sidebar.link_button("Follow @PMTXCoin", "https://x.com/PMTXCoin")

# 3. إضافة فاصل قبل قائمة الصفحات
st.sidebar.markdown("---")

# 4. قائمة الصفحات (تأتي الآن في الأسفل)
page = st.sidebar.radio("PMTX COIN", t["nav"])

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

# 7. تنظيم الصفحات باستخدام التبويبات الأفقية (Tabs)
tabs = st.tabs(t["nav"])

# 1. صفحة Overview (التبويب الأول)
with tabs[0]:
    st.markdown(f"## 🌟 {t.get('buy_title')}")
    
    st.markdown(f'''
        <p class="glowing-text">🚀 PMTX Price: {t.get("p1")} 🚀</p>
    ''', unsafe_allow_html=True)
    
    st.success(f"### 🔥 {t.get('why_buy_now')}")
    
    with st.expander("📊 " + t.get('roadmap_title', 'Details'), expanded=True):
        # نص مطور: حجم أكبر، تأثير لمعان، وصواريخ
        st.markdown(f'''
            <div class="glowing-text" style="font-size: 1.5rem !important; line-height: 1.6; padding: 15px; border-radius: 15px; background: rgba(126, 34, 206, 0.1);">
                🚀 {t.get('marketing_pitch')} 🚀
            </div>
        ''', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        col1.metric(t["rm"][0], t.get('p1'))
        col2.metric(t["rm"][2], t.get('p2'))
        col3.metric(t["rm"][4], t.get('p3'))
    
    st.subheader(f"💰 {t['bal']}")
    col_bal1, col_bal2 = st.columns(2)
    with col_bal1:
        st.metric("PMTX", f"{st.session_state.balance:,.0f}")
    with col_bal2:
        usd_value = st.session_state.balance * 0.2
        st.metric("USD", f"${usd_value:,.2f}")

    # قسم الاستثمار
    if not st.session_state.get('airdrop_claimed', False):
        st.info(f"ℹ️ {t.get('inv_label', 'Investment')}: 10$ - 1,000$")
        investment = st.number_input(label=str(t.get('inv_label')), min_value=1.0, max_value=2000.0, value=10.0)
        if 10 <= investment <= 1000:
            tokens_base = investment / 0.00005
            bonus = 1000 + ((investment - 10) / 990 * 9000)
            st.success(f"{t.get('receive_text')}: **{int(tokens_base + bonus):,.0f} PMTX**")
            st.write(f"💳 {t.get('pay_info')}:")
            st.code("0xc4AF4aEeBab3B717f771941ce7F1A3E4C765a53E", language="text")
            
            # --- التعديلات المطلوبة هنا ---
            
            # 1. إضافة رسالة "قريباً" المتوافقة مع اللغة (بدلاً من رسالة ثابتة)
            st.warning(t.get("payment_notice", "⚠️ Payment will be enabled soon!"))
            
            # 2. زر الشراء مع حفظ الرصيد في الـ Session State
            if st.button(t.get('pay_btn'), key="pay_button_main"):
                # حساب الرصيد الجديد
                new_balance = int(tokens_base + bonus)
                # حفظه في الذاكرة ليظهر في الـ Dashboard
                st.session_state.balance = new_balance
                # تأثير احتفالي
                st.balloons()
                # رسالة نجاح تظهر للمستخدم باسمه
                st.info(f"✅ {st.session_state.username}, {t.get('already_claimed', 'Request saved!')}")

# 2. صفحة Roadmap
with tabs[1]:
    st.subheader(f"📍 {t['roadmap_title']}")
    st.info(t["why_pmtx"])
    st.markdown(f"### {t['presale_header']}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Phase 1", t["p1"])
    col2.metric("Phase 2", t["p2"])
    col3.metric("Phase 3", t["p3"])
    st.markdown(f"**{t['target_price']}** 🚀 <span style='color: #FFD700; font-size: 24px;'>0.50 $</span>", unsafe_allow_html=True)
    st.divider()
    st.markdown("### 🗓️ Project Timeline")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"#### {t['roadmap_details'][0]}")
    c2.markdown(f"#### {t['roadmap_details'][1]}")
    c3.markdown(f"#### {t['roadmap_details'][2]}")
    st.divider()
    st.info(t["rm_footer"])

# 3. صفحة Dashboard
with tabs[2]:
    st.subheader(f"📈 {t['nav'][2]}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total PMTX", f"{st.session_state.balance:,.0f}")
    col2.metric("Referrals", "0")
    col3.metric("Growth", "+15%")

# 4. صفحة Presale & Referrals
with tabs[3]:
    st.subheader(f"🔗 {t['ref']}")
    st.info(f"🚀 {t['promo']}")
    user_input = st.text_input(t["user_lbl"], value=st.session_state.username)
    if st.button(t["gen_btn"]):
        st.session_state.username = user_input
        ref_link = f"https://pmtx-coin-official2026.streamlit.app/?ref={user_input}"
        st.success(f"🔗 Your Referral Link: {ref_link}")
        st.code(ref_link, language="text")
    st.divider()
    st.warning(f"💡 {t['explain']}")
    inv = st.number_input(t["inv_text"], min_value=0.0, step=10.0)
    if st.button(t["inv_btn"]):
        commission = inv * 0.02
        st.session_state.balance += commission
        st.success(f"🎉 2% Commission Calculated: ${commission:,.2f} added to your balance!")
        st.rerun()

# 5. الصفحات التي قيد الإنشاء (Staking & P2P)
with tabs[4]:
    st.markdown(f'<div class="soon-box">{t["soon"]}</div>', unsafe_allow_html=True)

with tabs[5]:
    st.markdown(f'<div class="soon-box">{t["soon"]}</div>', unsafe_allow_html=True)

# 6. صفحة Contact Us
with tabs[6]:
    st.subheader("✉️ اتصل بنا / Contact Us")
    with st.form("contact_form"):
        st.text_input("Name (You can use a pseudonym)")
        st.text_area("رسالتك / Message")
        st.form_submit_button("إرسال / Submit")
