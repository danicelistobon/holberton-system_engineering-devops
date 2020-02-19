# fix the Apache bug
exec { 'replaces the wrong extension':
    command => '/usr/bin/env sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
