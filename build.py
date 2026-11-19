# -*- coding: utf-8 -*-
"""Генерира сайта BoxLab: index.html, apps/<slug>.html и css/style.css.
Редактирай данните в APPS и пусни:  python build.py
"""
from pathlib import Path
from html import escape
import qrcode

ROOT = Path(__file__).parent
REVOLUT = "https://revolut.me/5co5cov"
EMAIL = "ppdesigned@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/petko-petkov-096461bb"
FACEBOOK = "https://www.facebook.com/petko.petkov.104"

DL_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
           '<path d="M12 3v12M7 10l5 5 5-5M5 21h14"/></svg>')
ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')

# ------------------------------------------------------------------ данни
APPS = [
  dict(
    slug="schoolcontrol", name="SchoolControl", group="school", version="8.1",
    img="schoolcontrol.webp", bg="#1e293b",
    motto="Централизирано управление на ученически компютри",
    short="Управление на компютърните кабинети от едно място: изключване, рестартиране, заключване на екрана и съобщения до учениците, статус на всеки компютър в реално време. Включва уеб панел с QR код за управление от телефона.",
    about=[
      "SchoolControl събира всички компютри от кабинетите в един прозорец. Учителят вижда кои машини са включени и с едно натискане изключва, рестартира или заключва целия кабинет или отделен компютър.",
      "Уеб панелът позволява същото от телефона: сканирате QR кода и управлявате кабинета, докато обикаляте между учениците.",
    ],
    features=[
      "Статус на всички компютри в реално време, с автоматично опресняване",
      "Групови бутони за всеки кабинет и карта за всеки отделен компютър",
      "Изключване, рестартиране и заключване на екрана",
      "Съобщения, които се показват на екрана на учениците",
      "Уеб панел с вход, роли и достъп по кабинети",
      "QR код за бърз вход от телефон; по избор достъп и извън училище",
      "Дневник на действията с цветово отбелязване",
      "Работи от системния трей",
    ],
    reqs=[
      "Учителски компютър: Windows 10 / 11 (64-bit)",
      "Отделна версия за Windows 7 (64-bit)",
      "Ученически компютри с Windows в същата локална мрежа",
      "Администраторски акаунт на ученическите компютри",
      "Права на администратор за инсталирането",
    ],
    downloads=[("Windows 10 / 11", "https://drive.google.com/file/d/1OH3-gC4MhzktRUD9_4znTt1HQbsIjUmk/view?usp=drive_link", "46 MB"),
               ("Windows 7 (64-bit)", "https://drive.google.com/file/d/1CXPhzK3GliVkLU9mATM-00afcTiWIHGd/view?usp=drive_link", "36 MB")],
    note="Инсталаторът включва ръководство на български с илюстрации.",
  ),
  dict(
    slug="fvs-coach", name="FVS Coach", group="school", version="1.1",
    img="fvscoach.webp", bg="#111827",
    motto="От учители за учители!",
    short="Софтуерен инструмент за оценяване на физическата дееспособност на учениците от 1 до 12 клас — класове, измервания, оценки по критериите и проследяване на напредъка.",
    about=[
      "FVS Coach е помощник за учителя по физическо възпитание и спорт. Въвеждате резултатите от измерванията, а програмата изчислява оценките по критериите за съответния клас.",
      "Резултатите се пазят по класове и ученици, така че напредъкът се вижда от година на година.",
    ],
    features=[
      "Класове и ученици от 1 до 12 клас",
      "Въвеждане на резултатите от измерванията",
      "Автоматично оценяване на физическата дееспособност по критериите",
      "Проследяване на напредъка на всеки ученик",
      "Уеб панел за учителите",
      "Ръководство с илюстрации (PDF), достъпно от менюто „Старт“",
    ],
    reqs=["Windows 10 / 11 (64-bit)", "Права на администратор за инсталирането", "Браузър за уеб панела"],
    downloads=[("Изтегли", "https://drive.google.com/file/d/1Hf_mr8f53ITGiLJ4NSSNK9ZMdFgHavs0/view?usp=drive_link", "82 MB")],
  ),
  dict(
    slug="schbox", name="SCHBox", group="school", status="soon",
    img="schbox.webp", bg="#242449",
    motto="Създаване на учебни седмични разписания",
    short="Седмични програми за класове, учители и кабинети. Учители специалисти, заключени часове, ръчно местене с влачене, други дейности и дежурства. Експорт в Word, Excel и PDF и директен печат.",
    about=[
      "SCHBox генерира седмичната програма на училището: за всеки клас, учител и кабинет. Подходящ е както за малки, така и за големи училища.",
      "Часовете на учителите специалисти се заключват, а останалите се нареждат около тях. Всеки час може да се премести ръчно с влачене, без генераторът да го разбърква после.",
    ],
    features=[
      "Учители, предмети, кабинети, паралелки и звънци",
      "Учители специалисти със заключени часове",
      "Ръчно местене на часове с влачене",
      "Консултации, приемно време и други дейности",
      "График за дежурства",
      "Програма за всеки клас, учител и кабинет",
      "Експорт в Word, Excel и PDF и директен печат на A4",
    ],
    reqs=["Windows 10 / 11 (64-bit)"],
    downloads=[],
    note="Приложението е в последна фаза на тестване.",
  ),
  dict(
    slug="boxmag", name="BoxMAG", group="other", version="2.4",
    img="boxmag.webp", bg="#2b2876",
    motto="От пиксела до рафта",
    short="Разгъвки на опаковки — кутии, торбички, етикети, чаши — с 3D преглед, поставяне на дизайн и експорт в PDF, SVG, EPS и PNG. Създадена за учениците по графичен дизайн.",
    about=[
      "BoxMAG създава разгъвки на опаковки по зададени размери. Избирате шаблон, въвеждате размерите и получавате готов нож с линии за биговане и зони за лепене.",
      "Върху разгъвката поставяте своя дизайн и веднага го виждате в 3D: кутията се върти, отваря и затваря.",
    ],
    features=[
      "Параметрични шаблони за кутии, торбички, етикети, чаши и др.",
      "3D преглед с въртене, отваряне и затваряне",
      "Поставяне на дизайн върху разгъвката",
      "Експорт в PDF, SVG, EPS, PNG и JPEG със спот цветове за нож и биговане",
      "Видео на 3D модела в MP4",
      "Печат в реален размер, с разделяне на няколко листа",
      "Собствен файл на проекта (.bmg)",
    ],
    reqs=["Windows 10 / 11 (64-bit)", "Видеокарта с OpenGL 3.3 за 3D прегледа (има и по-бавен софтуерен режим)"],
    downloads=[("Изтегли", "https://drive.google.com/file/d/1gAkdbxF0jY8W7kGCFCd62C63rsixD9_W/view?usp=drive_link", "64 MB")],
    note="Безплатна за държавни училища за образователни цели. Фирми и частни организации, включително частни училища и курсове, моля, свържете се с мен преди употреба.",
  ),
  dict(
    slug="imagebox", name="ImageBox", group="other", version="2.7",
    img="imagebox.webp", bg="#d6d6d6",
    motto="Преглед, конвертиране и редакция на изображения",
    short="JPG, PNG, HEIC, RAW, PSD, CDR, AI, EPS и още. Вграден видео плейър и конвертор, корекции, печат и сканиране, меню с десен бутон в Windows.",
    about=[
      "ImageBox отваря почти всеки графичен файл: от снимки от телефона до файлове на Photoshop, Illustrator и CorelDRAW. Конвертира един или много файлове наведнъж.",
      "Има вграден плейър и конвертор за видео и аудио, а в Explorer показва истински миниатюри и на файлове като CDR, PSD и EPS.",
    ],
    features=[
      "Преглед на растерни, RAW и векторни формати (HEIC, AVIF, PSD, CDR, AI, EPS, SVG…)",
      "Конвертиране на един или много файлове наведнъж",
      "Изрязване, корекции на яркост, контраст, сенки и цвят",
      "Вграден видео и аудио плейър и конвертор",
      "Печат и сканиране, включително многостраничен PDF",
      "Меню с десен бутон и миниатюри в Windows Explorer",
      "Бутон „Отвори с“ към инсталираните графични програми",
    ],
    reqs=["Windows 10 / 11 (64-bit)"],
    downloads=[("Изтегли", "https://drive.google.com/file/d/10o6xnFEgeAXe3vDWp8zsMofTRRjuY5nA/view?usp=drive_link", "319 MB")],
    note="ImageBox е безплатна програма и не се продава.",
  ),
  dict(
    slug="downbox", name="DownBox", group="other", version="1.2",
    img="downbox.webp", bg="#440018",
    motto="Свали всяко видео от интернет",
    short="Видео до 4K, MP3 с обложка и субтитри (SRT) от YouTube, Vimeo, TikTok, Facebook, Instagram и VBox7.",
    about=[
      "Поставяте линк, а DownBox показва наличните резолюции и вие избирате коя да изтеглите: 4K, Full HD, 720p и други.",
      "Може да изтеглите и само звука като MP3, като обложката на видеото става обложка на песента.",
    ],
    features=[
      "YouTube, Vimeo, TikTok, Facebook, Instagram и VBox7",
      "Избор на резолюция — до 4K",
      "MP3 с обложка от видеото",
      "Субтитри (SRT)",
    ],
    reqs=["Windows 10 / 11 (64-bit)", "Интернет връзка"],
    downloads=[("Изтегли", "https://drive.google.com/file/d/1Vm9qY-jGfGt747HTL3-gNJ50uSFfgp23/view?usp=drive_link", "174 MB")],
    note="Използвайте DownBox само за съдържание, което имате право да изтегляте.",
  ),
  dict(
    slug="ibox", name="iBox", group="other",
    img="ibox.webp", bg="#e6e7e8",
    motto="Твоят дигитален мост",
    short="Трансфер на музика, снимки, видео, рингтонове и файлове към iPhone и iPad по кабел и пълен архив на устройството.",
    about=[
      "iBox свързва вашия iPhone или iPad с компютъра по кабел. Прехвърляте музика, снимки, видео, рингтонове и файлове и правите пълен архив на устройството.",
      "За музиката и рингтоните iBox работи заедно с iTunes. Снимките, видеото, файловете и архивът работят и без него.",
    ],
    features=[
      "Музика и рингтони към iPhone и iPad",
      "Снимки и видео — в двете посоки",
      "Файлове към приложенията на устройството",
      "Пълен архив (backup) на устройството",
      "Вграден музикален плейър",
      "Работи по USB кабел — бързо и сигурно",
    ],
    reqs=[
      "Windows 10 / 11 (64-bit), 64-битов процесор",
      "Минимум 4 GB RAM и около 500 MB свободно място (архивите заемат допълнително)",
      "Класически iTunes за Windows (64-bit) от apple.com — за музика и рингтони. Версията от Microsoft Store не върши работа.",
      "Драйвер Apple Mobile Device (идва с iTunes)",
      "USB кабел (Lightning или USB-C) и „Доверие“ на устройството",
    ],
    downloads=[("Изтегли", "https://drive.google.com/file/d/19aaS3BB-kCN-iVnfD7NAsqAmKjWdIBgS/view?usp=drive_link", "125 MB")],
    note="Инсталаторът проверява дали iTunes е инсталиран и ако липсва, предлага да го изтегли от сайта на Apple.",
  ),
  dict(
    slug="rdbox", name="rdBox", group="other", status="dev",
    img=None, bg=None,
    motto="Отдалечен достъп до компютър",
    short="В локалната мрежа или през интернет, със защитена връзка, списък с любими компютри и прехвърляне на файлове.",
    about=["rdBox е програма за отдалечен достъп до компютър, подобна на TeamViewer и AnyDesk. В момента е в разработка."],
    features_title="Планирани функции",
    features=[
      "Връзка в локалната мрежа и през интернет",
      "Вход с парола и криптирана връзка",
      "Списък с любими компютри",
      "Прехвърляне на файлове",
    ],
    reqs=["Windows 10 / 11 (64-bit)"],
    downloads=[],
  ),
]

