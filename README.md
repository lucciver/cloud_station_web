# Web-based Ground Control Station

## Prerequisite 
```
Python 3.6+
Django
Django Channels
Django Background Tasks
Redis
Docker
```
> Tutorial to setup Python Django development environment: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment

## Getting started
```bash
pip3 install django
pip3 install -U channels
pip3 install django-background-tasks
git clone https://github.com/lyuyangh/cloud-station.git 
```
install and run docker: https://www.docker.com/get-started
```
docker run -p 6379:6379 -d redis:2.8
```
### Run server
```python
python3 manage.py runserver
```
## Architecture
## To Do
- [x] Rewrite mavlink streaming code
- [ ] Add map to html
- [ ] Deploy on AWS
- [ ] Mark drone location on map
## Authors
## License