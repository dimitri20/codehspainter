from PIL import Image
import csv



class ImageToJsCode:
	def __init__(self, imagePath):
		self.imagePath = imagePath

	def extractData(self):
		im = Image.open(self.imagePath, 'r')

		data = list(im.getdata())

		with open(f'{self.imagePath}.csv', 'w') as f:
		    writer = csv.writer(f, lineterminator='\n')
		    for tup in data:
		        writer.writerow(tup)		

	def generateJsCode(self):
    	#codeFile = open(f'{self.imagePath}.js', 'a')
    	#imageData = open(f'{self.imagePath}.csv', 'r')

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
		codeFile = open('code.js', 'a')
		codeFile.write(initCode)


		with open(f'{self.imagePath}.csv', 'r') as ts:
			data = ts.readlines()
			codeFile.write(f"createPxl({int(len(data)/400)});\n")
			for item in data:
				codeFile.write(f""" 

					for(var i = 0; i < {len(data)}; i++){{
						var pxl_dat[i] = {item};
					}}

					for(var i = 0; i < data.length; i++){{
						var color = new Color(pxl_dat[i]);
						setColor(pixels, [{data.index(item)%401}, {int(data.index(item)/400)}], color);
					}}

				    """)

		codeFile.close()

"""
		with open(f'{self.imagePath}.csv', 'r') as ts:
			data = ts.readlines()
			codeFile.write(f"createPxl({int(len(data)/400)});\n")
			for item in data:
				codeFile.write(f"setColor(pixels, [{data.index(item)%401}, {int(data.index(item)/400)}], {item});\n")

			codeFile.write("addPxs(pixels);")
"""