#run the migrations
python manage.py makemigrations
python manage.py migrate


echo "from stockapp.models import CustomUser; CustomUser.objects.create_superuser('trade','trade@gmail.com','stock@123')" | python manage.py shell