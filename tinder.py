import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

# Dummy data for buddies
buddies = [
    {"name": "H", "bio": "Loves to help and listen.", "image": "H.jpeg"},
    {"name": "J", "bio": "Passionate about mental well-being.", "image": "J.jpeg"},
    {"name": "M", "bio": "Always here to support.", "image": "M.jpeg"}
]

class BuddyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.current_index = 0
        self.show_profile()

    def initUI(self):
        self.setWindowTitle("Buddy Matcher")
        self.setGeometry(100, 100, 400, 500)
        self.setStyleSheet("background-color: purple;")  # Set background color
        
        # Create labels
        self.image_label = QLabel(self)
        self.name_label = QLabel(self)
        self.name_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))  # Larger text
        self.name_label.setStyleSheet("color: white;")  # Improve readability
        self.bio_label = QLabel(self)
        self.bio_label.setFont(QFont("Arial", 14))  # Larger text
        self.bio_label.setStyleSheet("color: white;")
        
        # Create buttons
        self.next_button = QPushButton("Next", self)
        self.prev_button = QPushButton("Previous", self)
        self.select_button = QPushButton("Select Buddy", self)
        
        # Connect buttons to functions
        self.next_button.clicked.connect(self.next_profile)
        self.prev_button.clicked.connect(self.prev_profile)
        self.select_button.clicked.connect(self.select_buddy)
        
        # Layout setup
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.name_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.bio_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.select_button)
        self.button_layout.addWidget(self.next_button)
        
        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Right:
            self.next_profile()
        elif event.key() == Qt.Key.Key_Left:
            self.prev_profile()

    def show_profile(self):
        buddy = buddies[self.current_index]
        self.name_label.setText(f"Name: {buddy['name']}")
        self.bio_label.setText(f"Bio: {buddy['bio']}")
        try:
            pixmap = QPixmap(buddy["image"])
            self.image_label.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
        except Exception as e:
            self.image_label.setText("Image not found")
    
    def next_profile(self):
        if self.current_index < len(buddies) - 1:
            self.current_index += 1
            self.show_profile()
    
    def prev_profile(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_profile()
    
    def select_buddy(self):
        self.welcome_screen()
    
    def welcome_screen(self):
        # Remove all existing widgets including buttons
        while self.layout.count():
            widget = self.layout.takeAt(0).widget()
            if widget is not None:
                widget.deleteLater()
        
        # Display welcome message
        welcome_label = QLabel("Welcome to a new you!", self)
        welcome_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        welcome_label.setStyleSheet("color: white;")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add only the welcome message
        self.layout.addWidget(welcome_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BuddyApp()
    window.show()
    sys.exit(app.exec())
