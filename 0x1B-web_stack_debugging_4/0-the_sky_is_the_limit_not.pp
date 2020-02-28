# fix the error
exec { 'fix the error':
    command => '/usr/bin sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/g" /etc/nginx/nginx.conf | service nginx restart'
}
