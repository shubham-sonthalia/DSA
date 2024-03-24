def main():
	t = int(input())
	def isArraySorted(arr):
		n = len(arr)
		sort = True
		for i in range(n - 1):
			if arr[i] > arr[i + 1]:
				sort = False
				break
		return sort
	while t > 0:
		n,k = map(int, input().split())
		arr = list(map(int, input().split()))[:n]
		if (not isArraySorted(arr) and k == 1):
			print("NO")
		else:
			print("YES")
		t -= 1

if __name__ == '__main__':
	main()
