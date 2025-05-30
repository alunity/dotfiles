#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

set -o vi

alias vi="nvim"

source $HOME/.bash_functions/competitive_programming.sh

[[ -r "/usr/share/z/z.sh" ]] && source /usr/share/z/z.sh


export PATH="$HOME/.cabal/bin:$HOME/.ghcup/bin:$PATH"

export MANPAGER='nvim +Man!'
