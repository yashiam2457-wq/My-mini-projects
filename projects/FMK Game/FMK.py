'''Add backend-
    combination- [(c1,c2,c3),[(fn1,mn1,kn1),(fn2,mn2,kn2),(f3,mn3,kn3)],totalplay]
    character- [name, catagory, img link]
    category list- [category, subcategory, count(char(category))]
    logic if (c1,c2,c3) exists- add player respective choices
    else- add new one at end
    
    FMK
    Logic for char customs- no full random get only specific category and then only show characters from that cat
    keep count that combination is being played while app is opened
    
    SP go full on random as only single char is shown
    
    checking for a fraction in which it has take all subcategory keep on memory
'''
import os
os.chdir("C:\\Users\\Loq\\Documents\\programs\\minipro\\MyFMKgame")
print("Running from:", os.getcwd())

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QStackedWidget,
    QFrame, QLineEdit, QTreeWidget, QTreeWidgetItem,
    QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QImage
import os
import pickle
import random, mmap, struct, itertools

FILE_1 = "C:\\Users\\Loq\\Documents\\programs\\minipro\\MyFMKgame\\Anime.mmap"
FILE_2 = "C:\\Users\\Loq\\Documents\\programs\\minipro\\MyFMKgame\\Superhero.mmap"
FILE_3 = "C:\\Users\\Loq\\Documents\\programs\\minipro\\MyFMKgame\\Game.mmap"
HEADER_FORMAT = "QIIQ"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
index_s1 = {}   # {category: [(file, offset), ...]}
index_s2 = {}   # {subcategory: [(file, offset), ...]}

# Backend Setup

# combinations Setup
dat_file = "C:\\Users\\Loq\\Documents\\programs\\minipro\\MyFMKgame\\combination.dat"

def load_database(dat_file):
    if not os.path.exists(dat_file):
        return []
    with open(dat_file, "rb") as f:
        try:
            return pickle.load(f)
        except EOFError:
            return []

def save_database(dat_file, data):
    with open(dat_file, "wb") as f:
        pickle.dump(data, f)

def search_by_first_element(dat_file, key):
    data = load_database(dat_file)
    results = [record for record in data if record[0] == key]
    return results

def update_record(dat_file, key, new_second_element):
    data = load_database(dat_file)
    found = False
    for record in data:
        if record[0] == key:
            record[1] = new_second_element
            record[2] += 1
            found = True
    if not found:
        data.append([key, new_second_element, 1])
    save_database(dat_file, data)

# Main backend Run
def init_database(File):
    global index_s1, index_s2
    if not os.path.exists(File):
        print(f"{File} not found")
        return
    with open(File, "rb") as f:
        mm_local = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        offset = 0
        size = len(mm_local)
        while offset + HEADER_SIZE <= size:
            total_size, s1_len, s2_len, img_len = struct.unpack_from(
                HEADER_FORMAT, mm_local, offset
            )
            base = offset + HEADER_SIZE
            s1 = mm_local[base:base+s1_len].decode().strip().lower()  # Category: anime/video game/superhero
            base += s1_len
            s2 = mm_local[base:base+s2_len].decode().strip().lower()  # Show name: naruto/bleach/etc

            index_s1.setdefault(s1, []).append((File, offset))  # Index by category
            index_s2.setdefault(s2, []).append((File, offset))  # Index by show name
            offset += total_size
        print(f"Loaded {File}")
        print(f"  Sample s1 (categories): {list(set([k for k in index_s1.keys()]))[:5]}")
        print(f"  Sample s2 (show names): {list(index_s2.keys())[:10]}")
        mm_local.close()

def close_database():
    global mm, file_handle
    if mm:
        mm.close()
    if file_handle:
        file_handle.close()

