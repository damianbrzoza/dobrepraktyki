import math

def closestPointToLines(l1, l2):
    """refer to https://en.wikipedia.org/wiki/Skew_lines#Distance"""

    #compute n, n1, n2 
    n = (0,0,0)
    n1 = (0,0,0)
    n2 = (0,0,0)

	#crossproduct l1,l2
    n[0] = l1[4]*l2[5]-l1[5]*l2[4];
    n[1] = l1[5]*l2[3]-l2[5]*l1[3];
    n[2] = l1[3]*l2[4]-l1[4]*l2[3];

	#crossproduct n, l1
    n1[0] = l1[4]*n[2]-l1[5]*n[1];
    n1[1] = l1[5]*n[0]-n[2]*l1[3];
    n1[2] = l1[3]*n[1]-l1[4]*n[0];
   
	#crossproduct n, l2
    n1[0] = l2[4]*n[2]-l2[5]*n[1];
    n1[1] = l2[5]*n[0]-n[2]*l2[3];
    n1[2] = l2[3]*n[1]-l2[4]*n[0];


    # declare template variables
    tmp1 = (0,0,0)
    tmp2 = (0,0,0)
    tmp3 = (0,0,0)
    tmp4 = (0,0,0)
    
    # cross points
   	c1 = (0,0,0)
    c2 = (0,0,0)

    # in case of failure, pick first line start point
	dest = (0,0,0)
    dest[0] = l1[0]
	dest[1] = l1[1]
	dest[2] = l1[2]
    
    #cross point 1, multiplier = dotproduct
	multiplier = l1[3]*n2[0]+l1[4]*n2[1]+l1[5]*n2[2]
    if multiplier == 0: return -1
	wagedpoint = (l2[0]-l1[0],l2[1]-l1[1],l2[2]-l1[2])
	# dotproduct ( wagedpoint, n2) / multiplier
    multiplier = *n2[0]*wagedpoint[0]+n2[1]*wagedpoint[1]+n2[2]*wagedpoint[2]) / multiplier;
	#c1 = l1[0,1,2] + multiplier * l2[3,4,5]
	c1[0] = l1[0]+multiplier*l2[3]
	c1[1] = l1[1]+multiplier*l2[4]
	c1[2] = l1[2]+multiplier*l2[5]

    #cross point 1, multiplier = dotproduct
	multiplier = l2[3]*n1[0]+l2[4]*n1[1]+l2[5]*n1[2]
    if multiplier == 0: return -1
	wagedpoint = (l1[0]-l2[0],l1[1]-l2[1],l1[2]-l2[2])
	# dotproduct ( wagedpoint, n2) / multiplier
    multiplier = *n1[0]*wagedpoint[0]+n1[1]*wagedpoint[1]+n1[2]*wagedpoint[2]) / multiplier;
	#c2 = l2[0,1,2] + multiplier * l1[3,4,5]
	c1[0] = l2[0]+multiplier*l1[3]
	c1[1] = l2[1]+multiplier*l1[4]
	c1[2] = l2[2]+multiplier*l1[5]

    return math.sqrt( (c1[0]-c2[0])*(c1[0]-c2[0])+(c1[1]-c2[1])*(c1[1]-c2[1])+(c1[2]-c2[2])*(c1[2]-c2[2]) );
}
