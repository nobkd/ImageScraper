# ImageScraper
[<img width=128px align=right src="https://github.com/1amn0body/ImageScraper/blob/master/icon/image_scraper_icon.png">](https://github.com/1amn0body/ImageScraper/releases)

The ImageScraper is a cross-platform tool for downloading a specified count from [xkcd](https://xkcd.com), [Astronomy Picture of the Day](https://apod.nasa.gov) and [Existential Comics](https://existentialcomics.com) (at the moment on the branch `system_background_image`).

With the config setup at the first start you can set the count and the save path. You can change it in the config file `image-scraper-config.yaml` or by deleting it and starting the application again.

## Build

This application is created with Python 3.9 and depends on following non standard python packages:
- requests
- beautifulsoup4

You can build the executable yourself by just using [pyinstaller](https://pyinstaller.org):

```bash
pip install pyinstaller
```

```bash
pyinstaller main.py --onefile --name ImageScraper --icon icon/image_scraper_icon.ico
```

## Features

- [x] Download latest xkcd and/or Astronomy Picture of the Day
   - [x] Custom image download count
   - [x] Custom image save-path
   - [x] List saved images
   - [x] Auto-remove option
   - [ ] Test for internet connection before auto-removing
   - [ ] Progress bar
- [ ] Automatically set background image in a platform and desktop environment specific way
   - [ ] Windows
   - [ ] Mac
   - [ ] Linux Desktop Environments     
      - [ ] KDE Plasma
      - [ ] Gnome
      - [ ] lxde
      - [ ] other