# ------------------------------------------------------------------ помощни
def qr_svg(url, cls="qr"):
    q = qrcode.QRCode(border=2, error_correction=qrcode.constants.ERROR_CORRECT_M)
    q.add_data(url); q.make(fit=True)
    m = q.get_matrix(); n = len(m)
    d = "".join(f"M{x},{y}h1v1h-1z" for y, r in enumerate(m) for x, v in enumerate(r) if v)
    return (f'<svg class="{cls}" viewBox="0 0 {n} {n}" role="img" aria-label="QR код към revolut.me/5co5cov" '
            f'shape-rendering="crispEdges"><rect width="{n}" height="{n}" fill="#fff"/><path d="{d}" fill="#121826"/></svg>')

QR = qr_svg(REVOLUT)

def tag(a):
    st = a.get("status")
    if st == "soon": return '<span class="tag soon">Очаквайте скоро</span>'
    if st == "dev":  return '<span class="tag dev">В разработка</span>'
    return f'<span class="tag">v{a["version"]}</span>' if a.get("version") else ""

def shot(a, prefix, big=False):
    cls = "shot big" if big else "shot"
    if a["img"]:
        return (f'<div class="{cls}" style="--shot:{a["bg"]}"><img src="{prefix}img/{a["img"]}" '
                f'alt="Splash екран на {escape(a["name"])}"{"" if big else " loading=\"lazy\""}></div>')
    return (f'<div class="{cls} rd"><div><b>rd<span>Box</span></b><small>Remote Desktop</small></div></div>')

