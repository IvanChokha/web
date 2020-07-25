sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
mysql -uroot -e "create database stepik_web;"
mysql -uroot -e "grant all privileges on setpik_web.* to 'box'@'localhost' with grant option;"
python3 ~/web/ask/manage.py makemigrations
python3 ~/web/ask/manage.py migrate
cd ./ask/
python3 manage.py runserver 0.0.0.0:8000
