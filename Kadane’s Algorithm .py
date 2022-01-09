"""Given a sequence of n real numbers A(1) … A(n), determine a contiguous subsequence A(i) … A(j)
 for which the sum of elements in the subsequence is maximized............."""

def solution(array:list) ->list:
	new_max =0
	result_max=0
	for i in range(len(array)):
		new_max = max(array[i], new_max+array[i])
		result_max = max(new_max, result_max)
	return result_max


array = [1,-2,23,4,56] 

print(solution(array))