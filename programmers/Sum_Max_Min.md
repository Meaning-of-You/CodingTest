# SUM, MAX, MIN

> 프로그래머스 코딩 테스트 연습 



##### 최댓값 구하기

- `ORDER BY` 활용
- `as`는 컬럼 레이블을 변경할 때 사용

```sql
SELECT DATETIME as 시간
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;
```

- `MAX` 활용

```sql
SELECT MAX(DATETIME) as 시간
FROM ANIMAL_INS;
```



##### 최솟값 구하기

- `ORDER BY` 활용

```sql
SELECT DATETIME as 시간
FROM ANIMAL_INS
ORDER BY DATETIME ASC
LIMIT 1;
```

- `MIN` 활용

```SQL
SELECT MIN(DATETIME) as 시간
FROM ANIMAL_INS
```



##### 동물 수 구하기

- `COUNT`: 테이블에 존재하는 행의 개수를 출력

```sql
SELECT COUNT(*) as count FROM ANIMAL_INS
```



##### 중복 제거하기

- `DISTINCT`: 중복된 데이터가 있는 경우 한 건으로 처리해서 출력

```sql
SELECT COUNT(DISTINCT NAME) as count FROM ANIMAL_INS
```

