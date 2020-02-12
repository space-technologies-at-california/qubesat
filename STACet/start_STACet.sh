osascript -e 'tell app "Terminal"
    do script "nc -l 8001"
end tell'

python3 receive.py