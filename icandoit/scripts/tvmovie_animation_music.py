import requests
import json
from crolling.models import TVmovie_Animation_Music_model

# action adeventure function

def tvmoive_ect_func(x):
    tvmoive_ect = []
    iter_num = len(x)
    for i in range(iter_num):
        if ('16' in str(x[i]['fields']['genres'])) or ('10402' in str(x[i]['fields']['genres'])) or ('10770' in str(x[i]['fields']['genres'])):
            tvmoive_ect.append(x[i]['fields'])
        else:
            continue
    print(tvmoive_ect)
    print("## 원하는 장르 결과 :  ", tvmoive_ect.__len__())
    return tvmoive_ect



def genreCast(x):
  input_list = x
  genre2str = [ str(i) for i in input_list]
  print(genre2str)
  return ','.join(genre2str)

def dbSave(tvmoive_ect):
    # print(fantasy_sf)
    for obj in tvmoive_ect:
        except_num = 0 
        # print(obj, type(obj))
        print('-----------------------------')
        try :
            movie_id = obj['movie_id']
            print("movie_id> ", movie_id)
            print(type(movie_id))
            title = obj['title']
            print("title > ", title)
            print(type(title))
            released_date = obj['released_date']
            print("'released_date > ", released_date)
            print(type(released_date))
            overview = obj['overview']
            print("overview > ", overview)
            print(type(overview))
            poster_path = obj['poster_path']
            print("poster_path > ", poster_path)
            print(type(released_date))
            genres = obj['genres']
            genres = genreCast(genres)
            print("new genres>>> ", genres)
            
            
            if TVmovie_Animation_Music_model.objects.filter(movie_id__iexact=movie_id).count() == 0:
                TVmovie_Animation_Music_model(movie_id=movie_id,title=title,released_date=released_date,overview=overview,poster_path=poster_path,genres=genres).save()
                print("저장완료")
                print("## 원하는 장르 결과 :  ", tvmoive_ect.__len__())
            else : 
                print("중복값")
        except Exception as e:
            print(e)
            except_num =+1
            print('답없음', except_num )
            



def run():
    TMDB_API_KEY = '4343395b65d4f99d0f3351458f26c8fd'
    total_data = []
    for i in range(1, 20):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&region=KR&language=ko&page={i}"
        movies = requests.get(request_url).json()
        for movie in movies['results']:
            if movie.get('release_date', ''):
                # print('여기에 값있음')
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'overview': movie['overview'],
                    'poster_path': "https://image.tmdb.org/t/p/w200"+movie['poster_path'],
                    'genres': movie['genre_ids']
                }
                data = {
                    "fields": fields
                }
                total_data.append(data)    
    # print(total_data)
    dbSave(tvmoive_ect_func(total_data))






# [{'id': 28, 'name': '액션'},
#  {'id': 12, 'name': '모험'},
#  {'id': 16, 'name': '애니메이션'},
#  {'id': 35, 'name': '코미디'},
#  {'id': 80, 'name': '범죄'},
#  {'id': 99, 'name': '다큐멘터리'},
#  {'id': 18, 'name': '드라마'},
#  {'id': 10751, 'name': '가족'},
#  {'id': 14, 'name': '판타지'},
#  {'id': 36, 'name': '역사'},
#  {'id': 27, 'name': '공포'},
#  {'id': 10402, 'name': '음악'},
#  {'id': 9648, 'name': '미스터리'},
#  {'id': 10749, 'name': '로맨스'},
#  {'id': 878, 'name': 'SF'},
#  {'id': 10770, 'name': 'TV 영화'},
#  {'id': 53, 'name': '스릴러'},
#  {'id': 10752, 'name': '전쟁'},
#  {'id': 37, 'name': '서부'}]