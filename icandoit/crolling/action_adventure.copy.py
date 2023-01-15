# import requests
# import json
# from crolling.models import Action_adventure_model

# def run():
# TMDB_API_KEY = '4343395b65d4f99d0f3351458f26c8fd'

# def get_movie_datas():
#     cnt = 0 
#     iter_num = 0 
#     total_data = []

#     # 1페이지부터 6페이지까지 (페이지당 20개, 총 100개)
#     for i in range(1, 10):
#         request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&region=KR&language=ko&page={i}"
#         movies = requests.get(request_url).json()
#         # print("# 저장된 길이 : ", len(movies['results']) )
#         # print('_____________________________________________')

#         for movie in movies['results']:
#             iter_num =+ 1
#             if movie.get('release_date', ''):
#                 # print('여기에 값있음')
#                 fields = {
#                     'movie_id': movie['id'],
#                     'title': movie['title'],
#                     'released_date': movie['release_date'],
#                     # 'popularity': movie['popularity'],
#                     # 'vote_avg': movie['vote_average'],
#                     'overview': movie['overview'],
#                     'poster_path': "https://image.tmdb.org/t/p/w200"+movie['poster_path'],
#                     'genres': movie['genre_ids']
#                 }


#                 data = {
#                     # "movie_num": movie['id'],
#                     # "model": "movies.movie",
#                     "fields": fields
#                 }
#                 # print(data)
#                 total_data.append(data)
#                 cnt=+1
                
#     return total_data



# total_data = get_movie_datas()
# print(total_data)
# print(cnt, iter_num, len(total_data), type(total_data[0]))
# print(total_data)


# if len(total_data)!= 0 :
#     print('total data 잘 저장됨')
#     with open("movie_data.json", "w", encoding="utf-8") as w:
#             json.dump(total_data, w, indent="\t", ensure_ascii=False)

#     def action_adventure(x):
#         action_adventure = []
#         iter_num = len(x)
#         for i in range(iter_num):
#             if ('28' in str(x[i]['fields']['genres'])) and ('12'  in str(x[i]['fields']['genres'])):
#                 action_adventure.append(x[i]['fields'])
#             else:
#                 continue
#         print(action_adventure.__len__())
#         return action_adventure
    


# action_adventure = action_adventure(total_data)
#     print(action_adventure)


# def func(x):
#     action_adventure = []
#     iter_num = len(x)
#     for i in range(iter_num):
#         if ('28' in str(x[i]['fields']['genres'])) and ('12'  in str(x[i]['fields']['genres'])):
#             action_adventure.append(x[i]['fields'])
#             # print(action_adventure)
#             for action_adventures in action_adventure:
#                 print(action_adventures)
#                 # try:
#                 #     movie_id = action_adventures[0]['movie_id']
#                 #     print(movie_id)
#             #         title = action_adventures[0]['title']
#             #         print(title)
#             #         released_date = action_adventures[0]['released_date']
#             #         print(released_date)
#             #         overview = action_adventures[0]['overview']
#             #         print(overview)
#             #         poster_path = action_adventures[0]['poster_path']
#             #         print(poster_path)
#             #         genres = action_adventures[0]['genres']
#             #         print(genres)
#             #         # Action_adventure_model(movie_id=movie_id,title=title,released_date=released_date,overview=overview,poster_path=poster_path,genres=genres).save()
#             #         print("저장완료")
#                 # except:
#                 #     print('답없음')
                
# print(func(total_data))
#     if len(action_adventure)!= 0 :
#         print('total data 잘 저장됨')
#         with open("movie_data.json", "w", encoding="utf-8") as w:
#                 json.dump(action_adventure, w, indent="\t", ensure_ascii=False)

