# Puppet script to install nginx server
exec {'install':
    provider => shell,
    command  => 'sudo apt-get -y update; sudo apt-get -y install nginx; echo "Hello World!" | sudo tee /var/www/html/puppet_index.html; sudo sed -i s"/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/otayomitv permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
