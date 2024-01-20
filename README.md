### Setup

```
pip install -r requirements.txt
```

### Configuration

Add your podcast URLs to download_podcasts.py

```
podcasts = {
   "MLOps.community": "https://podcasts.apple.com/us/podcast/mlops-community/id1505372978"
}
```

### Running

#### Download Podcasts

```
python download_podcast.py --run
```

#### Audio to Text

this will output a file named file.json

```
time whisper file.mp3 --model base --language en --output_format json 
```

### Youtube Transcript

Input is a Youtube ID number.

```
python download_youtube_transcript.py slIVToAG98M -t > transcript.txt
```