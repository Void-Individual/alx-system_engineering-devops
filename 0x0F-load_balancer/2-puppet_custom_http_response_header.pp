# Puppet script to create http header response on a server

exec { 'update':
    command => '/usr/bin/apt-get update',
}

#Install nginx and configure it
package { 'nginx':
    ensure => installed,
}

file_line {'http_header':
    path    => '/etc/nginx/nginx.conf',
    match   => 'http {',
    line    => "http {\n\tadd_header X-Served-By \"{hostname}\";",
    require => Package['nginx'],
}

exec {'run':
    command => 'service nginx restart',
}
