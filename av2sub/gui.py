# -*- coding: utf-8 -*-
# Copyright (C) 2023  HAL9000COM <f1226942353@icloud.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from subtoolkit import *
import sys
from multiprocessing import freeze_support
from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QFileDialog,
    QTextBrowser,
    QPushButton,
    QVBoxLayout,
    QApplication,
)
from gui_ui import Ui_MainWindow
import os
import shutil
import json
from send2trash import send2trash
from markdown2 import markdown


from constants import lang_dict_deepl, lang_dict_google

lang_dict = {}
lang_dict["DeepL"] = lang_dict_deepl
lang_dict["DeepL Pro"] = lang_dict_deepl
lang_dict["Google"] = lang_dict_google


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.config = {}
        try:
            self.load_config()
        except:
            self.init_config()
            self.save_config()

        self.read_config()

        self.comboBox_transcribe.currentIndexChanged.connect(self.api_changed)
        self.comboBox_translate.currentIndexChanged.connect(self.api_changed)
        self.comboBox_translate.currentIndexChanged.connect(self.set_lang)
        self.lineEdit_transcribe_key.textChanged.connect(self.key_changed)
        self.lineEdit_translate_key.textChanged.connect(self.key_changed)
        self.spinBox_max_lines.valueChanged.connect(self.config_changed)
        self.pushButton_av_browse.clicked.connect(self.av_browse)
        self.pushButton_out_browse.clicked.connect(self.out_browse)
        self.pushButton_sub_in_browse.clicked.connect(self.sub_in_browse)

        # self.checkBox_batch.stateChanged.connect(self.batch_changed)
        self.pushButton_process.clicked.connect(self.process)

        self.actionAbout.triggered.connect(self.about)
        self.actionOpen_Source_Licenses.triggered.connect(self.licenses)

    def load_config(self):
        with open("config.json", "r") as f:
            self.config = json.load(f)

    def config_changed(self):
        self.config["max_lines"] = self.spinBox_max_lines.value()

    def api_changed(self):
        self.config["transcribe_api"] = self.comboBox_transcribe.currentText()
        self.config["translate_api"] = self.comboBox_translate.currentText()
        # check if key exists
        if self.config["transcribe_api"] not in self.config["transcribe_key"].keys():
            self.config["transcribe_key"][self.config["transcribe_api"]] = ""
        if self.config["translate_api"] not in self.config["translate_key"].keys():
            self.config["translate_key"][self.config["translate_api"]] = ""
        self.lineEdit_transcribe_key.setText(
            self.config["transcribe_key"].get(self.config["transcribe_api"], "")
        )
        self.lineEdit_translate_key.setText(
            self.config["translate_key"].get(self.config["translate_api"], "")
        )
        if self.config["transcribe_api"] == "OpenAI":
            self.checkBox_transcribe_en.show()
        else:
            self.checkBox_transcribe_en.hide()

        if self.config["translate_api"] == "Google":
            self.lineEdit_translate_key.setEnabled(False)
        else:
            self.lineEdit_translate_key.setEnabled(True)

        self.set_lang()

    def key_changed(self):
        self.config["transcribe_key"][
            self.config["transcribe_api"]
        ] = self.lineEdit_transcribe_key.text()
        self.config["translate_key"][
            self.config["translate_api"]
        ] = self.lineEdit_translate_key.text()

    def set_lang(self):
        self.comboBox_target_lang.clear()
        for lang in lang_dict[self.config["translate_api"]].keys():
            self.comboBox_target_lang.addItem(lang)

    def init_config(self):
        self.config["transcribe_api"] = "OpenAI"
        self.config["translate_api"] = "DeepL"
        self.config["transcribe_key"] = {}
        self.config["transcribe_key"]["OpenAI"] = ""
        self.config["translate_key"] = {}
        self.config["translate_key"]["DeepL"] = ""
        self.config["max_lines"] = 20

    def save_config(self):
        with open("config.json", "w") as f:
            json.dump(self.config, f, indent=4)

    def read_config(self):
        self.comboBox_transcribe.setCurrentIndex(
            self.comboBox_transcribe.findText(self.config["transcribe_api"])
        )
        self.comboBox_translate.setCurrentIndex(
            self.comboBox_translate.findText(self.config["translate_api"])
        )
        self.lineEdit_transcribe_key.setText(
            self.config["transcribe_key"][self.config["transcribe_api"]]
        )
        self.lineEdit_translate_key.setText(
            self.config["translate_key"][self.config["translate_api"]]
        )
        self.spinBox_max_lines.setValue(self.config["max_lines"])
        self.set_lang()

    def av_browse(self):
        # if self.checkBox_batch.isChecked():
        #     file_path = QFileDialog.getExistingDirectory(
        #         self, "Select Video Folder", ""
        #     )
        #     if file_path:
        #         self.lineEdit_av.setText(file_path)
        #         self.lineEdit_output.setText(file_path)
        # else:
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Video File", "", "Video Files (*.*)"
        )
        # check if file_path is valid
        if os.path.isfile(file_path):
            self.lineEdit_av.setText(file_path)
            self.lineEdit_output.setText(file_path.split(".")[0] + ".srt")

    def sub_in_browse(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Subtitle File", "", "Subtitle Files (*.srt)"
        )
        # check if file_path is valid
        if os.path.isfile(file_path):
            self.lineEdit_sub_in.setText(file_path)

    def out_browse(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Select Output File", "", "SRT Files (*.srt)"
        )
        if file_path:
            self.lineEdit_output.setText(file_path)

    def batch_changed(self):
        # if self.checkBox_batch.isChecked():
        #     self.lineEdit_output.setEnabled(False)
        #     self.pushButton_out_browse.setEnabled(False)
        # else:
        self.lineEdit_output.setEnabled(True)
        self.pushButton_out_browse.setEnabled(True)

    def process(self):
        match self.tabWidget_input.currentIndex():
            case 0:
                mode = "av"
            case 1:
                mode = "subtitle"
            case _:
                raise

        kwargs = {}
        kwargs["mode"] = mode
        kwargs["video_path"] = self.lineEdit_av.text()
        kwargs["sub_in_path"] = self.lineEdit_sub_in.text()
        kwargs["out_path"] = self.lineEdit_output.text()
        kwargs["transcribe_api"] = self.comboBox_transcribe.currentText()
        kwargs["transcribe_key"] = self.lineEdit_transcribe_key.text()
        kwargs["transcribe_en"] = self.checkBox_transcribe_en.isChecked()
        kwargs["translate_api"] = self.comboBox_translate.currentText()
        kwargs["translate_key"] = self.lineEdit_translate_key.text()
        kwargs["max_lines"] = self.spinBox_max_lines.value()
        kwargs["target_lang"] = lang_dict[self.config["translate_api"]][
            self.comboBox_target_lang.currentText()
        ]
        kwargs["save_original"] = self.checkBox_save_original.isChecked()
        kwargs["clear_cache"] = self.checkBox_clear_cache.isChecked()

        self.message_window = MessageWindow()
        self.message_window.show()
        self.worker = Worker(**kwargs)
        self.thread = QThread(parent=self)  # type: ignore
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.worker_progress)
        self.worker.result.connect(self.worker_result)
        self.thread.start()

    def worker_progress(self, progress):
        self.message_window.append_line(progress)

    def worker_result(self, result):
        pass

    def about(self):
        with open("About.md", "r", encoding="utf-8") as f:
            md = f.read()
        html = markdown(md, extras=["fenced-code-blocks"])
        self.about_window = MessageWindow()
        self.about_window.setWindowTitle("About")
        self.about_window.textBrowser.setHtml(html)

    def licenses(self):
        with open("licenses.md", "r", encoding="utf-8") as f:
            md = f.read()
        html = markdown(md, extras=["fenced-code-blocks"])
        self.lic_window = MessageWindow()
        self.lic_window.setWindowTitle("Open Source Licenses")
        self.lic_window.textBrowser.setHtml(html)

    def closeEvent(self, event):
        self.save_config()
        event.accept()


class MessageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message")
        self.textBrowser = QTextBrowser(self)
        self.pushButton_clear = QPushButton(self)
        self.pushButton_clear.setText("Clear")
        self.pushButton_clear.clicked.connect(self.clear)
        self.textBrowser.setAcceptDrops(False)
        self.textBrowser.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.textBrowser)
        layout.addWidget(self.pushButton_clear)
        self.setLayout(layout)
        self.show()

    def append_line(self, line):
        # get current time
        self.textBrowser.append(line)
        ## auto scroll
        self.textBrowser.verticalScrollBar().setValue(
            self.textBrowser.verticalScrollBar().maximum()
        )

    def clear(self):
        self.textBrowser.clear()


class Worker(QObject):
    finished = Signal()
    result = Signal(object)
    progress = Signal(object)

    def __init__(self, **kwargs):
        super().__init__()
        self.mode = kwargs.get("mode", "av")
        self.video_path = kwargs.get("video_path", "")
        self.sub_in_path = kwargs.get("sub_in_path", "")
        self.out_path = kwargs.get("out_path", "")
        self.transcribe_api = kwargs.get("transcribe_api", "OpenAI")
        self.transcribe_key = kwargs.get("transcribe_key", "")
        self.translate_api = kwargs.get("translate_api", "DeepL")
        self.translate_key = kwargs.get("translate_key", "")
        self.max_lines = kwargs.get("max_lines", 20)
        self.target_lang = kwargs.get("target_lang", "ZH")
        self.save_original = kwargs.get("save_original", False)
        self.clear_cache = kwargs.get("clear_cache", True)
        self.transcribe_en = kwargs.get("transcribe_en", False)

    def run(self):
        try:
            match self.mode:
                case "av":
                    self.av_process()
                case "subtitle":
                    self.sub_process()
        except Exception as e:
            self.progress.emit(str(e))
            self.finished.emit()

    def av_process(self):
        try:
            self.progress.emit("Start FFmpeg...")
            audio_path = video2audio(self.video_path)
            self.progress.emit("Start Transcribing...")
            srt_path = audio2srt(
                audio_path,
                srt_path=self.out_path,
                api=self.transcribe_api,
                api_key=self.transcribe_key,
                en=self.transcribe_en,
            )
            if self.target_lang == "None":
                self.progress.emit("Finish!")
                self.finished.emit()
                return
            if self.save_original:
                # copy and rename original srt
                path = self.out_path.split(".")[0] + "_original.srt"
                shutil.copyfile(srt_path, path)
            self.progress.emit("Start Translating...")
            translate_sub(
                sub_path=srt_path,
                api=self.translate_api,
                api_key=self.translate_key,
                max_lines=self.max_lines,
                target_lang=self.target_lang,
            )
            self.progress.emit("Removing Cache...")
            if self.clear_cache:
                audio_path = audio_path.replace("/", "\\")  # fix for windows
                send2trash(audio_path)
            self.progress.emit("Finish!")
        except Exception as e:
            self.progress.emit(str(e))
        return

    def sub_process(self):
        try:
            srt_path = self.sub_in_path
            self.out_path = self.sub_in_path
            if self.target_lang == "None":
                self.progress.emit("Finish!")
                self.finished.emit()
                return
            if self.save_original:
                # copy and rename original srt
                path = self.out_path.split(".")[0] + "_original.srt"
                shutil.copyfile(srt_path, path)
            self.progress.emit("Start Translating...")
            translate_sub(
                sub_path=srt_path,
                api=self.translate_api,
                api_key=self.translate_key,
                max_lines=self.max_lines,
                target_lang=self.target_lang,
            )
            self.progress.emit("Finish!")
        except Exception as e:
            self.progress.emit(str(e))
        return


if __name__ == "__main__":
    freeze_support()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
