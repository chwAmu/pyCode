def square_num(nums):
	for i in nums:
		yield (i*i)


my_nums=square_num([1,2,3,4,5,6])


print(my_nums)

'''
generator do not hold the whole result in the memory.
so the return will be:
<generator object square_num at 0x10e787a50>

and yeilds one result as a time.
now it is waiting us for the next result.

so what happen if we using a next keyword?

'''

print next (my_nums) #result is 1
print next (my_nums) #result is 4
print next (my_nums) #result is 9
print next (my_nums) #result is 16
print next (my_nums) #result is 25
print next (my_nums) #result is 36

'''
i can get all the result. but what will happen if i next again?
i will have an error!
now let try to create a generator..
'''

my_nums2=(x*x for x in [1,2,3,4,5,6])
print(my_nums2)
print(list(my_nums2))

'''
although now the list is very small, we can not get the advantages while using
generator by the characties that do not hold the memory,but how about we have
100000 elements?
'''




