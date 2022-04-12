### service url: gitlini.com<br><br>

# Recommend Repositories

## 프로젝트 개요
![image](https://user-images.githubusercontent.com/92630511/157400997-2696e974-fe29-4277-8763-8073ab921831.png)
![image](https://user-images.githubusercontent.com/92630511/157476539-a825b50d-0ef6-4978-9f8a-15ed582b5ed5.png)
![image](https://user-images.githubusercontent.com/92630511/157476597-ddfd3fb6-fc3f-47c9-bb17-643b4f4b5aab.png)
<br>

 개발 관련한 상당수의 정보교류 부터 포트폴리오 관리까지 이미 업계에서 Github의 입지는 굳이 설명하지 않아도 될 정도입니다 게다가 현업자들이 신입 개발자에게 요구하는 가장 중요한 능력치로 Github가 1순위에 손꼽히는 것도 전혀 놀라운 일이 아니죠<br>
하지만 업계에 발을 들이고자 하는 주니어들에게 높은 진입장벽을 가진것 또한 Github 입니다<br>

이를 해소하기 위해 Github와 관련된 기본적인 정보와 더불어, 키워드를 기반으로 목적성에 부합하는 다양한 repository 추천시스템을 구축하려 합니다. 구글링과 유튜브 검색 등 으로 해결되지 않았던, 수많은 개발 노하우와 기술들이 잠들어있는 Github의 바다를 좀 더 쉽게 항해 하실 수 있도록 도와주는 나침반이 되겠습니다<br>
<br>
<br>

### 프로젝트명 : Github Repository 추천 페이지
개발자를 희망하거나 아직 깃허브에 익숙치 못한 주니어들을 위해 깃허브와 관련된 기초적인 정보와 더불어<br>
특정 키워드를 활용해 참고할 만한 repository 들을 추천
<br>

### 개발기간
22.03.04(금) ~ 22.04.12(화)
<br>

### 개발 일정 로드맵
![image](https://user-images.githubusercontent.com/92630511/157398692-ab31851a-bcf6-4b66-88bf-bf7ed809587f.png)
참고 링크: https://www.notion.so/ee0499b83cad437cabc8cf7e3b251c98?v=8d6c3d47571c41a493123b875dd9c4e0
<br>
<br>

## 서비스 기능

### 1. Main page
- 비로그인 활동 가능
- 댓글달기/북마크와 같은 기능 사용시 로그인 & 회원가입 유도
- 크게 4~5가지 섹션으로 나누어서 각 페이지로 이동할 수 있게 제작
<br>

### 2. Github Intro page
- 깃허브의 역사(깃허브를 우리가 공부하고 사용해야하는 이유 ++)소개
<br>

### 3. Github Tutorial page
- 로컬에서 깃허브 사용시에 반드시 알아야될 기본적인 커맨드 위주의 정보전달
- source tree 사용법은 기본적으로 배제
<br>

### 4. Recommend Repositories page
- word2vec & cosine_similarity를 활용한 관심사에 맞는 repository 추천
- 썸네일+카드 리스트 형태로 이루어진 게시판 형태
- 각 repository에 대한 댓글 달기 및 북마크 기능
<br>

### 5. User page
- 간단한 활동 기록과 더불어 북마크 한 repository 모아보기 기능
<br>

## 사용도구
- HTML, CSS
- Javascript
- Python - django, Mysql, requests
- sklearn - csv, word2vec, cosine_similarity
- colab pro
- AWS

### Collaboration & Tools
- Slack & gather
- Figma
- GIT / GIT Hub
<br>

## 팀빌딩 및 역할
- 부트캠프 <스파르타 내일배움캠프> 참가자로 구성
<br>
### 개발자 (가나다순)<br>

**김건우 @aopd408**<br>
✔️ BE 총괄<br>
✔️ 웹/API 서버 구축<br>
✔️ DB 연결 및 관리<br>
<br>

**김재명 @mungnpang**<br>
✔️ Machine Learning 총괄<br>
✔️ 추천시스템 구축<br>
✔️ FE support<br>
<br>

**김한석 @novahope** <br>
✔️ 디자인 파트 총괄<br>
✔️ 일러스트 및 영상 제작<br>
<br>

**김효은 @** <br>
✔️ BE support<br>
✔️ 로그인/회원가입 기능 담당<br>
✔️ 전체적인 일정관리 담당<br>
<br>

**박지훈 @** <br>
✔️ FE 총괄<br>
✔️ 페이지 디자인 프로토타입 제작<br>
✔️ javascript 활용 동적 페이지 구성<br>
<br>
<br>
## API소개
![image](https://images.velog.io/images/aopd48/post/0496214b-e337-4cc2-9126-4e41b3b8d64a/image.png)
![image](https://images.velog.io/images/aopd48/post/2549a777-bb49-4713-8d8c-c45bc8c21acc/image.png)
![image](https://images.velog.io/images/aopd48/post/0574a6bb-1400-4d95-9077-b5f60f500d0a/image.png)
![image](https://images.velog.io/images/aopd48/post/273b5e96-fc03-41a7-9097-e3faae7f4e82/image.png)<br>
참고 링크: https://www.notion.so/4a40f4e459c34cce97165a25b0b01b8b?v=d6e6bcce33624f908e6fa9dae6251de3<br>
<br>
<br>
## DB소개
![image](https://images.velog.io/images/aopd48/post/abc41f19-c8a3-42e3-aa56-26e9d53db5a7/image.png)
![image](https://images.velog.io/images/aopd48/post/db52a093-d303-477a-a8a1-e330b7106ead/image.png)
![image](https://images.velog.io/images/aopd48/post/719fb9a2-fda1-4757-b28c-2bc9aed53935/image.png)
![image](https://images.velog.io/images/aopd48/post/25bc691d-79e5-42c5-b903-e43c8782b599/image.png)
<br>
<br>
## Workflow
![image](https://user-images.githubusercontent.com/92630511/157398505-d11d0469-6dfc-4248-9196-a90ac5d42b1c.png)<br>

## Wireframe
![image](https://user-images.githubusercontent.com/92630511/157482826-0302237c-b963-4a22-b4de-acba68dad2f8.png)

Workflow & Wireframe in Figma: https://www.figma.com/file/1aZNTndbyzyAaJKDsvr2XO/RR?node-id=0%3A1
<br><br><br><br><br>

### KPT 회고<br><br>

[Keep]<br>
1. 기획단계에서 파트 배분과 구현하고자 하는 기능들을 비교적 구체적으로 정해놓고 출발하여 시간적으로 효율성있게 진행할 수 있었다
2. 정해진 회의 시간 이외에도 자주 소통하면서 현 상황이 어떤지, 어떤것을 수정해야될지 등을 빠르게 공유할 수 있었다
<br>

[Problem]<br>
1. 깃허브 관련 주제를 가지고 진행한 프로젝트임에도 불구하고 정작 우리조차 Github를 제대로 사용하지 못하였다
2. 초기에 정해놨던 구성은 다 완성시켰지만 추가적인 발전요소가 많지 않아서 아쉬웠다
3. 이슈 및 요청사항에 대한 대응이 기대했던 것 보다 신속하지 못했다
4. 코드리뷰에 대한 의지는 있었으나 지속적으로 진행되지 못하였다
<br>

[Try]<br>
1. 소통을 할 때 좀 더 구체적인 논점과 아이디어를 가지고 진행해야 할 것 같다
2. 완성된 작업물에 안주하지 않고 추가적인 논의가 지속적으로 이뤄져야 한다
3. 새로운 것을 찾고 끊임없는 변화를 받아들이는 것에 익숙해 질 필요가 있다
4. 각자 맡은 파트뿐 아니라 팀단위로 해야할 일들에 대해서도 다같이 책임을 분담해야 할 것 같다
