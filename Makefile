test:
	PYTHONPATH=. py.test tests

sync:
	rsync -vr --exclude=*.pyc --exclude=.git/* . linode:/srv/compose-server

deploy: sync
	ssh linode "supervisorctl restart compose-server"
