#!/usr/bin/env bash

apt-get update
apt-get install --yes git vim

# install postgresql-9.3
PG_REPO_APT_SOURCE=/etc/apt/sources.list.d/pgdg.list
if [ ! -f "$PG_REPO_APT_SOURCE" ]
then
    echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > "$PG_REPO_APT_SOURCE"
    wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-key add -
    apt-get update
fi

apt-get install --yes postgresql-9.3
sudo -u postgres psql < /vagrant/config/setup.sql

if [ ! -d "/opt/conda" ]; then
    wget --no-clobber http://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
    bash Miniconda2-latest-Linux-x86_64.sh -b -p "/opt/conda"
    echo 'export PATH="/opt/conda/bin:$PATH"' >> /home/vagrant/.bashrc
fi

export PATH="/opt/conda/bin:$PATH"

conda update --yes conda
conda env update --name root --file /vagrant/config/environment.yml

sudo chown -R vagrant:vagrant /opt/conda        # permissions things

exit 0
