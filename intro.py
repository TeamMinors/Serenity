from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, 
    QHBoxLayout, QListWidget
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt

class MainPage(QWidget):
    """ Main Page that appears after clicking 'Let's Begin' """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        label = QLabel("Welcome to the Main Page!", self)
        label.setFont(QFont("SF Pro", 24))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(label)
        self.setLayout(layout)

class HomePage(QMainWindow):
    """ Home Page with a Simple Clickable Hamburger Menu """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mental Health & Wellbeing App")
        self.setGeometry(200, 100, 900, 600)
        self.setStyleSheet("background-color: #FFCDB2;")  # Soft Background

        # Central Widget
        central_widget = QWidget()
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Top Bar (Logo + Hamburger Menu + Profile)
        top_bar = QHBoxLayout()
        top_bar.setSpacing(10)

        # Small Logo on the left
        logo_label = QLabel()
        logo_pixmap = QPixmap("logo.png").scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(logo_pixmap)

        # Hamburger Menu Button
        self.hamburger_menu = QPushButton("☰")
        self.hamburger_menu.setStyleSheet("background: transparent; font-size: 20px; border: none;")
        self.hamburger_menu.clicked.connect(self.toggle_menu)  # Now correctly calls toggle_menu()

        # Profile Icon on the right
        profile_icon = QPushButton("👤")
        profile_icon.setStyleSheet("background: transparent; font-size: 20px; border: none;")

        top_bar.addWidget(logo_label)  # Small logo first
        top_bar.addWidget(self.hamburger_menu)  # Then hamburger menu
        top_bar.addStretch(1)  # Push the rest to the right
        top_bar.addWidget(profile_icon)

        # Title
        title_label = QLabel("Your Journey to Wellness Begins Here")
        title_label.setFont(QFont("SF Pro", 22, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #B5828C;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Greeting
        greeting_label = QLabel("Hey there! We're glad you're here.")
        greeting_label.setFont(QFont("SF Pro", 18))
        greeting_label.setStyleSheet("color: #E5989B;")
        greeting_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Motivational Quote
        quote_label = QLabel("“Small steps every day lead to big changes.”")
        quote_label.setFont(QFont("SF Pro", 16, QFont.Weight.Medium))
        quote_label.setStyleSheet("color: #FFB4A2; font-style: italic;")
        quote_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # "Let's Begin" Button
        self.begin_button = QPushButton("Let's Begin")
        self.begin_button.setFont(QFont("SF Pro", 20, QFont.Weight.Bold))
        self.begin_button.setStyleSheet("""
            QPushButton {
                background-color: #B5828C;
                color: white;
                border-radius: 20px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #E5989B;
            }
        """)
        self.begin_button.clicked.connect(self.transition_to_main)

        # Hamburger Menu List (Hidden by Default)
        self.menu_list = QListWidget()
        self.menu_list.addItems([
            "⚙️  Settings",
            "ℹ️  Info",
            "📖  Daily Reflection",
            "🧑‍⚕️  Find a Counsellor",
            "🗨️  Chat with Buddies",
            "🧠  Neurocare",
            "📊  Mood Tracker",
            "🤖  AI Companion"
        ])
        self.menu_list.setStyleSheet("""
            QListWidget {
                color: black;
                font-size: 16px;
                background: #E5989B;
                padding: 10px;
                border-radius: 10px;
                border: none;
            }
            QListWidget::item {
                padding: 10px;
            }
            QListWidget::item:hover {
                background: rgba(255, 255, 255, 0.3);
                border-radius: 5px;
            }
        """)
        self.menu_list.setHidden(True)  # Start hidden

        # Add elements to layout
        self.main_layout.addLayout(top_bar)
        self.main_layout.addWidget(self.menu_list)  # Menu will appear here when clicked
        self.main_layout.addSpacing(10)
        self.main_layout.addWidget(title_label)
        self.main_layout.addWidget(greeting_label)
        self.main_layout.addSpacing(15)
        self.main_layout.addWidget(self.begin_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addSpacing(15)
        self.main_layout.addWidget(quote_label)

        # Set main layout
        self.setCentralWidget(central_widget)

    def toggle_menu(self):
        """ Show or hide the menu list below the hamburger button """
        if self.menu_list.isHidden():
            self.menu_list.setHidden(False)
        else:
            self.menu_list.setHidden(True)

    def transition_to_main(self):
        """ Smoothly transition to Main Page """
        self.main_page = MainPage()
        self.main_page.show()
        self.close()

# Run the App
if __name__ == "__main__":
    app = QApplication([])
    home = HomePage()
    home.show()
    app.exec()
