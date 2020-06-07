# api_final
api final

Работа с постами:

  GET  http://localhost:8000/api/v1/posts/        #просмотреть все посты
  
  GET  http://localhost:8000/api/v1/posts/{id}/   #Получить публикацию по id
       
  POST  http://localhost:8000/api/v1/posts/       #создание поста
  
  PUT   http://localhost:8000/api/v1/posts/{id}/  #Обновить публикацию по id
  
  PATCH http://localhost:8000/api/v1/posts/{id}/  #Частично обновить публикацию по id
  
  DELETE http://localhost:8000/api/v1/posts/{id}/ #Удалить публикацию по id
 
Работа с COMMENTS:

   GET  http://localhost:8000/api/v1/posts/{post_id}/comments/                #Получить список всех комментариев публикации
   
   GET  http://localhost:8000/api/v1/posts/{post_id}/comments/{comment_id}/   #Получить комментарий для публикации по id
        
   POST http://localhost:8000/api/v1/posts/{post_id}/comments/                #Создать новый комментарий для публикации
   
   PUT  http://localhost:8000/api/v1/posts/{post_id}/comments/{comment_id}/   #Обновить комментарий для публикации по id
   
   PATCH http://localhost:8000/api/v1/posts/{post_id}/comments/{comment_id}/  #Частично обновить комментарий для публикации по id
   
   JWT-токен:
   
   http://localhost:8000/api/v1/token/           #Получить JWT-токен
   
   http://localhost:8000/api/v1/token/refresh/   #Обновить JWT-токен
   
   Работа с FOLLOW:
   
   GET http://localhost:8000/api/v1/follow/  #Получить список всех подписчиков
   
   POST http://localhost:8000/api/v1/follow/ #Создать подписку
   
   Работа с GROUP:
    
   GET http://localhost:8000/api/v1/group/  #Получить список всех групп
   
   POST http://localhost:8000/api/v1/group/ #Создать новую группу
   
   DELETE http://localhost:8000/api/v1/posts/{post_id}/comments/{comment_id}/ #Удалить комментарий для публикации по id
