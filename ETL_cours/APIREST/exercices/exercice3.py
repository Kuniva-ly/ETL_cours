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