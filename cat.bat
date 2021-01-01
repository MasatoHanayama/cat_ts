@echo on
ffmpeg -f concat -safe 0 -i .\ts_cat.txt -c copy output.mp4
pause