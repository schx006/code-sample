#!/usr/bin/env bash

recipient='th3m1s@xs-net.io'
sender="root@`hosname --long`"
subject="Rapport de sauvegarde complète - `date +%d/%m/%y`"
report-mail="/tmp/backup-report-`date +%y%m%d`.txt"

if $# > 1  ; then
    for arg in $* ; do
        if   [ $arg -eq 'incr' ] ; then
            report-mail="/tmp/incr-backup-report-`date +%y%m%d`.txt"
        elif [ $arg -eq 'full' ] ; then
            report-mail="/tmp/full-backup-report-`date +%y%m%d`.txt"
        fi
    done
fi


# créer un fichier avec l'en-tête du mail
echo -e "To: $recipient\nFrom: $sender\nSubject: $subject\n\n" > $report-mail
# exécuter la sauvegarde et 
# rediriger les sorties (standard et erreur) dans le corps du mail
/root/bin/backup.sh $@ >> $report-mail 2>&1
# envoyer le mail
sendmail -t < $report-mail

# faire le ménage : suppression des rapports de plus d'une semaine
find /tmp/ -name (full-|incr-)backup-report-[0-9]{6}.txt -mtime +7 -delete