def read_record(file_offset_tuple):
    File, offset = file_offset_tuple    
    with open(File, "rb") as f:
        mm_local = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        total_size, s1_len, s2_len, img_len = struct.unpack_from(
            HEADER_FORMAT, mm_local, offset
        )
        base = offset + HEADER_SIZE
        s1 = mm_local[base:base+s1_len].decode()
        base += s1_len
        s2 = mm_local[base:base+s2_len].decode()
        base += s2_len
        img_bytes = mm_local[base:base+img_len]
        image = QImage()
        image.loadFromData(img_bytes)
        pixmap = QPixmap.fromImage(image)
        mm_local.close()
    return s1, s2, pixmap

# Random Retrievals
def SP_search(query_show_name):
    """Search for a random character from a specific show"""
    offsets = index_s1.get(query_show_name.strip().lower())
    print(f"SP_search called with show: '{query_show_name}'")
    print(f"  Offsets found: {len(offsets) if offsets else 0}")
    if not offsets:
        return None
    offset = random.choice(offsets)
    return read_record(offset)

def FMK_search(query_s1):
    """Search for 3 characters from the same show/subcategory (s1)"""
    offsets = index_s1.get(query_s1.strip().lower())
    if not offsets:
        print(f"FMK_search: No offsets found for show '{query_s1}'")
        return []
    
    if len(offsets) < 3:
        print(f"FMK_search: Not enough characters in show '{query_s1}' (found {len(offsets)})")
        return []
    
    # Select 3 random characters from this show
    selected_offsets = random.sample(offsets, 3)
    return [read_record(off) for off in selected_offsets]

