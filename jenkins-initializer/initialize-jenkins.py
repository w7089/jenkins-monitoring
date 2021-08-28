
from api4jenkins import Jenkins
import string
import random


def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

jenkins_client = Jenkins('http://jenkins:8080/', auth=('admin', 'admin'))
xml = """<?xml version='1.1' encoding='UTF-8'?>
<project>
  <builders>
    <hudson.tasks.Shell>
      <command>echo $JENKINS_VERSION</command>
    </hudson.tasks.Shell>
  </builders>
</project>"""

try:
    jenkins_client.create_job(randomword(10), xml)
except:
    pass

