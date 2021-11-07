# JOIN

> 프로그래머스 코딩 테스트 연습 



##### 루시와 엘라 찾기

- ` IN` 활용

```sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID
```



##### 이름에 el이 들어가는 동물 찾기

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%El%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME
```



##### 중성화 여부 파악하기

- `IF` 활용

```sql
SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE LIKE 'Neutered%' OR SEX_UPON_INTAKE LIKE 'Spayed%', 'O', 'X') AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```



##### 오랜 기간 보호한 동물(2)

```sql
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I
LEFT JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.DATETIME IS NOT NULL
ORDER BY I.DATETIME - O.DATETIME ASC
LIMIT 2
```



##### DATETIME에서 DATE로 형 변환

- DATE_FORMAT 구분기호

| 구분기호 | 역할                      |
| -------- | ------------------------- |
| %Y       | 4자리 년도                |
| %y       | 2자리 년도                |
| %M       | 긴 월                     |
| %b       | 짧은 월                   |
| %W       | 긴 요일 이름              |
| %a       | 짧은 요일 이름            |
| %i       | 분                        |
| %T       | hh:mm:SS                  |
| %m       | 숫자 월 (두자리)          |
| %c       | 숫자 월 (한자리는 한자리) |
| %d       | 일자 (두자리)             |
| %e       | 일자 (한자리는 한자리)    |
| #l       | 시간 (12시간)             |
| %H       | 시간(24시간)              |
| %r       | hh:mm:ss AM, PM           |
| %S       | 초                        |

```shell
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

