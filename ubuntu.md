# Ubuntu related notes

## baseline - things I do as part of any server provisioning

```
locale-gen C.UTF-8 || true
update-locale LANG=en_US.UTF-8
echo "export LANG=C.UTF-8" >> /etc/skel/.bashrc
echo "force-confnew" >> /etc/dpkg/dpkg.cfg
echo 'Defaults    env_keep += "DEBIAN_FRONTEND"' >> /etc/sudoers.d/env_keep

echo Acquire::Languages \"none\"\; | tee /etc/apt/apt.conf.d/02nolang
echo APT::Install-Recommends \"0\"\;  | sudo tee -a /etc/apt/apt.conf.d/03norecommends
sed -i -e 's/^deb-src/#deb-src/' /etc/apt/sources.list

rm -f /etc/dpkg/dpkg.cfg.d/multiarch
sudo dpkg --remove-architecture i386

apt-get install software-properties-common
add-apt-repository -r universe
add-apt-repository -r multiverse

apt-get purge -y apt-xapian-index linux-headers-generic linux-headers-virtual
apt-get purge -y libx11-data xkb-data
apt-get purge -y command-not-found command-not-found-data
apt-get purge -y ntfs-3g


sudo DEBIAN_FRONTEND=noninteractive apt-get -y update
sudo DEBIAN_FRONTEND=noninteractive apt-get -y upgrade
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install curl unzip zip

```
