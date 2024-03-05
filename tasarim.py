from fileinput import filename

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QTextDocument


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from new_new_welcome_python import Ui_MainWindow
import webbrowser
import os
import speech_recognition as sr
import glob
from pydub import AudioSegment
from pydub.silence import split_on_silence
import ffmpeg
import sys
import time





class dersler(QMainWindow, QDialog , QMenu, QRectF, QTextDocument, QPushButton):
    def __init__(self):
        super().__init__() #super() methoduyla üst sınıftaki parametler çağrılıyor


        self.ui = Ui_MainWindow() #burada designer modulünde classı çağırıp tanımlıyoruz
        self.ui.setupUi(self) # setupUi fonksiyonu çağırıyoruz ... #böylellikle tasarımda yer alan elemanlar çalışıyor




        self.ui.pushButton.clicked.connect(self.Return)
         #burası dönüştürme fonksiyonunu çalışıtran buton 
        self.ui.soundBox.clicked.connect(self.text_start)

        self.ui.soundBox.clicked.connect(self.browseSound)
        self.ui.textButton.clicked.connect(self.browseText)

        ###Open Video##
        self.ui.video_en.clicked.connect(lambda: webbrowser.open('http://www.youtube.com'))
        self.ui.Video_tr.clicked.connect(lambda: webbrowser.open('http://www.youtube.com'))


        ###Welcome###
        self.buttonWe = QAction("Welcome", self)
        self.buttonWe.setStatusTip("Welcome")

        self.buttonWe.setCheckable(True)
        self.ui.menubar.addAction(self.buttonWe)
        self.buttonWe.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
               #####Türkçe#####
        self.buttonTr = QAction("Türkçe", self)
        self.buttonTr.setStatusTip("Türkçe")
        self.buttonTr.triggered.connect(self.set_Turkce)
        self.buttonTr.setCheckable(True)
        self.ui.menubar.addAction(self.buttonTr)
        self.buttonTr.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

              #####English#####
        self.buttonEn = QAction("English", self)
        self.buttonEn.setStatusTip("English")
        self.buttonEn.triggered.connect(self.set_English)
        self.buttonEn.setCheckable(True)
        self.ui.menubar.addAction(self.buttonEn)
        self.buttonEn.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))


        #####Français####
        self.buttonFr = QAction("Français", self)
        self.buttonFr.setStatusTip("Français")
        self.buttonFr.triggered.connect(self.set_Francais)
        self.buttonFr.setCheckable(True)
        self.ui.menubar.addAction(self.buttonFr)
        self.buttonFr.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        #####Deutsch#####
        self.buttonDe = QAction("Deutsch", self)
        self.buttonDe.setStatusTip("Deutsch")
        self.buttonDe.triggered.connect(self.set_Deutsch)
        self.buttonDe.setCheckable(True)
        self.ui.menubar.addAction(self.buttonDe)
        self.buttonDe.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))




    def text_start(self):
        
            self.ui.label.setText('{}...'.format(self.convert))
            #burada convert başladığı anda kullanıcıya bilgi text gönderiyoruz


    def text_finish(self):
        self.ui.label.setText('{}...'.format(self.done))