def head(title, prefix, desc):
    return f'''<!DOCTYPE html>
<html lang="bg">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Onest:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}css/style.css">
<script data-goatcounter="https://5co.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</head>
<body>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="{prefix}index.html" aria-label="BoxLab — към началото"><img src="{prefix}img/boxlab-logo.webp" alt="BoxLab" width="166" height="34"></a>
    <nav aria-label="Основно меню">
      <a href="{prefix}index.html#school">Инструменти за училище</a>
      <a href="{prefix}index.html#other">Други инструменти</a>
      <a href="{prefix}index.html#about">За мен</a>
      <a href="{prefix}index.html#contact">Контакти</a>
    </nav>
    <a class="btn btn-accent" href="{REVOLUT}" target="_blank" rel="noopener" data-goatcounter-click="revolut" data-goatcounter-title="Revolut — подкрепа">Подкрепи разработките</a>
  </div>
</header>
'''

def foot(prefix):
    return f'''<footer>
  <div class="wrap">
    <span>BoxLab · © 2026 Петко Петков (5co). Всички права запазени.</span>
    <a href="#top">Към началото ↑</a>
  </div>
</footer>
</body>
</html>
'''

# ------------------------------------------------------------------ главна
def card(a):
    url = f"apps/{a['slug']}.html"
    return f'''        <article class="card">
          <a class="card-link" href="{url}" tabindex="-1" aria-hidden="true">{shot(a, "")}</a>
          <div class="body">
            <h3><a href="{url}">{escape(a["name"])}</a> {tag(a)}</h3>
            <p class="motto">{escape(a["motto"])}</p>
            <p class="desc">{escape(a["short"])}</p>
            <div class="dl">
              <a class="btn btn-accent" href="{url}">Виж повече{ARROW}</a>
            </div>
          </div>
        </article>
'''

