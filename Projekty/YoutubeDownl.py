from pytube import YouTube

def pobierz_film(url, sciezka):
    try:
        video = YouTube(url)
        video.streams.get_highest_resolution().download(output_path=sciezka)
        print("Pobieranie zakończone pomyślnie!")
    except Exception as e:
        print("Wystąpił błąd podczas pobierania filmu:", str(e))


url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
sciezka = "D:/downloads"
pobierz_film(url, sciezka)