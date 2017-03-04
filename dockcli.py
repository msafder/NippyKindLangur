import click
import docker
import time

def healthcheck(container):
    """curls the container on 8080 and URI "/hello"
    returns HTTP response code
    """
    hcheck = 'curl -sw %{http_code} --output /dev/null http://0.0.00:8080/hello'
    time.sleep(5)
    return container.exec_run(hcheck)

def run(name, client):
    """starts the container with name
    must be passed a docker client
    """
    kwargs = {
        'detach': True,
        'name': name,
        'ports': {'8080/tcp': 8080}
    }
    container = client.containers.run("sudomilk/nippykindlangur:latest", **kwargs)
    healthcheck_rsp = healthcheck(container)
    if healthcheck_rsp == b'200':
        click.echo('Your app is running on http://127.0.0.1:8080/hello')

def stop(name, client):
    """stops the container of the given name
    must be passed a docker client
    """
    container = client.containers.get(name)
    container.stop()
    container.remove()

#main cli config
@click.command()
@click.argument('action')
@click.argument('name')
def main(action, name):
    client = docker.from_env()
    #kick it on, do a healthcheck, and return the URL to hit
    if action == 'run':
        run(name, client)
    #turn it off
    if action == 'stop':
        stop(name, client)

if __name__ == '__main__':
    main()
