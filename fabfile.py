from fabric.api import local
def prepare_deploy():
  local("cd /home/visualpath/python/fab00 && touch 1a 2a 3a")
  local("cd /home/visualpath/python/fab00 && git add . && git commit -m tested")
  local("cd /home/visualpath/python/fab00 && git push origin master")

