<<<<<<< HEAD
# Set up a web server for deployment of web files

$html = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

$var="server {
        listen 80 default_server;
        listen [::]:80 default_server;
        location /hbnb_static {
            alias /data/web_static/current;
	    index index.html index.htm;
        }
        add_header X-Served-By ${hostname};
        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGU1\wu4 permanent;
}"

exec { 'Update':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'sudo apt-get update -y',
  provider => 'shell',
  returns  => [0,1],
} ->

package { 'nginx':
  ensure => 'present',
} ->

file { '/data':
  ensure  => 'directory',
} ->

file { '/data/web_static':
  ensure => 'directory',
} ->

file { '/data/web_static/releases':
  ensure => 'directory',
} ->

file { '/data/web_static/releases/test':
  ensure => 'directory',
} ->

file { '/data/web_static/shared':
  ensure => 'directory',
=======
# Configures a web server for deployment of web_static.

# Nginx configuration file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

file { '/data':
  ensure  => 'directory'
} ->

file { '/data/web_static':
  ensure => 'directory'
} ->

file { '/data/web_static/releases':
  ensure => 'directory'
} ->

file { '/data/web_static/releases/test':
  ensure => 'directory'
} ->

file { '/data/web_static/shared':
  ensure => 'directory'
>>>>>>> a1a68afd0dca7866b0e2a5e292f4e0a52be6468c
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
<<<<<<< HEAD
  content => $html,
=======
  content => "Holberton School Puppet\n"
>>>>>>> a1a68afd0dca7866b0e2a5e292f4e0a52be6468c
} ->

file { '/data/web_static/current':
  ensure => 'link',
<<<<<<< HEAD
  target => '/data/web_static/releases/test',
  force  => 'yes',
} ->

exec { 'permissions' :
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin', 'usr/local/bin'],
  command => 'chown -R ubuntu:ubuntu /data/',
  returns => [0,1],
=======
  target => '/data/web_static/releases/test'
} ->

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www':
  ensure => 'directory'
} ->

file { '/var/www/html':
  ensure => 'directory'
} ->

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School Nginx\n"
} ->

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
>>>>>>> a1a68afd0dca7866b0e2a5e292f4e0a52be6468c
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
<<<<<<< HEAD
  content => $var,
} ->

service { 'nginx':
  ensure => 'running',
=======
  content => $nginx_conf
} ->

exec { 'nginx restart':
  path => '/etc/init.d/'
>>>>>>> a1a68afd0dca7866b0e2a5e292f4e0a52be6468c
}
