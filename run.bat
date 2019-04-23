if [[ "$1" = "pi" ]]; then
  python src/raspberry-pi/Portahorn
elif [[ "$1" = "app" ]]; then
  cd src/android
  python main.py
fi
