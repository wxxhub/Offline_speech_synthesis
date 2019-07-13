from pydub import AudioSegment
import os

mp3_path = "voice/"
wave_path = "wav/"

def main():
    files = os.listdir(mp3_path)
    for file_name in files:
        mp3 = AudioSegment.from_mp3(mp3_path+file_name)
        file_name = file_name.split('.')[0] + ".wav"
        mp3.export(wave_path+file_name, format="wav")
        print (file_name)
    pass

if __name__ == "__main__":
    main()