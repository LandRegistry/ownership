#!/bin/bash

source /vagrant/script/dev-env-functions
source ./environment.sh
create_virtual_env "ownership"
python manage.py create_owner --lrid='2fd71646-7ebb-4b90-89d0-1a0221aafbff' --owner_index='1' --title_number='DN300'
deactivate
