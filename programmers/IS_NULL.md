# IS NULL

> 프로그래머스 코딩 테스트 연습 



##### 이름이 없는 동물의 아이디

- `IS NULL` 활용
  - 입력값을 확인하여 NULL이면 TRUE를 NULL이 아니면 FALSE를 리턴

```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
```



##### 이름이 있는 동물의 아이디

- `IS NOT NULL` 활용

  - 입력값을 확인하여 NULL이 아니면 TRUE를 NULL이면 FALSE를 리턴

  ```sql
  SELECT ANIMAL_ID
  FROM ANIMAL_INS
  WHERE NAME IS NULL
  ```



##### NULL 처리하기

- `IFNULL` 활용
  -  컬럼의 값이 NULL을 반환할 때, 다른 값으로 출력할 수 있도록 하는 함수

```sql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```
