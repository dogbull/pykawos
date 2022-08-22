# pykawos

`pykawos`(Python KMA AWS and ASOS)는 파이썬을 이용하여 [kawos](https://github.com/dogbull/kawos)의 데이터를 조회할 수 있습니다.

조회 가능한 기상청 종관기상관측(ASOS)자료와 방재기상관측자료(AWS)의 기간은 [kawos](https://github.com/dogbull/kawos)를 따릅니다.

## 사용법

### 설치

```bash
pip install -U pykawos
```

### 불러오기

```python
import pykawos
```

### 종관기상관측(ASOS)지점 목록

```python
pykawos.read_asos_stations()
```

또는

```python
pykawos.read_stations('asos')
```

[DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)의 헤더를 한글로 조회

```python
pykawos.read_asos_stations(kor_header=True)  # or pykawos.read_stations('asos', kor_header=True)
```

### 방재기상관측(AWS)지점 목록

```python
pykawos.read_aws_stations()
```

또는

```python
pykawos.read_stations('aws')
```

[DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)의 헤더를 한글로 조회

```python
pykawos.read_aws_stations(kor_header=True)  # or pykawos.read_stations('aws', kor_header=True)
```

### 단일 지점의 종관기상관측(ASOS) 자료 조회

```python
pykawos.read_asos_single_point(108, '20210101', '20211231')
```

또는

```python
pykawos.read_single_point('asos', 108, '20210101', '20211231')
```

### 모든 지점의 종관기상관측(ASOS) 자료 조회

```python
pykawos.read_asos_multi_point('20210101')
```

또는

```python
pykawos.read_multi_point('asos', '20210101')
```

### 단일 지점의 방재기상관측(AWS) 자료 조회

```python
pykawos.read_aws_single_point(96, '20210101', '20211231')
```

또는

```python
pykawos.read_single_point('aws', 96, '20210101', '20211231')
```

### 모든 지점의 방재기상관측(AWS) 자료 조회

```python
pykawos.read_aws_multi_point('20210101')
```

또는

```python
pykawos.read_multi_point('aws', '20210101')
```


