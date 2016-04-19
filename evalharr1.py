#build on this code
#http://stackoverflow.com/questions/19297790/fastest-python-way-to-evaluate-haar-feature-values

def Zero(x,y,i,h,w):        
    #bottom rect - top rect
    if x==0 and y==0:       
       return i.item(x+2*h-1,y+w-1) -2*(i.item(x+h-1,y+w-1))       

    elif y==0:       
       return (i.item(x+2*h-1,y+w-1))-2*(i.item(x+h-1,y+w-1))+(i.item(x-1,y+w-1))      

    elif x==0:       
       return i.item(x+2*h-1,y+w-1)+2*(i.item(x+h-1,y-1))-2*(i.item(x+h-1,y+w-1))-i.item(x+2*h-1,y-1)     

    else:    
       bright = (i.item(x+h-1,y+w-1)+i.item(x-1,y-1))-(i.item(x-1,y+w-1)+i.item(x+h-1,y-1))       
       dark = (i.item(x+2*h-1,y+w-1)+i.item(x+h-1,y-1))-(i.item(x+h-1,y+w-1)+i.item(x+2*h-1,y-1))
       return dark - bright

def One(x,y,i,h,w):
    #left rect - right rect
    
     if x==0 and y==0:     
        return 2*(i.item(x+h-1,y+w-1))-(i.item(x+h-1,y+2*w-1))     

     elif y==0:     
         return 2*(i.item(x+h-1,y+w-1))-2*(i.item(x-1,y+w-1))+(i.item(x-1,y+2*w-1))-(i.item(x+h-1,y+2*w-1))     

     elif x==0:            
         return 2*(i.item(x+h-1,y+w-1))-(i.item(x+h-1,y+2*w-1)+i.item(x+h-1,y-1))     

     else:     
          bright = (i.item(x+h-1,y+2*w-1)+i.item(x-1,y+w-1))-(i.item(x-1,y+2*w-1)+i.item(x+h-1,y+w-1))     
          dark = (i.item(x+h-1,y+w-1)+i.item(x-1,y-1))-(i.item(x-1,y+w-1)+i.item(x+h-1,y-1))    

          return dark-bright 


def Two(x,y,i,h,w):
	#brights are centered, just 1
	if x!=0 and y!=0:
		dark = i.item(x+3*h-1,y+w-1)+i.item(x-1,y-1)-i.item(x+3*h-1,y-1)-i.item(x-1,y+w-1)
		bright = i.item(x+2*h-1,y+w-1)+i.item(x+h-1,y-1)-i.item(x+h-1,y+w-1)-i.item(x+2*h-1,y-1)
		return dark - 2*bright

	#simplication of above formula, all eqs st x-1 < 0 or y-1<0 are set to zero
	elif x==0 and y==0:
		dark = i.item(x+3*h-1,y+w-1)
		bright = i.item(x+2*h-1,y+w-1)-i.item(x+h-1,y+w-1)
		return dark - 2*bright
	
	elif x==0:
		dark = i.item(x+3*h-1,y+w-1)-i.item(x+3*h-1,y-1)
		bright = i.item(x+2*h-1,y+w-1)+i.item(x+h-1,y-1)-i.item(x+h-1,y+w-1)-i.item(x+2*h-1,y-1)
		return dark - 2*bright

	else:
		dark = i.item(x+3*h-1,y+w-1)-i.item(x-1,y+w-1)
		bright = i.item(x+2*h-1,y+w-1)-i.item(x+h-1,y+w-1)
		return dark - 2*bright


def Three(x,y,i,h,w):
	#bright is centered, just1
	if x!=0 and y!=0:
		dark = i.item(x+h-1,y+3*w-1)+i.item(x-1,y-1)-i.item(x-1,y+3*w-1)-i.item(x+h-1,y-1)
		bright = i.item(x+h-1,y+2*w-1)+i.item(x-1,y+w-1)-i.item(x-1,y+2*w-1)-i.item(x+h-1,y+w-1)
		return dark - 2*bright
		
	elif x==0 and y==0:
		dark = i.item(x+h-1,y+3*w-1)
		bright = i.item(x+h-1,y+2*w-1)-i.item(x+h-1,y+w-1)
		return dark - 2*bright

	elif x==0:
		dark = i.item(x+h-1,y+3*w-1)-i.item(x+h-1,y-1)
		bright = i.item(x+h-1,y+2*w-1)-i.item(x+h-1,y+w-1)
		return dark - 2*bright

	else:
		dark = i.item(x+h-1,y+3*w-1)-i.item(x-1,y+3*w-1)
		bright = i.item(x+h-1,y+2*w-1)+i.item(x-1,y+w-1)-i.item(x-1,y+2*w-1)-i.item(x+h-1,y+w-1)
		return dark - 2*bright
		
def Four(x,y,i,h,w):
    #unlike others input full-feature height,width i.e h,w = 2*k 
    #type-D, top-leftmost corner is assumed dark
    return One(x,y,i,h/2,w/2)-One(x+h/2,y,i,h/2,w/2)


def EvaluateHaar(Lis,(x,y,h,w,f,p)):       


    options = {0 : Zero, 
               1 : One,
               2 : Two,
               3 : Three,
               4 : Four,
    }
    R = []     
    append1 = R.append     

    for i in Lis:      
        append1(options[f](x,y,i,h,w))

    return R


