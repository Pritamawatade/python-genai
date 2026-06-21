import shutil
import subprocess
import speech_recognition as sr
import pyttsx3

def speak_with_pyttsx3(text: str) -> bool:
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        return True
    except Exception as exc:
        print("pyttsx3 error:", exc)
        return False

def get_audio_player() -> list[str] | None:
    if shutil.which("aplay"):
        return ["aplay", "-"]
    if shutil.which("paplay"):
        return ["paplay"]
    if shutil.which("ffplay"):
        return ["ffplay", "-nodisp", "-autoexit", "-"]
    return None


def speak_with_espeak(text: str) -> bool:
    if shutil.which("espeak") is None:
        return False

    player = get_audio_player()
    if player is None:
        print("espeak is installed, but no audio player was found (aplay/paplay/ffplay).")
        return False

    try:
        espeak_proc = subprocess.Popen(
            ["espeak", "--stdout", text],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if espeak_proc.stdout is None:
            return False

        player_proc = subprocess.Popen(player, stdin=espeak_proc.stdout, stderr=subprocess.PIPE)
        espeak_proc.stdout.close()
        _, player_err = player_proc.communicate()

        if player_proc.returncode != 0:
            print("Audio playback failed:", player_err.decode(errors="ignore"))
            return False

        return True
    except subprocess.SubprocessError as exc:
        print("espeak playback error:", exc)
        return False

def speak(text: str) -> None:
    if speak_with_espeak(text):
        return
    if speak_with_pyttsx3(text):
        return

    print(
        "Unable to speak audio. Install eSpeak or an audio player, or fix pyttsx3/ALSA configuration."
        " On Arch Linux: sudo pacman -S espeak alsa-utils pipewire pipewire-pulse"
        " On Debian/Ubuntu: sudo apt install espeak libasound2-plugins"
    )

def listen_and_transcribe() -> str | None:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Please speak now...")
        audio = recognizer.listen(source)

    try:
        transcript = recognizer.recognize_google(audio)
        print("Transcription:", transcript)
        return transcript
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as err:
        print("Speech recognition service error:", err)
    return None

if __name__ == "__main__":
    text = listen_and_transcribe()
    if text:
        speak("You said: " + text)