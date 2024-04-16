# Puppet script to install nginx server

exec { 'update':
    provider =>
    command  => 'sudo apt-get -y update',
    before   => Exec['install nginx],
}

#Install nginx and configure it
exec { 'install nginx':
    provider => shell,
    command  => 'sudo apt-get -y install nginx',
}


exec {'install':
    provider => shell,
    command  => 'sudo apt-get -y update; sudo apt-get -y install nginx; echo "Hello World!" | sudo tee /puppet_index.html; sudo sed -i s"/server_name _;/root /;\n\tindex puppet_index.;\n\n\tserver_name _;\n\n\trewrite ^\/redirect_me https:\/\/github.com\/otayomitv permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
