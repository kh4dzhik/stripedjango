
git clone https://github.com/kh4dzhik/stripedjango.git
cd stripedjango

Запустите контейнер
docker-compose up --build

если запускаете без docker:
pip install -r requirements.txt
python manage.py runserver


Так как вы теперь мы имеем дело с заказом который может содержать несколько продуктов, решил поменять /item/{id} на /order/{id}.
Функционал платежа в реализовал отдельном приложении payment. /buy/{id} помеяль на /buy/order/{id}

  Получите HTML страницу с информацией о заказе и кнопкой для оплаты:
  curl -X GET http://localhost:8000/order/4

  Получите Stripe Session ID для оплаты заказа:
  curl -X GET http://localhost:8000/payment/buy/order/4


ключи к API STRIPE залил в репозиторий в файле .env , чтоб вы могли проверить работоспособность
username админки - admin
пароль админки - pass
