#!/bin/bash

cd Service1/ || exit
docker volume create --name NewDataVolume
docker build -t service_one .
docker run -ti --rm -v NewDataVolume:/data_volume1 service_one
cd ../Service2/ || exit
docker build -t service_two .
docker run -ti --rm -v NewDataVolume:/data_volume1 service_two

