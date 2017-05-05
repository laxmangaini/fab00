from fabric.api import local
def prepare_deploy():
  local("cd /home/devops/python/fabric-scripts/fab00 && touch f1 f2 f3")
  local("cd /home/devops/python/fabric-scripts/fab00 && git add . && git commit -m test")
  local("cd /home/devops/python/fabric-scripts/fab00 && git push origin master")