BTN_STYLE = """
QPushButton {
    background:#2d89ef;color:white;padding:10px;border-radius:8px;font-size:14px;}
"""
TITLE_STYLE = "color:white; font-size:72px;"
TEXT_STYLE = "color:white; font-size:22px;"
CARD_STYLE = "background:#1e1e1e; border-radius:16px; padding:20px;"
PANEL_WIDTH = 320

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FMK / SP")
        self.setMinimumSize(900, 600)
        self.setStyleSheet("background:#121212;")
        
        # Initialize database
        try:
            init_database(FILE_1)
            init_database(FILE_2)
            init_database(FILE_3)
        except Exception as e:
            print("DB Init Error:", e)
        
        # Initialize state variables
        self.selected_categories = []
        self.current_sp_record = None
        self.current_fmk_records = []
        self.sp_choice = None
        self.fmk_results = {}
        self.current_idx = None
        self.tables = []
        self.fmk_name_labels = []
        self.sp_pool = []           # Remaining unseen offsets for SP
        self.sp_last_selection = [] # Tracks which shows were selected when pool was built
        self.fmk_pool = []          # Remaining unseen 3-combos for FMK
        self.fmk_last_selection = []# Tracks which shows were selected when fmk pool was built
        
        # Create screens
        self.stack = QStackedWidget()
        self.stack.addWidget(self.home_screen())
        self.stack.addWidget(self.SP_screen())
        self.stack.addWidget(self.FMK_screen())
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)
    
    def get_selected_categories(self):
        selected = []
        for table in self.tables:
            for r in range(table.rowCount()):
                item = table.item(r, 0)
                if item.checkState() == Qt.CheckState.Checked:
                    name = table.item(r, 1).text()
                    selected.append(name.lower())
        return selected
    
    def debug_check_on_open(self, mode):
        print(f"\n===== DEBUG {mode} OPEN =====")
        categories = self.get_selected_categories()
        print("Selected Categories:", categories)
        print("Indexed s1 keys sample:", list(index_s1.keys())[:10])
        
        if not categories:
            print("No categories selected.")
            return
        
        for cat in categories:
            print(f"\nChecking category: {cat}")
            offsets = index_s1.get(cat)
            print("Offsets:", offsets)
            
            if not offsets:
                print("No records found for this category.")
                continue
            
            test_record = read_record(offsets[0])
            if test_record:
                s1, s2, _ = test_record
                print("Read Record → s1:", s1, "| s2:", s2)
            else:
                print("Failed to read record.")
    
    # Load character functions
    def _build_sp_pool(self, selected_shows):
        """Collect all offsets for the selected shows, shuffle, and store as the pool."""
        pool = []
        for show in selected_shows:
            offsets = index_s1.get(show.strip().lower(), [])
            pool.extend(offsets)
        random.shuffle(pool)
        self.sp_pool = pool
        self.sp_last_selection = list(selected_shows)
        print(f"SP pool built: {len(pool)} characters across {len(selected_shows)} show(s)")

    def load_sp_character(self):
        selected_shows = self.get_selected_categories()
        if not selected_shows:
            print("No shows selected for SP")
            return

        # Rebuild pool if selection changed or pool is empty
        if selected_shows != self.sp_last_selection or not self.sp_pool:
            self._build_sp_pool(selected_shows)

        # If pool still empty, no characters available
        if not self.sp_pool:
            self.sp_name_label.setText("All characters seen!")
            print("SP: All characters have been shown.")
            return

        # Pop next character from pool (no repeats)
        offset = self.sp_pool.pop()
        record = read_record(offset)
        if not record:
            print("SP: Failed to read record, trying next")
            self.load_sp_character()
            return

        show_name, char_name, pix = record
        self.current_sp_record = record
        self.sp_img.setPixmap(
            pix.scaled(
                self.sp_img.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
        self.sp_name_label.setText(f"{show_name} - {char_name}")
        print(f"Loaded SP character: Show='{show_name}', Character='{char_name}' | {len(self.sp_pool)} remaining")
    
    def _build_fmk_pool(self, selected_shows):
        """
        Build a pool of every unique 3-character combination across all selected shows.
        Each combo is a tuple of 3 file-offset tuples, sorted so that order doesn't
        matter — (A,B,C) and (C,A,B) are the same combination and only appear once.
        Shows with fewer than 3 characters are skipped.
        """
        pool = []
        for show in selected_shows:
            offsets = index_s1.get(show.strip().lower(), [])
            if len(offsets) < 3:
                continue
            # itertools.combinations already yields sorted (index-stable) tuples,
            # but we normalise by sorting each tuple so the pool key is canonical.
            for combo in itertools.combinations(offsets, 3):
                pool.append(tuple(sorted(combo)))  # order-normalised

        # Deduplicate (edge case: same offset listed under multiple shows)
        pool = list(set(pool))
        random.shuffle(pool)
        self.fmk_pool = pool
        self.fmk_last_selection = list(selected_shows)
        total_combos = sum(
            len(list(itertools.combinations(index_s1.get(s.strip().lower(), []), 3)))
            for s in selected_shows if len(index_s1.get(s.strip().lower(), [])) >= 3
        )
        print(f"FMK pool built: {len(pool)} unique combinations across {len(selected_shows)} show(s)")

    def load_fmk_characters(self):
        self.fmk_results.clear()
        self.fmk_msg.setText("")
        self.fmk_skip.setText("Skip")

        # Clear previous choice labels
        for label in self.fmk_choice_labels:
            label.setText("")

        selected_shows = self.get_selected_categories()
        if not selected_shows:
            print("No shows selected")
            self.fmk_msg.setText("Please select at least one show")
            return

        # Rebuild pool if selection changed or exhausted
        if selected_shows != self.fmk_last_selection or not self.fmk_pool:
            self._build_fmk_pool(selected_shows)

        if not self.fmk_pool:
            self.fmk_msg.setText("Not enough characters in selected shows (need 3+)")
            print("FMK: No valid combinations available")
            return

        # Pop next combination — guaranteed unique, order-normalised
        combo = self.fmk_pool.pop()
        records = [read_record(off) for off in combo]

        # Shuffle display order so the same 3 chars appear in a random arrangement
        random.shuffle(records)

        self.current_fmk_records = records
        print(f"\n===== FMK COMBO ({len(self.fmk_pool)} remaining) =====")
        for i, rec in enumerate(records):
            show_name, char_name, pix = rec
            self.fmk_imgs[i].setPixmap(
                pix.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)
            )
            self.fmk_name_labels[i].setText(f"{show_name}\n{char_name}")
            self.fmk_choice_labels[i].setText("")
            print(f"  Character {i+1}: Show='{show_name}', Name='{char_name}'")
    
    # Main layout
    def home_screen(self):
        w = QWidget()
        h = QHBoxLayout(w)
        
        left = QWidget()
        left.setFixedWidth(PANEL_WIDTH)
        lv = QVBoxLayout(left)
        lv.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        title = QLabel("FMK / SP")
        title.setStyleSheet(TITLE_STYLE)
        
        b1 = QPushButton("Smash or Pass")
        b2 = QPushButton("Kiss Marry Kill")
        b1.setStyleSheet(BTN_STYLE)
        b2.setStyleSheet(BTN_STYLE)
        
        def go_sp():
            if not self.get_selected_categories():
                print("No category selected")
                return
            self.stack.setCurrentIndex(1)
            self.debug_check_on_open("SP")
            self.load_sp_character()
        
        def go_fmk():
            if not self.get_selected_categories():
                print("No category selected")
                return
            self.stack.setCurrentIndex(2)
            self.debug_check_on_open("FMK")
            self.load_fmk_characters()
        
        b1.clicked.connect(go_sp)
        b2.clicked.connect(go_fmk)
        
        lv.addWidget(title)
        lv.addWidget(b1)
        lv.addWidget(b2)
        
        right = self.search_panel()
        right.setFixedWidth(PANEL_WIDTH)
        right.setStyleSheet("color:#888;")
        
        h.addStretch()
        h.addWidget(left)
        h.addStretch()
        h.addWidget(right)
        h.addStretch()
        
        return w
    
    # Search and category list layout
    def search_panel(self):
        panel = QWidget()
        v = QVBoxLayout(panel)
        
        search = QLineEdit()
        search.setPlaceholderText("Search...")
        search.setStyleSheet("padding:8px; background:#2a2a2a; color:white;")
        v.addWidget(search)
        
        tree = QTreeWidget()
        tree.setHeaderHidden(True)
        v.addWidget(tree)
        
        category_file = "C:\\Users\\Loq\\Documents\\programs\\minipro\\MyFMKgame\\category.txt"
        data = {
            "Anime": [],
            "Video Game": [],
            "SuperHero": [],
        }
        
        try:
            with open(category_file, 'r') as f:
                lines = f.read().split("\n")
                for line in lines:
                    if not line.strip():
                        continue
                    parts = line.split(',')
                    if len(parts) >= 3:
                        cat_type = parts[0]
                        name = parts[1]
                        count = int(parts[2])
                        if cat_type == "Anime":
                            data["Anime"].append((name, count))
                        elif cat_type == "Video Game":
                            data["Video Game"].append((name, count))
                        elif cat_type == "SuperHero":
                            data["SuperHero"].append((name, count))
        except Exception as e:
            print(f"Error loading category file: {e}")
        
        for cat, rows in data.items():
            parent = QTreeWidgetItem(tree)

            # Header widget: category label + Select All checkbox
            header_widget = QWidget()
            header_layout = QHBoxLayout(header_widget)
            header_layout.setContentsMargins(2, 2, 2, 2)
            header_layout.setSpacing(8)

            cat_label = QLabel(cat)
            cat_label.setStyleSheet("color:white; font-size:13px; font-weight:bold;")

            select_all_chk = QCheckBox("Select All")
            select_all_chk.setStyleSheet(
                "QCheckBox { color:#aaa; font-size:11px; }"
                "QCheckBox::indicator { width:13px; height:13px; }"
            )

            header_layout.addWidget(cat_label)
            header_layout.addStretch()
            header_layout.addWidget(select_all_chk)
            tree.setItemWidget(parent, 0, header_widget)

            table = QTableWidget(len(rows), 3)
            table.setHorizontalHeaderLabels(["", "Name", "No"])
            table.verticalHeader().setVisible(False)
            table.setColumnWidth(0, 28)
            table.setColumnWidth(2, 36)
            table.horizontalHeader().setSectionResizeMode(
                1, QHeaderView.ResizeMode.Stretch
            )

            for r, (name, num) in enumerate(rows):
                chk = QTableWidgetItem()
                chk.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                chk.setCheckState(Qt.CheckState.Unchecked)
                table.setItem(r, 0, chk)
                table.setItem(r, 1, QTableWidgetItem(name))
                table.setItem(r, 2, QTableWidgetItem(str(num)))

            # Wire Select All to toggle every row in this table
            def make_select_all_handler(tbl, chk_box):
                def handler(state):
                    check_state = Qt.CheckState.Checked if state else Qt.CheckState.Unchecked
                    for row in range(tbl.rowCount()):
                        item = tbl.item(row, 0)
                        if item:
                            item.setCheckState(check_state)
                # Also sync checkbox if user manually checks/unchecks all rows
                def sync_select_all():
                    all_checked = all(
                        tbl.item(r, 0) and tbl.item(r, 0).checkState() == Qt.CheckState.Checked
                        for r in range(tbl.rowCount())
                    )
                    chk_box.blockSignals(True)
                    chk_box.setChecked(all_checked)
                    chk_box.blockSignals(False)
                tbl.itemChanged.connect(lambda _: sync_select_all())
                return handler

            select_all_chk.stateChanged.connect(make_select_all_handler(table, select_all_chk))

            child = QTreeWidgetItem(parent)
            tree.setItemWidget(child, 0, table)
            self.tables.append(table)
        
        def search_handler(text):
            text = text.lower()
            found = False
            for table in self.tables:
                for r in range(table.rowCount()):
                    name = table.item(r, 1).text().lower()
                    match = text in name
                    table.setRowHidden(r, not match)
                    if match:
                        found = True
            if text and not found:
                for table in self.tables:
                    for r in range(table.rowCount()):
                        table.setRowHidden(r, True)
        
        search.textChanged.connect(search_handler)
        tree.expandAll()
        
        return panel
    
    # Smash or Pass layout
    def SP_screen(self):
        w = QWidget()
        v = QVBoxLayout(w)
        
        # Add top stretch to center content
        v.addStretch()
        
        self.sp_img = QLabel("IMAGE")
        self.sp_img.setFixedSize(400, 400)
        self.sp_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sp_img.setStyleSheet("background:#333; border-radius:12px;")
        
        # Label to show character info (Show name and Character name)
        self.sp_name_label = QLabel("")
        self.sp_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sp_name_label.setStyleSheet("color:#fff; font-size:20px; font-weight:bold; padding:5px;")
        self.sp_name_label.setFixedHeight(30)
        
        # Label to show choice below image
        self.sp_choice_label = QLabel("")
        self.sp_choice_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sp_choice_label.setStyleSheet("color:#4CAF50; font-size:24px; font-weight:bold; padding:10px;")
        self.sp_choice_label.setFixedHeight(40)
        
        def img_click(e):
            self.sp_img.setFixedSize(500, 500)
        self.sp_img.mousePressEvent = img_click
        
        opt = QHBoxLayout()
        opt.setSpacing(20)
        smash = QPushButton("Smash")
        pas = QPushButton("Pass")
        smash.setFixedSize(150, 50)
        pas.setFixedSize(150, 50)
        for b in (smash, pas):
            b.setStyleSheet(BTN_STYLE)
        opt.addStretch()
        opt.addWidget(smash)
        opt.addWidget(pas)
        opt.addStretch()
        
        nav = QHBoxLayout()
        nav.setSpacing(20)
        back = QPushButton("← Back")
        nextb = QPushButton("Next →")
        back.setFixedSize(150, 45)
        nextb.setFixedSize(150, 45)
        back.setStyleSheet(BTN_STYLE)
        nextb.setStyleSheet(BTN_STYLE)
        
        nav.addStretch()
        nav.addWidget(back)
        nav.addWidget(nextb)
        nav.addStretch()
        
        back.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        
        def choose(val):
            if not self.current_sp_record:
                return
            self.sp_choice = val
            print("SP:", val, self.current_sp_record[0])
            
            # Display choice below image with color
            if val == "Smash":
                self.sp_choice_label.setText("💚 SMASH 💚")
                self.sp_choice_label.setStyleSheet("color:#4CAF50; font-size:24px; font-weight:bold; padding:10px;")
            else:  # Pass
                self.sp_choice_label.setText("❌ PASS ❌")
                self.sp_choice_label.setStyleSheet("color:#f44336; font-size:24px; font-weight:bold; padding:10px;")
        
        def next_character():
            # Save the choice if one was made
            if self.sp_choice and self.current_sp_record:
                print(f"Saved: {self.sp_choice} for {self.current_sp_record[1]}")
                # TODO: Save to database here if needed
            
            # Reset and load next character
            self.sp_choice = None
            self.sp_choice_label.setText("")
            self.load_sp_character()
        
        smash.clicked.connect(lambda: choose("Smash"))
        pas.clicked.connect(lambda: choose("Pass"))
        nextb.clicked.connect(next_character)
        
        w.mousePressEvent = lambda e: self.sp_img.setFixedSize(400, 400)
        
        # Add all widgets to vertical layout
        v.addWidget(self.sp_img, alignment=Qt.AlignmentFlag.AlignCenter)
        v.addSpacing(10)
        v.addWidget(self.sp_name_label)
        v.addSpacing(5)
        v.addWidget(self.sp_choice_label)
        v.addSpacing(20)
        v.addLayout(opt)
        v.addSpacing(15)
        v.addLayout(nav)
        v.addSpacing(20)
        
        # Add bottom stretch
        v.addStretch()
        
        return w
    
    # FMK layout
    def FMK_screen(self):
        w = QWidget()
        v = QVBoxLayout(w)
        v.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.fmk_msg = QLabel("")
        self.fmk_msg.setStyleSheet(TEXT_STYLE)
        
        img_row = QHBoxLayout()
        self.fmk_imgs = []
        self.fmk_name_labels = []
        self.fmk_choice_labels = []
        
        for i in range(3):
            col = QVBoxLayout()
            img = QLabel(f"IMG {i+1}")
            img.setFixedSize(200, 200)
            img.setAlignment(Qt.AlignmentFlag.AlignCenter)
            img.setStyleSheet("background:#333; border-radius:12px;")
            img.mousePressEvent = lambda e, idx=i: self.open_fmk(idx)
            
            # Name label (Show - Character)
            name_lbl = QLabel("")
            name_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            name_lbl.setStyleSheet("color:#fff; font-size:14px; font-weight:bold; padding:3px;")
            name_lbl.setWordWrap(True)
            name_lbl.setFixedWidth(200)
            
            # Choice label (Kiss/Marry/Kill)
            choice_lbl = QLabel("")
            choice_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            choice_lbl.setStyleSheet("color:#aaa; font-size:18px; font-weight:bold; padding:5px;")
            
            self.fmk_imgs.append(img)
            self.fmk_name_labels.append(name_lbl)
            self.fmk_choice_labels.append(choice_lbl)
            
            col.addWidget(img)
            col.addWidget(name_lbl)
            col.addWidget(choice_lbl)
            img_row.addLayout(col)
        
        self.fmk_overlay = QFrame()
        self.fmk_overlay.setStyleSheet(CARD_STYLE)
        ov = QVBoxLayout(self.fmk_overlay)
        
        self.fmk_status = QLabel("Choose one option")
        self.fmk_status.setStyleSheet(TEXT_STYLE)
        ov.addWidget(self.fmk_status)
        
        for val in ["Kiss", "Marry", "Kill"]:
            b = QPushButton(val)
            b.setStyleSheet(BTN_STYLE)
            b.clicked.connect(lambda _, x=val: self.fmk_choice(x))
            ov.addWidget(b)
        
        self.fmk_choice_label = QLabel("")
        self.fmk_choice_label.setStyleSheet("color:#aaa; font-size:16px;")
        ov.addWidget(self.fmk_choice_label)
        
        self.fmk_overlay.hide()
        
        nav = QHBoxLayout()
        back = QPushButton("← Back")
        submit = QPushButton("Submit")
        self.fmk_skip = QPushButton("Skip")
        
        for b in (back, submit, self.fmk_skip):
            b.setStyleSheet(BTN_STYLE)
        
        back.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        
        def submit_all():
            if len(self.fmk_results) != 3:
                self.fmk_msg.setText("Select all 3 first")
                return
            if len(set(self.fmk_results.values())) != 3:
                self.fmk_msg.setText("Duplicate choice!")
                return
            print("FMK FINAL:", self.fmk_results)
            self.fmk_skip.setText("Next")
        
        submit.clicked.connect(submit_all)
        self.fmk_skip.clicked.connect(self.load_fmk_characters)
        
        nav.addWidget(back)
        nav.addWidget(submit)
        nav.addWidget(self.fmk_skip)
        
        w.mousePressEvent = lambda e: self.reset_fmk()
        
        v.addLayout(img_row)
        v.addWidget(self.fmk_msg)
        v.addWidget(self.fmk_overlay)
        v.addLayout(nav)
        
        return w
    
    def open_fmk(self, idx):
        self.current_idx = idx
        img = self.fmk_imgs[idx]
        img.setFixedSize(300, 300)
        self.fmk_overlay.show()
    
    def fmk_choice(self, val):
        old_val = self.fmk_results.pop(self.current_idx, None)
        
        if val in self.fmk_results.values():
            self.fmk_status.setText("Duplicate choice! Pick another.")
            self.fmk_choice_label.setText(f"Choice: {val} (duplicate)")
            if old_val is not None:
                self.fmk_results[self.current_idx] = old_val
            return
        
        self.fmk_results[self.current_idx] = val
        
        # Display choice below the image with color coding
        if val == "Kiss":
            self.fmk_choice_labels[self.current_idx].setText("💋 KISS")
            self.fmk_choice_labels[self.current_idx].setStyleSheet("color:#E91E63; font-size:18px; font-weight:bold;")
        elif val == "Marry":
            self.fmk_choice_labels[self.current_idx].setText("💍 MARRY")
            self.fmk_choice_labels[self.current_idx].setStyleSheet("color:#4CAF50; font-size:18px; font-weight:bold;")
        else:  # Kill
            self.fmk_choice_labels[self.current_idx].setText("🔪 KILL")
            self.fmk_choice_labels[self.current_idx].setStyleSheet("color:#f44336; font-size:18px; font-weight:bold;")
        
        self.fmk_status.setText("Choice saved")
        self.fmk_choice_label.setText("")
        self.fmk_overlay.hide()
        
        # Reset image size
        self.fmk_imgs[self.current_idx].setFixedSize(200, 200)
        
        if len(self.fmk_results) == 3:
            print("FMK FINAL:", self.fmk_results)
            self.fmk_skip.setText("Next")
    
    def reset_fmk(self):
        for img in self.fmk_imgs:
            img.setFixedSize(200, 200)
        self.fmk_overlay.hide()
        self.fmk_status.setText("")
        self.fmk_choice_label.setText("")

# Main run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
