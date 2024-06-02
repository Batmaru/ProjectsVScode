def construct_rectangle(area: float) ->list[float]:
    for width in range(1, area + 1):
        for height in range( 1, area + 1):
            if width * height == area and width >=height:
                return  [width, height]
       
            
print(construct_rectangle(49))
    
   