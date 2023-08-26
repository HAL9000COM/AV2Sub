# AV2Sub

Audio/Video to Subtitle converter with translation.

## Features

* Transcribe audio/video to srt
* Translate srt to bilingual srt
* Transcribe API: OpenAI Whisper
* Translate API: DeepL, DeepL Pro

## Requirements

* ffmpeg

## TODO

* [ ] Audio splitting
* [ ] Google APIs
* [ ] Better timestamp accuracy with other model
* [ ] Translation
* [ ] GUI translation

## GUI compile

    python -m nuitka gui.py --standalone --include-data-files="licenses.md=licenses.md" --include-data-files="about.md=about.md" --enable-plugin=pyside6 --include-module=pygments --disable-console

## Disclaimer

According to Article 8 of [Berne Convention for the Protection of Literary and Artistic Works](https://www.wipo.int/treaties/en/ip/berne/):
> Authors of literary and artistic works protected by this Convention shall enjoy the exclusive right of making and of authorizing the translation of their works throughout the term of protection of their rights in the original works.

Please comply with the copyright laws in the jurisdiction where you intend to create, distribute, or use translations as well as the terms and conditions of APIs used.