import requests
import pandas as pd





BASE_URL = "https://jsonplaceholder.typicode.com"
users_url = f"{BASE_URL}/users"

response_user = requests.get(users_url)
# print(response.json())
# 2. Afficher le nom et l'email de chaque utilisateur
for user in response_user.json():
    print(f"Name: {user['name']}") 
    print(f"Email: {user['email']}")

# 3. Récupérer tous les posts de l'utilisateur avec `userId=1`
posts_url = f"{BASE_URL}/posts"

params = {"userId": 1}

response_post = requests.get(posts_url, params=params)
print(response_post.json())

# 4. Compter combien de posts chaque utilisateur a créé

posts_user_1 = response_post.json()
print(len(posts_user_1))
# 5. Récupérer les commentaires du post `id=1`
for post in posts_user_1:
    print({post['id'] : post['body']})

# 6. Créer un DataFrame Pandas avec :
#    - Colonnes : post_id, post_title, nombre_commentaires
#    - Pour les 10 premiers posts

posts_data = []
for post in posts_user_1[:10]:
    post_id = post['id']
    post_title = post['title']
    comment_url = f"{BASE_URL}/comments"
    response = requests.get(comment_url)
    comments = response.json()
    nombre_commentaires = len(comments)
    posts_data.append({
        'post_id': post_id,
        'post_title': post_title,
        'nombre_commentaires': nombre_commentaires
    })
    
df_posts = pd.DataFrame(posts_data)
print(df_posts)


todos_url = f"{BASE_URL}/todos"
response_todos = requests.get(todos_url)


todos_data = []
for todos in response_todos.json():
    todos_id = todos['id']
    todos_title = todos['title']
    todos_status = todos["completed"]
    todos_data.append({
        'todos_id': todos_id,
        'todos_title': todos_title,
        'status': todos_status
    })
    
df_todos = pd.DataFrame(todos_data)
True_df = df_todos.loc[df_todos['status'] == True]
False_df = df_todos.loc[df_todos['status'] == False]
# print(df_todos)
with pd.ExcelWriter('api_rapport.xlsx') as writer:
    True_df.to_excel(writer, sheet_name='todos True', index=False)
    False_df.to_excel(writer, sheet_name='todos False', index=False)
    