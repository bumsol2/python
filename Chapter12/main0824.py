###BLOG 게시글 로딩하기
# data.csv 파일이 있으면 
# 		게시글을 로딩 한다.		
# data.csv 파일이 없으면
# 		data.csv 파일을 만든다.
# 게시글 로딩하기
# data.csv 파일을 읽는다.	
# 데이터 한 줄 마다		
# 		Post 인스턴스를 만든다.
# 		Post 리스트에 인스턴스를 저장한다. 

from multiprocessing.sharedctypes import Value
import os
import csv
from post0824 import Post

#파일 경로
file_path = "E:/python/Chapter12/data1.csv"

#post 객체 저장할 리스트
post_list = []

#data.csv 파일이 있다면
if os.path.exists(file_path):
    #게시글 로딩
    print("게시글 로딩중...")
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        # Post 인스턴스 생성
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
else:
    #파일 생성
    f = open(file_path, "w", encoding="utf8", newline="")
    f.close()
#게시글 쓰기
def write_post():
    """게시글 쓰기 함수"""
    print("\n\n- 게시글쓰기-")
    title = input("제목입력해\n")
    content = input("내용 입력해\n")
    # 글번호
    id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print("# 게시글 등록되었다.")


# 게시글 목록
def list_post():
    """게시글 목록 함수"""
    print("\n\n- 게시글 목록 -")
    id_list = []
    for post in post_list:
        print("번호 :", post.get_id())                
        print("제목 :", post.get_title())                
        print("조회수 :", post.get_view_count())                
        print("")
        id_list.append(post.get_id())                

    while True:
        print("Q) 글 번호 선택하셈 (메뉴 돌아갈려면 -1입력해)")
        try:
            id = int(input(">>>>>>"))
            if id in id_list:
                print("게시글 상세보기")
            elif id == -1:
                break
            else:
                print("없는글번호이다.")
        except ValueError:
            print("숫자입력해")
        
#메뉴 출력하기
while True: #무한반복
    print("\n\n- sol Blog -")
    print("- 메뉴를 선택해라-")
    print("1. 게시글쓰기")
    print("2. 게시글 목록")
    print("3.프로그램 종료")
    try:
        choice = int(input(">>>"))
    except ValueError:
        print("숫자입력해")
    else:
        if choice == 1:
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            print("프로그램종료")
            break
# 게시글 쓰기
# 게시글 등록
# Post 인스턴스 생성
# Post 리스트에 저장
# Post 인스턴스
# 글번호 
# 제목
# 내용
# 조회수
# 마지막 글번호???
# 현재 post_list의 마지막 요소의 id값 +1 