def build_index():
    school = "".join(card(a) for a in APPS if a["group"] == "school")
    other = "".join(card(a) for a in APPS if a["group"] == "other")
    html = head("BoxLab — програмите на 5co", "",
                "Безплатни програми за Windows от Петко Петков (5co): SchoolControl, FVS Coach, SCHBox, BoxMAG, ImageBox, DownBox, iBox.")
    html += f'''
<main id="top">
  <section class="hero">
    <div class="wrap">
      <h1>Софтуер, създаден в училище — <em>за училище и за всеки ден</em></h1>
      <p>Безплатни програми за Windows от Петко Петков (5co) — за учители, ученици и всеки, който иска нещата да работят просто.</p>
      <div class="actions">
        <a class="btn btn-accent" href="#school">Разгледай програмите</a>
        <a class="btn btn-ghost" href="{REVOLUT}" target="_blank" rel="noopener" data-goatcounter-click="revolut" data-goatcounter-title="Revolut — подкрепа">Подкрепи разработките</a>
      </div>
      <div class="facts">
        <div><b>{len(APPS)}</b>програми</div>
        <div><b>Windows</b>10 / 11, някои и 7</div>
        <div><b>Безплатно</b>за училища и ученици</div>
      </div>
    </div>
  </section>

  <section class="block" id="school">
    <div class="wrap">
      <h2>Инструменти за училище</h2>
      <p class="lead">За компютърните кабинети, учителите по ФВС и съставянето на седмичната програма.</p>
      <div class="grid">
{school}      </div>
    </div>
  </section>

  <section class="block alt" id="other">
    <div class="wrap">
      <h2>Други софтуерни инструменти</h2>
      <p class="lead">Програми за графичен дизайн, изображения, видео, iPhone и отдалечен достъп.</p>
      <div class="grid">
{other}      </div>
    </div>
  </section>

  <section class="block" id="about">
    <div class="wrap about">
      <div class="me">
        <img class="avatar" src="img/petko.webp" alt="Петко Петков (5co)" width="150" height="150">
        <div>
        <h2>За мен</h2>
        <p>Казвам се Петко Петков (5co) — графичен дизайнер и учител. В училище всеки ден виждам какво отнема време на учителите и учениците.</p>
        <p>Така се роди BoxLab: малки програми, всяка от които решава конкретна задача — от управлението на цял кабинет до разгъвката на една кутия. Пиша ги сам, тествам ги в истински класни стаи и ги предоставям безплатно на училищата.</p>
        <p>Имате идея или открихте грешка? Пишете ми — от такива съобщения се раждат следващите версии.</p>
        </div>
      </div>
      <div class="panel" id="contact">
        <h3>Контакти</h3>
        <ul class="contact-list">
          <li><span>Имейл</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><span>LinkedIn</span><a href="{LINKEDIN}" target="_blank" rel="noopener">linkedin.com/in/petko-petkov-096461bb</a></li>
          <li><span>Facebook</span><a href="{FACEBOOK}" target="_blank" rel="noopener">facebook.com/petko.petkov.104</a></li>
        </ul>
        <div class="qr-box">
          <a href="{REVOLUT}" target="_blank" rel="noopener" data-goatcounter-click="revolut" data-goatcounter-title="Revolut — подкрепа">{QR}</a>
          <div><span>Revolut</span><a href="{REVOLUT}" target="_blank" rel="noopener" data-goatcounter-click="revolut" data-goatcounter-title="Revolut — подкрепа">revolut.me/5co5cov</a><small>Сканирай с телефона, за да подкрепиш разработките.</small></div>
        </div>
      </div>
    </div>
    <div class="wrap">
      <div class="support">
        <div>
          <h3>Подкрепи разработките</h3>
          <p>Благодаря, че ползвате програмите ми! Зад всяка от тях стоят много вечери, тестове и поправки. Създавам ги в малкото свободно време, с което разполагам, и ги споделям напълно безплатно, защото вярвам, че добрите инструменти трябва да са достъпни за всички. Ако някоя от тях ви е спестила време, можете да подкрепите разработката чрез Revolut — така ще има нови функции, поправки и нови програми. Всяка подкрепа, голяма или малка, означава много.</p>
        </div>
        <a class="btn btn-accent" href="{REVOLUT}" target="_blank" rel="noopener" data-goatcounter-click="revolut" data-goatcounter-title="Revolut — подкрепа">Отвори Revolut</a>
      </div>
    </div>
  </section>
</main>
'''
    html += foot("")
    (ROOT / "index.html").write_text(html, encoding="utf-8")

