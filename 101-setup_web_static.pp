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
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => $html,
} ->

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => 'yes',
} ->

exec { 'permissions' :
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin', 'usr/local/bin'],
  command => 'chown -R ubuntu:ubuntu /data/',
  returns => [0,1],
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $var,
} ->

service { 'nginx':
  ensure => 'running',
}
