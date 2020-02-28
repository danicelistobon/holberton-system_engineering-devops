# fix the error
exec { 'fix the error':
    command => '/usr/bin/env sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/g" /etc/default/nginx | service nginx restart'
}
