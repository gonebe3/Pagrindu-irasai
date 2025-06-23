
import sqlite3
from datetime import datetime
from Classes.Knyga import Knyga
from Classes.Skaitytojas import Skaitytojas
from Classes.Bibliotekininkas import Bibliotekininkas

DB_PATH = "biblioteka.db"

def gauti_conn():
    return sqlite3.connect(DB_PATH)

def dabartine_data():
    return datetime.now().isoformat()

def inicijuoti_db():
    # Sukuria lenteles, jei jos neegzistuoja
    try:
        with gauti_conn() as conn:
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id TEXT PRIMARY KEY,
                    pavadinimas TEXT,
                    autorius TEXT,
                    metai INTEGER,
                    zanras TEXT,
                    turimas_kiekis INTEGER,
                    paimtas_kiekis INTEGER,
                    created_on TEXT,
                    created_by TEXT,
                    modified_on TEXT,
                    modified_by TEXT,
                    deleted INTEGER DEFAULT 0
                )""")
            c.execute("""
                CREATE TABLE IF NOT EXISTS readers (
                    id TEXT PRIMARY KEY,
                    vardas TEXT,
                    pavarde TEXT,
                    kontaktai TEXT,
                    created_on TEXT,
                    created_by TEXT,
                    modified_on TEXT,
                    modified_by TEXT,
                    deleted INTEGER DEFAULT 0
                )""")
            c.execute("""
                CREATE TABLE IF NOT EXISTS librarians (
                    id TEXT PRIMARY KEY,
                    vardas TEXT,
                    pavarde TEXT,
                    vartotojo_vardas TEXT UNIQUE,
                    slaptazodis TEXT,
                    created_on TEXT,
                    created_by TEXT,
                    modified_on TEXT,
                    modified_by TEXT,
                    deleted INTEGER DEFAULT 0
                )""")
            c.execute("""
                CREATE TABLE IF NOT EXISTS pasiskolinimai (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    skaitytojo_id TEXT,
                    knygos_id TEXT,
                    paemimo_data TEXT,
                    grazinti_iki TEXT,
                    ar_grazinta INTEGER,
                    created_on TEXT,
                    created_by TEXT,
                    modified_on TEXT,
                    modified_by TEXT,
                    deleted INTEGER DEFAULT 0,
                    FOREIGN KEY (skaitytojo_id) REFERENCES readers(id),
                    FOREIGN KEY (knygos_id) REFERENCES books(id)
                )""")
            conn.commit()
            print("Lenteles sekmingai sukurtos arba jau egzistuoja.")
    except sqlite3.Error as e:
        print(f"Klaida kuriant lenteles: {e}")

# ----------- Knygos ----------
def prideti_knyga(book, created_by="system"):
    # Prideda nauja knyga i duomenu baze
    with gauti_conn() as conn:
        conn.execute("""
            INSERT INTO books (id, pavadinimas, autorius, metai, zanras, turimas_kiekis, paimtas_kiekis, created_on, created_by, deleted)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
        """, (
            book.unikalus_id,
            book.pavadinimas,
            book.autorius,
            book.metai,
            book.zanras,
            book.turimas_kiekis,
            book.paimtas_kiekis,
            dabartine_data(),
            created_by
        ))

def atnaujinti_knyga(book, modified_by="system"):
    # Atnaujina knygos informacija
    with gauti_conn() as conn:
        conn.execute("""
            UPDATE books SET pavadinimas=?, autorius=?, metai=?, zanras=?, turimas_kiekis=?, paimtas_kiekis=?, modified_on=?, modified_by=?
            WHERE id=?
        """, (
            book.pavadinimas,
            book.autorius,
            book.metai,
            book.zanras,
            book.turimas_kiekis,
            book.paimtas_kiekis,
            dabartine_data(),
            modified_by,
            book.unikalus_id
        ))

def pasalinti_knyga(book_id):
    # Pažymi knyga kaip istrinta
    with gauti_conn() as conn:
        conn.execute("UPDATE books SET deleted=1 WHERE id=?", (book_id,))

def pasalinti_senas_knygas(metai):
    # Pašalina knygas (pažymi deleted=1), kurios išleistos pries nurodytus metus
    with gauti_conn() as conn:
        result = conn.execute("SELECT COUNT(*) FROM books WHERE metai < ? AND deleted=0", (metai,)).fetchone()
        kiek = result[0] if result else 0
        conn.execute("UPDATE books SET deleted=1 WHERE metai < ?", (metai,))
    return kiek

def gauti_knyga_pagal_id(book_id):
    # Grazina knygos objekta pagal ID
    with gauti_conn() as conn:
        r = conn.execute("SELECT * FROM books WHERE id=? AND deleted=0", (book_id,)).fetchone()
        if not r:
            return None
        k = Knyga(r[1], r[2], r[3], r[4], r[5], r[6])
        k.unikalus_id = r[0]
        return k

def gauti_visas_knygas_db():
    # Grazina visas knygas (neistrintas)
    with gauti_conn() as conn:
        rows = conn.execute("SELECT * FROM books WHERE deleted=0").fetchall()
    knygos = []
    for r in rows:
        k = Knyga(r[1], r[2], r[3], r[4], r[5], r[6])
        k.unikalus_id = r[0]
        knygos.append(k)
    return knygos

def ieskoti_knygu_pagal_pavadinima(pavadinimas):
    # Grazina knygas pagal pavadinima ar jo dali (LIKE)
    with gauti_conn() as conn:
        rows = conn.execute("SELECT * FROM books WHERE pavadinimas LIKE ? AND deleted=0", ('%' + pavadinimas + '%',)).fetchall()
    rezultatai = []
    for r in rows:
        k = Knyga(r[1], r[2], r[3], r[4], r[5], r[6])
        k.unikalus_id = r[0]
        rezultatai.append(k)
    return rezultatai

def ieskoti_knygu_pagal_autoriu(autorius):
    # Grazina knygas pagal autoriu (LIKE)
    with gauti_conn() as conn:
        rows = conn.execute("SELECT * FROM books WHERE autorius LIKE ? AND deleted=0", ('%' + autorius + '%',)).fetchall()
    rezultatai = []
    for r in rows:
        k = Knyga(r[1], r[2], r[3], r[4], r[5], r[6])
        k.unikalus_id = r[0]
        rezultatai.append(k)
    return rezultatai

def ieskoti_knygu_pagal_zanra(zanras):
    # Grazina knygas pagal zanra (LIKE)
    with gauti_conn() as conn:
        rows = conn.execute("SELECT * FROM books WHERE zanras LIKE ? AND deleted=0", ('%' + zanras + '%',)).fetchall()
    rezultatai = []
    for r in rows:
        k = Knyga(r[1], r[2], r[3], r[4], r[5], r[6])
        k.unikalus_id = r[0]
        rezultatai.append(k)
    return rezultatai

def ar_yra_laisvu_knygu(book_id):
    # Patikrina, ar yra laisvu egzemplioriu (turimas_kiekis > paimtas_kiekis)
    with gauti_conn() as conn:
        r = conn.execute("SELECT turimas_kiekis, paimtas_kiekis FROM books WHERE id=? AND deleted=0", (book_id,)).fetchone()
    if not r:
        return False
    return r[0] > r[1]

# ----------- Skaitytojai ----------
def prideti_skaitytoja(s, created_by="system"):
    # Prideda nauja skaitytoja i duomenu baze
    with gauti_conn() as conn:
        conn.execute("""
            INSERT INTO readers (id, vardas, pavarde, kontaktai, created_on, created_by, deleted)
            VALUES (?, ?, ?, ?, ?, ?, 0)
        """, (
            s.korteles_numeris,
            s.vardas,
            s.pavarde,
            s.kontaktai,
            dabartine_data(),
            created_by
        ))

def gauti_skaitytoja_pagal_kortele(korteles_nr):
    # Grazina skaitytoja pagal korteles numeri
    with gauti_conn() as conn:
        r = conn.execute("SELECT * FROM readers WHERE id=? AND deleted=0", (korteles_nr,)).fetchone()
    if not r:
        return None
    s = Skaitytojas(r[1], r[2], r[3])
    s.korteles_numeris = r[0]
    return s

def gauti_visus_skaitytojus_db():
    # Grazina visus skaitytojus
    with gauti_conn() as conn:
        rows = conn.execute("SELECT * FROM readers WHERE deleted=0").fetchall()
    sarasas = []
    for r in rows:
        s = Skaitytojas(r[1], r[2], r[3])
        s.korteles_numeris = r[0]
        sarasas.append(s)
    return sarasas

# ----------- Bibliotekininkai ----------
def prideti_bibliotekininka(b, created_by="system"):
    # Prideda bibliotekininka i duomenu baze
    with gauti_conn() as conn:
        conn.execute("""
            INSERT INTO librarians (id, vardas, pavarde, vartotojo_vardas, slaptazodis, created_on, created_by, deleted)
            VALUES (?, ?, ?, ?, ?, ?, ?, 0)
        """, (
            b.vartotojo_vardas,
            b.vardas,
            b.pavarde,
            b.vartotojo_vardas,
            b.slaptazodis,
            dabartine_data(),
            created_by
        ))

def gauti_bibliotekininka_pagal_vartotojo_varda(vartotojo_vardas):
    # Grazina bibliotekininka pagal vartotojo varda
    with gauti_conn() as conn:
        r = conn.execute("SELECT vardas, pavarde, vartotojo_vardas, slaptazodis FROM librarians WHERE vartotojo_vardas=? AND deleted=0", (vartotojo_vardas,)).fetchone()
        if r:
            return Bibliotekininkas(r[0], r[1], r[2], r[3])
        return None

def gauti_visus_bibliotekininkus_db():
    # Grazina visus bibliotekininkus
    with gauti_conn() as conn:
        rows = conn.execute("SELECT vardas, pavarde, vartotojo_vardas, slaptazodis FROM librarians WHERE deleted=0").fetchall()
    return [Bibliotekininkas(r[0], r[1], r[2], r[3]) for r in rows]

def pasalinti_bibliotekininka(username):
    # Pažymi bibliotekininka kaip istrinta
    with gauti_conn() as conn:
        conn.execute("UPDATE librarians SET deleted=1 WHERE vartotojo_vardas=?", (username,))

# ----------- Pasiskolinimai ----------
def prideti_pasiskolinima(reader_id, book_id, paemimo_data, grazinti_iki, created_by="system"):
    # Prideda nauja pasiskolinima (knygos emima) i duomenu baze
    with gauti_conn() as conn:
        conn.execute("""
            INSERT INTO pasiskolinimai (skaitytojo_id, knygos_id, paemimo_data, grazinti_iki, ar_grazinta, created_on, created_by, deleted)
            VALUES (?, ?, ?, ?, 0, ?, ?, 0)
        """, (
            reader_id,
            book_id,
            paemimo_data.isoformat(),
            grazinti_iki.isoformat(),
            dabartine_data(),
            created_by
        ))
        # Atnaujina knygos paimtas_kiekis
        conn.execute("UPDATE books SET paimtas_kiekis = paimtas_kiekis + 1 WHERE id=?", (book_id,))

def grazinti_knyga(reader_id, book_id):
    # Grazina knyga: pazymi pasiskolinima kaip grazinta ir sumazina paimtas_kiekis
    with gauti_conn() as conn:
        pask = conn.execute(
            "SELECT id FROM pasiskolinimai WHERE skaitytojo_id=? AND knygos_id=? AND ar_grazinta=0 AND deleted=0",
            (reader_id, book_id)
        ).fetchone()
        if not pask:
            return False
        pask_id = pask[0]
        conn.execute("UPDATE pasiskolinimai SET ar_grazinta=1, modified_on=?, modified_by=? WHERE id=?",
                     (dabartine_data(), "system", pask_id))
        conn.execute("UPDATE books SET paimtas_kiekis = paimtas_kiekis - 1 WHERE id=?", (book_id,))
    return True

def gauti_skaitytojo_pasiskolinimus(skaitytojo_id):
    # Grazina visus pasiskolinimus konkretaus skaitytojo
    with gauti_conn() as conn:
        rows = conn.execute(
            "SELECT * FROM pasiskolinimai WHERE skaitytojo_id=? AND deleted=0", (skaitytojo_id,)
        ).fetchall()
    return rows

def gauti_veluojancias_knygas():
    # Grazina visas veluojancias knygas (visu skaitytoju)
    with gauti_conn() as conn:
        now = datetime.now().isoformat()
        rows = conn.execute("""
            SELECT p.id, p.skaitytojo_id, p.knygos_id, p.paemimo_data, p.grazinti_iki, r.vardas, r.pavarde, b.pavadinimas
            FROM pasiskolinimai p
            JOIN readers r ON p.skaitytojo_id = r.id
            JOIN books b ON p.knygos_id = b.id
            WHERE p.ar_grazinta=0 AND p.deleted=0 AND p.grazinti_iki < ?
        """, (now,)).fetchall()
    # Grazina sarasa su info apie skaitytoja ir knyga
    sarasas = []
    for r in rows:
        sarasas.append({
            "id": r[0],
            "skaitytojo_id": r[1],
            "knygos_id": r[2],
            "paemimo_data": r[3],
            "grazinti_iki": r[4],
            "skaitytojas": f"{r[5]} {r[6]}",
            "pavadinimas": r[7]
        })
    return sarasas

def skaitytojas_turi_veluojanciu(skaitytojo_id):
    # Tikrina ar skaitytojas turi veluojanciu knygu
    with gauti_conn() as conn:
        now = datetime.now().isoformat()
        r = conn.execute(
            "SELECT COUNT(*) FROM pasiskolinimai WHERE skaitytojo_id=? AND ar_grazinta=0 AND deleted=0 AND grazinti_iki < ?",
            (skaitytojo_id, now)
        ).fetchone()
    return r[0] > 0 if r else False

def skaitytojo_negrązintos_knygos(skaitytojo_id):
    # Grazina visas negrązintas skaitytojo knygas
    with gauti_conn() as conn:
        rows = conn.execute(
            "SELECT * FROM pasiskolinimai WHERE skaitytojo_id=? AND ar_grazinta=0 AND deleted=0",
            (skaitytojo_id,)
        ).fetchall()
    return rows

def populiariausi_zanrai():
    # Grazina populiariausius zanrus (pagal visas knygas)
    with gauti_conn() as conn:
        rows = conn.execute(
            "SELECT zanras, COUNT(*) FROM books WHERE deleted=0 GROUP BY zanras ORDER BY COUNT(*) DESC"
        ).fetchall()
    return rows

def populiariausi_zanrai_pagal_paemimus():
    # Grazina populiariausius zanrus pagal paimimus (pasiskolinimus)
    with gauti_conn() as conn:
        rows = conn.execute("""
            SELECT b.zanras, COUNT(*) FROM pasiskolinimai p
            JOIN books b ON p.knygos_id = b.id
            WHERE p.deleted=0
            GROUP BY b.zanras ORDER BY COUNT(*) DESC
        """).fetchall()
    return rows

def vidutinis_veluojanciu_kiekis():
    # Grazina vidutini veluojanciu knygu kieki skaitytojui
    with gauti_conn() as conn:
        skaitytojai = conn.execute("SELECT id FROM readers WHERE deleted=0").fetchall()
        if not skaitytojai:
            return 0
        kiekiai = []
        for s in skaitytojai:
            kiek = conn.execute(
                "SELECT COUNT(*) FROM pasiskolinimai WHERE skaitytojo_id=? AND ar_grazinta=0 AND deleted=0 AND grazinti_iki < ?",
                (s[0], datetime.now().isoformat())
            ).fetchone()[0]
            kiekiai.append(kiek)
        return sum(kiekiai) / len(kiekiai) if kiekiai else 0

