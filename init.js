


function createPxl(height){
	var pixels = [];
	for(var i = 0; i < height; i++){
		for(var j = 0; j < 400; j++){
			var px = new Rectangle(1, 1);
			px.setPosition(j, i);
			var pixels_x = [];
			pixels_x[j] = px;
		}
		pixels[i] = pixels_x;
	}

	return pixels;
}

function setColor(pixels, pxPos, color){
	pixels[pxPos[0]][pxPos[1]];
}

function addPxs(pixels){
	for(var i = 0; i < pixels.length; i++){
		for(var j = 0; j < 400; j++){
			add(pixels[i][j]);
		}
	}
}


    def generateJsCode(self):
    	codeFile = open(f'{self.imagePath}.js', 'a')
    	imageData = open(f'{self.imagePath}.csv', 'r')

    	initCode = """ 

			function createPxl(height){
				var pixels = [];
				for(var i = 0; i < height; i++){
					for(var j = 0; j < 400; j++){
						var px = new Rectangle(1, 1);
						px.setPosition(j, i);
						var pixels_x = [];
						pixels_x[j] = px;
					}
					pixels[i] = pixels_x;
				}

				return pixels;
			}

			function setColor(pixels, pxPos, color){
				pixels[pxPos[0]][pxPos[1]];
			}

			function addPxs(pixels){
				for(var i = 0; i < pixels.length; i++){
					for(var j = 0; j < 400; j++){
						add(pixels[i][j]);
					}
				}
			}
    			
    	"""
    	codeFile.append(initCode)

    	
    	
	