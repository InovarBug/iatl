
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import QTimer

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

        self.setLayout(layout)
        self.setWindowTitle('Automação de Habilidades')
        self.setGeometry(300, 300, 250, 150)

    def toggle_automation(self):
        if not self.running:
            self.running = True
            self.start_button.setText('Parar')
            self.status_label.setText('Status: Em execução')
            self.timer.start(1000)  # Atualiza a cada segundo
        else:
            self.running = False
            self.start_button.setText('Iniciar')
            self.status_label.setText('Status: Parado')
            self.timer.stop()

    def update_status(self):
        # Aqui você pode adicionar a lógica para verificar e ativar habilidades
        print(f"Verificando habilidade: {self.skill_key_input.text()}")
        # Exemplo: if not skill_active: activate_skill(self.skill_key_input.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SkillAutomationGUI()
    ex.show()
    sys.exit(app.exec_())

