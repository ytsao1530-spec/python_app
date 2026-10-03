#FizzBuzz
x = 0
y = 0
z = 0
for i in range(1, 101):
    if i % 15 == 0:
        print("Fizz Buzz")
        #continue
        x += 1
       
    if i % 3 == 0:
        print("Fizz")
        #continue
        y += 1
      
    if i % 5 == 0:
        print("Buzz")
        #continue
        z += 1
 
    print(i)
print("Fizz Buzz count: ", x)
print("Fizz count: ", y)
print("Buzz count: ", z)

