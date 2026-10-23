# if we devide any int by 0 it will be infinnite and it will give us error
# result = 45 / 0

# but the problem is that if we have something else after the division, it will not go there. it will not come to the done
# print('Done')

# the same thing we can do with try and except. in this case the next code will run
try:
    # result = 45 / 0
    result = 45 / 5 # now it is right but it will still hit the finally here
except:
    print('error happend')
finally:
    print("finaaly here") # it will hit with error and without error
print('doen') #now code reach this code