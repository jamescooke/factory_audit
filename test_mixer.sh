#!/bin/bash

set -e

pip-sync requirements/mixer.txt
cd factory_audit/ && ./manage.py test plant.mixer_tests
