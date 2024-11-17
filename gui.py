from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import QTimer
from screen_capture import capture_screen
from image_processing import convert_to_grayscale, resize_image
from skill_detection import detect_skill_active
from key_automation import activate_skill

class SkillAutomationGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_status)
        self.running = False

    def initUI(self):
        layout = QVBoxLayout()

        self.status_label = QLabel('Status: Parado')
        layout.addWidget(self.status_label)

        self.start_button = QPushButton('Iniciar')
        self.start_button.clicked.connect(self.toggle_automation)
        layout.addWidget(self.start_button)

        self.skill_key_input = QLineEdit()
        self.skill_key_input.setPlaceholderText('Tecla da habilidade (ex: 1)')
        layout.addWidget(self.skill_key_input)

        self.skill_region_input = QLineEdit()
        self.skill_region_input.setPlaceholderText('Região da habilidade (x,y,w,h)')
        layout.addWidget(self.skill_region_input)

        self.active_color_input = QLineEdit()
        self.active_color_input.setPlaceholderText('Cor ativa (R,G,B)')
        layout.addWidget(self.active_color_input)

        self.setLayout(layout)
        self.setWindowTitle('Automação de Habilidades')
        self.setGeometry(300, 300, 300, 200)

    def toggle_automation(self):
        if not self.running:
            self.running = True
            self.start_button.setText('Parar')
            self.status_label.setText('Status: Em execução')
            self.timer.start(1000)
        else:
            self.running = False
            self.start_button.setText('Iniciar')
            self.status_label.setText('Status: Parado')
            self.timer.stop()

    def update_status(self):
        skill_key = self.skill_key_input.text()
        skill_region = tuple(map(int, self.skill_region_input.text().split(',')))
        active_color = tuple(map(int, self.active_color_input.text().split(',')))

        screenshot = capture_screen()
        gray_image = convert_to_grayscale(screenshot)
        resized_image = resize_image(gray_image, 50)

        is_active = detect_skill_active(resized_image, skill_region, active_color)

        if not is_active:
            activate_skill(skill_key)
            self.status_label.setText(f'Status: Ativando habilidade {skill_key}')
        else:
            self.status_label.setText(f'Status: Habilidade {skill_key} ativa')
