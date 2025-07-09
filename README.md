# Felix_Archive_Bot

This is a simple Telegram bot built with [aiogram](https://docs.aiogram.dev/) that automatically sends new images from a specified folder to a Telegram group every 30 minutes.

##  Features

- Automatically scans a local folder for new image files
- Sends media files to a Telegram group using a bot token
- Keeps track of already sent files to avoid duplicates
- Runs continuously with periodic checking (every 30 minutes)
- Supports media formats: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.mp4`, `.jfif`

##  Requirements

- Python 3.7+
- `aiogram` library

1. Install dependencies using:

```bash
pip install -r requirements.txt
```
2. Fill in the config file with your data

