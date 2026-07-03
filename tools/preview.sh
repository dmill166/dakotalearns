#!/usr/bin/env bash
# Preview dakotalearns.com locally — INCLUDING unpushed course-repo work.
#
# Syncs course prose from the local working trees (not GitHub), then serves
# the site at http://127.0.0.1:8000 with live reload. Ctrl-C to stop.
#
# One-time setup for a shortcut, either flavor:
#   zsh alias:  echo 'alias dl-preview="bash ~/dev/dakotalearns/tools/preview.sh"' >> ~/.zshrc
#   git alias:  git -C ~/dev/dakotalearns config alias.preview '!bash tools/preview.sh'
#               (then: cd ~/dev/dakotalearns && git preview)
#
# Requires the pinned venv:  pyenv virtualenv 3.13.7 dakotalearns-site
#   + pip install mkdocs-material==9.7.6 mkdocs-awesome-nav==3.3.0 mkdocs-rss-plugin==1.19.0
set -euo pipefail

SITE="$HOME/dev/dakotalearns"
VENV="$HOME/.pyenv/versions/dakotalearns-site"

if [ ! -x "$VENV/bin/mkdocs" ]; then
    echo "Missing venv: $VENV — see the setup note in this script's header." >&2
    exit 1
fi

cd "$SITE"
"$VENV/bin/python" tools/sync_courses.py \
    --local "computer-science-1=$HOME/dev/computer-science-1"
exec "$VENV/bin/mkdocs" serve -a 127.0.0.1:8000
