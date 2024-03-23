# A file script to install Flask

exec { 'install_flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
    path    => '/usr/bin',
    creates => '/usr/local/lib/python3.8/dist-packages/flask/__init__.py'
}

exec { 'install_werkzeug':
    command => '/usr/bin/pip3 install werkzeug==2.1.1',
    path    => '/usr/bin',
    creates => '/usr/local/lib/python3.8/dist-packages/werkzeug/__init__.py'
}
