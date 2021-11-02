# GROUP BY

> 프로그래머스 코딩 테스트 연습 



##### 고양이와 개는 몇 마리 있을까

- `GROUP BY` 활용
  - 유형별로 갯수를 알고 싶을 때 컬럼에 데이터를 그룹화 하기 위해 사용

```sql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) as count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE
```



##### 동명 동물 수 찾기

- `HAVING` 활용
  - 특정 컬럼을 그룹화한 결과에 조건을 걸기 위해 사용

```sql
SELECT NAME, COUNT(NAME) as COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL 
GROUP BY NAME
HAVING COUNT(NAME) > 1
ORDER BY NAME
```



##### 입양 시각 구하기(1)

- 날짜 데이터에서 일부만 추출하기

|  함수  | 설명                |
| :----: | :------------------ |
|  YEAR  | 연도 추출           |
| MONTH  | 월 추출             |
|  DAY   | 일 추출(DAYOFMONTH) |
|  HOUR  | 시 추출             |
| MINUTE | 분 추출             |
| SECOND | 초 추출             |

```sql
SELECT HOUR(DATETIME) as HOUR, COUNT(HOUR(DATETIME)) as COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR(DATETIME)
HAVING HOUR >= 9 AND HOUR < 20
ORDER BY HOUR(DATETIME)
```



##### 입양 시각 구하기(2) - 보류
