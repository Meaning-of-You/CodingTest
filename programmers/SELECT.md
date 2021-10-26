# SELECT

> 프로그래머스 코딩 테스트 연습 



### SELECT란?

- 데이터 조작어(DML, Data Manipulation Language)
- 데이터 베이스에 들어 있는 데이터를 조회하거나 검색하기 위한 명령어

```sql
SELECT 컬럼명 FROM 테이블 명;
```



##### 모든 레코드 조회하기

- `*(애스터리스크)`: 해당 테이블의 모든 컬럼 정보

```sql
SELECT * FROM ANIMAL_INS
```



##### 역순 정렬하기

- `ORDER BY`: 조회된 데이터를 특정 컬럼을 기준으로 정렬하기 위해 사용
  - `DESC`: 내림차순 정렬
  - `ASC`: 오름차순 정렬 (기본 값)

```sql
SELECT NAME, DATETIME 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;
```



##### 아픈 동물 찾기

- `WHERE`: 원하는 자료만 조회하기 위해서 자료들을 제한
- 연산자

| 구분             | 연산자                                                       | 연산자의 의미                                                |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 비교 연산자      | =<br />><br />>=<br /><<br /><=                              | 같다<br />보다 크다<br />보다 크거나 같다<br />보다 작다<br />보다 작거나 같다 |
| SQL 연산자       | Between A AND B<br />IN (list)<br />Like '문자열'<br />IS NULL | A와 B사이에 값이 있다 (A, B포함)<br />리스트에 있는 값 중 하나라도 일치한다<br />문자열과 형태가 일치한다 (%, _ 사용)<br />NULL 값이다 |
| 논리 연산자      | AND<br />OR<br />NOT                                         | 앞의 조건과 뒤의 조건 동시에 만족한다<br />앞뒤 조건 중 하나라도 만족한다<br />뒤에 오는 조건과 반대된다 |
| 부정 비교 연산자 | !=<br />^=<br /><><br />NOT 컬럼명 =<br />NOT 컬럼명 >       | 같지 않다<br />같지 않다<br />같지 않다<br />~와 같지 않다<br />~보다 크지 않다 |
| 부정 SQL 연산자  | NOT Between A AND B<br />NOT IN (list)<br />IS NOT NULL      | A와 B사이에 값이 없다 (A, B포함 X)<br />리스트에 있는 값과 일치하지 않는다<br />NULL 값을 갖지 않는다 |

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION Like 'Sick'
```



##### 어린 동물 찾기

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
```



##### 동물의 아이디와 이름

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;
```



##### 여러 기준으로 정렬하기

```sql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC;
```



##### 상위 n개 레코드

- `LIMIT`: 상위부터 n개의 데이터만 출력
  - LIMIT 3, 7: 상위 3부터 7개의 데이터 출력
  - LIMIT 5: 상위 5개의 정보 출력

```sql
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME ASC
LIMIT 1;
```