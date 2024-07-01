# COmment
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
}

exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install werkzeug==2.1.1',
}
