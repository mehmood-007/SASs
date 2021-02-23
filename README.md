
## Instructions
The repository contains prometheus configurations, alert rules, nginx configs and python api to trigger alerts based on the rules  

* Currently,  cAdvisor cluster execute at docker cluster using following command:

`docker service create --name cadvisor -l prometheus-job=cadvisor \
--mode=global --publish published=8040,target=8080,mode=host \
--mount type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock,ro \
--mount type=bind,src=/,dst=/rootfs,ro \
--mount type=bind,src=/var/run,dst=/var/run \
--mount type=bind,src=/sys,dst=/sys,ro \
--mount type=bind,src=/var/lib/docker,dst=/var/lib/docker,ro \
google/cadvisor -docker_only`

* So far currently, docker cluster manage through docker-cli, therefore python API must be executed at swarm cluster manager using following command inside SASs folder:

`python3 api.py`

* Deploy docker cluster through docker compose located inside docker-swarm folder

`docker stack deploy stack`