#bu kısımda da dillere göre ön yüzdeki diller ayarlanıyor
    def set_Turkce(self):
        self.ui.pushButton.setText("Dönüştür")
        self.ui.textBrowser.setText("Dönüştürmek istediğiniz ses dosyasını seçiniz")
        self.ui.textBrowser_2.setText("Oluşturacağınız yazı dosyasnın yerini ve adını seçiniz")
        self.ui.label.setText("Bekleniyor...")
        self.lg="tr"  #lg ile birlikte goople api'ye hangi dilde çevirme yapacağımızı yazıyoruz
        self.convert = "dönüşüm için hazırlanıyor"
        self.done = "Tamamlandı"
    def set_English(self):
        self.ui.pushButton.setText("Convert")
        self.ui.textBrowser.setText("Please select the audio file what will convert")
        self.ui.textBrowser_2.setText("Please select the where of the text file it will create")
        self.ui.label.setText("Waiting...")
        self.lg="en" #lg ile birlikte goople api'ye hangi dilde çevirme yapacağımızı yazıyoruz
        self.convert = "readying for converting"
        self.done="Completed"
    def set_Francais(self):
            self.ui.pushButton.setText("Convertir")
            self.ui.textBrowser.setText("Veuillez sélectionner le fichier audio qui sera converti")
            self.ui.textBrowser_2.setText("Veuillez sélectionner l'emplacement du fichier texte qu'il va créer")
            self.ui.label.setText("Attendre...")
            self.lg="fr" #lg ile birlikte goople api'ye hangi dilde çevirme yapacağımızı yazıyoruz
            self.convert = "prêt pour la conversion"
            self.done="Complété"
    def set_Deutsch(self):
            self.ui.pushButton.setText("Konvertieren")
            self.ui.textBrowser.setText("Bitte wählen Sie die Audiodatei aus, die konvertiert werden solli")
            self.ui.textBrowser_2.setText("Bitte wählen Sie den Ort der Textdatei aus, die erstellt werden soll")
            self.ui.label.setText("das Warten...")
            self.lg="de" #lg ile birlikte goople api'ye hangi dilde çevirme yapacağımızı yazıyoruz
            self.convert="bereit für die Konvertierung"
            self.done="Vollendet"
    def browseSound(self):
        self.fname = QFileDialog.getOpenFileName(self,"Open Sound File","","Sound Files (*.mp4 *.mp3 *.ogg *.wav)")
        self.ui.lineEdit_3.setText(self.fname[0])
        print(self.fname[0])
        head_tail=os.path.split(self.fname[0])
        self.path = str(head_tail[0])
        print(self.path)
      #ses dosyasının formatını buluyoruz
        self.x = str(self.fname[0].split('.')[-1])
        print(self.x)
        self.ft = str(self.fname[0].split('.')[0])
        print(self.ft)
        self.y = str(self.fname[0].split('/')[-1])
        print(self.y)
     



    def browseText(self):
        self.fileName = QFileDialog.getSaveFileName(self, "Save File","C//","Text (*.txt)")
        self.ui.lineEdit_4.setText(self.fileName[0])


    def long(self):

        r = sr.Recognizer()
        if self.x == "wav":
            self.path1 = str(self.fname[0])
        elif self.x == "mp4":
            self.path1 = "{}.wav".format(self.ft)
        elif self.x == "mp3":
            self.path1 = "{}.wav".format(self.ft)
        elif self.x == "ogg":
            self.path1 = "{}.wav".format(self.ft)
        else:
            print("Yanlış format seçtiniz")
        sound = AudioSegment.from_wav(self.path1)
        # ses dosyalarını burada sessizlik süresine göre parçalıyoruz
        chunks = split_on_silence(sound,
                                  # experiment with this value for your target audio file
                                  min_silence_len=500,
                                  # adjust this per requirement
                                  silence_thresh=sound.dBFS - 16,
                                  # keep the silence for 1 second, adjustable as well
                                  keep_silence=500,
                                  )

        folder_name = self.path + "/audio-chunks"
        print(folder_name)
        # burada eğer belirtilen dosya yoksa dosya oluşturuyoruz
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)

        whole_text = ""   
      #başlangıçtaki whole text değerini "" veriyoruz


        for i, audio_chunk in enumerate(chunks, start=1):
            # export audio chunk and save it in
            # the `folder_name` directory.

            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")

            audio_chunk.export(chunk_filename, format="wav")

            # recognize the chunk
            with sr.AudioFile(chunk_filename) as source:
                audio = r.record(source)

                try:
                    text = r.recognize_google(audio, language=self.lg) #lg ile birlikte goople api'ye hangi dilde çevirme yapacağımızı yazıyoruz
                except sr.UnknownValueError as e:
                    print("Error:", str(e))
                else:
                    text = f"{text.capitalize()}. "
                    print(chunk_filename, ":", text)

                    whole_text += text



        fileList = glob.glob(folder_name + '/*.wav', recursive=True)
    
        for filePath in fileList:
            try:
                os.remove(filePath)
            except OSError:
                print("Error while deleting file")

        print("silindi")

        os.rmdir(folder_name)
        document = open(self.fileName[0], "w", encoding="utf8")
        document.write(whole_text)
        document.close()
        self.text_finish()

        return whole_text


    def Return(self):
    #bu fonksiyonda ses dosyası formatlarını wav formatına dönüştürüyoruz
        if self.x == "wav":

            self.long()

        elif self.x == "ogg":

            command2wav = "ffmpeg -y -i {}.ogg {}.wav".format(self.ft, self.ft)
            os.system(command2wav)
            os.system("clear")

            self.long()

        elif self.x == "mp4":

            command2mp3 = "ffmpeg -y -i {}.mp4 {}.mp3".format(self.ft, self.ft)
            command2wav = "ffmpeg -y -i {}.mp3 {}.wav".format(self.ft, self.ft)
            os.system(command2mp3)
            os.system(command2wav)
            os.system("clear")

            self.long()

        elif self.x == "mp3":

            command2wav = "ffmpeg -y -i {}.mp3 {}.wav".format(self.ft , self.ft)
            os.system(command2wav)

            self.long()

        else:
            print("Yanlış format girdiniz")

if __name__ == '__main__':
#bukısım gereklilik hali her projede belirtilmesi gerekiyor
    uygulama = QApplication([]) #QApplication([]) 'nu tanımlıyourz
    window = dersler()
    window.show()

    uygulama.exec_() #burada döngüye sokuyoruz
