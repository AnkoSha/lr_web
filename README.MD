Клонируйте репозиторий и откройте его
git clone https://github.com/AnkoSha/lr_web.git
при ошибке памяти сначала сделайте это: git config --global http.postBuffer 524288000
В командной строке создайте виртуальное окружение и активируйте его (перед этим проверьте при помощи pwd находитесь ли вы в нужном репозитории) 
cd lr_web
python -m venv venv
source venv/bin/activate # для Linux/MacOS
.\\venv\\Scripts\\activate # для Windows
Установите зависимости
pip install -r requirements.txt
Выполните миграции
python manage.py migrate
Запустите сервер
python manage.py runserver
Для проверки отзывов:
логин: admin
пароль: admin
