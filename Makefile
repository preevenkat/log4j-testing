docker_compose_project_name = ezpz-docker-elk
docker_compose_cmd = /usr/local/bin/docker-compose --project-name $(docker_compose_project_name)

start_services:
	$(docker_compose_cmd) up -d --build

destroy_services:
	$(docker_compose_cmd) kill
	$(docker_compose_cmd) rm -fv
