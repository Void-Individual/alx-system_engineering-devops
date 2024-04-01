# Puppet script to create http header response on a server

exec { 'update':
    provider =>
    command  => 'sudo apt-get -y update',
    before   => Exec['install nginx],
}

#Install nginx and configure it
exec { 'install nginx':
    provider => shell,
    command  => 'sudo apt-get -y install nginx',
    before   => 'Exec['add_header'],
}

Exec { 'add_header':
    provider    => shell,
    environment => ["HOST=${hostname}"],
    command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
    before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
