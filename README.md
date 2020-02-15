# rpitemp
logs cpu temperature to firebase (be warned I've no idea what I'm doing)

## to run locally

`./install.sh`

set environment variables:
* DATABASE_URL
* SERVICE_ACCOUNT
* INTERVAL
* HOST_NAME

`./temp.py`

## to build docker image:

`docker build -t maxpeart/rpitemp .`

## to run:

```
docker run -d --env DATABASE_URL \
    --env SERVICE_ACCOUNT \
    --env INTERVAL \
    -e 'HOST_NAME=raspberrypi' \
    --name rpitemp \
    -v firebase:/firebase:ro \
    maxpeart/rpitemp
```
### required environment variables:
`DATABASE_URL` "https://<your_project>.firebaseio.com"

`SERVICE_ACCOUNT` is the filename of the json produced from firebase > project > project overview > users and permissions > service accounts > Generate new private key

`INTERVAL` is the number of seconds between polls

### volumes
I put the service json in a volume called filebase then referenced it in the run command `-v firebase:/firebase:ro`

create it with `docker volume create firebase`

to get the json into the volume 
```
docker container create --name dummy -v firebase:/root hello-world
docker cp <firebase admin service account>.json dummy:/root/config.json
docker rm dummy
```
in the example above SERVICE_ACCOUNT would be set to `export SERVICE_ACCOUNT=/firebase/config.json`
