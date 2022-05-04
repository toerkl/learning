# How to run

# Local
ansible-playbook -K --connection=local --inventory 127.0.0.1, playbook-local.yml

# Non-local
ansible-playbook -K --connection=local --inventory hosts playbook-non-local.yml

