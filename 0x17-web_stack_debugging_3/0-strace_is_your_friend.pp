# fix the Apache bug
exec { 'replaces the wrong extension':
    command => 'sudo sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
