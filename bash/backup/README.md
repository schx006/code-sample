### HowTo

If needed, create `/root/bin` directory with `drwx------` perms.   
As 'root', exec the belows commands:   
``` sh
apt-get update
apt-get upgrade
aptget install duplicity gpg


cp /path/to/Downloads/backup.sh /root/bin/
chmod 600 /root/.duplicity.conf
cp /path/to/Downloads/duplicity.conf /root/.duplicity.conf
chmod 700 /root/bin/backup.sh
``` 

Edit `/root/.duplicity.conf` with _ad-hoc_ parameters…
* S3 server name
* S3 bucket name
* IAM access key Id.
* IAM secret key
* GnuPG key signature or fingerprint (to identify wich to use)
* GnuPG key passphrase (in clear text; if not present, the passphrase will be prompted, needed to schedule backup task)

