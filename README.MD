1. Клонируйте репозиторий и откройте его
git clone https://github.com/ваш-проект.git cd lr
2. В командной строке создайте виртуальное окружение и активируйте его (перед этим проверьте при помощи pwd находитесь ли вы в нужном репозитории)
python -m venv venv
source venv/bin/activate # для Linux/MacOS
venv\Scripts\activate    # для Windows
3. Установите зависимости
pip install -r requirements.txt
4. Выполните миграции
python manage.py migrate
5. Запустите сервер
python manage.py runserver
