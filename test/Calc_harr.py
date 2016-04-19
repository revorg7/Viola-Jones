def Calc_harr(window_size=19):
	n = window_size
	n = (n/2)*2

	#let h,w be height,width respectively
	#no of 2-features horizontally divided
	k = 2
	h_list = range(k,n+k,k)
	w_list = range(4,n+1,2)		# ==> to reduce the no. of features, increased the gap from 1 to 2, start the smallest width from 4

	feature_list=[]
	for h in h_list:
		for w in w_list:
			feature_list.append((h,w)) 

	#feature type-0 (horizontally divided)
	hf0=[]
	for rect_feature in feature_list:
		h,w = rect_feature
		for x in range(n-h+1):
			for y in range(n-w+1):
				hf0.append((x,y,h/2,w,0,1))

	#feature type-1 (vertically divided)
	hf1=[]
	for rect_feature in feature_list:
		w,h = rect_feature
		for x in range(n-h+1):
			for y in range(n-w+1):
				hf1.append((x,y,h,w/2,1,1))

	#adding 3-features
	k = 3
	h_list = range(k,n+k,k)
	w_list = range(1,n+1,1)		# ==> change this to reduce no. of features, it represents the pixel-gap btw diff types of features as before 

	feature_list=[]
	for h in h_list:
		for w in w_list:
			feature_list.append((h,w)) 

	hf2=[]
	for rect_feature in feature_list:
		h,w = rect_feature
		for x in range(n-h+1):
			for y in range(n-w+1):
				hf2.append((x,y,h/3,w,2,1))

	hf3=[]
	for rect_feature in feature_list:
		w,h = rect_feature
		for x in range(n-h+1):
			for y in range(n-w+1):
				hf3.append((x,y,h,w/3,3,1))

	#adding 4-features
	k = 2
	h_list = range(k,n+k,k)
	w_list = range(k,n+1,k)		# k  now ==> each side is now power of 2 

	feature_list=[]
	for h in h_list:
		for w in w_list:
			feature_list.append((h,w)) 

	hf4=[]
	for rect_feature in feature_list:
		h,w = rect_feature
		for x in range(n-h+1):
			for y in range(n-w+1):
				hf4.append((x,y,h,w,4,1))

	return hf0,hf1,hf2,hf3,hf4
