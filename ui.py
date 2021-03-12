import sys
import asyncio
import json

from qasync import QEventLoop, asyncSlot
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QLabel, QHBoxLayout

from main import Center

with open("./data/config.json", "r") as configfile:
    configdata = json.load(configfile)
    token = configdata["discord_token"]
    prefix = configdata["prefix"]


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(700,500)
        self.setWindowTitle("CenterQuickBot")

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)


        self.baslat_btn = QPushButton(f"Başlat")
        self.yeniden_btn = QPushButton(f"Yeniden Başlat")
        self.durdur_btn = QPushButton(f"Durdur")
        self.yazi_alani = QLabel("Bot Token : " + token +"\nBot Prefix : " + prefix)

        self.baslat_btn.clicked.connect(self.baslat_slot)

        self.baslat_btn.setStyleSheet("color:green;")
        self.yeniden_btn.setStyleSheet("color:darkorange;")
        self.durdur_btn.setStyleSheet("color:red;")

        self.vbox.addWidget(self.baslat_btn)
        self.vbox.addWidget(self.yeniden_btn)
        self.vbox.addWidget(self.durdur_btn)


        self.msg_gonder = QLineEdit()
        self.msg_gonder.setPlaceholderText("Mesaj gönder")
        self.msg_gonder.returnPressed.connect(self.msg_gonder_slot)

        self.kanal_id = QLineEdit()
        self.kanal_id.setPlaceholderText("Kanal ID")
        self.kanal_id.returnPressed.connect(self.kanal_id_slot)

        self.vbox.addWidget(self.msg_gonder)
        self.vbox.addWidget(self.kanal_id)


        self.logs = QListWidget()
        self.logs_last = 0

        self.vbox.addWidget(self.yazi_alani)
        self.vbox.addWidget(self.logs)


        self.bot = Center(self)


    def log(self, msg):
        self.logs.insertItem(self.logs_last, msg)
        self.logs_last += 1

    @asyncSlot()
    async def msg_gonder_slot(self):
        ch = self.bot.get_guild(804058227515588628).get_channel(int(self.text))
        await ch.send(self.msg_gonder.text())
        self.msg_gonder.setText("")

    @asyncSlot()
    async def kanal_id_slot(self):
        self.text = self.kanal_id.text()
        self.kanal_id.setText("")


    @asyncSlot()
    async def baslat_slot(self):
        await self.bot.start(token)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    eventloop = QEventLoop(app)
    asyncio.set_event_loop(eventloop)

    mw = MainWindow()
    mw.show()

    eventloop.run_forever()
