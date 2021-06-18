#!/bin/bash

set -e

MAX_ARANGO_RETRIES=60

check_service(){
    counter=1
    while ! nc -w 1 "$1" "$2" > /dev/null 2>&1; do
        sleep 1
        counter=`expr ${counter} + 1`
        if [[ ${counter} -gt ${3} ]]; then
            >&2 echo "SERVICE $1:$2 NOT AVAILABLE"
            exit 1
        fi;
    done
}

health_check(){
     check_service "$ARANGO_HOST" "$ARANGO_PORT" "$MAX_ARANGO_RETRIES"
}


migrate(){
    python manage.py arango build;
}


health_check
migrate
if [[ "$1" == "serve" ]]; then
    exec uvicorn xatu.asgi:app \
    --host 0.0.0.0 \
    --port ${XATU_PORT} \
    --workers ${XATU_WORKERS}
elif [[ "$1" == "serve:watch" ]]; then
    # health_check
    exec uvicorn xatu.asgi:app \
    --host 0.0.0.0 \
    --port ${XATU_PORT} \
    --workers ${XATU_WORKERS} \
    --reload
fi


# system_setup
exec $@
