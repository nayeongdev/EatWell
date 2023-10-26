일정 계획
-----------
```mermaid
gantt
    title 프로젝트 일정
    dateFormat YY-MM-DD
    section 기획
        0단계    :2023-10-26, 1d
        1단계    :2023-10-28, 1d
        2단계    :2023-10-30, 1d
        3단계    :2023-11-1, 1d
    section 디자인
        1단계    :2023-10-28, 1d
        2단계    :2023-10-30, 1d
        3단계    :2023-11-1, 1d
    section FE
        0단계 :2023-10-26, 2d
        1단계    :2023-10-28, 2d
        2단계    :2023-10-30, 2d
        3단계    :2023-11-2, 3d
    section BE
        0단계 :2023-10-26, 2d
        1단계    :2023-10-28, 2d
        2단계    :2023-10-30, 2d
        3단계    :2023-11-2, 3d
```

DB 모델
-----------
![식당 DB](<readme_source/식당 모델.png>)

URL 구조
-----------
```
1.1 ''                                 : 메인
1.2 'about/'                           : 사이트 소개
2.1 'restaurants/'                     : 추천식당 목록
2.2 'restaurants/<int:pk>/'            : 추천식당 읽기
```

| 앱이름: `main` | views 함수이름 | html 파일이름 | 비고    |
|:--------------|:---------------|:-------------|:--------|
|`''`           |index           |`index.html`  |         |
|`'about/'`     |about           |`about.html`  |         |

| 앱이름: `restaurants`            | views 함수이름    | html 파일이름           |  비고                         |
|:--------------------------------|:-----------------|:------------------------|:------------------------------|
|`'restaurants/'`                 |RestaurantsList   |`restaurants.html`       |                               |
|`'restaurants/<int:pk>'`         |RestaurantsDetail |`restaurants-detail.html`|게시물이 없을 경우에는 404로 연결|