# ------------------------------------------------------------------ страница на програма
def build_app(a):
    p = "../"
    name = escape(a["name"])
    lis = "".join(f"<li>{escape(f)}</li>" for f in a["features"])
    reqs = "".join(f"<li>{escape(r)}</li>" for r in a["reqs"])
    about = "".join(f"<p>{escape(t)}</p>" for t in a["about"])
    if a["downloads"]:
        btns = "".join(
            f'<a class="btn {"btn-accent" if i == 0 else "btn-ghost"} wide" href="{u}" target="_blank" rel="noopener" '
            f'data-goatcounter-click="download-{a["slug"]}{"" if i == 0 else "-" + str(i + 1)}" '
            f'data-goatcounter-title="Изтегляне: {escape(a["name"])} ({escape(label)})">'
            f'{DL_ICON}{escape(label if label != "Изтегли" else "Изтегли за Windows")}<small>{size}</small></a>'
            for i, (label, u, size) in enumerate(a["downloads"]))
        dl = f'''<h3>Изтегляне</h3>
          {btns}
          <p class="fine">{"Версия " + a["version"] + " · " if a.get("version") else ""}Безплатно · Инсталатор за Windows</p>'''
    else:
        msg = "Очаквайте скоро" if a.get("status") == "soon" else "В разработка"
        dl = f'''<h3>Изтегляне</h3>
          <div class="pending">{msg}</div>
          <p class="fine">Бутонът за изтегляне ще се появи тук, когато програмата е готова.</p>'''
    note = f'<p class="note">{escape(a["note"])}</p>' if a.get("note") else ""
    support_text = ("Благодаря, че ползвате програмите ми! Създавам ги в малкото си свободно време и ги споделям напълно безплатно. "
                    "Ако някоя от тях ви е спестила време, можете да подкрепите разработката чрез Revolut — така ще има нови функции, "
                    "поправки и нови програми. Всяка подкрепа, голяма или малка, означава много.")
    html = head(f"{a['name']} — BoxLab", p, a["short"])
    html += f'''
<main id="top" class="app">
  <div class="wrap">
    <a class="back" href="{p}index.html#{"school" if a["group"] == "school" else "other"}">← Всички програми</a>
    {shot(a, p, big=True)}
    <div class="app-head">
      <h1>{name} {tag(a)}</h1>
      <p class="motto">{escape(a["motto"])}</p>
    </div>
    <div class="app-grid">
      <div class="app-main">
        <h2>За програмата</h2>
        {about}
        <h2>{escape(a.get("features_title", "Какво може"))}</h2>
        <ul class="ticks">{lis}</ul>
        {note}
      </div>
      <aside class="app-side">
        <div class="panel">
          {dl}
        </div>
        <div class="panel">
          <h3>Системни изисквания</h3>
          <ul class="reqs">{reqs}</ul>
        </div>
      </aside>
    </div>

    <div class="support app-support">
      <div class="support-qr"><a href="{REVOLUT}" target="_blank" rel="noopener" data-goatcounter-click="revolut" data-goatcounter-title="Revolut — подкрепа">{QR}</a></div>
      <div class="support-text">
        <h3>Подкрепи разработката на {name}</h3>
        <p>{support_text}</p>
      </div>
      <a class="btn btn-accent" href="{REVOLUT}" target="_blank" rel="noopener" data-goatcounter-click="revolut" data-goatcounter-title="Revolut — подкрепа">Отвори Revolut</a>
    </div>
  </div>
</main>
'''
    html += foot(p)
    (ROOT / "apps" / f"{a['slug']}.html").write_text(html, encoding="utf-8")

