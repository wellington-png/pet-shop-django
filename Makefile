restart:
	sudo systemctl restart clinica_pet.service
	sudo systemctl restart clinica_pet.socket
	sudo systemctl restart clinica_pet
	sudo systemctl daemon-reload
