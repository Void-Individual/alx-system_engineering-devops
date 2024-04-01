# Puppet script to create http header response on a server

# Retrieve the hostname of the machine
$name = $::hostname
$config = "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /;
    index hello.html;

    server_name _;

    error_page 404 /my_404.html;

    location /redirect_me {
        return 301 https://github.com/Void-Individual;
    }

    location / {
        add_header X-Served-By \"$name\";
        try_files \$uri \$uri/ =404;
    }
}"
#Install nginx and configure it
package { 'nginx':
    ensure => installed,
}

file { 'puppet_index.html':
    path    => '/puppet_index.html',
    content => "Hello World!\n",
}

file { '/etc/nginx/sites-available/default':
    content => $config,
}

service { 'nginx':
    ensure  => running,
    enable  => true,
    require => File['/etc/nginx/sites-available/default'],
}
