
# EasyVectorsPy
## Eng 

library that helps when working with coordinates like (Pillow, Pygame)

### Examples ###

```python 
from EasyVectors import Vector2

vector = Vector2(10, 67)
print(vector.x)
```

This code will give the output 10
```python 
from EasyVectors import Vector2

vector = Vector2()
print(str(vector))
```
This code will give the output X 0  Y 0 
```python 
from EasyVectors import Vector2

vector = Vector2()
vector2 = Vector2(56, 81)
vector.x = 1
vector.y = 8

print(vector.distance_to(vector2))
```
This code will give the output 93.2952303175248 

**A description of all methods can be found on the Wiki**

## Ru

Библиотека для упрощения работы с координатами, например(Pillow, Pygame)

### Примеры ###

```python 
from EasyVectors import Vector2

vector = Vector2(10, 67)
print(vector.x)
```

Этот код выведет 10

```python 
from EasyVectors import Vector2

vector = Vector2()
print(str(vector))
```

Этот код выведет X 0  Y 0 

```python 
from EasyVectors import Vector2

vector = Vector2()
vector2 = Vector2(56, 81)
vector.x = 8
vector.y = 1

print(vector.distance_to(vector2))
```
Этот код выведет 93.2952303175248 

**Описание всех методов можно найти на Wiki**
