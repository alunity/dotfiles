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

[[ -r "/usr/share/z/z.sh" ]] && source /usr/share/z/z.sh

export PATH="$HOME/.cabal/bin:$HOME/.ghcup/bin:$PATH"
alias config='/usr/bin/git --git-dir=/home/alunity/.cfg/ --work-tree=/home/alunity'
