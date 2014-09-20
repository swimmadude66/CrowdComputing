#Added this usefull function from a Stack Overflow post:
#Link: http://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux
function coloredEcho(){
   local exp=$1;
    local color=$2;
    if ! [[ $color =~ '^[0-9]$' ]] ; then
       case $(echo $color | tr '[:upper:]' '[:lower:]') in
        black) color=0 ;;
        red) color=1 ;;
        green) color=2 ;;
        yellow) color=3 ;;
        blue) color=4 ;;
        magenta) color=5 ;;
        cyan) color=6 ;;
        white|*) color=7 ;; # white or invalid color
       esac
    fi
    tput setaf $color;
    echo $exp;
    tput sgr0;
}

# setup.sh for Surround Sound Project
coloredEcho "Installing base dependencies:" green

# add repository for newest npm
sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-get update

# installing extras
sudo apt-get install -y gcc g++ autoconf automake libtool
sudo apt-get install -y python-software-properties python make
sudo apt-get install -y build-essential libssl-dev
sudo apt-get install -y software-properties-common
sudo apt-get install -y rlwrap

# install nodejs and npm
sudo apt-get install nodejs
sudo apt-get install npm

# install all server dependencies
sudo npm install