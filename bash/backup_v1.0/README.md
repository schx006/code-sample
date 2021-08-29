# Backup a VPS on a S3 Object Storage server with _Duplicity_

### Docs

* _Duplicity_ man page
* [_Duplicity_ on Debian Wiki](https://wiki.debian.org/Duplicity)

### HowTo

If needed, create `/root/bin` directory with `drwx------` perms.   
Load `backup.sh` and `duplicity.conf` files on VPS.
As 'root', exec the belows commands:   
``` sh
apt-get update
apt-get upgrade
aptget install duplicity gpg

cp /path/to/Downloads/backup.sh /root/bin/
chmod 700 /root/bin/backup.sh
cp /path/to/Downloads/duplicity.conf /root/.duplicity.conf
chmod 600 /root/.duplicity.conf
``` 

Edit `/root/.duplicity.conf` with _ad-hoc_ parameters…
* S3 server name
* S3 bucket name
* IAM access key Id.
* IAM secret key
* GnuPG key signature or fingerprint (to identify wich to use)
* GnuPG key passphrase (in clear text; if not present, the passphrase will be prompted, needed to schedule backup task)
* set the list of directories to backup as required (Warning: do not try to backup `/proc` directory! Backup will crash.)

Run the bachup task:
``` sh
/root/bin/backup.sh
```

When everything is OK, you can schedule the `/root/bin/backup.sh` command with `crontab -e`.
To backup the VPS every monday at 1:00 am, add the line:
``` sh
0 1 * * 1     /root/bin/backup.sh
```

---

**DON'T FORGET** to backup GnuPG keys and the other backup parameters in a independant way to be able to restore the backup datas.

For instance, using an USB storage device:   
on the VPS,   
``` sh
tar -czvf /root-$HOSTNAME.tgz --exclude='.bash_history' --exclude='.cache' /root
```
… on the local computer,   
``` sh
scp -P sshPort user@vpsName.domainName.tld:/root-vpsName.tgz /path/to/USB/StorageDevice
```
… then, keep the USB storage device in a secure place. Remove the `/root-*.tgz` file on VPS.