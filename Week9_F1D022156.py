import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTabWidget, QAction, QFileDialog,
    QFontDialog, QInputDialog, QMessageBox, QTextEdit
)
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 9 - QDialog, QTabWidget & MenuBar")
        self.setGeometry(100, 100, 500, 300)

        # ========== MenuBar ==========
        menubar = self.menuBar()

        # File Menu
        file_menu = menubar.addMenu("File")
        exit_action = QAction("Keluar", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Fitur Menu
        fitur_menu = menubar.addMenu("Fitur")
        input_nama_action = QAction("Input Nama", self)
        pilih_font_action = QAction("Pilih Font", self)
        buka_file_action = QAction("Buka File", self)

        input_nama_action.triggered.connect(self.show_input_nama_dialog)
        pilih_font_action.triggered.connect(self.show_font_dialog)
        buka_file_action.triggered.connect(self.show_file_dialog)

        fitur_menu.addAction(input_nama_action)
        fitur_menu.addAction(pilih_font_action)
        fitur_menu.addAction(buka_file_action)

        # ========== Tab Widget ==========
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tab_input_nama = QWidget()
        self.tab_pilih_font = QWidget()
        self.tab_buka_file = QWidget()

        self.tabs.addTab(self.tab_input_nama, "Input Nama")
        self.tabs.addTab(self.tab_pilih_font, "Pilih Font")
        self.tabs.addTab(self.tab_buka_file, "Buka File")

        self.init_input_nama_tab()
        self.init_pilih_font_tab()
        self.init_buka_file_tab()

    # ---------- Tab: Input Nama ----------
    def init_input_nama_tab(self):
        layout = QVBoxLayout()
        self.nama_label = QLabel("Nama: ")
        btn_input_nama = QPushButton("Input Nama")
        btn_input_nama.clicked.connect(self.show_input_nama_dialog)
        layout.addWidget(btn_input_nama)
        layout.addWidget(self.nama_label)
        self.tab_input_nama.setLayout(layout)

    def show_input_nama_dialog(self):
        nama, ok = QInputDialog.getText(self, "Input Nama", "Masukkan nama:")
        if ok and nama:
            self.nama_label.setText(f"Nama: {nama}")

    # ---------- Tab: Pilih Font ----------
    def init_pilih_font_tab(self):
        layout = QVBoxLayout()
        self.font_label = QLabel("Nama: ")
        btn_pilih_font = QPushButton("Pilih Font")
        btn_pilih_font.clicked.connect(self.show_font_dialog)
        layout.addWidget(btn_pilih_font)
        layout.addWidget(self.font_label)
        self.tab_pilih_font.setLayout(layout)

    def show_font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.font_label.setFont(font)

    # ---------- Tab: Buka File ----------
    def init_buka_file_tab(self):
        layout = QVBoxLayout()
        btn_buka_file = QPushButton("Buka File .txt")
        btn_buka_file.clicked.connect(self.show_file_dialog)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        layout.addWidget(btn_buka_file)
        layout.addWidget(self.text_edit)
        self.tab_buka_file.setLayout(layout)

    def show_file_dialog(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Buka File", "", "Text Files (*.txt)"
        )
        if path:
            try:
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.text_edit.setPlainText(content)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Gagal membaca file:\n{str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
