# Med_Expert
## API для небольшого мед центра :pill:, реализует след функционал:
- Просмотр списка новостей, а также детальный просмотр конкретной новости <br/> 
- Просмотр списка лицензий, а также детальный просмотр конкретной лицензии <br/>
- Просмотр списка категорий <br/>
- Просмотр услуг, принадлежащих к конкретной категории <br/>
- Просмотр компаний, принадлежащих к конретному типу компании <br/>
- Реализация поиска по услугам <br/>

## Использованные технологии:
- Django, DRF <br/>
- PostgreSQL <br/>
- Docker <br/>

## Запуск проекта:
- git clone https://github.com/o-l-e-z-a/med_expert.git && cd med_expert <br/>
- создать .env файл со след константами: DEBUG, SECRET_KEY,DJANGO_ALLOWED_HOSTS,DB_ENGINE,DB_DATABASE,DB_USER,DB_PASSWORD,DB_HOST,DB_PORT
- docker-compose up --build <br/>