EXTRA_CSS = r"""
/* --- общи добавки --- */
section.block.alt{background:#0f1420;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.card h3 a{text-decoration:none}
.card h3 a:hover{color:var(--accent)}
.card-link{display:block}
.card-link .shot{transition:filter .15s}
.card-link:hover .shot{filter:brightness(1.08)}
.btn svg{width:16px;height:16px}

/* --- страница на програма --- */
.app{padding:28px 0 64px}
.back{display:inline-block;color:var(--muted);text-decoration:none;font-weight:500;margin-bottom:18px}
.back:hover{color:var(--accent)}
.shot.big{aspect-ratio:auto;height:clamp(220px,40vw,440px);border-radius:18px;border:1px solid var(--line)}
.shot.big.rd b{font-size:clamp(48px,8vw,88px)}
.app-head{margin:28px 0 8px}
.app-head h1{font:800 clamp(30px,4.6vw,46px)/1.1 var(--display);margin:0 0 8px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.app-head h1 .tag{font-size:14px;padding:6px 11px}
.app-head .motto{font-size:18px}
.app-grid{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(280px,1fr);gap:32px;margin-top:24px;align-items:start}
.app-main h2{font:700 22px/1.2 var(--display);margin:28px 0 12px}
.app-main h2:first-child{margin-top:0}
.app-main p{margin:0 0 14px;max-width:66ch}
.ticks{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.ticks li{position:relative;padding-left:30px}
.ticks li::before{content:"";position:absolute;left:0;top:4px;width:18px;height:18px;border-radius:50%;background:rgba(247,148,29,.16);border:1.5px solid var(--accent)}
.ticks li::after{content:"";position:absolute;left:6px;top:8px;width:5px;height:8px;border:solid var(--accent);border-width:0 2px 2px 0;transform:rotate(45deg)}
.note{margin-top:22px!important;padding:14px 16px;border-left:3px solid var(--cyan);background:var(--surface);border-radius:0 10px 10px 0;color:var(--muted)}
.app-side{display:grid;gap:18px;position:sticky;top:84px}
.app-side .btn.wide{width:100%;justify-content:center;margin-bottom:10px;padding:14px 18px}
.app-side .btn small{font-weight:500;opacity:.75;margin-left:4px}
.fine{color:var(--muted);font-size:13px;margin:4px 0 0}
.pending{padding:14px;border-radius:10px;border:1px dashed var(--line);text-align:center;color:var(--cyan);font-weight:600}
.reqs{margin:0;padding-left:18px;display:grid;gap:8px;color:var(--text);font-size:15px}
.reqs li::marker{color:var(--accent)}
.app-support{margin-top:48px;justify-content:flex-start}
.app-support .support-text{flex:1;min-width:240px}
.support p{max-width:78ch}
.support-qr .qr{width:124px;height:124px;display:block;border-radius:10px}
@media (max-width:860px){.app-grid{grid-template-columns:1fr}.app-side{position:static}}
"""

def build_css():
    base = (ROOT / "css" / "base.css").read_text(encoding="utf-8")
    (ROOT / "css" / "style.css").write_text(base + EXTRA_CSS, encoding="utf-8")

if __name__ == "__main__":
    (ROOT / "apps").mkdir(exist_ok=True)
    build_css(); build_index()
    for a in APPS: build_app(a)
    print("OK:", 1 + len(APPS), "страници")
