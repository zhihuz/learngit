#!/usr/bin/env bash
nohup python run.py -c energy/cpnn_config -s "2010-01-01 00:00:00" > cpnn_energy.out &
