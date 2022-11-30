# Idioma del teclado
setxkbmap es

# Transparencia
picom &

# Dispositivos externos
udiskie -t &

# Teclas especiales
xmodmap -e "add mod3 = Scroll_Lock" 

# Icono de red
nm-applet &

# Script de usuario
$HOME/.config/qtile/autostart.sh
